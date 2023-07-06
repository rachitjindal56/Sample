from flask import Flask, jsonify, request
import openai
import os
from dotenv import load_dotenv
import random
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
import numpy


app = Flask(__name__)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

def sentiment_transformer(inp:str):
    encoded_input = tokenizer(inp, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    return numpy.argmax(scores)

@app.route('/',methods=['POST'])
def home():
    if request.method == 'POST':
        
        response = ""
        
        response_sentiment = sentiment_transformer("Let's proceed to apply now")
        print(response_sentiment,end="\n")
        
        if response_sentiment == 2:
            response = "Proceed for further steps"
        
        else:
            intents_sample = ["Inspire me","Tell something interesting","Don't feel interested", "Tell me something interesting about me",
                            "Tell something interesting about my capabilities","Hmm, what to do?",
                            "Hmm","Oh"]
            
            gpt_response = openai.Completion.create(
                model="text-curie-001",
                prompt=intents_sample[random.randint(0,len(intents_sample)-1)],
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"])
            
            response = gpt_response['choices'][0]['text']
        
        print(response)
        
        return jsonify({
            "responses": [
                {
                    "type": 'randomText',
                    "messages": [response.lstrip().rstrip()]
                }
            ]
        })

@app.route('/', methods = ['GET'])
def disp():
    return request.args.get('challenge')

if __name__ == '__main__':
	app.run(debug = True)