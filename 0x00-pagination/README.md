# Pagination

This project implements pagination techniques for a database of popular baby names.

## Description

This project demonstrates different pagination approaches:
1. Simple pagination
2. Hypermedia pagination 
3. Deletion-resilient hypermedia pagination

## Files

* `0-simple_helper_function.py` - A helper function that calculates the start and end indices for pagination
* `1-simple_pagination.py` - Basic pagination implementation
* `2-hypermedia_pagination.py` - Hypermedia pagination implementation
* `3-hypermedia_del_pagination.py` - Deletion-resilient hypermedia pagination implementation

## Requirements

* Python 3.7
* Ubuntu 18.04 LTS
* pycodestyle 2.5.*

## Installation

Clone this repository:

```
git clone https://github.com/yourusername/alx-backend.git
cd alx-backend/0x00-pagination
```

## Usage

Run each file to see the pagination in action:

```
./0-main.py
./1-main.py
./2-main.py
./3-main.py
```

## Features

1. **Simple Pagination**: Basic pagination with page and page_size parameters.
2. **Hypermedia Pagination**: Enhanced pagination with metadata about current page, next/previous pages, and total pages.
3. **Deletion-resilient Pagination**: Handles situations where items might be deleted between pagination requests.
