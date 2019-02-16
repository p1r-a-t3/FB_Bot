import unittest
from BotLib.template.button_template import ButtonTemplate
from BotLib.utility.button import Button
from BotLib.utility.util import Utility
from Tests.send_message import Facebook

class TestButtonTemplate(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.button = Button()
        self.facebook = Facebook()
        self.template = ButtonTemplate("1475588502509679")
        self.url = "https://adventures.is/wp-content/uploads/2017/06/eyjafjallajokull-glacier-volcano-iceland1.jpg"
    
    @classmethod
    def tearDownClass(self):
        del self.button
        del self.facebook
        del self.template

    def test_button_template_with_web_url(self):
        buttons = list()
        for _ in range(0, 3):
            title = "Test 1 - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        title_text = "test_button_template_with_web_url - Test 1 - {}".format(_)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "First run worked?")

    def test_2_button_template_with_web_url(self):
        buttons = list()
        whitelist_payload = Utility.whitelist_domain(self.url)
        self.facebook.send_message(whitelist_payload)
        title = "Test 2 - {}".format(1)
        buttons.append(self.button.create_url_button(title, self.url, messenger_extensions= True, fallback_url= self.url))
        title_text = "test_button_template_with_web_url - Test 2 - {}".format(1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Should Work")

    def test_3_button_template_with_web_url(self):
        buttons = list()
        title = "Test 3 - {}".format(1)
        buttons.append(self.button.create_url_button(title, None))
        self.assertEqual(type(buttons[0]), type(None), "Must be None")
        title_text = "test_button_template_with_web_url - Test 3 - {}".format(1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "Must not Work")

    
    def test_4_button_template_with_web_url(self):
        buttons = list()
        title = "Test 4 - {}".format(1)
        _ = "A" * 640
        _another = "A" * 40
        title += _another
        buttons.append(self.button.create_url_button(title, self.url))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")
        title_text = "test_button_template_with_web_url - Test 4 - {} --- {}".format(1, _)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "DO NOT work again!")
        for _ in range(0, 3):
            title = "Test 4 - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        title_text = "test_button_template_with_web_url - Test 4 - {}".format(2)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "DO NOT work again!")

    def test_5_button_template_with_web_url(self):
        buttons = list()
        title = "Test 5 - {}".format(1)
        _another = "A" * 40
        title += _another
        buttons.append(self.button.create_url_button(title, self.url))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")
        title_text = "test_button_template_with_web_url - Test 5 - {}".format(1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")