#!/usr/bin/env python3

from typing import Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: T, default: Union[T, None] = None) -> Union[T, None]:
    """Safely get a value from a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
