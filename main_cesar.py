'''
future implementation: portuguese and spanish
future implementation: add dial to make text larger from input

future idea: vignere cypher
'''

from string import ascii_lowercase, ascii_uppercase
from collections import Counter
import itertools
from cesar_v3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Display_program(QtWidgets.QMainWindow):

    def __init__(self):
        super(Display_program, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Click connections
        # self.ui.how_works_button.clicked.connect()
        self.ui.rand_key_button.clicked.connect(self.random_key)
        self.ui.key_select_spin.valueChanged.connect(self.hand_key)
        self.ui.run_button.clicked.connect(self.encrypt)

        self.ui.normal_radio.clicked.connect(self.normal_mode_selected)
        self.ui.awesome_radio.clicked.connect(self.awesome_mode_selected)

        # self.ui.english_radio.clicked.connect(self.back_to_eng)
        self.ui.portuguese_radio.clicked.connect(self.back_to_eng)
        self.ui.spanish_radio.clicked.connect(self.back_to_eng)
        self.ui.english_radio.setChecked(True) #temp
        self.ui.normal_radio.setChecked(True)
        # User info
        self.ui.how_works_button.setToolTip("Here is a test case!")

        # Class variables
        self.current_key = 0
        self.hold_original_str = ''

    #     # Radio button area
        self.ui.button_group_mode = QtWidgets.QButtonGroup(self)
        self.ui.button_group_mode.addButton(self.ui.normal_radio)
        self.ui.button_group_mode.addButton(self.ui.awesome_radio)
        self.ui.button_group_mode.setExclusive(True)

        self.ui.button_group_lang = QtWidgets.QButtonGroup(self)
        self.ui.button_group_lang.addButton(self.ui.english_radio)
        self.ui.button_group_lang.addButton(self.ui.portuguese_radio)
        self.ui.button_group_lang.addButton(self.ui.spanish_radio)
        self.ui.button_group_lang.setExclusive(True)

    def normal_mode_selected(self):
        pass

    def awesome_mode_selected(self):
        pass

    def back_to_eng(self):
        self.ui.english_radio.setChecked(True)


    def random_key(self):
        self.current_key = random.randint(1, 27)
        self.ui.current_key_label.setText(f'Current Key: {self.current_key}')

    def hand_key(self):
        self.current_key = self.ui.key_select_spin.value()
        self.ui.current_key_label.setText(f'Current Key: {self.current_key}')

    def encrypt(self):
        if self.ui.awesome_radio.isChecked():
            self.hold_original_str = self.ui.user_input.toPlainText()
            self.normalize_string(self.ui.user_input.toPlainText())
            return

        text = self.ui.user_input.toPlainText()
        key = self.current_key
        result = ''.join(
            [list(ascii_lowercase)[(list(ascii_lowercase).index(letter) + key) % 26] if letter in list(ascii_lowercase)
            else list(ascii_uppercase)[(list(ascii_uppercase).index(letter) + key) % 26] if letter in list(ascii_uppercase)
            else letter for letter in text])

        self.ui.program_output.setPlainText(result)

    def normalize_string(self, input_str):
        '''
        Normalizes a string into its most basic form (all lowercase, no space, no punctuations)
        string won't be displayed but will be used for analysis
        '''
        new_string = ''
        for letter in input_str.lower():
            if letter.isalpha():
                new_string += letter
        self.comp_list(new_string)
        return new_string # For testing purposes

    def comp_list(self, norm_string, standard_op=False):
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
        if standard_op:
            return info_list
        self.rotate(info_list)

    def rotate(self, user_list):
        '''
        Rotates the list, essentially proposing other combinations
        each rotation gets its letter occurence percentage compared to the target percentage for that letter
        the resulting difference is essentially a score of proximity to standard English letter distribution frequency
        resulting difference is raised to the power of 2 and added to the score.
        The lower the score, the closer to the standard distribution that hypothesis is and vice-versa
        A list of most likely keys is returned along with the score
        '''

        # Occurences of each letter out of a sample of 100,000
        # target is used by the rotate function
        # Future inplementation of other languagues will require different target values
        count_dist = Counter({
            'e': 12702, 't': 9056, 'a': 8167, 'o': 7507, 'i': 6966, 'n': 6749, 's': 6327, 'h': 6094, 'r': 5987,
            'd': 4253, 'l': 4025, 'c': 2782, 'u': 2758, 'm': 2406, 'w': 2360, 'f': 2228, 'g': 2015, 'y': 1974, 'p': 1929, 'b': 1492,
            'v': 978, 'k': 772, 'j': 153, 'x': 150, 'q': 95, 'z': 74
        })
        target = self.comp_list(count_dist, standard_op=True)

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

        key = list_of_scores[0][0]
        s = self.hold_original_str
        result = ''.join([list(ascii_lowercase)[(list(ascii_lowercase).index(letter) - key) % 26] if letter in list(ascii_lowercase)
            else list(ascii_uppercase)[(list(ascii_uppercase).index(letter) - key) % 26] if letter in list(ascii_uppercase) else letter for letter in s
        ])
        self.ui.program_output.setPlainText(result)
        self.ui.program_output_label.setText(f'Thinking the key is {key}!')
        self.ui.program_output_label.resize(221, 21)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Display_program()
    MainWindow.show()
    sys.exit(app.exec_())
