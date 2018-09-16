from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from nltk.tag import pos_tag
import nltk

def extract_NN(sent):
    grammar = r"""
    NBAR:
        # Nouns and Adjectives, terminated with Nouns
        {<NN.*>*<NN.*>}

    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """
    chunker = nltk.RegexpParser(grammar)
    ne = set()
    chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
    for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        ne.add(' '.join([child[0] for child in tree.leaves()]))
    if "i" in ne:
        ne.remove("i")
    return ne

analyser = SentimentIntensityAnalyzer()

# read in database of controversial words
with open("controversial_words.txt") as f:
    controversial_words = [x.lower().strip() for x in f.readlines()]

with open("bad_words.txt") as f:
    bad_words = [x.lower().strip() for x in f.readlines()]

while(1):
    sentence = input("Input a tweet to test: ")
    if sentence == "q":
        break
    sentiment_inversion = False
    good_subject = False
    controversial_comparison = False
    bad_word = False

    bad_word_list = []
    controversial_word_list = []
    negative_word_list = []
    controversial_final = []

    subjects = [x.lower() for x in extract_NN(sentence)]
    # check if tweet has any offensive topics
    for cwd in controversial_words:
        cwd_blob = TextBlob(cwd)
        singular_cwd = ""
        plural_cwd = ""

        # make sure that plural and singular versions of the word are detected
        for x in range(len(cwd_blob.words)):
            if x == len(cwd_blob.words) - 1:
                singular_cwd += cwd_blob.words[x].singularize()
                plural_cwd += cwd_blob.words[x].pluralize()
            else:
                singular_cwd += cwd_blob.words[x] + " "
                plural_cwd += cwd_blob.words[x] + " "

        if singular_cwd in sentence.lower() or plural_cwd in sentence.lower() or cwd in sentence.lower():
            # if tweet has offensive topics, sentiment is flipped
            print("test")
            sentiment_inversion = True
            controversial_word_list.append(cwd)

    # for subject in sentence.split():
    #     if not any(subject.lower() in s for s in controversial_words) and subject[0].isupper():
    #         print(not any [subject.lower() in s for s in controversial_words])
    #         good_subject = True
    #         break

    for bwd in bad_words:
        if bwd in sentence.lower().split():
            bad_word = True
            bad_word_list.append(bwd)

    if sentiment_inversion and good_subject:
        controversial_comparison = True

    snt = analyser.polarity_scores(sentence)
    for word in sentence.split():
        if analyser.polarity_scores(word)["compound"] < 0:
            negative_word_list.append(word)

    final_score = 0

    if bad_word:
        final_score = -1.5
        controversial_final = bad_word_list
    elif controversial_comparison:
        final_score = abs(snt["compound"])*-1 - 0.75
        controversial_final = controversial_word_list
    elif snt["compound"] > 0 and sentiment_inversion:
        final_score = -1*snt["compound"] - 0.5
        controversial_final = controversial_word_list
    elif snt["compound"] <= 0 and sentiment_inversion:
        final_score = -1*snt["compound"]
        controversial_final = controversial_word_list
    else:
        final_score = snt["compound"]
        controversial_final = negative_word_list
        if good_subject:
            final_score *= 1.25

    print("Final score:", final_score)
    print("Controversial due to:", controversial_final)
