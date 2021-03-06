'''
Created on 14.06.2016

@author: Hubert
'''

def rounded(decimal_places):
    def decorator(func):
        def wrapped_function(*args):
            return round(func(*args), decimal_places)
        return wrapped_function 
    return decorator

@rounded(2)
def divide(a: float, b: float):
    return a/b

if __name__ == '__main__':
    print(divide(7, 6))