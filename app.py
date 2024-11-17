from flask import Flask, render_template, request
from content_generator import generate_content, generate_hashtags, analyze_sentiment, customize_prompt

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Generate content route
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    tone = request.form.get('tone', 'casual')
    audience = request.form.get('audience', 'general')

    # Customize and generate content
    customized_prompt = customize_prompt(prompt, tone, audience)
    content = generate_content(customized_prompt)
    hashtags = generate_hashtags(content)
    sentiment = analyze_sentiment(content)

    return render_template('result.html', content=content, hashtags=hashtags, sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
