import pandas as pd
from transformers import AutoTokenizer
from collections import Counter
import warnings 
warnings.filterwarnings("ignore" , message=".clean_up_tokenization_spaces.")

with open('output.txt', 'r') as file:
    text = file.read()

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.tokenize(text)
counter = Counter(tokens)
top_30_tokens = counter.most_common(30)
print(top_30_tokens)
