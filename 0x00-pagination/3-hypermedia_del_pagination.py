#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


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
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                print(f"Error: Could not find file {self.DATA_FILE}")
                return []
            except Exception as e:
                print(f"Error loading dataset: {e}")
                return []

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of the dataset that is deletion-resilient.
        
        Args:
            index (int): The start index
            page_size (int): The size of the page
            
        Returns:
            Dict: A dictionary containing the data and metadata
        """
        indexed_data = self.indexed_dataset()
        data_length = len(indexed_data)
        
        # Handle initial index value
        if index is None:
            index = 0
            
        # Verify index is in valid range
        assert isinstance(index, int) and 0 <= index < data_length
        
        # Prepare data for the current page
        data = []
        current_index = index
        counter = 0
        
        # Collect page_size items starting from index
        while counter < page_size and current_index < data_length:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                counter += 1
            current_index += 1
            
        # Calculate next_index
        next_index = current_index
        
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
