from flask import Flask, jsonify, render_template
from selenium_script import fetch_trending_topics, store_trending_topics_in_mongo
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run_script")
def run_script():
    try:
       
        trending_topics = fetch_trending_topics(woeid=1) 
        if trending_topics:
           
            store_trending_topics_in_mongo(trending_topics)

            
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ip_address = socket.gethostbyname(socket.gethostname())

            return jsonify({
                "date": date_time,
                "topics": trending_topics,
                "ip": ip_address
            })
        else:
            return jsonify({"error": "No trending topics found"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
