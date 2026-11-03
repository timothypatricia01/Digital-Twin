import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from rag_storage import DigitalTwinRAG
rag = DigitalTwinRAG()
# Create a neat sidebar section for managing your twin's memory data documents
st.sidebar.title("📚 Memory Management")
uploaded_file = st.sidebar.file_uploader("Upload background knowledge PDF", type=["pdf"])

if uploaded_file is not None:
    # Build a temporary filepath directory to store incoming files safely
    temp_dir = "storage_temp"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, uploaded_file.name)
    
    # Write the bytes down to the file system so pypdf can read it
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    with st.sidebar.spinner("Processing document..."):
        rag.ingest_pdf(temp_path)
    st.sidebar.success(f"Successfully memorized {uploaded_file.name}!")

# 1. Load configuration and secret key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = Groq(api_key=groq_api_key)


# 2. Re-import your prompt blueprint function logic
def generate_digital_twin_prompt(user_question):
    retrieved_facts = rag.retrieve_context(user_question, top_k=3)
    system_persona = f"""
    You are the AI Digital Twin of an aspiring AI Engineer.
    Respond in a confident, encouraging, and highly professional manner.
    Crucial Rule: Answer the user's message using ONLY the provided verified context facts below.
    
    VERIFIED DATABASE CONTEXT:
    {retrieved_facts}
    
    If the answer cannot be found in the context above, strictly say 'I don't remember or have data on that' to avoid hallucinating.
    """

    personal_facts = (
        "- Background: Completed 'Building with LLMs' training\n"
        "- Current Project: Building an independent Digital Twin app\n"
        "- Skills: Local Python development, Virtual environments"
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
        messages=[
            {"role": "system", "content": packaged_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    # Display results inside a nice UI box layout block
    st.subheader("Twin Response:")
    st.info(completion.choices[0].message.content)
