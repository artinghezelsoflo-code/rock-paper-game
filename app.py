from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "my_secret_game"

@app.route("/", methods=["GET", "POST"])
def game():
    session.setdefault("player", 0)
    session.setdefault("computer", 0)

    result = ""

    if request.method == "POST":
        choice = request.form.get("choice")
        choices = ["سنگ", "کاغذ", "قیچی"]

        if choice in choices and session["player"] < 5 and session["computer"] < 5:
            computer = random.choice(choices)

            if choice == computer:
                result = "مساوی شد! 🤝"

            elif (choice == "سنگ" and computer == "قیچی") or \
                 (choice == "کاغذ" and computer == "سنگ") or \
                 (choice == "قیچی" and computer == "کاغذ"):
                session["player"] += 1
                result = "تو برنده شدی! 🎉"
            else:
                session["computer"] += 1
                result = "کامپیوتر برنده شد! 🤖"

            result += " انتخاب کامپیوتر: " + computer

    winner = ""
    if session["player"] == 5:
        winner = "🏆 تو برنده نهایی شدی!"
    elif session["computer"] == 5:
        winner = "🤖 کامپیوتر برنده شد!"

    return render_template(
        "index.html",
        player=session["player"],
        computer=session["computer"],
        result=result,
        winner=winner
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("game"))

if __name__ == "__main__":
    app.run(debug=True)