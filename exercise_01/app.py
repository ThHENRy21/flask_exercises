# I got help from the following resources:
# Flask Walkthrough: https://www.youtube.com/watch?v=oVA0fD13NGI&t=4298s
# Tyler Rebman, John Sulzen also helped me out!

from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Gets the current date and time
@app.route('/')
def index():
    now = datetime.now()
    # Returns the time in the form "day of the week, Month Day Year Time"
    return "The current date and time is " + now.strftime("%A, %B %d %Y %X")

if __name__ == "__main__":
    app.run(debug = True)
