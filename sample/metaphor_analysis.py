"""metaphor_analysis.py: This program exams a piece of text to detect possible metaphors."""
__author__ = "Alex Martakis"
__version__ = "1.0.1"
__maintainer__ = "Alex Martakis"
__email__ = "asmartak@iu.edu"
__status__ = "Beta"


# The class creates a metaphor object. The object has a series of attributes to store the counts of the hit words found within the text
class Metaphors:
    def __init__(self, argue_count, time_count, mind_count, argue_unique, time_unique, mind_unique, metaphor_count):
        self.argue_count = argue_count
        self.time_count = time_count
        self.mind_count = mind_count
        self.argue_unique = argue_unique
        self.time_unique = time_unique
        self.mind_unique = mind_unique

    argue_is_war = ["war", "battle", "indefensible", "attack", "target", "demolish", "won", "win", "shoot", "shot",
                    "strategy",
                    "wipe", "agree"]
    time_is_money = ["time", "waste", "wasting", "save", "spend", "cost", "invested", "invest", "spare", "time",
                     "running out", "budget", "worth", "borrow", "borrowed", "lost"]

    mind_is_brittle = ["mind", "fragile", "handle", "care", "broke", "break", "easily", "crushed", "shattered",
                       "pieces", "snap", "snapped"]

    metaphors = [argue_is_war, time_is_money, mind_is_brittle]


# this method will read through each word within the dictionary of each metaphor and activate a series of methods to perform the analysis
def metaphor_analysis():
    meta_list = Metaphors.metaphors
    i = 0
    while i < len(meta_list):
        if i == 0:
            Metaphors.argue_count = get_metaphor_word_count(meta_list[i])
        elif i == 1:
            Metaphors.time_count = get_metaphor_word_count(meta_list[i])
        elif i == 2:
            Metaphors.mind_count = get_metaphor_word_count(meta_list[i])
        i = i + 1
    Metaphors.argue_unique = get_unique_metaphors_used(Metaphors.argue_count)
    Metaphors.time_unique = get_unique_metaphors_used(Metaphors.time_count)
    Metaphors.mind_unique = get_unique_metaphors_used(Metaphors.mind_count)
    lineSeparator()
    print(
        f"The array of hits for Argument is War is: {Metaphors.argue_count}")
    print(
        f"The array of hits for Time is Money is: {Metaphors.time_count}")
    print(
        f"The array of hits for Mind is Brittle is: {Metaphors.mind_count}")
    lineSeparator()
    print(
        f"The number of unique words used for Argument is War is: {Metaphors.argue_unique}")
    print(
        f"The number of unique words used for Time is Money is: {Metaphors.time_unique}")
    print(
        f"The number of unique words used for Mind is Brittle is: {Metaphors.mind_unique}")
    lineSeparator()

    return


# Everytime a hit word is found within the text, the array counting each metaphor will increase by one
def get_metaphor_word_count(my_list):
    metaphor_count = [0 for i in range(len(my_list))]
    i = 0
    sum = 0
    while i < len(my_list):
        with open("context.txt", 'r') as f:
            for line in f:
                for word in line.split():
                    if word == my_list[i]:
                        sum = sum + 1
        metaphor_count[i] = sum
        i = i + 1
    return metaphor_count


# Each index within the array will be read. If it is greater than zero, the count will increase by one to get the number of unique words found within the text
def get_unique_metaphors_used(my_list):
    i = 0
    total = 0
    while i < len(my_list):
        if my_list[i] > 0:
            total = total + 1
        else:
            total = total + 0
        i = i + 1
    return total


def lineSeparator():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


# Function is called her to perform metaphor detection
metaphor_analysis()
