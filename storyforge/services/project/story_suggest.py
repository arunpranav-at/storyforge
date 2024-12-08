# service to generate some story line suggestions for the users

# importing necessary libraries
from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForCausalLM

# model id for the text generation model
model_id = "OpenVINO/Phi-3-mini-128k-instruct-int8-ov"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = OVModelForCausalLM.from_pretrained(model_id)

# function to generate some story line suggestions for the users
# genre: str, genre for which story line suggestions are to be generated
# suggestion_length: int, length of the story line suggestion in number of characters
# returns: str, generated story line suggestion for the given genre
def generate_story_suggestions(genre, suggestion_length=200):
    prompt = f"Generate few story line suggestions for the given genre: {genre} so that it will be helpful for me to write story on it."
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=suggestion_length)
    suggestion = tokenizer.batch_decode(outputs)[0]
    return suggestion