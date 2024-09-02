import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import PyPDF2
from gtts import gTTS  # Google Text-to-Speech
import speech_recognition as sr  # Speech Recognition
import tempfile

# Load environment variables
load_dotenv()

# Configure the Gemini Pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def extract_text_from_pdf(file):
    """Extracts text from the provided PDF file using PyPDF2."""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_gemini_response(question, context):
    """Gets a response from the Gemini model, including the provided context in the question."""
    full_message = context + "\n\n" + question
    response = chat.send_message(full_message, stream=True)
    return response

def text_to_speech(text):
    """Converts text to speech and returns the path to the audio file."""
    # Show "Generating Audio..." message
    st.info("Generating Audio...")
    
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    temp_file_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3').name
    tts.save(temp_file_path)
    
    # Update the status to "Audio generated!"
    st.success("Audio generated!")
    
    return temp_file_path

def recognize_speech():
    """Captures voice input from the user and returns it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak into the microphone.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.error("Error with the Speech Recognition service.")

def extract_texts_from_folder(folder):
    """Extracts and concatenates text from all PDF files in the given folder."""
    combined_text = ""
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            with open(os.path.join(folder, filename), "rb") as file:
                combined_text += extract_text_from_pdf(file)
    return combined_text

def store_feedback(user_input, bot_response):
    """Stores user input and bot response to the backend (e.g., database)."""
    # Implement the logic to store the conversation data
    # in your backend system (e.g., a database or an API endpoint).
    pass

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.title("SmartBot : Your PDF Assistant")

# Initialize session state for PDF context if it doesn't exist
if 'pdf_context' not in st.session_state:
    st.session_state['pdf_context'] = ""

if 'latest_audio_path' not in st.session_state:
    st.session_state['latest_audio_path'] = ""

# Folder upload
st.sidebar.header("Upload PDFs and ask Questions")
uploaded_folder = st.sidebar.file_uploader("Please upload max upto 5 PDFs.", type=None, accept_multiple_files=True)
if uploaded_folder:
    # Create a temporary directory to store uploaded files
    temp_dir = tempfile.TemporaryDirectory()
    for uploaded_file in uploaded_folder:
        with open(os.path.join(temp_dir.name, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())

    # Extract and combine text from all PDFs in the folder
    st.session_state['pdf_context'] = extract_texts_from_folder(temp_dir.name)
    st.sidebar.success("PDFs loaded successfully!")

# Voice input button
st.header("Voice Input")
if st.button("Speak Your Question"):
    input_text = recognize_speech()
    if input_text and st.session_state['pdf_context']:
        response = get_gemini_response(input_text, context=st.session_state['pdf_context'])
        response_text = ''.join([chunk.text for chunk in response])

        # Display "Response" and the text response
        st.subheader("Response")
        st.write(response_text)

        # Generate and display the audio after showing the response text
        audio_path = text_to_speech(response_text)
        st.session_state['latest_audio_path'] = audio_path  # Update latest audio path

        # Display the audio player
        audio_bytes = open(st.session_state['latest_audio_path'], "rb").read()
        st.audio(audio_bytes, format="audio/mp3")

        # Store the conversation as feedback in the backend
        store_feedback(input_text, response_text)

    elif not st.session_state['pdf_context']:
        st.write("Please upload PDFs first.")

# Text input for fallback or preference
st.header("Text Input")
input_text = st.text_input("Type Your Question:")
submit = st.button("Ask the question")

if submit and input_text:
    if st.session_state['pdf_context']:
        response = get_gemini_response(input_text, context=st.session_state['pdf_context'])
        response_text = ''.join([chunk.text for chunk in response])

        # Display "Response" and the text response
        st.subheader("Response")
        st.write(response_text)

        # Generate and display the audio after showing the response text
        audio_path = text_to_speech(response_text)
        st.session_state['latest_audio_path'] = audio_path  # Update latest audio path

        # Display the audio player
        audio_bytes = open(st.session_state['latest_audio_path'], "rb").read()
        st.audio(audio_bytes, format="audio/mp3")

        # Store the conversation as feedback in the backend
        store_feedback(input_text, response_text)

    else:
        st.write("Please upload a PDF folder first..")
