from string import ascii_lowercase
from string import ascii_uppercase
from collections import Counter
import itertools


def caesar_cypher_encrypt(s, key):
    '''
    Takes a plain language string and an integer, returns an encrypted string
    non-ascii characters are maintained
    Uppercase characters are maintained
    '''
    return ''.join(
        [list(ascii_lowercase)[(list(ascii_lowercase).index(letter) + key) % 26] if letter in list(ascii_lowercase)
        else list(ascii_uppercase)[(list(ascii_uppercase).index(letter) + key) % 26] if letter in list(ascii_uppercase)
        else letter for letter in s
    ])

def caesar_cypher_decrypt(s, key):
    '''
    Takes an encrypted string and an integer, returns a plain language string
    non-ascii characters are maintained
    Uppercase characters are maintained
    '''
    return ''.join([list(ascii_lowercase)[(list(ascii_lowercase).index(letter) - key) % 26] if letter in list(ascii_lowercase)
        else list(ascii_uppercase)[(list(ascii_uppercase).index(letter) - key) % 26] if letter in list(ascii_uppercase) else letter for letter in s
    ])

def normalize_string(input_str):
    '''
    Normalizes a string into its most basic form (all lowercase, no space, no punctuations)
    string won't be displayed but will be used for analysis
    '''
    new_string = ''
    for letter in input_str.lower():
        if letter.isalpha():
            new_string += letter
        # else:
        #     new_string += '.'
    return new_string

def comp_list(norm_string):
    '''
    Creates a list of lists where values can be rotated to find the most likely key to the encryption
    Takes a normalized string, creates a counter object, updates the counter object to include any missing letters and set their value to 0
    Each list element should have: index by alphabet, letter, percentage of occurance)
    technically only the latter element is necessary but for testing and debugginf purposes the each sublist has a more complete information set
    '''
    set_letters = set(norm_string)
    set_total = set(ascii_lowercase)
    missing_letters = set_total.difference(set_letters)
    counter_obj = Counter(norm_string)

    for letter in missing_letters:
        counter_obj[letter] = 0

    total = counter_obj.total()
    info_list = [[num, letter, round(counter_obj[letter] / total*100, 4)] for num, letter in (enumerate(ascii_lowercase))]
    return info_list

def rotate(user_list):
    '''
    Rotates the list, essentially proposing other combinations
    each rotation gets its letter occurence percentage compared to the target percentage for that letter
    the resulting difference is essentially a score of proximity to standard English letter distribution frequency
    resulting difference is raised to the power of 2 and added to the score.
    The lower the score, the closer to the standard distribution that hypothesis is and vice-versa
    A list of most likely keys is returned along with the score
    '''
    list_of_scores = []
    for rotation in range(26):
        total_score = 0
        for sub_list, sub_check in zip(user_list, target):
            _, _, test_per = sub_list
            _, _, check_per = sub_check
            total_score += (check_per - test_per) **2

        list_of_scores.append([rotation, total_score])
        user_list = [[user_list[num][0], user_list[num][1], user_list[(num+1)%26][2]] for num in range(26)]

    list_of_scores.sort(key=lambda x:x[1])
    print(list_of_scores[:3])


# Occurences of each letter out of a sample of 100,000
# target is used by the rotate function
# Future inplementation of other languagues will require different target values
count_dist = Counter({
    'e': 12702, 't': 9056, 'a': 8167, 'o': 7507, 'i': 6966, 'n': 6749, 's': 6327, 'h': 6094, 'r': 5987,
    'd': 4253, 'l': 4025, 'c': 2782, 'u': 2758, 'm': 2406, 'w': 2360, 'f': 2228, 'g': 2015, 'y': 1974, 'p': 1929, 'b': 1492,
    'v': 978, 'k': 772, 'j': 153, 'x': 150, 'q': 95, 'z': 74
})
target = comp_list(count_dist)

# Strings used for testing purposes
test_string = 'This is A VERY interesting test! We are going to start by looking at the standard distribution of letters in a text, then guessing which cipher we used'
test_coded = 'Uijt jt B WFSZ joufsftujoh uftu! Xf bsf hpjoh up tubsu cz mppljoh bu uif tuboebse ejtusjcvujpo pg mfuufst jo b ufyu, uifo hvfttjoh xijdi djqifs xf vtfe'

'''
Sources for frequency and further reading
https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
https://norvig.com/mayzner.html

https://en.wikipedia.org/wiki/Frequency_analysis
https://en.wikipedia.org/wiki/Caesar_cipher
'''


# original_string = 'Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.'
# norm_string = normalize_string(original_string)
# list_for_analysis = comp_list(norm_string)
# result = rotate(list_for_analysis)
# print(result)

# print(caesar_cypher_decrypt(original_string, 7))

print(normalize_string('...T\nest2*\#sym\tbo[ls'))
