import speech_recognition as sr  # import the speech recognition library

r = sr.Recognizer()  # create a recognizer object that processes audio

while True:  # keep looping until we successfully get a result
    with sr.Microphone() as source:  # open the microphone as the audio source
        print("say something...")

        # listen to the room for 0.5s and calibrate so background
        # noise doesn't get picked up as speech
        r.adjust_for_ambient_noise(source, duration=0.5)

        # record audio until you stop speaking
        audio = r.listen(source)

    try:
        # send the recorded audio to Google's speech API
        # and convert it to text — this can fail, hence try/except
        text = r.recognize_google(audio)
        print("What you said:", text)
        break  # success! exit the loop

    except sr.UnknownValueError:
        # Google heard the audio but couldn't make out any words
        # (mumbling, too much noise) → ask the user to retry
        print("Sorry, I couldn't understand the audio.")

    except sr.RequestError as e:
        # network/API problem (no internet, service down) → can't
        # recover by retrying, so print the error and give up
        print(f"Could not request results; {e}")
        break