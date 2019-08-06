import json

def GetJson():
  person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
  # Getting dictionary
  person_dict = json.loads(person_string)
  return person_dict
