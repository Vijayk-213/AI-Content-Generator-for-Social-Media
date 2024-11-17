import requests
from textblob import TextBlob

import nltk
nltk.download('punkt_tab')

# Set your Gemini API credentials here
# GEMINI_API_KEY = 'AIzaSyB7fsn1vfkUo-YV0QwEXewy1T4kmbERmYY'
# GEMINI_API_URL = 'https://api.gemini-platform.com/v1/generate'

# Function to generate content using Gemini API
# def generate_content(prompt, max_tokens=100, temperature=0.7):
#     headers = {
#         "Authorization": f"Bearer {GEMINI_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "prompt": prompt,
#         "max_tokens": max_tokens,
#         "temperature": temperature
#     }
#     try:
#         response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
#         response.raise_for_status()
#         data = response.json()
#         return data.get("text", "Error: No content generated")
#     except requests.exceptions.RequestException as e:
#         return f"Error: {e}"
import os
from openai import OpenAI
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

def generate_content(prompt, max_tokens=100, temperature=0.7):
    # Pick one of the Azure OpenAI models from the GitHub Models service
    model_name = "gpt-4o-mini"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": f"Generate a good social media post for given prompt {prompt}",
            },
        ],
        model=model_name,
        # Optional parameters
        temperature=1.,
        max_tokens=1000,
        top_p=1.    
    )

    return response.choices[0].message.content

# Function to customize the prompt based on tone and audience
def customize_prompt(prompt, tone='casual', audience='general'):
    if tone == 'professional':
        prompt = f"Write a professional post: {prompt}"
    elif tone == 'friendly':
        prompt = f"Write a friendly and engaging post: {prompt}"
    elif tone == 'humorous':
        prompt = f"Add a humorous touch: {prompt}"
    return prompt

# Function to generate hashtags based on content
def generate_hashtags(content):
    blob = TextBlob(content)
    keywords = blob.noun_phrases
    hashtags = [f"#{keyword.replace(' ', '')}" for keyword in keywords if len(keyword) > 2]
    return hashtags[:5]  # Return top 5 hashtags

# Function to analyze sentiment of the content
def analyze_sentiment(content):
    blob = TextBlob(content)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
