#!/usr/bin/env python3
"""
Hypermedia pagination implementation
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indices for a specific page and page size.
    
    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page
        
    Returns:
        Tuple[int, int]: A tuple containing start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return (start_index, end_index)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.
        
        Args:
            page (int): The page number (1-indexed)
            page_size (int): The number of items per page
            
        Returns:
            List[List]: A list of rows corresponding to the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        if start_index >= len(dataset):
            return []
        
        return dataset[start_index:end_index]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return hypermedia pagination for the dataset.
        
        Args:
            page (int): The page number (1-indexed)
            page_size (int): The number of items per page
            
        Returns:
            Dict: A dictionary containing hypermedia pagination information
        """
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
