# EASY-JSON DB
### works for Telegram Bots or simple systems

- Connect and set:
```
a = connect(databasename)
#set an object:
a.set(True,'person' , 'user1' , name = 'hosein' , lname = 'erish')
# res = {"person" : {"user1" : {"name" : "hosein" , "lname" : "erish"}}}
#for set just arg
a.set(False ,'person' , SELF = 'hoseinerish')
#res = {"person" : "hoseinerish"}
```
:params if_not_exists: if False = set was delete an object and make new if new set has interference with last
elif True = does not delete last one and does not import any data in database
------------

- Get method:
```
z = a.Get('person' , 'user1')
#z res = {'name' : 'hosein' , 'lname' : 'erish'}
```


------------

- delete_obj method:
```
# delete_obj(*attribute, delete)
a.delete_obj('person' , 'person1' , delete = 'name')
z = a.Get('person' , 'person1')
#z res = {'name' : 'hosein'}
```
```
a.delete_obj('person' , delete = 'person1')
z = a.Get('person' , 'person1')
#z res = KeyError
# "person" : {}
```


------------

- selector class:
```
con = connect('base.json')
for i in range(100):
    con.set(False , 'person' , f'person{i}' , name = 'test' , uid = i)
z = con.Get('person')
s = selector(z)
s.get_atter('name' , 'uid')
s.right('[1] < 6 ')
print(s.data)
```

any question?
[Telegram](http://t.me/idbag "Telegram")

