import requests
import feedparser
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/feed', methods=['GET'])
def get_feed():
    URLs = [
        "https://www.faz.net/rss/aktuell",
        "https://www.tagesschau.de/xml/rss2",
        "https://www.spiegel.de/schlagzeilen/index.rss",
        "https://rss.dw.com/rdf/rss-de-all",
        "https://www.welt.de/politik/?service=Rss"  
    ]
    feeds = []
    for URL in URLs:
        feed = feedparser.parse(URL)
        feeds.append(feed)
    return jsonify(feeds)


if __name__ == '__main__':
    app.run(debug=True)