
#with start button

import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-US')  # Use 'en-US' for English language
        return text
    except sr.UnknownValueError:
        return "Sorry, couldn't recognize speech"
    except sr.RequestError:
        return "Sorry, there was an error requesting speech recognition service"

# Here you can integrate the recognized text into your chatbot

while True:
    user_input = input("Enter on the keyboard 's' to start speech recognition: ")
    if user_input.lower() == "s":
        speech_text = recognize_speech()
        print("Recognized text:", speech_text)
    else:
        print("Invalid command")




# Without Start button
# import speech_recognition as sr

# def record_volume():
#     r = sr.Recognizer()  # Create a Recognizer object from the SpeechRecognition library
#     with sr.Microphone(device_index=0) as source:  # Open the microphone as the audio source
#         print("Say something!")  # Display a message on the screen
#         audio = r.listen(source)  # Record audio from the microphone

#     try:
#         text = r.recognize_google(audio, language='en-US')  # Attempt to recognize speech using the Google Web Speech API
#         print("You said: {}".format(text))  # Display the recognized text
#     except:
#         print("Sorry, I didn't understand.")  # Display an error message in case of an exception

# record_volume()  # Call the function to start recording and speech recognition
