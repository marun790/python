- work with interpreter, no need of compiling the code
- python code styling follows P8 - https://peps.python.org/pep-0008/

## Compilation Diagram

![Compilation Flow](./compilation.png)

The diagram shows how Python code flows through different interpreters:

- **Python** → **CPython** → Binary (0100100101...)
- **Python** → **Jython** → Binary (0100100101...)

### data types:

| Category          | Type       | Class   | Description             | Example         | Mutability  |
| :---------------- | :--------- | :------ | :---------------------- | :-------------- | :---------- |
| **Primitive**     | Integer    | `int`   | Whole numbers.          | `10`, `-5`      | Immutable   |
| **Primitive**     | Float      | `float` | Decimal numbers.        | `3.14`, `10.0`  | Immutable   |
| **Primitive**     | Boolean    | `bool`  | True/False values.      | `True`, `False` | Immutable   |
| **Primitive**     | String     | `str`   | Text characters.        | `"Hello"`       | Immutable   |
| **Non-Primitive** | List       | `list`  | Ordered collection.     | `[1, 2, 3]`     | **Mutable** |
| **Non-Primitive** | Tuple      | `tuple` | Immutable ordered list. | `(10, 20)`      | Immutable   |
| **Non-Primitive** | Dictionary | `dict`  | Key-value pairs.        | `{"id": 1}`     | **Mutable** |
| **Non-Primitive** | Set        | `set`   | Unique unordered items. | `{1, 2, 3}`     | **Mutable** |

## 🔑 Key Technical Differences

| Feature        | Primitive Types           | Non-Primitive Types     |
| :------------- | :------------------------ | :---------------------- |
| **Complexity** | Basic building blocks.    | Complex structures.     |
| **Data Count** | Stores a single value.    | Stores multiple values. |
| **Memory**     | Less memory (Stack).      | More memory (Heap).     |
| **Methods**    | Limited built-in methods. | Rich set of operations. |

WE can call the functions without object

```
name = "arun"
len(name) ==> 4
```

String is immutable in python
Some of the functions in stting is having different name in pythin
ex:

```
obj.trim() ==> obj.strip() also lstrip(),
other usefull functions
rstrip()
find("value to find in string")
```

### print() method

can accept expressions

```
sentance = " learning python is cool"
print(f"{2 + 2}") ==> 4
notice f"{2 + 2}" ==> formater it just accept an expression and returns the value

print("python" in  sentance) ==> true
but the above method differs with inbuilt string method
        print(sentance.find("python")) ==> index
```

### Number

```
x = 5 + 2j
here 2j is the complex number
use of complex number
```

### Operation

```
Some additional operations
print(10 // 3 ) ==> 3
print(10 ** 3 ) ==> exponent 10^3

x += 3 == x = x+3 ==> augmented operator
```

### switch-case

Puthon not hving direct switch case, but can be achived through below, [ref](https://www.geeksforgeeks.org/python/switch-case-in-python-replacement/)

```
1. Using Dictionary Mapping
2. If-Elif-Else
3. Using Class Method
4. Using Match-Case (Python 3.10+)
```

### operators

```
if True and True and not False => here and is an operator don't use &&


Chaining comparision:
if 18 <= age < 65 => here ecpression is simple, age not repeating multiple times

```

### loops

```
for x in range(-10, 10, 2): => -10-> begins with, 10-> ends with, 2->  step
    for y in range(2):  => inner loop
        print(f"x: {x}, y: {y}")

range => is an complex typr in python

```

### function

```
def greeting(name):
    print(f"Hello, {name}")


print(greeting("Arun")) ==> None, because all the function in python bydefault will return a value. the default return value of the function is None
```

```
def increment(number, by):
    return number + by

print(increment(2, by=1)) ==> by is an keyword argument

```

```
def increment(number, by=2):  ==> by holds default value
    return number + by

print(increment(2)

```

### Inheridance

There is no concept of interface in python, It is achived through ABC

```
from abc import ABC, abstractmethod
from symtable import Function


class Animal(ABC): => Animal extends ABC, which is abstractclass, and this is also an optional it just give you echosystem like throwing errors during runtime to overwride all the abstract methods

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"hello {self.name}")

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):  ==> Dog exteds animal

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Woof Woof")


dog = Dog(name="Buddy")
dog.greeting()
soundFunction: Function = dog.make_sound
soundFunction()

```

### Variable scopping

```
In python there is no deticated keywords for private like java, instead the responsibility is lyes on developers by following below naming conventions

_name => protected
__name => protected
```
