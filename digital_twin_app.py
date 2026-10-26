import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# 1. Load configuration and secret key
load_dotenv()
api_key_value = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key_value)

# 2. Re-import your prompt blueprint function logic
def generate_digital_twin_prompt(user_question):
    system_persona = (
        "You are the AI Digital Twin of an aspiring AI Application Developer. "
        "Respond in a confident, encouraging, and highly technical tone."
    )
    personal_facts = (
        "- Background: Completed 'Building with LLMs' training course.\n"
        "- Current Project: Building an independent Digital Twin in VS Code.\n"
        "- Skills: Local Python development, Virtual Environments, NumPy math foundations."
    )
    guardrails = (
        "CRITICAL RULES:\n"
        "- Base your answer ONLY on the personal facts provided above.\n"
        "- If asked about experiences or topics not listed, reply strictly with: "
        "'I have not logged that specific experience in my knowledge base yet.'"
    )
    return (
        f"=== SYSTEM INSTRUCTIONS ===\n{system_persona}\n\n"
        f"=== VERIFIED KNOWLEDGE ===\n{personal_facts}\n\n"
        f"=== CONSTRAINT GUARDRAILS ===\n{guardrails}\n\n"
        f"=== USER QUERY ===\nQuestion: {user_question}\n\n"
        f"Response:"
    )

# 3. Streamlit Page Design Elements
st.title("🤖 My Developer Digital Twin")
st.write("Ask my AI double anything about my skills, background, or current focus!")

# 4. Text Input field for the user to chat
user_query = st.text_input("Type your question here:")

if user_query:
    st.write(f"Thinking about your question: *'{user_query}'*...")
    
    # Package prompt and call the active Groq engine
    packaged_prompt = generate_digital_twin_prompt(user_query)
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": packaged_prompt}]
    )
    
    # Display results inside a nice UI box layout block
    st.subheader("Twin Response:")
    st.info(completion.choices[0].message.content)
