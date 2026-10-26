import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load hidden environment variables from the .env file
load_dotenv()

# Fetch the key from the environment variables list
api_key_value = os.getenv("GROQ_API_KEY")

# 2. Initialize the Groq client by passing the key value directly into it
client = Groq(api_key=api_key_value)


# 3. Our structured prompt blueprint function
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
    
    full_prompt = (
        f"=== SYSTEM INSTRUCTIONS ===\n{system_persona}\n\n"
        f"=== VERIFIED KNOWLEDGE ===\n{personal_facts}\n\n"
        f"=== CONSTRAINT GUARDRAILS ===\n{guardrails}\n\n"
        f"=== USER QUERY ===\nQuestion: {user_question}\n\n"
        f"Response:"
    )
    return full_prompt

# 4. Live Interactive Chat Loop
print("==================================================")
print("Digital Twin Live Agent Active! (Type 'quit' to exit)")
print("==================================================")

while True:
    # Accept typing directly from the user in the terminal
    user_query = input("\nAsk your Digital Twin a question: ")
    
    # Check if the user wants to leave the chat
    if user_query.lower() == 'quit':
        print("Closing chat. Goodbye!")
        break
        
    # Skip empty questions
    if not user_query.strip():
        continue
        
    # Package the prompt using our blueprint
    packaged_prompt = generate_digital_twin_prompt(user_query)
    
    print("Thinking...")
    
    # Make the live network call
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": packaged_prompt}
        ]
    )
    
    # Print out the results live
    print("\n=== DIGITAL TWIN RESPONSE ===")
    print(completion.choices[0].message.content)
    print("=============================")
