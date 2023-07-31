from JLdata import JLD
import Jldata as JL

db = JLD(file="db.json")
data = db.data

""" before
{
  "name": ""
}
"""

data["name"] = "Denis"
db.commit()

""" after
{
  "name": "Denis"
}
"""
