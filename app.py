import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = '5118286f6eb44c1e96b211eeb35a07d8'

@app.route('/')
def home():
    query = request.args.get('q')  # Kullanıcının arama sorgusunu al
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])
    return render_template('index.html', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/borsa')
def borsa():
    return render_template('borsa.html')



if __name__ == '__main__':
    app.run(debug=True)


