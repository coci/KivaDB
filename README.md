# KivaDB
key-value database like Redis ( not same :) ) . it's for educational purpose .

usage :

```
  from core import KivaDB

  my_db = my_db = KivaDB("~/Desktop/test.db")
  my_db.set("foo","bar")
```
now if get 'foo' value :
```
  >>> my_db.get("foo") ==>
```
it prints out :
```
  'bar'
```
