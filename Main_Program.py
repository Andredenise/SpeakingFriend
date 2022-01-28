from Voice_cloning import RTVC
# Initialize the models
rtvc = RTVC()

# Start the conversation, it ends when the speaker says "bye"
while 1:
    voice_data = rtvc.answer()
    if "bye" in voice_data:
        break