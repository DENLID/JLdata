from JLdata import JLD
import JLdata as JL

db = JLD(file="db.json")
data = db.data

''' Example file
{
  "name": [
    {
    "name": "Bob",
    "age": "18"
    },
    {
    "name": "Ilya",
    "age": "20"
    }
  ]
}
'''
users = data["name"]

user = JL.find_cell(users, "name", "Bob")
print(user["age"]) # 18

user = JL.find_cell(users, "name", "Ilya")
print(user["age"]) # 20

user = JL.find_cell(users, "name", "Denis")
print(user["age"]) # None
