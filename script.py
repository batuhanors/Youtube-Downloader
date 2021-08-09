from datetime import time
import time
import flask
from pytube import YouTube
from flask import Flask, render_template, request

from hurry.filesize import size

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/youtube")
def yt():
    url = request.args.get('url')
    if url:
        tyt = YouTube(url)
        data = {
                "info": {

                    "title": tyt.title,
                    "author": tyt.author,
                    "thumbnail": tyt.thumbnail_url,
                    "description": tyt.description,
                    "length": time.strftime("%H:%M:%S", time.gmtime(tyt.length)),
                    "views": tyt.views
                },
                "sources": []
        }
        videos = tyt.streams.filter(progressive=True)
        for element in videos:
            data['sources'].append({
                "url": element.url,
                "size": size(element.filesize),
                "resolution": element.resolution
            })
        return data
 






if __name__ == "__main__":
    app.run()
