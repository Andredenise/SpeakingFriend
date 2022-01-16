# For the voice cloning we need a recorded sample of what the speaker said so he can start cloning
# And we need a text input from the gpt_model so that he knows what to say

import librosa
from voice_cloning_files.synthesizer.utils import text
from voice_cloning_files.synthesizer.inference import Synthesizer
from voice_cloning_files.encoder_voice_cloning import inference as encoder
from voice_cloning_files.vocoder_voice_cloning import inference as vocoder
import sounddevice as sd
import numpy as np


# Update wav_path to the recorded sample in Record_Speaker
wav_path = "samples/p240_00000.mp3"
original_wav, sampling_rate = librosa.load(wav_path)
preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
embed = encoder.embed_utterance(preprocessed_wav)
print("Created the embedding")

# Place the rest of the code in your generation loop.
# texts = ["Put your GPT texts in a list, one per sentence.",
            #"This is an example so the code will run."]

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
specs = synthesizer.synthesize_spectrograms(texts, embeds)
print("Created the mel spectrogram")
           
for i, spec in enumerate(specs):
    ## Generating the waveform
    print("Synthesizing the waveform for: \"{}\"".format(texts[i]))
    generated_wav = vocoder.infer_waveform(spec)
                
    ## Post-generation
    # There's a bug with sounddevice that makes the audio cut one second earlier, so we pad it.
    generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")

    # Play the audio (non-blocking)
    sd.stop()
    sd.play(generated_wav, synthesizer.sample_rate)
