import streamlit as st
import openai

def summarize_text(text, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=[
            {"role": "system", "content": "Summarize the following text in 3 sentences."},
            {"role": "user", "content": text}
        ]
    )
    summary = response.choices[0].message['content'].strip()
    return summary

def generate_hashtags(text, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=[
            {"role": "system", "content": "Generate 5 hashtags for the following text."},
            {"role": "user", "content": text}
        ]
    )
    hashtags = response.choices[0].message['content'].strip().split("\n")
    return hashtags

st.title("Text Summarizer and Hashtag Generator")

api_key = st.text_input("Enter your OpenAI API Key:")
text = st.text_area("Enter the text you want to summarize:", height=200)

if st.button("Summarize and Generate Hashtags"):
    if api_key and text:
        summary = summarize_text(text, api_key)
        hashtags = generate_hashtags(text, api_key)
        
        st.subheader("Summary")
        st.write(summary)
        
        st.subheader("Hashtags")
        st.write(", ".join(hashtags))
    else:
        st.error("Please enter both the API key and the text.")
