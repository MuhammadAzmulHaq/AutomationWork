"""
This module contains shared fixtures.
"""
import json
from selenium import  webdriver
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

 # Read the file
  with open('config.json') as config_file:
   config = json.load(config_file)

 #Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  #Return config so it can be used
  return config


@pytest.fixture
def browser(config):

  # Initialize the WebDriver instance
  if config['browser'] == 'Chrome':
   b = webdriver.Chrome("C:/Users/pc/PycharmProjects/CourseSelenium/venv/drivers/chromedriver.exe")
  elif config['browser'] == 'Firefox':
   b = selenium.webdriver.Firefox()
  elif config['browser'] == 'Headless Chrome':
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    b = webdriver.Chrome(options=opt)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()