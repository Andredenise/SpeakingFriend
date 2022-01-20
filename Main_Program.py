import os # to remove creat
import tensorflow as tf
from voice_cloning_files.synthesizer.utils import text
from voice_cloning_files.synthesizer.inference import Synthesizer
import voice_cloning_files.encoder_voice_cloning.inference as encoder
import voice_cloning_files.vocoder_voice_cloning.inference as vocoder
from pathlib import Path
import os.path
from tqdm import trange
from time import sleep, time
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration # Import the model class and the tokenizer for the model

# First we have to make a chat.txt directory where we send all input and outpu text to so we have a document with the whole conversation
# Function to check if chat.txt already exist
file_name = r"directory of the chat txt file"
if os.path.isfile(file_name):
    expand = 1
    while True:
        expand += 1
        new_file_name = file_name.split(".txt")[0] + str(expand) + ".txt"
        if os.path.isfile(new_file_name):
            continue
        else:
            file_name = new_file_name
            break
chat = open(file_name, 'w')  


# Load the models and create the speaker embedding.
# This only needs to be done once, at the beginning of your script.
# We have to do this in the begin before the while loop because it only has to be done once
print("Preparing the encoder, the synthesizer and the vocoder...")
encoder.load_model(Path("voice_cloning_files/encoder_voice_cloning/saved_models/pretrained.pt"))
synthesizer = Synthesizer(Path("voice_cloning_files/synthesizer/saved_models/pretrained/pretrained.pt"))
vocoder.load_model(Path("voice_cloning_files/vocoder_voice_cloning/saved_models/pretrained/pretrained.pt"))



# Printed text to inform the speaker what to do and how the program works 
# How to quit, How to record,...
# -----------------------------------------------

# Here has to start a while loop untill speaker wants to stop the conversation
# -----------------------------------------------

# Function to call Record_Speaker and record the speaker
# -----------------------------------------------

# Function to get output from Record_Speaker to Interact_gpt_model
# -----------------------------------------------

# Function to get output of Interact_gpt_model
# -----------------------------------------------

# Alternative for the model, instant call function for other model
# -----------------------------------------------

tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill") # Download and setup the model and tokenizer
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

utterance = "Here has to come the output of the record_speaker --> voice_data"

inputs = tokenizer(utterance, return_tensors="pt") # Tokenize the utterance

res = model.generate(**inputs) # Passing through the utterances to the Blenderbot model

output = tokenizer.decode(res[0]) # Decoding the model output

# Function to start Voice_cloning.py
# -----------------------------------------------

# When speaker quits conversation, the instant print function has to start (print.py), so that you can have a printed version of the conversation
# -----------------------------------------------
