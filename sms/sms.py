import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '',
  'message': '',
  'key': '',
});

print(resp.json())