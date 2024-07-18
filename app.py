from flask import Flask, request, jsonify, render_template
import openai
import logging
import json

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

openai.api_key = 'your-api-key'  # Replace with your actual API key

# Example wine data corpus
with open('wine.json', 'r', encoding='utf-8') as f:
    wine_data = json.load(f)

def find_answer(query):
    for wine in wine_data['wines']:
        if wine['name'].lower() in query.lower() or wine['type'].lower() in query.lower():
            return f"{wine['name']}: {wine['description']} - {wine['price']}"
    return None

def get_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )
        logging.debug(f"API response: {response}")
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "Sorry, there was an error generating a response."

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_chat_response():
    data = request.json
    user_query = data['query']
    logging.debug(f"User query: {user_query}")

    # Try to find answer from local corpus
    answer = find_answer(user_query)
    if answer:
        logging.debug(f"Found local answer: {answer}")
        return jsonify({"response": answer})

    # Fallback to OpenAI API
    logging.debug("Using OpenAI API for response")
    ai_response = get_response(user_query)
    logging.debug(f"AI response: {ai_response}")
    return jsonify({"response": ai_response})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    ai_response = generate_openai_response(user_input)
    return jsonify({'message': user_input, 'response': ai_response})

def generate_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
