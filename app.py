import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI # If using Gemini
# from langchain_openai import ChatOpenAI # If using OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts import CODE_REVIEW_PROMPT_TEMPLATE # Import from prompts.py

# Load environment variables
load_dotenv()

# --- LLM Configuration ---
LLM_PROVIDER = "google" # or "openai" - Change this to switch

llm = None
try:
    if LLM_PROVIDER == "google":
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
            st.error("GOOGLE_API_KEY not found in .env file.")
            st.stop()
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=GOOGLE_API_KEY,
                                 temperature=0.3) # Lower temp for more factual review
    # elif LLM_PROVIDER == "openai":
    #     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    #     if not OPENAI_API_KEY:
    #         st.error("OPENAI_API_KEY not found in .env file.")
    #         st.stop()
    #     llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY, temperature=0.3)
    else:
        st.error(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
        st.stop()

except Exception as e:
    st.error(f"Error initializing LLM: {e}")
    st.stop()
# --- End LLM Configuration ---

def get_code_review(code_snippet_str: str) -> str:
    if not llm:
        return "LLM not initialized."

    prompt = PromptTemplate.from_template(CODE_REVIEW_PROMPT_TEMPLATE)
    
    # Simple chain for now
    chain = prompt | llm | StrOutputParser()
    
    try:
        review = chain.invoke({"code_snippet": code_snippet_str})
        return review
    except Exception as e:
        st.error(f"Error getting review from LLM: {e}")
        return "Failed to get review."


def main():
    st.set_page_config(page_title="AI Code Review Assistant", page_icon="🤖")
    st.header("AI Code Review Assistant 🤖")

    st.write("Paste your code snippet below (e.g., Python) and get an AI-powered review.")

    # Default example code
    default_code = """
def calculate_fibonaci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a,b=0,1
        for _ in range(2,n):
            a,b = b,a+b
        return b

result = calculate_fibonaci(10)
print(result)
"""

    code_input = st.text_area("Enter Code Snippet Here:", value=default_code, height=300, key="code_input_area")

    # review_type = st.selectbox(
    #     "Select Review Type:",
    #     ("General Feedback", "Potential Bugs", "Style Check"),
    #     key="review_type_selector"
    # ) # We can add more sophisticated logic for review_type later

    if st.button("Review Code", key="review_button"):
        if code_input:
            with st.spinner("AI is reviewing your code..."):
                review_feedback = get_code_review(code_input)
                st.subheader("Review Feedback:")
                st.markdown(review_feedback) # Use markdown for better formatting of LLM output
        else:
            st.warning("Please enter some code to review.")

if __name__ == '__main__':
    main() 