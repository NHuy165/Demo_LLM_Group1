from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Specify the GPT-2 model variant (e.g., 'gpt2', 'gpt2-medium', 'gpt2-large')
model_name = "gpt2"

# Download the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Save the model and tokenizer locally
model.save_pretrained("./gpt2_offline")
tokenizer.save_pretrained("./gpt2_offline")

