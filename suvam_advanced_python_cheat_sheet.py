# Advanced Python Cheat Sheet created by SUVAM
# This file contains executable code examples covering advanced Python concepts.

# 1. Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Suvam, {func.__name__} is running!")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Suvam"))

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("Suvam")

# 2. Context Managers
from contextlib import contextmanager

with open('suvam_file.txt', 'w') as f:
    f.write("Hello, Suvam!")

@contextmanager
def suvam_context():
    print("Entering Suvam's context")
    yield
    print("Exiting Suvam's context")

with suvam_context():
    print("Suvam is working inside the context!")

# 3. Generators
def suvam_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in suvam_fibonacci(5):
    print(num)

suvam_squares = (x**2 for x in range(5))
print(list(suvam_squares))

# 4. List Comprehensions and Dict/Set Comprehensions
suvam_evens = [x for x in range(10) if x % 2 == 0]
print(suvam_evens)

suvam_dict = {f"Suvam_{i}": i**2 for i in range(5)}
print(suvam_dict)

suvam_set = {x for x in [1, 1, 2, 2, 3]}
print(suvam_set)

# 5. Lambda Functions
suvam_add = lambda x, y: x + y
print(suvam_add(5, 3))

numbers = [1, 2, 3, 4]
suvam_squared = list(map(lambda x: x**2, numbers))
print(suvam_squared)

suvam_even = list(filter(lambda x: x % 2 == 0, numbers))
print(suvam_even)

# 6. Advanced Data Structures (Collections)
from collections import Counter, defaultdict, namedtuple

suvam_counter = Counter("Suvam")
print(suvam_counter)

suvam_default = defaultdict(list)
suvam_default["key"].append("Suvam")
print(suvam_default)

Person = namedtuple("Person", ["name", "age"])
suvam = Person(name="Suvam", age=25)
print(suvam.name)

# 7. Exception Handling
class SuvamError(Exception):
    pass

try:
    raise SuvamError("Suvam, something went wrong!")
except SuvamError as e:
    print(e)
finally:
    print("Cleanup for Suvam")

# 8. Metaclasses
class SuvamMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs["suvam_info"] = lambda self: f"Class created for Suvam: {name}"
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=SuvamMeta):
    pass

obj = MyClass()
print(obj.suvam_info())

# 9. Multithreading and Multiprocessing
import threading
import multiprocessing

def suvam_task():
    print(f"Suvam is running in thread: {threading.current_thread().name}")

thread = threading.Thread(target=suvam_task)
thread.start()
thread.join()

def suvam_process():
    print(f"Suvam is running in process: {multiprocessing.current_process().name}")

if __name__ == "__main__":
    process = multiprocessing.Process(target=suvam_process)
    process.start()
    process.join()

# 10. Asyncio
import asyncio

async def suvam_async_task():
    print("Suvam is starting async task")
    await asyncio.sleep(1)
    print("Suvam completed async task")

async def main():
    await asyncio.gather(suvam_async_task(), suvam_async_task())

if __name__ == "__main__":
    asyncio.run(main())

# 11. Type Hints
from typing import List, Dict

def greet_suvam(names: List[str]) -> Dict[str, str]:
    return {name: f"Hello, {name}!" for name in names}

print(greet_suvam(["Suvam", "Python"]))

# 12. Regular Expressions
import re

text = "Suvam loves Python, and Suvam codes daily."
matches = re.findall(r"Suvam", text)
print(matches)

replaced = re.sub(r"Suvam", "SUVAM", text)
print(replaced)


