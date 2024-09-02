#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """hyper_indexing that safeguard against deletion
        """
        assert index in range(len(self.dataset()))
        data = []
        index_val = index
        index = 0 if None else index
        next_index = index
        page_count = 0

        for step in range(page_size):
            print(index + step)
            if (index + step) in self.indexed_dataset().keys():
                print("Entered")
                if page_count == 0:
                    index_val = index + step
                data.append(self.indexed_dataset()[index + step])
                page_count += 1
                next_index += step
        return {'index': index_val,
                'next_index': next_index + 1,
                'page_size': page_size,
                'data': data}
