# <p align = "center">JsonListdata
<p align = "center">JsonListdata is easy instrument for read and write json file

## Getting started
* Installation from source
```
$ git clone https://github.com/DENLID/JLdata.git
```

## Firsts steps
### Edit data
The JLD class enables us to interact with the file.
In argument `file` you can set your json file.
```
from JLdata import JLD
import JLdata as JL

db = JLD(file="db.json")
data = db.data
```
