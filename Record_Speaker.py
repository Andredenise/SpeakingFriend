import keyboard
import sounddevice as sd
from time import sleep, time
import speech_recognition as sr


# Option 1
# -----------------------------------------------

print("Press spacebar to start recording")
# Choose a sample rate that is compatible with your hardware
sampling_rate = 44100
duration = 5  # seconds

# Start recording the user
if keyboard.is_pressed(' '): 
    original_wav = sd.rec(duration*sampling_rate, sampling_rate, 1, dtype='int32')

# Display a progress bar while recording
# Get current time to keep track of recording length
start_time = time()
print("Press enter to stop recording")
input()  # This blocks the program from continuing until user presses enter

# Trim wav to actual length of recording
recording_length = time() - start_time
if recording_length < duration:
    original_wav = original_wav[:int(recording_length*sampling_rate)]

# Save as WAV file in 32-bit format
write('output.wav', sampling_rate, original_wav.astype(np.int32))
sound = "output.wav"

# Convert audio to text
r = sr.Recognizer() # initialise a recogniser
with sr.AudioFile(sound) as source:
   r.adjust_for_ambient_noise(source)
   audio = r.listen(source)
   voice_data = r.recognize_google(audio)



# Option 2
# -----------------------------------------------

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    print("Start speeking")
    with sr.Microphone() as source: # microphone as source
        if ask:
            print(ask)
        try:
            audio = r.listen(source, 8, 8)  # listen for the audio via source
        except sr.WaitTimeoutError:
            exit()
        print("Terminé de escucharte fuerte y claro")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('No te escuché bien')
            return record_audio("Repítelo, porfavor")
        except sr.RequestError:
            print('Disculpa, el servidor se cayó') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()


voice_data = record_audio() # get the voice input

# The output from the recording has to go in the interact_gpt_model as input
