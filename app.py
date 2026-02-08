import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from textblob import TextBlob
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Voice Emotion Dashboard", layout="wide")
st.title("🎙️ Voice Emotion Timeline Dashboard")

# ---------------------------
# Emotion Mapping Function
# ---------------------------
def map_emotion(polarity):
    if polarity > 0.4:
        return "Happy"
    elif polarity > 0.1:
        return "Calm"
    elif polarity >= -0.1:
        return "Neutral"
    elif polarity >= -0.4:
        return "Sad"
    else:
        return "Angry"

# ---------------------------
# Audio Upload
# ---------------------------
audio_file = st.file_uploader(
    "Upload an audio file (WAV / MP3)",
    type=["wav", "mp3"]
)

if audio_file:
    st.info("Processing audio... please wait")

    with open("input_audio.wav", "wb") as f:
        f.write(audio_file.read())

    audio = AudioSegment.from_file("input_audio.wav")
    recognizer = sr.Recognizer()

    CHUNK_LEN = 10 * 1000  # 10 seconds
    results = []

    for i, chunk in enumerate(audio[::CHUNK_LEN]):
        chunk_file = f"chunk_{i}.wav"
        chunk.export(chunk_file, format="wav")

        with sr.AudioFile(chunk_file) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
            except:
                text = ""

        polarity = TextBlob(text).sentiment.polarity
        emotion = map_emotion(polarity)

        results.append({
            "Start (sec)": i * 10,
            "End (sec)": (i + 1) * 10,
            "Emotion": emotion,
            "Polarity": polarity,
            "Transcript": text
        })

        os.remove(chunk_file)

    df = pd.DataFrame(results)

    # ---------------------------
    # Dashboard
    # ---------------------------
    st.subheader("📊 Emotion Change Over Time")

    fig = px.scatter(
        df,
        x="Start (sec)",
        y="Emotion",
        title="Emotion Timeline (Every 10 Seconds)",
        size=[1]*len(df)
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📋 Detailed Emotion Log")
    st.dataframe(df, use_container_width=True)

    st.success("Analysis completed successfully!")
