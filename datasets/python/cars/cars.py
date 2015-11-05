import sys as _sys
import os as _os
import json as _json
import sqlite3 as _sql
import difflib as _difflib

_HEADER = {'User-Agent': 
          'CORGIS Cars library for educational purposes'}
_PYTHON_3 = _sys.version_info >= (3, 0)
_TEST = False
_HARDWARE = 1000

if _PYTHON_3:
    import urllib.request as _request
    from urllib.parse import quote_plus as _quote_plus
else:
    import urllib2 as _urllib2
    from urllib import quote_plus as _quote_plus

class DatasetException(Exception):
    ''' Thrown when there is an error loading the dataset for some reason.'''
    pass
    
_DATABASE_NAME = "cars.db"
if _os.path.isfile(_DATABASE_NAME):
    _DATABASE = _sql.connect(_DATABASE_NAME)
else:
    raise DatasetException("Error! Could not find the \"{}\" file. Make sure that it is in the same directory as {}.py!".format(_DATABASE_NAME, __name__))

################################################################################
# Auxilary
################################################################################

def _parse_type(value, type_func):
    """
    Attempt to cast *value* into *type_func*, returning *default* if it fails.
    """
    default = type_func(0)
    if value is None:
        return default
    try:
        return type_func(value)
    except ValueError:
        return default
        
def _byteify(input):
    """
    Force the given input to only use `str` instead of `bytes` or `unicode`.
    This works even if the input is a dict, list,
    """
    if isinstance(input, dict):
        return {_byteify(key): _byteify(value) for key, value in input.items()}
    elif isinstance(input, list):
        return [_byteify(element) for element in input]
    elif _PYTHON_3 and isinstance(input, str):
        return str(input.encode('ascii', 'replace').decode('ascii'))
    elif not _PYTHON_3 and isinstance(input, unicode):
        return str(input.encode('ascii', 'replace').decode('ascii'))
    else:
        return input
        
def _guess_schema(input):
    if isinstance(input, dict):
        return {str(key.encode('ascii', 'replace').decode('ascii')): 
                _guess_schema(value) for key, value in input.items()}
    elif isinstance(input, list):
        return [_guess_schema(input[0])] if input else []
    else:
        return type(input)
        


################################################################################
# Domain Objects
################################################################################
    

    


################################################################################
# Interfaces
################################################################################



def get_cars(test=True):
    """
    Returns the complete list of cars.
    
    """
    
    
    if _TEST or test:
        rows = _DATABASE.execute("SELECT data FROM cars LIMIT {hardware}".format(
            hardware=_HARDWARE))
        data = [r[0] for r in rows]
        data = [_json.loads(r) for r in data]
        
        return _byteify(data)
        
    else:
        rows = _DATABASE.execute("SELECT data FROM cars".format(
            hardware=_HARDWARE))
        data = [r[0] for r in rows]
        data = [_json.loads(r) for r in data]
        
        return _byteify(data)
        

def get_cars_by_year(year, test=True):
    """
    Returns all the cars for a given year.
    
    :param year: The year as an integer, between 1921 and 2013.
    :type year: int
    """
    
    if not isinstance(year, int):
        raise DatasetException("Error, the parameter year must be of type int")
    
    
    
    
    if _TEST or test:
        rows = _DATABASE.execute("SELECT data FROM cars WHERE year=? LIMIT {hardware}".format(
            hardware=_HARDWARE),
            (year, ))
        data = [r[0] for r in rows]
        data = [_json.loads(r) for r in data]
        
        return _byteify(data)
        
    else:
        rows = _DATABASE.execute("SELECT data FROM cars WHERE year=?".format(
            hardware=_HARDWARE),
            (year, ))
        data = [r[0] for r in rows]
        data = [_json.loads(r) for r in data]
        
        return _byteify(data)
        

def get_cars_by_make(make, test=True):
    """
    Returns all the cars of a certain make.
    
    :param make: The make of the cars
    :type make: Str
    """
    
    # Match it against recommend values
    potentials = [r[0].lower() for r in _DATABASE.execute("SELECT DISTINCT make FROM cars").fetchall()]
    if make.lower() not in potentials:
        best_guesses = _difflib.get_close_matches(make, potentials)
        if best_guesses:
            raise DatasetException("Error, the given identifier could not be found. Perhaps you meant one of:\n\t{}".format('\n\t'.join(map('"{}"'.format, best_guesses))))
        else:
            raise DatasetException("Error, the given identifier could not be found. Please check to make sure you have the right spelling.")
    
    
    
    if _TEST or test:
        rows = _DATABASE.execute("SELECT data FROM cars WHERE make=? COLLATE NOCASE LIMIT {hardware}".format(
            hardware=_HARDWARE),
            (make, ))
        data = [r[0] for r in rows]
        data = [_json.loads(r) for r in data]
        
        return _byteify(data)
        
    else:
        rows = _DATABASE.execute("SELECT data FROM cars WHERE make=? COLLATE NOCASE".format(
            hardware=_HARDWARE),
            (make, ))
        data = [r[0] for r in rows]
        data = [_json.loads(r) for r in data]
        
        return _byteify(data)
        

################################################################################
# Internalized testing code
################################################################################

def _test_interfaces():
    from pprint import pprint as _pprint
    from timeit import default_timer as _default_timer
    # Production test
    print("Production get_cars")
    start_time = _default_timer()
    result = get_cars(test=False)
    
    print("{} entries found.".format(len(result)))
    _pprint(_guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    # Test test
    print("Test get_cars")
    start_time = _default_timer()
    result = get_cars()
    
    print("{} entries found.".format(len(result)))
    _pprint(_guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    
    # Production test
    print("Production get_cars_by_year")
    start_time = _default_timer()
    result = get_cars_by_year(2001, test=False)
    
    print("{} entries found.".format(len(result)))
    _pprint(_guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    # Test test
    print("Test get_cars_by_year")
    start_time = _default_timer()
    result = get_cars_by_year(2001)
    
    print("{} entries found.".format(len(result)))
    _pprint(_guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    
    # Production test
    print("Production get_cars_by_make")
    start_time = _default_timer()
    result = get_cars_by_make('Pontiac', test=False)
    
    print("{} entries found.".format(len(result)))
    _pprint(_guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    # Test test
    print("Test get_cars_by_make")
    start_time = _default_timer()
    result = get_cars_by_make('Pontiac')
    
    print("{} entries found.".format(len(result)))
    _pprint(_guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    

if __name__ == '__main__':
    from optparse import OptionParser as _OptionParser
    _parser = _OptionParser()
    _parser.add_option("-t", "--test", action="store_true",
                      default=False,
                      help="Execute the interfaces to test them.")
    _parser.add_option("-r", "--reset", action="store_true",
                      default=False,
                      help="Reset the cache")
    (_options, _args) = _parser.parse_args()
    
    if _options.test:
        _test_interfaces()

    if _options.reset:
        _modify_self()