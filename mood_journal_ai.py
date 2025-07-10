import streamlit as st

st.set_page_config(page_title="Mood Journal AI")

st.title("🧠 Mood Journal AI")
st.write("Type your feelings below and I’ll guess your mood!")

# User input box
journal = st.text_area("How are you feeling today?", "")

# Show what the user typed
if journal:
    st.write("You wrote:")
    st.write(journal)
