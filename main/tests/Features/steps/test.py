from behave import *
from django.contrib.auth.models import User
from main.models import Order, Product, OrderItem
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

@given("Main page")
def step_impl(context):
    url = 'http://afanasovi.pythonanywhere.com/login/'

    op = Options()

    #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

    op.add_argument("--no-sandbox")
    #op.add_argument("--headless")
    op.add_argument("start-maximized")
    op.add_argument("window-size=1900,1080")
    op.add_argument("disable-gpu")
    op.add_argument("--disable-software-rasterizer")
    op.add_argument("--disable-dev-shm-usage")
    #op.add_argument(f'user-agent={user_agent}')

    context.driver = webdriver.Chrome(options=op)
    context.driver.get(url)

    user = context.driver.find_element(By.XPATH, "/html/body/section/div[2]/div/form/div[1]/input")
    user.send_keys('ivan')
    password = context.driver.find_element(By.XPATH, "/html/body/section/div[2]/div/form/div[2]/input")
    password.send_keys('admin')
    context.driver.find_element(By.XPATH, "/html/body/section/div[2]/div/form/button").click()


@when('I click on добавить в корзину')
def step_impl(context):
    context.driver.get('http://afanasovi.pythonanywhere.com/main/')
    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div[3]/button').click()

@then("The брусничка should be in the cart")
def step_impl(context, res: int):
    context.driver.get('http://afanasovi.pythonanywhere.com/cart/')
    try:
        res = context.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/span').text
        return res == 'Брусничка'
    except NoSuchElementException:
        return False

# @then("an error should be displayed")
# def step_impl(context):
#     assert (context.calc_pres.calc_view.result_field.cget("text") == "Поля нужно заполнить числами")