# -*- coding: utf-8 -*-
"""gabung.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sUWAh9uSvY9DaSviAnxEz1qt85UZBAze
"""

#Referensi: https://play.google.com/store/apps/details?id=id.or.muhammadiyah.quran

import subprocess

# Instalasi paket
subprocess.check_call(["pip", "install", "google-play-scraper"])

from google_play_scraper import app

import pandas as pd

import numpy as np

#Scrape desired number of reviews
#Run kode ini jika ingin scrape data dengan jumlah tertentu. Ganti (misal, ingin scrape sejumlah 1000, maka ganti kode , count = 1000 )

from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'id.or.muhammadiyah.quran',
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT you can use Sort.NEWEST to get newst reviews
    count=100, # defaults to 100
    filter_score_with=None # defaults to None(means all score) Use 1 or 2 or 3 or 4 or 5 to select certain score
)

df_busu = pd.DataFrame(np.array(result),columns=['review'])

df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))

df_busu.head()

len(df_busu.index) #count the number of data we got

df_busu[['userName', 'score','at', 'content']].head()  #preview userName, rating, date-time, and reviews only

#Run This Code to Sort the Data By Date

new_df = df_busu[['userName', 'score','at', 'content']]
sorted_df = new_df.sort_values(by='at', ascending=False) #Sort by Newst, change to True if you want to sort by Oldest.
sorted_df.head()

my_df = sorted_df[['userName', 'score','at', 'content']] #get userName, rating, date-time, and reviews only

my_df.head()

my_df.to_csv("scrapped_data.csv", index = False)  #Save the file as CSV , to download: click the folder icon on the left. the csv file should be there.

!pip install yake

import yake

text = """
Beribadah
Belajar
Membaca Al-Qur'an
Menghafal
Memperdalam ilmu agama
Berdoa
Mengaji
Menjalankan ibadah
Mengingatkan waktu sholat
Memahami ajaran Islam
Mengunduh
Menginstall
Mendaftar
Menggunakan fitur
Mengakses
Melakukan update
Mengaktifkan notifikasi
Memberikan ulasan
Mencari fitur
Berlangganan
Berdonasi
Menyukai fitur-fitur
Merasa terbantu
Memberikan saran
Memperhatikan ketepatan waktu sholat
Mengapresiasi aplikasi
Berharap adanya pembaruan
Merasa bangga
Mengeluhkan kesulitan saat pendaftaran
Meminta peningkatan fitur
Menyebutkan kesalahan dalam aplikasi
Mengusulkan perbaikan
Mengalami kesulitan dalam penggunaan
Berharap aplikasi bisa digunakan secara universal
"""

# Specify parameters for YAKE keyword extraction
language = "id"  # Language of the text
max_ngram_size = 2  # Maximum size of ngrams to consider
deduplication_threshold = 0.9  # Threshold for deduplicating similar keywords
num_keywords = 30  # Number of keywords to extract

# Create YAKE keyword extractor object
kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)

# Extract keywords from the text
keywords = kw_extractor.extract_keywords(text)

# Print the extracted keywords
for kw in keywords:
    print(kw)

pip install wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Convert extracted keywords to string format
extracted_keywords = [kw[0] for kw in keywords]
text = ' '.join(extracted_keywords)

# Initialize WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

!pip install keybert

