from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AddProductSystemTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Khởi tạo WebDriver
        cls.selenium.implicitly_wait(5)  # Đợi tối đa 10 giây cho các phần tử hiển thị
        cls.port = 8000  # Đặt cổng
        cls.live_server_url = f'http://localhost:{cls.port}'

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()  # Đóng WebDriver khi kết thúc
        super().tearDownClass()

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
        password_input.send_keys('123')

        # Submit form bằng cách nhấn Enter
        password_input.send_keys(Keys.RETURN)

        # Đợi cho trang admin xuất hiện
        WebDriverWait(self.selenium, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'navbar'))
        )

        # Chuyển đến trang thêm sản phẩm
        self.selenium.get('%s%s' % (self.live_server_url, '/manage-product/'))

        # Đợi cho trang thêm sản phẩm xuất hiện
        WebDriverWait(self.selenium, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'container'))
        )

        # Đợi cho trường tên sản phẩm xuất hiện và điền thông tin
        name_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )
        name_input.send_keys('Quả Đào')

        # Đợi cho trường giá xuất hiện và điền thông tin
        price_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'price'))
        )
        price_input.send_keys('10000')

        # Đợi cho trường số lượng xuất hiện và điền thông tin
        quantity_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'quantity'))
        )
        quantity_input.send_keys('100')

        # Đợi cho trường mô tả xuất hiện và điền thông tin
        description_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'desc'))
        )
        description_input.send_keys('Quả Đào ngon tuyệt vời')

        # Đợi cho trường ảnh xuất hiện và điền thông tin
        image_input = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'url'))
        )
        image_input.send_keys('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRy3zayBOjaN2QxHblUVyWB6sly_Se7AK6yYzT9Ns62Pqrh9Qgm-CxqTImkx7ECays-zA&usqp=CAU')

        # Submit form bằng cách nhấn Enter
        image_input.send_keys(Keys.RETURN)

        # Đợi cho thông báo thêm sản phẩm thành công xuất hiện
        WebDriverWait(self.selenium, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'alert-success'))
        )

class AddUserSystemTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Khởi tạo WebDriver
        cls.selenium.implicitly_wait(3)  # Đợi tối đa 10 giây cho các phần tử hiển thị
        cls.port = 8000  # Đặt cổng
        cls.live_server_url = f'http://localhost:{cls.port}'

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()  # Đóng WebDriver khi kết thúc
        super().tearDownClass()

    def test_add_user(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))

        # Đợi cho trường email xuất hiện và điền thông tin
        email_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('admin@gmail.com')

        # Đợi cho trường password xuất hiện và điền thông tin
        password_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('123')

        # Submit form bằng cách nhấn Enter
        password_input.send_keys(Keys.RETURN)

        # Đợi cho trang admin xuất hiện
        WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'navbar'))
        )

        # Chuyển đến trang thêm người dùng

        self.selenium.get('%s%s' % (self.live_server_url, '/manage-user/'))

        # Đợi cho trang thêm người dùng xuất hiện
        WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'container'))
        )

        # Đợi cho trường tên người dùng xuất hiện và điền thông tin
        name_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )
        name_input.send_keys('Nguyễn Văn A')

        # Đợi cho trường Ngày sinh xuất hiện và điền thông tin
        dob_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'date'))
        )
        dob_input.send_keys('01/01/2000')

        # Đợi cho trường so dien thoai xuất hiện và điền thông tin
        phone_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'phone'))
        )
        phone_input.send_keys('0123456789')

        # Đợi cho trường email xuất hiện và điền thông tin
        email_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('a@gmail.com')

        # Đợi cho trường password xuất hiện và điền thông tin
        password_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('123')

        # Đợi cho trường Dịa chỉ xuất hiện và điền thông tin
        address_input = WebDriverWait(self.selenium, 3).until(
            EC.presence_of_element_located((By.NAME, 'address'))
        )
        address_input.send_keys('Hà Nội')

        # Submit form bằng cách nhấn Enter
        address_input.send_keys(Keys.RETURN)

        # Đợi cho thông báo thêm người dùng thành công xuất hiện
        WebDriverWait(self.selenium, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'alert-success'))
        )










