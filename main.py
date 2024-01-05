from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

# Load pre-trained DistilBERT model and tokenizer
model_name = "distilbert-base-cased-distilled-squad"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForQuestionAnswering.from_pretrained(model_name)

# Function to perform question answering
def answer_question(question, context):
    inputs = tokenizer(question, context, return_tensors="pt")
    outputs = model(**inputs)
    
    # Get the predicted start and end positions
    start_logits = outputs.start_logits
    end_logits = outputs.end_logits

    # Get the most likely answer
    start_index = torch.argmax(start_logits, dim=1).item()
    end_index = torch.argmax(end_logits, dim=1).item()

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_index:end_index + 1]))
    return answer

# Example usage
context = "DistilBERT is a smaller version of BERT, designed to be more memory-efficient."
question = "What is DistilBERT?"

answer = answer_question(question, context)
print("Answer:", answer)
