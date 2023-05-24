from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/IGotIt.gif",
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/MustHaveWater.gif",
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/KitteninMilk.gif",
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/GoingforaWalk.gif",
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/TankCat.gif",
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/SelfBrush.gif",
   "https://moderncat-wpengine.netdna-ssl.com/sites/default/files/images/uploads/HanaandMaru.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")