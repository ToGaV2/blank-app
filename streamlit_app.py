import streamlit as st 
from groq import Groq


st.title("Groq Test Bed")
st.write(
    "Let's start..."
)



def groqit(uprompt:str) -> str: 
    client = Groq( 
        api_key = st.secrets['GROQ_API_KEY']
        )
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                 
            "role": "system",
            "content": "you are an expert"
            },
            {
            "role": "user",
            "content": uprompt
            }
            
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
        )
    x = []
    for chunk in completion:
        x.append(chunk.choices[0].delta.content )

    return x

with st.form('q1', clear_on_submit=False, border=True):

    user_question = st.text_input("Ask a question here:")
    submitbutton = st.form_submit_button('Submit the Question.')

    if submitbutton:
        st.write("Question: " , user_question)
        if user_question.isalnum and user_question is not None:
            res = groqit(user_question)
            outputs = []
         
            st.write("Response: " , str("".join(y for y in res if y is not None)))
        else:
            st.write("The question has illegal characters. Remove illegal characters and resubmit.")

