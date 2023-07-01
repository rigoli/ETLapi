from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from scrappers.cointelegraph import ScraperCointelegraph

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
      cointelegraph = ScraperCointelegraph(keyword)
      news = cointelegraph.get_news(nNews)
      response = {'status': 200, 'message': 'Todo bien', 'data': news}
    else:
      response = {'status': 400, 'message': 'No se envió el keyword'}
      
    return jsonify(response)
  
@app.route('/singlenews', methods=['POST', 'GET'])
def singlenews():
  response = {}
  urlId = request.args.get('urlId')
  try:
    cointelegraph = ScraperCointelegraph('market')
    content = cointelegraph.get_news_single(urlId)
    response = {'status': 200, 'message': 'Todo bien', 'data': content}
  except Exception as e:
    response = {'status': 500, 'message': 'Error al obtener la noticia', 'error': str(e)}
  return jsonify(response)

app.run(debug=True, host='localhost', port=8000)