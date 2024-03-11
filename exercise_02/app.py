# I got help from the following resources:
# Flask Walkthrough: https://www.youtube.com/watch?v=oVA0fD13NGI&t=4298s
# Tyler Rebman, John Sulzen also helped me out!

from flask import Flask, render_template, request

app = Flask(__name__)

# Route to main page
@app.route("/")
def index():
    return render_template("index.html")

# Once the user inputs a number it calls this route
# Which calculates if the input is even or not
@app.route("/answer")
def answer():
    # Retrieve user input from argument list
    input = request.args.get("number", "")

    # If the answer is a number, calculate!
    if input.isnumeric():
        # Decision is equal to the inputted number plus a ternary operator
        # which says return even if the input cast as an int modulo 2 is equal to 0
        # else the number is odd and it should append as such
        decision = input + (" is Even" if int(input) % 2 == 0 else " is Odd")

    # Other cases include if the text entry was blank     
    elif input == "":
        decision = "No Input Provided!"
    # or if the entry was a string with other characters than numbers 
    # which obviously means the entry is not an integer
    else:
        decision = input + " is not an Integer!"

    # Return the answer page with the decision attached as a variable
    return render_template("answer.html", outcome = decision)