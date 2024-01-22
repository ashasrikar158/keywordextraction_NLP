from flask import Flask, render_template,request
import Keyword_Extract
from  Keyword_Extract import extract_words
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd


app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    try:
        input_text = request.form.get("inputText")
        # print("Received input text:", input_text)
        # Add your keyword extraction logic here if needed
        keywords = extract_words(input_text)
        # Generate the Word Cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keywords)

        # Save the Word Cloud as an image
        image_stream = BytesIO()
        wordcloud.to_image().save(image_stream, format='PNG')
        image_stream.seek(0)

        # Convert the image to a base64-encoded string
        image_data = base64.b64encode(image_stream.getvalue()).decode('utf-8')

        return render_template("index.html", inputText=input_text, wordcloud=image_data)
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
