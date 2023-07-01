from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from scrappers.cointelegraph import get_news

app = Flask(__name__)

@app.route('/')
def hello():
  return jsonify({
    'message': 'API DSG24 RGL', 
    'endpoints': {
      '/': 'GET',
      '/news': 'GET'
    }, 
    'status': 200
  })

@app.route('/news/<keyword>/<nNews>', methods=['POST', 'GET'])
def getNews(keyword, nNews=10):
    response = {}
    
    if (keyword and len(keyword) > 0 and not ' ' in str()):
      news = get_news(keyword, nNews)
      response = {'status': 200, 'message': 'Todo bien', 'data': news}
    else:
      response = {'status': 400, 'message': 'No se envió el keyword'}
      
    return jsonify(response)
  
@app.route('/singlenews/<url>', methods=['POST', 'GET'])
def singlenews(url):
    response = {}
    
    return url

app.run(debug=True, host='localhost', port=8000)