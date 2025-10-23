from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

bot = ChatBot(
    "chatbot",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, but I do not understand.",
            "maximum_similarity_threshold": 0.90
        }
    ]
)


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get")
def get_chatbot_response():
    userText = request.args.get("userMessage")
    return jsonify(str(bot.get_response(userText)))

if __name__ == "__main__":
    app.run(debug=True)