class Car: 
    def __init__(self,
        year:int ,
        make:str,
        model:str
                ) -> None: 
        self._year = year 
        self._make = make
        self._model = model 
            
    @property 
    def year(self):
        return self._year
    
    @property
    def make(self): 
        return self._make
    
    @property
    def model(self):
        return self._model
    
    def __repr__(self) -> str:
        return f"\n Year: {self.year} \n Make: {self.make} \n Model: {self.model}"



pyp_car_string_query = r">(\d\d\d?\d?) (\w+-?\w+?) (\w+-?\w+?)<"

pyp_next_page_query = r'<a class=\"button pypvi_pageButton\" href=\"([\?=\/\w-]+)\">Next Page'

pyp_store_query = r'/parts/([\w\-\d]+)/'


pyp_zip_store_query = r'\"Zip\":\"(\d+)\"[,\"\w:() -.{/]+/parts/([-\w]+)'