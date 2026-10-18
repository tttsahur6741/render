from flask import Flask, request

app = Flask(__name__)

saved_messages = []


@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    user_text = request.form.get("msg")
    if user_text:
      saved_messages.append(user_text)

  return f"""
    <div style="font-family: Arial; max-width: 400px; margin: 50px auto; padding: 20px;">
        <h2>test 67 tung tung tung sahur</h2>
        <form method="POST">
            <input type="text" name="msg" placeholder="Type something..." style="padding: 8px; width: 70%;">
            <button type="submit" style="padding: 8px;">Save</button>
        </form>
        <h3>Saved Items:</h3>
        <ul>
            {"".join([f"<li>{msg}</li>" for msg in saved_messages])}
        </ul>
    </div>
    """


if __name__ == "__main__":
  app.run(debug=True, port=5000)