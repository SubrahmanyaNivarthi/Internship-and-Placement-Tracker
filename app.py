from flask import Flask, render_template, request, redirect, url_for, session
import PyPDF2

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        dob = request.form.get("dob")
        session["username"] = username
        session["email"] = email
        session["dob"] = dob
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("dashboard.html")

@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("profile.html",
                           username=session["username"],
                           email=session["email"],
                           dob=session["dob"])

@app.route("/resume", methods=["POST"])
def resume():
    if "resume" not in request.files:
        return "No file uploaded", 400
    file = request.files["resume"]
    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        keywords = [word for word in text.split() if word.lower() in ["python", "java", "sql", "ml", "ai"]]
        return render_template("resume.html", text=text, keywords=keywords)
    return "Please upload a PDF file", 400

if __name__ == "__main__":
    app.run(debug=True)
