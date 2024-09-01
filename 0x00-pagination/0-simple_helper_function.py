#!/usr/bin/env python3
"""
Simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
   Function that return the start and stop of a page
    """
    return ((page * page_size) - page_size, page * page_size)
