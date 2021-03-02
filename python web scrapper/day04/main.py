import os
import requests

def do_again():
  is_again = input('Do you want to start over? y/n ')
  if is_again == 'y' or is_again == 'Y':
    return True
  elif is_again == 'n' or is_again == 'N':
    return False
  else:
    print("That's not a valid answer")
    do_again()
  
def check_url_response(url):
  try:
    url_test = requests.get(url)
    if url_test.status_code == requests.codes.ok:
      return True
    else:
      return False
  except:
    return False

def set_url_form(url):
  HTTP = 'http://'
  if HTTP not in url:
    url = HTTP + url
  return url

def check_valid_url(url):
  if '.' in url:
    return True
  else:
    return False
    
def get_urls():
  urls = input().split(',')
  for i, url in enumerate(urls):
    urls[i] = url.strip().lower()
  return urls

def print_welcome():
  print('Welcome to IsItDown.py!')
  print('Please write a URL or URLs you want to check. (separated by comma)')

def main():
  os.system('clear')
  print_welcome()
  urls = get_urls()
  for url in urls:
    is_valid = check_valid_url(url)
    if is_valid is False:
      print(f'{url} is not a valid URL.')
    else:
      url = set_url_form(url)
      is_ok = check_url_response(url)
      if is_ok:
        print(f'{url} is up!')
      else:
        print(f'{url} is down!')
  is_again = do_again()
  if is_again:
    main()
  else:
    print('k. bye!')
    return

main()