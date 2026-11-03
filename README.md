# My Developer Digital Twin

An interactive AI twin dashboard built with Python and Streamlit, powered by large language models via the Groq API. This application acts as a digital agent capable of discussing technical backgrounds, coding skills, and probability foundations.

## 🧠 Architecture Upgrade: Retrieval-Augmented Generation (RAG)
This project has been upgraded from a basic conversational persona wrapper to a production-ready **Retrieval-Augmented Generation (RAG)** architecture. 

### Key Features
* **Dynamic Ingestion Pipeline:** Integrates a Streamlit frontend file uploader allowing runtime ingestion of custom PDF context background documents.
* **Groq Embeddings Integration:** Utilizes high-speed inference endpoints (`nomic-embed-text-v1.5`) to convert extracted text chunks into dense numeric vectors.
* **In-Memory Vector Orchestration:** Employs a low-latency, in-memory `QdrantClient` topology to manage similarity vector search.
* **Anti-Hallucination Guardrails:** Restricts system prompt completions strictly to verified context facts returned during database search operations.

## Features
- **Interactive AI Agent:** Employs advanced prompting guardrails to simulate professional responses.
- **Streamlit Web UI:** A clean, easy-to-use front-end interface for continuous interaction.
- **Fast Inference:** Connected to Groq's high-speed API endpoints.

## Getting Started

### Prerequisites
Make sure you have Python installed, then clone this repository.

### Installation
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

### Running the Application
Launch the local web server using:
```bash
streamlit run digital_twin_app.py
```
