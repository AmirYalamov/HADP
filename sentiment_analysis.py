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

while(1):
    sentence = input("Input a tweet to test: ")
    if sentence == "q":
        break
    sentiment_inversion = False
    good_subject = False
    controversial_comparison = False

    subjects = [x.lower() for x in extract_NN(sentence)]
    print("SUBJECTS: ", subjects)
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
            sentiment_inversion = True
            break

    for subject in subjects:
        if subject not in cwd:
            good_subject = True
            break

    if sentiment_inversion and good_subject:
        controversial_comparison = True

    snt = analyser.polarity_scores(sentence)
    final_score = 0

    if controversial_comparison:
        final_score = abs(snt["compound"])*-1 - 0.5
    elif snt["compound"] > 0 and sentiment_inversion:
        final_score = -1*snt["compound"] - 0.5
    elif snt["compound"] < 0 and sentiment_inversion:
        final_score = -1*snt["compound"]
    else:
        final_score = snt["compound"]

    print("Final score:", final_score)
    print("Detailed score:", snt)
