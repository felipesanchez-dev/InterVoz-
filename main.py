# Import necessary libraries
import gradio as gr
import whisper
from translate import Translator
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

# Define ElevenLabs API key
ELEVENLABS_API_KEY = "ElevenLabs API key"

# Main function to handle voice translation
def translator(audio_file):
    """
    Transcribes an audio file in Spanish, translates it to multiple languages, and
    converts the translations to audio files in each target language.
    
    Arguments:
    - audio_file: Path to the input audio file in Spanish.
    Returns:
    - Paths to audio files containing translations in English, Italian, French, and Japanese.
    """
    
    try:
        # Load Whisper model and transcribe audio file in Spanish
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(f"Error occurred during transcription: {str(e)}")
    
    print(f"Original text: {transcription}")
    
    try:
        # Translate the Spanish transcription to other languages
        en_transcription = Translator(from_lang="es", to_lang="en").translate(transcription)
        it_transcription = Translator(from_lang="es", to_lang="it").translate(transcription)
        fr_transcription = Translator(from_lang="es", to_lang="fr").translate(transcription)
        ja_transcription = Translator(from_lang="es", to_lang="ja").translate(transcription)
    except Exception as e:
        raise gr.Error(f"Error occurred during translation: {str(e)}")
    
    # Print translated texts for debugging or confirmation
    print(f"Translated to English: {en_transcription}")
    print(f"Translated to Italian: {it_transcription}")
    print(f"Translated to French: {fr_transcription}")
    print(f"Translated to Japanese: {ja_transcription}")
    
    # Convert each translation to audio and save paths to audio files
    en_save_file_path = text_to_speach(en_transcription, "en")
    it_save_file_path = text_to_speach(it_transcription, "it")
    fr_save_file_path = text_to_speach(fr_transcription, "fr")
    ja_save_file_path = text_to_speach(ja_transcription, "ja")
    
    return en_save_file_path, it_save_file_path, fr_save_file_path, ja_save_file_path

# Helper function to convert text to speech and save the audio file
def text_to_speach(text: str, language: str) -> str:
    """
    Converts a text string to speech using ElevenLabs API and saves it as an audio file.
    
    Arguments:
    - text: The text to convert to audio.
    - language: The target language for file naming.
    
    Returns:
    - The path to the saved audio file.
    """
    
    try:
        # Initialize ElevenLabs client and generate speech from text
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Using Adam's voice
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
        save_file_path = f"{language}.mp3"
        
        # Save the response to an audio file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
    except Exception as e:
        raise gr.Error(f"Error occurred while creating audio: {str(e)}")
    
    return save_file_path

# Web server interface for the user
web = gr.Interface(
    fn=translator,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Español"
    ),
    outputs=[
        gr.Audio(label="English"),
        gr.Audio(label="Italian"),
        gr.Audio(label="French"),
        gr.Audio(label="Japanese")
    ],
    title="Voice Translator",
    description="AI-powered voice translator to multiple languages"
)

# Launch the web application
web.launch()
