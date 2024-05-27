# Unittests and Integration Tests (0x03. Unittests and Integration Tests)

This project focuses on creating unittests and integration tests for various Python functions and classes. The tests are designed to ensure the correct functionality of the provided utility functions and the `GithubOrgClient` class, including their interactions and edge cases.

## Project Structure

- **utils.py**: Contains utility functions `access_nested_map`, `get_json`, and the `memoize` decorator.
- **client.py**: Contains the `GithubOrgClient` class which interacts with the GitHub API.
- **fixtures.py**: Contains fixture data for integration tests.
- **test_utils.py**: Contains unittests for the functions in `utils.py`.
- **test_client.py**: Contains unittests and integration tests for the `GithubOrgClient` class in `client.py`.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Code follows the `pycodestyle` style guide (version 2.5).
- All functions, classes, and modules include documentation.
- Functions and coroutines must be type-annotated.

## How to Run Tests

To execute the tests, use the following command:

```sh
$ python -m unittest discover -s path/to/tests

Replace path/to/tests with the directory containing the test files (test_utils.py and test_client.py).
Resources

-    [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
-    [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
-    [How to mock a readonly property with mock?](https://stackoverflow.com/questions/13575114/how-to-mock-a-readonly-property-with-mock)
-    [parameterized](https://pypi.org/project/parameterized/)
-    [Memoization](https://en.wikipedia.org/wiki/Memoization)

Learning Objectives

By the end of this project, you should be able to:

    Understand the difference between unit and integration tests.
    Use common testing patterns such as mocking, parameterization, and fixtures.
