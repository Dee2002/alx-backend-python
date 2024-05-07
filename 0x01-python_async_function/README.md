# Python Async - Backend Project

This project focuses on asynchronous programming in Python, specifically using the asyncio module. It includes implementations of various asyncio concepts and practices.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [File Descriptions](#file-descriptions)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Asynchronous programming is a programming paradigm that allows concurrent execution of tasks. In Python, the asyncio module provides a powerful framework for writing asynchronous code.

This project contains several Python scripts that demonstrate different aspects of asynchronous programming, including:

- Basic async syntax
- Executing multiple coroutines concurrently
- Measuring runtime of async tasks
- Creating and managing asyncio tasks

## Project Structure

The project is structured as follows:

.
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
├── 4-tasks.py
└── README.md


## File Descriptions

- `0-basic_async_syntax.py`: Contains an asynchronous coroutine for generating random delays.
- `1-concurrent_coroutines.py`: Implements a function to execute multiple coroutines concurrently.
- `2-measure_runtime.py`: Measures the runtime of executing multiple coroutines and returns average time per coroutine.
- `3-tasks.py`: Provides functions for creating asyncio tasks.
- `4-tasks.py`: Builds upon `3-tasks.py` to execute multiple coroutines as asyncio tasks.
- `README.md`: Documentation file providing an overview of the project.

## Usage

To use these scripts, simply import them into your Python environment and call the relevant functions. Each script includes docstrings explaining the purpose and usage of the functions.

Example usage:

```python
import asyncio
from 1-concurrent_coroutines import wait_n

async def main():
    delays = await wait_n(5, 10)
    print(delays)

asyncio.run(main())
