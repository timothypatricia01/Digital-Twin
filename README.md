# My Developer Digital Twin

An interactive AI twin dashboard built with Python and Streamlit, powered by large language models via the Groq API. This application acts as a digital agent capable of discussing technical backgrounds, coding skills, and probability foundations.

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
