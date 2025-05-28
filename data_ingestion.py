import pandas as pd
import requests
from newspaper import Article

def load_financials(path):
    return pd.read_csv(path)

def fetch_news(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def load_mock_api(path):
    with open(path, 'r') as f:
        return f.read()
