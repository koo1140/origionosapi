from transformers import BertForMaskedLM, BertTokenizer

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForMaskedLM.from_pretrained(model_name)

# Function to generate text using masked language modeling
def generate_text(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    mask_token_index = input_ids[0].tolist().index(tokenizer.mask_token_id)
    
    outputs = model(input_ids)
    predictions = outputs.logits[0, mask_token_index].topk(5).indices

    generated_text = [tokenizer.decode(input_ids[0].tolist()[:mask_token_index] + [pred] + input_ids[0].tolist()[mask_token_index + 1:]) for pred in predictions]
    return generated_text

# Example usage
prompt = "I enjoy working with"
generated_texts = generate_text(prompt)
for text in generated_texts:
    print("Generated Text:", text)
