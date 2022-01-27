from Voice_Cloning import RTVC

# Load the models and create the speaker embedding.
# This only needs to be done once, at the beginning of your script.
# We have to do this in the begin before the while loop because it only has to be done once
rtvc = RTVC()

# Printed text to inform the speaker what to do and how the program works 
# How to quit, How to record,...
# -----------------------------------------------

# Here has to start a while loop untill speaker wants to stop the conversation
# -----------------------------------------------
while 1:
# Function to call Record_Speaker and record the speaker
# -----------------------------------------------
    voice_data = rtvc.answer()
    if "bye" in voice_data:
        break
# Function to get output from Record_Speaker to Interact_gpt_model
# -----------------------------------------------

# Function to get output of Interact_gpt_model
# -----------------------------------------------

# Alternative for the model, instant call function for other model
# -----------------------------------------------


# Function to start Voice_cloning.py
# -----------------------------------------------

# When speaker quits conversation, the instant print function has to start (print.py), so that you can have a printed version of the conversation
# -----------------------------------------------
