#!/usr/bin/env python3

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on an array."""
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
