import requests
from flask import Flask, Response
app = Flask(__name__)
@app.route('/')
def index():
    image_url = 'https://ctf-web-content.s3.ap-southeast-2.amazonaws.com/leaky-bucket-black-background.png'
    image_data = requests.get(image_url).content
    return Response(image_data, content_type='image/png')
if __name__ == '__main__':
    app.run(host='0.0.0.0')