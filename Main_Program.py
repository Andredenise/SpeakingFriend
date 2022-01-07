import os # to remove creat
import tensorflow as tf
from voice_cloning_files.synthesizer.utils import text
from voice_cloning_files.synthesizer.inference import Synthesizer
from voice_cloning_files.encoder_voice_cloning import inference as encoder
from voice_cloning_files.vocoder_voice_cloning import inference as vocoder
from pathlib import Path
import os.path
from tqdm import trange
from time import sleep, time

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
encoder.load_model(Path("encoder_VC/saved_models/pretrained.pt"))
synthesizer = Synthesizer(Path("synthesizer/saved_models/pretrained/pretrained.pt"))
vocoder.load_model(Path("vocoder_VC/saved_models/pretrained/pretrained.pt"))



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

# Function to start Voice_cloning.py
# -----------------------------------------------

# When speaker quits conversation, the instant print function has to start (print.py), so that you can have a printed version of the conversation
# -----------------------------------------------
