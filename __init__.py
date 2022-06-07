import json

class connect:
    def __init__(self , database) -> None:
        """
        Start With connect to a json file
        :param database: database name
        """
        try:
            self.data = json.load(open(database , 'rb'))
            self.database_path = database
        except FileNotFoundError:
            open(database , '+wt').write('{}')
            self.data = json.load(open(database , 'rb'))
            self.database_path = database


    def create_obj(self , name , placeholder):
        self.data = json.load(open(self.database_path , 'rb'))
        self.data.update({name : placeholder})
        self.commit()
    
    def commit(self):
        with open(self.database_path , 'w') as data:
            json.dump(self.data , data , indent=2)
        self.data = json.load(open(self.database_path , 'rb'))


    def Get(self , *attribute):
        self.data = json.load(open(self.database_path , 'rb'))
        d = self.data
        for i in attribute:
            d = d[i]
        return d

    
    def set(self , if_not_exists = False,*attribute , **value ):
        
        def t(values = value):
            exe = 'self.data'
            for i in attribute:
                exe = exe+f'["{i}"]'
                try:
                    if if_not_exists ==True:
                        pass
                    else:
                        exec(exe + '.update({})')
                except :
                    exec(exe + '={}')
            if 'SELF' in str(values):
                values = '"'+values['SELF']+'"'
            exe = exe+'='+str(values)
            exec(exe)
            self.commit()
            self.data = json.load(open(self.database_path , 'rb'))

        if if_not_exists == True:
            d = self.data
            try:
                for i in attribute:
                    d = d[i]
            except KeyError:
                t()
            else:
                pass
        else:
            t()    
        
    
    def delete_obj(self ,  *attribute, delete,):

        exe = 'self.data'
        for i in attribute:
            exe = exe+f'["{i}"]'
        exe = exe+f'.pop("{delete}")'
        exec(exe)
        self.commit()
        
class selector:
    def __init__(self , dictionary) -> None:
        self.dic = dictionary
        lst = []
        for i in dictionary:
            lst.append(dictionary[i])
        self.data = lst

    def get_atter(self , *atter):
        lst = []
        for i in self.data:
            zp = []
            for d in atter:
                try:
                    zp.append(i[d])
                except Exception as a:
                    print(a)
            lst.append(zp)
        self.data = lst
        return lst
    
    def right(self , condition):
        con = condition
        lst = []
        for i in self.data:
            a = eval(f'{i}{con}')
            if a == True:
                lst.append(i)
            else:
                pass
        self.data = lst
        return lst






