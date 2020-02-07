from flask import Flask, render_template
import pandas as pd
import time

app = Flask(__name__)

# Time variables
t = time.localtime()
current_time = int(time.strftime("%M", t))


####### HANDLING DATA BEARLY AWAKE
df = pd.read_csv('inputs.csv', delimiter=',', usecols = ['Titles'])
titles = [list(x) for x in df.values]

df = pd.read_csv('inputs.csv', delimiter=',', usecols = ['Submitters'])
submitters = [list(x) for x in df.values]

df = pd.read_csv('inputs.csv', delimiter=',', usecols = ['Audiences'])
audiences = [list(x) for x in df.values]

df = pd.read_csv('inputs.csv', delimiter=',', usecols = ['Texts'])
texts = [list(x) for x in df.values]


del titles[0]
del submitters[0]
del audiences[0]
del texts[0]

length = len(titles)

for i in range(length):

    titles[i] = str(titles[i])[2:]
    titles[i] = str(titles[i])[:-2]

    submitters[i] = str(submitters[i])[2:]
    submitters[i] = str(submitters[i])[:-2]

    audiences[i] = str(audiences[i])[2:]
    audiences[i] = str(audiences[i])[:-2]

    texts[i] = str(texts[i]).split("\\n")
    texts[i][0] = texts[i][0][2:]
    texts[i][-1] = texts[i][-1][:-2]

########


if True:
    @app.route("/")
    def index():
        return render_template("index.html", titles=titles, submitters=submitters, audiences=audiences, texts=texts, length=length)
else:
    #### NIGHTMODE
    @app.route("/")
    def index():
        return render_template("nightmode.html")






if __name__ == "__main__":
    app.run(debug=True)

