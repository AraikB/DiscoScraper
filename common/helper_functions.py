
def filter_found_cars(found_cars:list, min_year:int, max_year:int, query_make:str, query_model:str): 
    found_cars = list(filter(lambda u :min_year <= int(u.year) <= max_year, found_cars))
    found_cars = list(filter(lambda u: u.make.upper == query_make.upper(), found_cars))
    found_cars = list(filter(lambda u: u.model.upper() == query_model.upper(), found_cars))
    return found_cars