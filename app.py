from flask import Flask, render_template, request
import os
import aiml

BRAIN_FILE = "brain.dump"
app = Flask(__name__)

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get')
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = k.respond(user_input)
    return str(bot_response)

if __name__ == '__main__':
    app.run(debug=True)
