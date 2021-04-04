from functools import wraps
from collections import namedtuple
from typing import Callable

RecursData = namedtuple("RecursData", ["args", "kwargs", "recurs_depth"])

def stop_recurs_if(func_bool: Callable) -> Callable:
    """
    Wrapper for a recursive function to stop the recursion given
    a function to be true.
    
    The function takes one argument which is a namedtuple object
    with the following attributes:
        
        RecursData.args -> list
            a list of the arguments in the current recursion
        RecursData.kwargs -> dict
            a dictionary of the keyword arguments in the current
            recursion
        RecursData.recurs_depth -> int
            the number of times the function ran

    Usage:
    >>> @stop_recurs_if(lambda r_data: r_data.recurs_depth == 5)
    ... def foo():
    ...     print("called")
    ...     foo()
    ...
    >>> foo()
    called
    called
    called
    called
    called
    """
    def wrapper(func: Callable) -> Callable:
        func._recurs_depth = 0
        func._stop = False
        @wraps(func)
        def new_func(*args, **kwargs):
            func._recurs_depth += 1
            if func._stop:
                func._recurs_depth = 0
                func._stop = False
                return
            if func_bool(RecursData(args, kwargs, func._recurs_depth)):
                func._stop = True
            return func(*args, **kwargs)
        return new_func
    return wrapper
