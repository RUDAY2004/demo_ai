import os
from flask import Flask, request, jsonify
from voice_recognition import listen_to_audio
from text_to_speech import speak_text
from chatgpt_integration import get_response
import flipkart_scraper

app = Flask(__name__)

# Set Groq API Key
os.environ['GROQ_API_KEY'] = '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'

@app.route('/process-query', methods=['POST'])
def process_query():
    data = request.json
    query = data.get('query')

    if 'exit' in query.lower():
        return jsonify({'response': 'Exiting the program.'})

    # Get response from GroqCloud and Flipkart scraper
    gpt_response = get_response(query)
    product_info = flipkart_scraper.get_product_info(query)
    response = f"{gpt_response}\n{product_info}"

    # Respond back with the AI and product information combined
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
