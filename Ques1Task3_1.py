import pandas as pd
from collections import Counter
import re

with open('output.txt', 'r') as file:
    text = file.read()
words = re.findall(r' \w+ ', text.lower())
counter = Counter(text)
top_30_words = counter.most_common(30)

# write to csv
pd.DataFrame(top_30_words, columns=['word', 'count']).to_csv('top_30_words.csv',index=False)