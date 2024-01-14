import speech_recognition as sr

def convert_audio_to_text(audio_file_path, language='bn-BD'):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return ""

# Example usage
audio_file_path = "Duah.wav"  # Replace with the path to your audio file
extracted_text = convert_audio_to_text(audio_file_path)

print("Extracted Text:")
print(extracted_text)
