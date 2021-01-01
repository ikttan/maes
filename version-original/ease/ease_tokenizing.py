"""
Ignore this, it is just a "storage" for me to dump random codes  
"""


np.random.seed(500)
tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

for index, entry in enumerate(text):
    new_text = []
    word_lemmatized = WordNetLemmatizer()
    
    for word, tag in pos_tag(entry):
        if word not in stopwords.words("english") and word.isalpha():
            word_final = word_lemmatized.lemmatize(word, tag_map[tag[0]])
            new_text.append(word_final)
    text[index] = new_text

reload(create)
reload(essay_set)
reload(feature_extractor)
reload(grade)
reload(model_creator)
reload(predictor_extractor)
reload(predictor_set)
reload(util_functions)
