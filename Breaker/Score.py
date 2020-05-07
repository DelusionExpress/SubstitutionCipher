from math import log10
import json

def log_probability(ngrams_file):
    with open(ngrams_file) as json_file:
       ngrams = json.load(json_file)

    N = sum(ngrams.values())
    log_ngrams = {}
    for key in ngrams.keys():
        log_ngrams[key] = log10(float(ngrams[key]) / N)
    floor = log10(0.01/N)
    log_ngrams_file = ngrams_file.replace('../NGrams/','Log_Ngrams_File/Log_')

    with open(log_ngrams_file,'w') as json_file:
        json.dump(
            {'log_ngrams': log_ngrams,
             'floor': floor,
             },
              json_file,
              indent=0,
             )
    print('Done!')

log_probability('../NGrams/Trigrams.json')

def load_data(file):
    with open(file) as json_file:
        obj = json.load(json_file)
        log_ngrams = obj['log_ngrams']
        floor = obj['floor']
    return log_ngrams,floor

log_quadgrams,floor = load_data('Log_Ngrams_File/Log_Quadgrams.json')


def score(text,n=4,log_ngrams=log_quadgrams,floor_value=floor):

    cleaned_text = ''.join(c for c in text if c.isalpha())
    cleaned_text = cleaned_text.upper()
    score = 0
    for i in range(len(cleaned_text) - n+1):
        if cleaned_text[i:i+n] in log_ngrams.keys():
            score += log_ngrams[cleaned_text[i:i+n]]
        else:
            score += floor_value
    return score





