import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import firestore

# Load the Firestore key from Streamlit secrets
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project=st.secrets["project"])

# Streamlit widgets to let a user create a new post
title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

# Once the user has submitted, upload it to the database
if title and url and submit:
    doc_ref = db.collection("posts").document(title)
    doc_ref.set({"title": title, "url": url})

# And then render each post, using some light Markdown
posts_ref = db.collection("posts")
for doc in posts_ref.stream():
    post = doc.to_dict()
    title = post["title"]
    url = post["url"]

    st.subheader(f"Post: {title}")
    st.write(f":link: [{url}]({url})")
