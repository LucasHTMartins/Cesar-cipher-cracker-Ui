'''
Contains a sample of unit tests for the project
'''
import unittest
import main_cesar
import sys
from PyQt5.QtWidgets import QApplication

class TestCesar(unittest.TestCase):
    # each test should be unique

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.instance = main_cesar.Display_program()

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()
    '''
    Once
    '''

    # def setUp(self):
    #     self.app = QApplication(sys.argv)
    #     self.instance = main_cesar.Display_program()

    # def tearDownClass(cselfls):
    #     self.app.exit()
    # '''
    # Every time
    # '''

    def test_normalize_string(self):
        result = self.instance.normalize_string('CASE and sPaCeS')
        self.assertEqual(result, 'caseandspaces')

        result = self.instance.normalize_string('...T\nes&t2*\#sym\tbo[l0s')
        self.assertEqual(result, 'testsymbols')

    def test_encrypt(self):
        self.instance.current_key = 1
        self.instance.ui.user_input.setPlainText('AaBbCc Dd')
        self.instance.encrypt()
        self.assertEqual(self.instance.ui.program_output.toPlainText(), 'BbCcDd Ee')

        self.instance.ui.rand_key_button.click()
        self.instance.ui.user_input.setPlainText('')
        self.instance.encrypt()
        self.assertEqual(self.instance.ui.program_output.toPlainText(), '')

# # Strings used for testing purposes
# test_string = 'This is A VERY interesting test! We are going to start by looking at the standard distribution of letters in a text, then guessing which cipher we used'
# test_coded = 'Uijt jt B WFSZ joufsftujoh uftu! Xf bsf hpjoh up tubsu cz mppljoh bu uif tuboebse ejtusjcvujpo pg mfuufst jo b ufyu, uifo hvfttjoh xijdi djqifs xf vtfe'

# original_string = 'Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.'
# norm_string = normalize_string(original_string)
# list_for_analysis = comp_list(norm_string)
# result = rotate(list_for_analysis)
# print(result)

# print(caesar_cypher_decrypt(original_string, 7))

#print(normalize_string('...T\nest2*\#sym\tbo[ls'))

if __name__ == '__main__':
    unittest.main()
