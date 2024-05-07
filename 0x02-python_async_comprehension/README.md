# 0x02. Python - Async Comprehension

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep525)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives

By the end of this project, you should be able to explain to anyone:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## General Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the folder is mandatory
- Code should follow the `pycodestyle` style (version 2.5.x)
- Length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be descriptive and sentence-like
- All functions and coroutines must be type-annotated

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that loops 10 times, asynchronously waits for 1 second each time, then yields a random number between 0 and 10.

### 1. Async Comprehensions

Write a coroutine called `async_comprehension` that collects 10 random numbers using async comprehensions over `async_generator`.

### 2. Run time for four parallel comprehensions

Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

## Files

- `0-async_generator.py`: Contains the implementation of the `async_generator` coroutine.
- `1-async_comprehension.py`: Contains the implementation of the `async_comprehension` coroutine.
- `2-measure_runtime.py`: Contains the implementation of the `measure_runtime` coroutine.
- `README.md`: This file, providing an overview of the project and instructions.
