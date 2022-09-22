from cProfile import run
from scrapers.pick_your_part_scraper import main as pick_your_part

def runner(min_year, max_year, make, model, zip_code): 
    all_results = {}
    pick_your_part_cars = pick_your_part(min_year=min_year, max_year=max_year, query_make=make, query_model=model, zip_code=zip_code)
    all_results.update(pick_your_part_cars)
    return all_results

if __name__ == "__main__": 
    min_year = 1994
    max_year = 2006
    make = "LAND ROVER"
    model = 'DISCOVERY' 
    print(runner(min_year=min_year, max_year=max_year, make=make, model=model, zip_code=91605))