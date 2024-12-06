from sqlite3 import connect

class Model:
    con = connect("app.db")
    cur = con.cursor()

class Asset(Model):
    
    @classmethod
    def create_table(cls):
        cls.cur.execute(f"""DROP table if exists{cls.__name__}""")
        cls.cur.execute(f"""CREATE table if not exists {cls.__name__} (url,title)""")
        
    @classmethod
    def create(cls, url, title):
        instance = cls()
        instance.url = url
        instance.title = title
        return instance
    
    @classmethod
    def get_by_name(cls, name):
        cls.cur.execute(f"""
                    SELECT * FROM {cls.__name__}
                    WHERE {name}
            """)
        return cls.create(*cls.cur.fetchone())
    
    @classmethod
    def all(cls):
        cls.cur.execute(f"SELECT * FROM {cls.__name__}")
    
    def save(self):
        self.cur.execute(
            f"""INSERT INTO {self.__class__.__name__} 
            VALUE (
                '{self.url}'
                '{self.title}' 
                )"""
        )
        self.con.commit()