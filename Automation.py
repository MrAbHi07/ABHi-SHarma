import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_type = filename.split('.')[-1]
            folder_path = os.path.join(directory, file_type)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(directory, filename), folder_path)

# Use the function
directory = '/path/to/your/directory'
organize_files(directory)

import requests
from bs4 import BeautifulSoup

def scrape_latest_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h2', class_='title')
    for article in articles:
        print(article.get_text())

# Use the function
news_url = 'https://news.ycombinator.com/'
scrape_latest_news(news_url)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    from_email = 'your_email@gmail.com'
    password = 'your_password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)

# Use the function
subject = 'Test Email'
body = 'This is a test email sent from Python script.'
to_email = 'recipient_email@gmail.com'
send_email(subject, body, to_email)

import pandas as pd

def analyze_data(file_path):
    data = pd.read_csv(file_path)
    summary = data.describe()
    summary.to_csv('summary.csv')
    print("Data analysis complete. Summary saved to 'summary.csv'.")

# Use the function
file_path = 'data.csv'
analyze_data(file_path)

import schedule
import time

def job():
    print("Scheduled task is running...")

# Schedule the job
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
