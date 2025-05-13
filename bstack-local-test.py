import pytest

def test_local(selenium):
  selenium.get('http://bs-local.com:45454')
  local_page_title = selenium.title
  assert local_page_title == 'BrowserStack Locals'

def test_example():
  assert 2 + 2 == 4