from keybert import KeyBERT
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample questions/statements from the questionnaire
questions = ["Bagus banget lengkap fiturnya, semoga ditambah widget untuk penanda waktu sholat😁",
"terdapat bug di widget",
"Maaf, widget waktu sholatnya masih eror ya min?, aplikasi berhenti terus",
"Keren aplikasinya, tapi segera update fitur Muhammadiyah nya biar kita pelajari juga",
"Alhamdulillah, ada aplikasi yang super lengkap dan sangat membantu, khususnya warga Muhammadiyah"
"Sayangnya nggak ada jadwal Imsakiyahnya. Khususnya pas Ramadan. Padahal, Jadwal Imsyak sangat penting saat Ramadan ini.",
"Muhammadiyah sudah berpuasa hari ini 11 Maret 2024, tapi di aplikasi ini baru besok 12 Maret 1 Ramadhan. Bagaimana ini kok beda?",
"Recommended sekali ini dengan banyaknya fitur-fitur yang sangat bermanfaat utk memperdalam ilmu agama juga",
"Bagus, lengkap, sangat membantu",
"sangat suka fitur-fitur nya",
"Keren ada banyak fitur-fitur dan kitab-kitab dan tidak mengambil bacaan dari 1 bacaan tapi berbagai macamnya, saran kitab hadits nya di tambah ada kitab Arba'in Annawawiyah dan disegerakan fitur Muhammadiyah nya",
"sangat bermanfaat, sedikit saran pemberitahuan jadwal sholat sering tidak tepat (waktu sholat maghrib tp pemberitahuan asyar) 🙏",
"Enak, mudah dipakai, tidak berat",
"sangat membantu dalam pembelajaran Al Qur'an dan ke-Islaman",
"QuranMu aplikasi Al Qur'an yang sangat membantu saya untuk tetap membaca Al Qur'an di manapun ketika saya tidak membawa mushaf teks. fitur ibadah berisi banyak hal terkait ibadah dan hal-hal lain yang berguna untuk menambah pengetahuan tentang Islam. terimakasih QuranMu🙏🤗"
]

# Combine all questions into one text
combined_text = " ".join(questions)

# Initialize KeyBERT model
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Extract keywords
keywords = model.extract_keywords(combined_text)

print("Keywords:")
for keyword, score in keywords:
    print(f"{keyword}: {score}")

keywords = [
    "Beribadah","Fitur","Aplikasi","Sholat","Belajar","Memberikan","Merasa","Berharap","Waktu",
    "Kesulitan","Membaca","Waktu sholat","Islam","Menghafal","Berdoa","Mengaji","Ajaran Islam",
    "Mengunduh","Menginstall","Mendaftar","Mengakses","Berlangganan","Berdonasi","Memperdalam",
    "Agama","Menjalankan","Ibadah","Mengingatkan","Memahami","Menggunakan"
]

!pip install -qq google-play-scraper

!pip install google-play-scraper tqdm

!pip install --upgrade google-play-scraper

import json
import pandas as pd
from tqdm import tqdm
from google_play_scraper import Sort, reviews, app

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
path = "gdrive/MyDrive/"

app_packages = [
    'id.or.muhammadiyah.quran'
]

app_infos = []

for application in tqdm(app_packages):
        info = app(application, lang='id', country='id')
        del info['comments']
        app_infos.append(info)

app_reviews = []

for ap in tqdm(app_packages):
  for score in list(range(1,6)):
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
      rvs, _ = reviews(
          ap,
          lang='id',
          country='id',
          sort=sort_order,
          count=200 if score == 3 else 100,
          filter_score_with = score
      )
      for r in rvs:
        r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
        r['appId'] = ap
      app_reviews.extend(rvs)

app_reviews_df = pd.DataFrame(app_reviews)

app_reviews_df = app_reviews_df.sort_values(["appId","at"])

app_reviews_df.to_csv(path+'crawlingquran.csv', index=None, header=True)

import pandas as pd
data = pd.read_csv("/content/gdrive/MyDrive/crawlingquran.csv")
data.info()
data.head()

data.describe()

df = pd.DataFrame(data[['userName','content']])
df.head()

df.to_excel('dataset.xlsx', index=False)

data = pd.read_excel('/content/dataset.xlsx')

data.info()

data.drop_duplicates(subset='content', keep='first', inplace= True)
data.info()

df = pd.DataFrame(data[['userName','content']])

import re
import string
import nltk

def remove_URL(riview):
  url = re.compile(r'https ?: //\S+|www\.\s+')
  return url.sub(r'', riview)

def remove_html(riview):
  html =re.compile(r' <.*? >')
  return html.sub(r'', riview)

