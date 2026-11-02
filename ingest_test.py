from rag_storage import DigitalTwinRAG
import os

# Initialize our database controller
rag = DigitalTwinRAG()

# TODO: Put a real PDF file inside your Digital Twin folder, 
# then replace 'my_profile.pdf' below with its exact name!
pdf_filename = "my_profile.pdf"

if os.path.exists(pdf_filename):
    print(f"Starting to ingest: {pdf_filename}...")
    rag.ingest_pdf(pdf_filename)
    print("Successfully memorized document!")
else:
    print(f"Error: Please drop your PDF file into the folder and name it '{pdf_filename}' first!")
