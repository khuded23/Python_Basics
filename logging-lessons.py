'''
CRITICAL 50
ERROR 40
WARNING 30
INFO 20
DEBUG 10
NOTSET 0
'''
import logging

logging.basicConfig(level=logging.DEBUG, filename='test.log', format="%(asctime)s:%(levelname)s:%(message)s")

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

x = 10
y = 5

result  = add(x,y)

logging.debug(f'result is {result}')

result2 = subtract(x,y)
logging.debug(f'result is {result2}')
