'''
    Learning to Speak Object-Oriented
'''
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%%(has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrase first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    # str.count(sub [, start[, end]])
    # Return the number of non-overlapping occurrences of substring sub in the range [start, end]
    # random.sample()
    # Return a k length list of unique elements chosen from the population sequence or set.
    # Used for random sampling without replacement.
    class_names = [
        # str.capitalize()
        # Return a copy of the string with its first character capitalized and the rest lowercased.
        # count the "%%%" numbers appear in the snippet, and use the number to get a
        w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))
    ]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # random.randint(a, b)
        # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)
        param_count = random.randint(1, 3)  # set the parameters number 1-3
        param_names.append(', '.join(random.sample(
            WORDS, param_count)))  # convert a list to a string

    for sentence in snippet, phrase:
        result = sentence[:]

        # str.replace(old, new[, count])
        # Return a copy of the string with all occurrences of substring old replaced by new.
        # If the optional argument count is given, only the first count occurrences are replaced.

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake param names
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)

    # return a list
    return results


# keep going until they hit CTRL-D
try:
    while True:
        # get the keys from the dict, for example:  "class %%%(%%%):"
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            print(">>>>>>>>snippet:\t\t" + snippet)
            print(">>>>>>>>phrase:\t\t" + phrase)
            question, answer = convert(snippet, phrase)
            print(convert(snippet, phrase))
            print(">>>>>>>>question>>>>>>>\n " + question)
            print(">>>>>>>>answer>>>>>>>>\n" + answer)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
