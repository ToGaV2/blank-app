# 🎈 Simple Groq Chat LLM Implementation with LLaMa 3.1

Ever wanted to build a super fast chat engine inside a  python streamlit? Groq, SambaNova, and Cerebras are the fastest 3 at the time of publishing. Each is built in a way that integrates pretty seamlessly into a streamlit app. The example here is built with Groq.
 
There are only a few steps to get your implementation running: 
- You'll need a login at Groq, where you can get an API Key.
- Load the API key into the toml as instructed in step 2.
- Load the software as instructed in step 1.
- Run the program. Enjoy!

Want to try mine? [![Okay, Click here to open now in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Get a Groq API key
   
   ```
   https://console.groq.com/keys

   install this in CWD/.streamlit/secrets.toml as "GROQ_API_KEY"
   ```

4. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
