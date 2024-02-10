from flask import Flask, render_template, request, jsonify
from transformers import BertForSequenceClassification, BertTokenizer, TextClassificationPipeline
model_path = "JiaqiLee/imdb-finetuned-bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=2)
pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/post_example', methods=['POST'])
def post_example():
    if request.method == 'POST':
        # Get JSON data from the request
        data = request.json

        # Process the data (replace this with your logic)
        processed_data = {'received_data': data['input_data']}
        print(processed_data['received_data'])
        text = pipeline(processed_data)
        print(text)
        return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)