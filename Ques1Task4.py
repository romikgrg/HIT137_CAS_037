import spacy

def ner_with_spacy(text_file, model_name):
    nlp = spacy.load(model_name)
    
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

# Example usage with scispaCy models
en_core_sci_sm_entities = ner_with_spacy('/path/to/output/textfile.txt', 'en_core_sci_sm')
en_ner_bc5cdr_md_entities = ner_with_spacy('/path/to/output/textfile.txt', 'en_ner_bc5cdr_md')

# For BioBert, use Hugging Face transformers
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline

def ner_with_biobert(text_file, model_name='dmis-lab/biobert-base-cased-v1.1'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    nlp_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)
    
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    entities = nlp_pipeline(text)
    return entities

# Example usage
biobert_entities = ner_with_biobert('/path/to/output/textfile.txt')

# Compare entities from the models
def compare_entities(spacy_entities, biobert_entities):
    spacy_set = set([ent[0] for ent in spacy_entities])
    biobert_set = set([ent['word'] for ent in biobert_entities])
    
    overlap = spacy_set & biobert_set
    spacy_only = spacy_set - biobert_set
    biobert_only = biobert_set - spacy_set
    
    return overlap, spacy_only, biobert_only

# Example comparison
overlap, spacy_only, biobert_only = compare_entities(en_ner_bc5cdr_md_entities, biobert_entities)
print("Overlap:", overlap)
print("SpaCy only:", spacy_only)
print("BioBert only:", biobert_only)