import json

class JLD:
  data = {}
  file = ""
  def __init__(self, file):
    self.file = file
    
    with open(file) as json_file:
      data = json.load(json_file)
      self.data = data
    

  def commit(self):
    with open(self.file, "w") as f:
      json.dump(self.data, f, indent=4)

def find_cell(data, key, name):
  for i in data:
    if i[key] == name:
      return i
