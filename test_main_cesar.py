'''
Contains a sample of unit tests for the project
'''
import unittest
import main_cesar
import sys
from PyQt5.QtWidgets import QApplication

class TestCesar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.instance = main_cesar.Display_program()

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()

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

if __name__ == '__main__':
    unittest.main()
