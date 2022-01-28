from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration # Import the model class and the tokenizer for the model
class BB:
    def __init__(self):
        self.tokenizer = None
        self.model = None
        self._load()

    def _load(self):
        self.tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill") # Download and setup the model and tokenizer
        self.model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

    # Function to get output of Interact_gpt_model
    # -----------------------------------------------
    def get_answer(self,voice_data):
        inputs = self.tokenizer(voice_data, return_tensors="pt") # Tokenize the utterance
        res = self.model.generate(**inputs) # Passing through the utterances to the Blenderbot model
        output = self.tokenizer.decode(res[0]) # Decoding the model output
        return output