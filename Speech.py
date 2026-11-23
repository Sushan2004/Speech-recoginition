import Speech_recognition as sr

r = sr.recognizer()


while True: # with this there wont be infinit loop
# use the microphone

 with sr.Microphone() as source:
    print("say something...")

# lets adjust the noise mainly ambient noise
 r.adjust_for_ambient_noise( source, duration = 0.5)

 audio = r.listen(source) # listen for audio

 try: # this will not crash the code and jumps to a handler i.e 
    text = r.recoginze_google(audio) # sends audio to the Google
    print( " what you said", text)
    break
except sr.UnkownValueError:
    print ("Sorry, I couldn't understand the audio.")
except sr.RequestErroe as e:
    print(f"Counld not request results;{e}")
    break




