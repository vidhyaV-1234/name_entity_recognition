import streamlit as st
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title("Named Entity Recognition with spaCy")

# Text input
user_input = st.text_area("Enter text:", "Tesla Inc is going to acquire Twitter Inc for $45 billion")

# Process the text
doc = nlp(user_input)

# Display entities
st.subheader("Named Entities")
if doc.ents:
    for ent in doc.ents:
        st.write(f"{ent.text} | {ent.label_} | {spacy.explain(ent.label_)}")
else:
    st.write("No named entities found.")

# Display entities visualization
st.subheader("Entity Visualization")
html = displacy.render(doc, style="ent", jupyter=False)
st.write(html, unsafe_allow_html=True)
