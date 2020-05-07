import json

def ngram_count(n, text):
    return len(text) - n + 1
def list_ngrams(n, text):
    for i in range(ngram_count(n, text)):
        yield text[i:i + n]


def generate(n,ngrams_file,file_sentences):
    with open(ngrams_file) as json_file:
       ngrams = json.load(json_file)
    with open(file_sentences, encoding='utf-8') as file:

        for line in file:

            line = ''.join(e for e in line if e.isalpha())
            line = [e for e in line if ord(e) >= 65 and ord(e) <= 122]
            line = ''.join(line)
            line = line.upper()

            line_ngrams = list_ngrams(n, line)

            for item in line_ngrams:
                if item not in ngrams:
                    ngrams[item] = 1
                else:
                    ngrams[item] += 1
    with open(ngrams_file ,'w') as json_file:
        json.dump(ngrams, json_file)
    print('Generation successfully!')


#generate(2,'Bigrams.json','Sentences.txt')
generate(3,'Trigrams.json','Sentences.txt')
#generate(4,'Quadgrams.json','Sentences.txt')



