from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import shelve


def connect(username, password):
    driver.get('https://instagram.com')

    WebDriverWait(driver, 15).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username'))
    )

    username_input = driver.find_element_by_name('username')
    username_input.send_keys(username)
    password_input = driver.find_element_by_name('password')
    password_input.send_keys(password)

    submit_button = driver.find_element_by_class_name('L3NKy')
    submit_button.click()

    WebDriverWait(driver, 15).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, '_2dbep'))
    )

    return driver


def get_followings_recursively(current_nested_value, username):
    visited_users.append(username)

    memory = shelve.open('memory_db')

    if username in memory:
        following_names = memory[username]
    else:
        driver.get(f'https://instagram.com/{username}')
        try:
            following_button = driver.find_element_by_partial_link_text('following')
            following_button.click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'FPmhX'))
            )
            following_users = driver.find_elements_by_class_name('FPmhX')
            following_names = [user.text for user in following_users][:8]
            memory[username] = following_names
        except NoSuchElementException:
            following_names = []
            memory[username] = following_names

    memory.close()

    if current_nested_value == max_nexted_value:
        for following_name in following_names:
            node_edge.append((username, following_name))
        return

    for following_name in following_names:
        node_edge.append((username, following_name))

        if following_name in visited_users:
            continue

        get_followings_recursively(current_nested_value + 1, following_name)


driver = webdriver.Chrome('/selenium-drivers/chromedriver')

root_username = 'username'
root_password = 'password'
connect(root_username, root_password)

visited_users = list()
node_edge = list()
max_nexted_value = 6

get_followings_recursively(0, root_username)
