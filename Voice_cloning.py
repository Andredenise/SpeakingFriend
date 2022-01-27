# For the voice cloning we need a recorded sample of what the speaker said so he can start cloning
# And we need a text input from the gpt_model so that he knows what to say

import librosa
from voice_cloning_files.synthesizer.utils import text
from voice_cloning_files.synthesizer.inference import Synthesizer
from voice_cloning_files.encoder_voice_cloning import inference as encoder
from voice_cloning_files.vocoder_voice_cloning import inference as vocoder
from Blender_Bot import BB
import sounddevice as sd
import numpy as np
from time import sleep, time
import speech_recognition as sr
from scipy.io.wavfile import write
from pathlib import Path

class RTVC:
    def __init__(self,
                 wav_path='output.wav',
                 sampling_rate=44100,
                 duration=5,
                 encoder_model="pretrained.pt",
                 synthesizer_model="pretrained.pt",
                 vocoder_model="pretrained.pt"):
        self.wav_path = wav_path
        self.sampling_rate = sampling_rate
        self.duration = duration
        self.encoder_model = encoder_model
        self.synthesizer_model = synthesizer_model
        self.vocoder_model = vocoder_model
        self.encoder = None
        self.synthesizer = None
        self.vocoder = None
        self.blender_bot = None
        self._load()

    def _load(self):
        print("Preparing the encoder, the synthesizer and the vocoder...")
        self.encoder = encoder.load_model(Path("voice_cloning_files/encoder_voice_cloning/saved_models/"+self.encoder_model))
        self.synthesizer = Synthesizer(Path("voice_cloning_files/synthesizer/saved_models/pretrained/"+self.synthesizer_model))
        self.vocoder = vocoder.load_model(Path("voice_cloning_files/vocoder_voice_cloning/saved_models/pretrained/"+self.vocoder_model))
        self.blender_bot = BB()

    def get_utterance_data(self):
        original_wav = sd.rec(self.duration*self.sampling_rate, self.sampling_rate, 1, dtype='int32')

        # Display a progress bar while recording
        # Get current time to keep track of recording length
        start_time = time()
        print("Press enter to stop recording")
        input()  # This blocks the program from continuing until user presses enter

        # Trim wav to actual length of recording
        recording_length = time() - start_time
        if recording_length < self.duration:
            original_wav = original_wav[:int(recording_length*self.sampling_rate)]

        # Save as WAV file in 32-bit format
        original_wav = original_wav.astype(np.int32)
        write(self.wav_path, self.sampling_rate, original_wav)

        # Convert audio to text
        r = sr.Recognizer() # initialise a recogniser
        with sr.AudioFile(self.wav_path) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            voice_data = r.recognize_google(audio)
        return voice_data

    def preprocess_wav(self):
        original_wav, sampling_rate = librosa.load(self.wav_path)
        preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
        embed = encoder.embed_utterance(preprocessed_wav)
        print("Created the embedding")
        return embed

        # Place the rest of the code in your generation loop.
        # texts = ["Put your GPT texts in a list, one per sentence.",
                    #"This is an example so the code will run."]
    def answer(self):
        voice_data = self.get_utterance_data()
        embed = self.preprocess_wav()
        text = self.blender_bot.get_answer(voice_data)
        # Example how we can split the input text in sentences
        texts = []
        points_list = [0]  
        for pos,char in enumerate(text):
            if(char == '.'):
                points_list.append(pos)
        for i in range(len(points_list)-1):
            texts += [text[points_list[i]:points_list[i+1]]]


        # We also need a list of embeds to match.
        embeds = [embed] * len(texts)
        specs = self.synthesizer.synthesize_spectrograms(texts, embeds)
        print("Created the mel spectrogram")
                
        for i, spec in enumerate(specs):
            ## Generating the waveform
            print("Synthesizing the waveform for: \"{}\"".format(texts[i]))
            generated_wav = vocoder.infer_waveform(spec)
                        
            ## Post-generation
            # There's a bug with sounddevice that makes the audio cut one second earlier, so we pad it.
            generated_wav = np.pad(generated_wav, (0, self.synthesizer.sample_rate), mode="constant")

            # Play the audio (non-blocking)
            sd.stop()
            sd.play(generated_wav, self.synthesizer.sample_rate)
        
        return voice_data
