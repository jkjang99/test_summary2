import streamlit as st
import openai

def summarize_text(text, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize this text in 3 sentences: {text}",
        max_tokens=100,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    return summary

def generate_hashtags(text, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate 5 hashtags for this text: {text}",
        max_tokens=50,
        temperature=0.5,
    )
    hashtags = response.choices[0].text.strip().split("\n")
    return hashtags

st.title("Text Summarizer and Hashtag Generator")

api_key = st.text_input("Enter your OpenAI API Key:", type="password")
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
