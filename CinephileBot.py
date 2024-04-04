from flask import Flask, render_template, request, jsonify
import openai

# Configurez votre clé API de ChatGPT
openai.api_key = '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'

# Fonction pour filtrer les questions sur le cinéma
def is_cinema_related(prompt):
    cinema_keywords = ['film', 'cinéma', 'acteur', 'actrice', 'réalisateur', 'scénario', 'Bonjour', 'Merci']
    for keyword in cinema_keywords:
        if keyword in prompt:
            return True
    return False

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if is_cinema_related(user_input):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=150
        )
        bot_response = response.choices[0].text.strip()
    else:
        bot_response = "Désolé, je ne peux répondre qu'aux questions sur le cinéma."
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)