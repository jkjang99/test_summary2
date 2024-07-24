app_py_content = """
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_summary_and_tags(text, max_length_summary=50):
    # Encode input text
    inputs = tokenizer.encode(text, return_tensors="pt")
    
    # Generate summary
    summary_ids = model.generate(inputs, max_length=max_length_summary, num_return_sequences=1, no_repeat_ngram_size=2)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    # Generate hashtags (simple example, can be improved)
    words = text.split()
    hashtags = [f"#{word.strip(',.!?').lower()}" for word in words[:5]]
    
    return summary, hashtags

# Streamlit app
st.title("Text Summary and Hashtag Generator")

text_input = st.text_area("Enter text to summarize:", "")
if st.button("Generate Summary and Hashtags"):
    if text_input:
        summary, hashtags = generate_summary_and_tags(text_input)
        st.subheader("Summary:")
        st.write(summary)
        st.subheader("Hashtags:")
        st.write(" ".join(hashtags))
    else:
        st.write("Please enter some text to summarize.")
"""

with open('/mnt/data/app.py', 'w') as f:
    f.write(app_py_content)
