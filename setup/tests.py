from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("C:\Projetos\TDD\projeto\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_abre_janela_do_chrome(self):
        self.browser.get(self.live_server_url)

    def test_falhou(self):
        """Teste de exemplo de erro"""
        self.fail('Test Falhou - não foi dessa vez')