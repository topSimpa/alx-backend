#!/usr/bin/env python3
"""
Hypermedia Pagination
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Function that return the start and stop of a page
    """
    return ((page * page_size) - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the rows in page"""
        assert isinstance(page_size, int)
        assert isinstance(page, int)
        assert page > 0
        assert page_size > 0
        [start, end] = index_range(page, page_size)
        if start > len(self.dataset()) or end > len(self.dataset()):
            return []
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns data and other info"""
        data = self.get_page(page, page_size)
        prev_page = None if page == 1 else page - 1
        next_page = None
        total_page = (len(self.dataset) // page_size)
        if get_page(page + 1, page_size) != []:
            next_page = page + 1
        return {page_size: page_size,
                page: page,
                data: data,
                next_page: next_page,
                prev_page: prev_page,
                total_page: total_page}
