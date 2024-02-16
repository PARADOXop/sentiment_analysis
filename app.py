import streamlit as st
import os
import sys
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline


model_path = "PARADOXop1002/text-classification"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=2)
inference = pipeline(model=model, tokenizer=tokenizer, task='sentiment-analysis')
os.makedirs('./models/', exist_ok=True)
tokenizer.save_pretrained('./models/')
model.save_pretrained('./models/')
st.title('This is a title') 
text = st.text_area('Enter your sentence here:')
if text:
    st.title(inference(text))
st.title('_PARADOXop_ is :blue[cool] :sunglasses:')

st.page_link("http://www.google.com", label="Linkedin", icon="🌎")
