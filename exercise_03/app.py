# I got help from the following resources:
# Flask Walkthrough: https://www.youtube.com/watch?v=oVA0fD13NGI&t=4298s
# Tyler Rebman, John Sulzen also helped me out!

from flask import Flask, render_template, request

app = Flask(__name__)

# Create dict for list of students and their cooresponding orgs
studentsRegistered = {}
# Hard Coded Orgs for selection
organizations = ["Chess", "Running", "Fencing", "Rotary", "Cooking"]

# Route to home
@app.route("/")
def index():
    # load page, passing the orgs array as a variable
    return render_template("index.html", organizations=organizations)

# When user submits the form, this activates
@app.route("/register", methods=["POST"])
def register():
    # Retrives the name and organization fields from the form
    name = request.form.get("name")
    organization = request.form.get("organization")

    # Set them to a key-value pair in the registration dict
    studentsRegistered[name] = organization
    # Send user to registration roster with the registration passed as a variable
    return render_template("studentRegister.html", studentsRegistered=studentsRegistered)

# If the user wants to visit the registration without inputting info
@app.route("/studentRegister")
def studentRegister():
    # Still need to pass the register as the stored info will be shown on the next page
    return render_template("studentRegister.html", studentsRegistered=studentsRegistered)