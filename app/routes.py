from flask import request, redirect, render_template

def routes(app, check_pwned_password):
    @app.route("/", methods=["POST", "GET"])
    def main():
        if request.method == "GET": 
            return render_template("main.html")
        else:
            password = request.form.get("password")
            status, result_message, res = check_pwned_password(password)
            if status:
                if res:
                    message = f"Oh no — pwned! This password has been seen {res} times before."
                else:
                    message = f"Good news — no pwnage found!"
            else:
                message = result_message
            return render_template("main.html", message=message)
