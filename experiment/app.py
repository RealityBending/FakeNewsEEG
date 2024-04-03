from flask import Flask, render_template
# import tobii_research as tr 

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
# found_eyetrackers = tr.find_all_eyetrackers()
# print(found_eyetrackers)