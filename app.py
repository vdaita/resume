import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

hugging_face_email = st.secrets["hf_email"]
hugging_face_password = st.secrets["hf_password"]

sign = Login(hugging_face_email, hugging_face_password)
cookies = sign.login()
sign.saveCookies()

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

st.title("Try using LLMs to refine your resume!")

resume_area = st.text_area("Resume", placeholder="Copy and paste key parts of your resume, adding as much detail as you can")
job_description_area = st.text_area("Job Description", placeholder="Add your job description here, including as much information as possible about key skills")


def process():
    # st.session_state["disabled"] = b
    prompt = """Write a tailored CV for the following job application " """ + job_description_area \
    + """ " using the profile of someone with the following resume: " """ + resume_area + '"'
    output = chatbot.chat(prompt)
    st.write(output)
    # st.session_state["disabled"] = None

process_btn = st.button('Process', key="btn", on_click=process)