def remove_emoji(riview):
  emoji_pattern = re.compile("["
  u"\U0001F600-\U0001F64F"
  u"\U0001F300-\U0001F5FF"
  u"\U0001F680-\U0001F6FF"
  u"\U0001F1E0-\U0001F1FF"
  "]+", flags=re.UNICODE)
  return emoji_pattern.sub(r'', riview)

def remove_numbers(riview):
  riview = re.sub(r'\d+', '', riview)
  return riview

def remove_symbols(riview):
    riview = re.sub(r'[^a-zA-Z0-9\s]', '', riview)  # Corrected character range
    return riview

df['cleaning'] = df['content'].apply(lambda x: remove_URL(x))
df['cleaning'] = df['cleaning' ].apply(lambda x: remove_html(x))
df['cleaning'] = df['cleaning'].apply(lambda x: remove_emoji(x))
df['cleaning'] = df['cleaning' ].apply(lambda x: remove_symbols(x))
df['cleaning'] = df['cleaning' ].apply(lambda x: remove_numbers(x))

df.head(100)

# Simpan DataFrame yang telah dibersihkan ke dalam file CSV
df.to_csv('hasil_cleaning.csv', index=False)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Daftar kata kunci yang Anda berikan
keywords = ["Beribadah","Fitur","Aplikasi","Sholat","Belajar","Memberikan","Merasa","Berharap","Waktu",
    "Kesulitan","Membaca","Waktu sholat","Islam","Menghafal","Berdoa","Mengaji","Ajaran Islam",
    "Mengunduh","Menginstall","Mendaftar","Mengakses","Berlangganan","Berdonasi","Memperdalam",
    "Agama","Menjalankan","Ibadah","Mengingatkan","Memahami","Menggunakan"]

# Membuat fungsi untuk mengambil sinonim dari kata kunci
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

# Membuat fungsi untuk preprocessing teks
def preprocess_text(text):
    # Tokenisasi
    tokens = word_tokenize(text.lower())
    # Menghilangkan tanda baca dan angka
    words = [word for word in tokens if word.isalpha()]
    # Lematisasi
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Menghilangkan stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if not word in stop_words]
    return " ".join(words)

# Membaca DataFrame dari file CSV
df = pd.read_csv('hasil_cleaning.csv')

# Menggantikan nilai np.nan dengan string kosong di kolom 'cleaning'
df['cleaning'].fillna('', inplace=True)

all_keywords = ["Beribadah","Fitur","Aplikasi","Sholat","Belajar","Memberikan","Merasa","Berharap","Waktu",
    "Kesulitan","Membaca","Waktu sholat","Islam","Menghafal","Berdoa","Mengaji","Ajaran Islam",
    "Mengunduh","Menginstall","Mendaftar","Mengakses","Berlangganan","Berdonasi","Memperdalam",
    "Agama","Menjalankan","Ibadah","Mengingatkan","Memahami","Menggunakan"]  # Definisi manual

# Membuat TF-IDF Vectorizer
vectorizer = TfidfVectorizer(vocabulary=all_keywords)

# Mengubah konten review yang sudah dibersihkan menjadi vektor TF-IDF
review_vectors = vectorizer.fit_transform(df['cleaning'])

# Mengubah set ke dalam list
all_keywords = list(all_keywords)

# Membuat threshold
threshold = 0.5

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Memuat data dari file CSV
data = pd.read_csv("/content/gdrive/MyDrive/data-similarity.csv")

# Mengambil teks dari kolom 'text'
texts = data['text'].tolist()

# Inisialisasi TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Mengubah teks menjadi vektor TF-IDF
tfidf_matrix = vectorizer.fit_transform(texts)

# Menghitung similarity score antara semua pasangan teks
all_similarity_scores = cosine_similarity(tfidf_matrix)

# Mencetak similarity score untuk setiap pasangan teks
for i in range(len(texts)):
    for j in range(len(texts)):
        similarity_score = all_similarity_scores[i, j]
        print(f"Similarity score antara teks {i+1} dan {j+1}: {similarity_score}")
