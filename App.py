import streamlit as st
import google.generativeai as genai

# 1. Configure the Page
st.set_page_config(page_title="Viral Script Generator", page_icon="🚀")

# 2. Add your API Key securely
# (We will set this up in Step 4, don't paste your key directly here for safety)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 3. Define the System Prompt
SYSTEM_PROMPT = """
[PASTE THE SYSTEM PROMPT FROM PHASE 2 HERE INSIDE THESE QUOTES]
"""

# 4. The Website Layout
st.title("🚀 Viral Hook & Script Generator")
st.subheader("Turn a boring topic into 10k views.")

# User Input
topic = st.text_input("What is your video about?", placeholder="e.g. How to save money on groceries")
tone = st.selectbox("Choose Tone", ["Funny", "Controversial", "Educational", "Urgent"])

# 5. The Magic Button
if st.button("Generate Viral Script"):
    if not topic:
        st.warning("Please enter a topic first!")
    else:
        with st.spinner('Cooking up something viral...'):
            try:
                # Call Gemini
                model = genai.GenerativeModel('gemini-1.5-pro')
                full_prompt = f"{SYSTEM_PROMPT}\n\nUSER TOPIC: {topic}\nTONE: {tone}"
                response = model.generate_content(full_prompt)
                
                # Display Result
                st.markdown("---")
                st.markdown(response.text)
                st.success("Copy this script and film it!")
                
            except Exception as e:
                st.error(f"Error: {e}")
st.write("---")
st.write("### 🛠 Debug: Available Models")
if st.button("List My Models"):
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                st.code(m.name)
    except Exception as e:
        st.error(e)
# 6. Viral Loop (Free Marketing)
st.markdown("---")

st.caption("Built for free. Share this tool with a creator friend!")

