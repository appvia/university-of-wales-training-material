from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3BvMzl3b2NpdzJqNzV3dXMxcnBpMnRrMmFyN3NvOGY0dmJidzF6eSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/p4xp4BjHIdane/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGJpa21rMHRtbTBnOG1pcm9jMXpmY21ncjExZjc5MHJqeGtzM2twZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPnAiaMCws8nOsE/giphy.gif",
   "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDc4ZjN2bjdkZml6Ym9qdXdsMGJxNnQweDYwdzZzM2M0aWZ0MjBsYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ES4Vcv8zWfIt2/giphy.gif",
   "https://media.giphy.com/media/b76TBpbMcv8MU/giphy.gif?cid=ecf05e47kadn034wmu4g4gq0rb9507oycs8yw6vo0yk5s1ca&ep=v1_gifs_search&rid=giphy.gif&ct=g",
   "https://media.giphy.com/media/11fucLQCTOdvBS/giphy.gif?cid=ecf05e47jy6cqp48e0kdhxyh1fs8tpoqz5dlshzeygjik886&ep=v1_gifs_search&rid=giphy.gif&ct=g",
   "https://media.giphy.com/media/QBtzAnMFO5i9O/giphy.gif?cid=ecf05e47jn521w3bldthz3bjcs2wznhmudzwcuqrooczodd8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
   "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGFqN3NvMXN2eGpieWM1cHU2NHp5Nng1ZGE4MndpaDViYWVudXRpaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C9x8gX02SnMIoAClXa/giphy-downsized-large.gif"
   "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdThld2pobGxzMjAxa2Q4bmkzZTRieTlpYjhkYWVvc2tyZ3o3MGEwcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihPSIgIXuZv/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")