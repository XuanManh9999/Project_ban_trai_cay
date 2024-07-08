from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductSystemTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Khởi tạo WebDriver
        cls.selenium.implicitly_wait(10)  # Đợi tối đa 10 giây cho các phần tử hiển thị

    def test_add_product(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))

        # Đợi cho trường email xuất hiện và điền thông tin
        email_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('admin@gmail.com')

        # Đợi cho trường password xuất hiện và điền thông tin
        password_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('1')

        # Submit form bằng cách nhấn Enter
        password_input.send_keys(Keys.RETURN)

        # Đợi cho trang được load và kiểm tra URL hiện tại
        WebDriverWait(self.selenium, 10).until(
            EC.url_to_be(self.live_server_url + '/manage-app/')
        )

        # Kiểm tra rằng URL hiện tại đã đúng
        current_url = self.selenium.current_url
        self.assertTrue(current_url.endswith('/manage-app/'))
