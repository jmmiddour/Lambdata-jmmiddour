# Lambdata-jmmiddour
My Lambda Data Science collection of utility functions.

## Installation:

    pip install -i https://test.pypi.org/simple/ dspt7-utilities-jmiddour==0.0.1
    
## Usage:

Function #1 - `get_business_info`

    This function  will scrape the yellowpages website and
    will return a list of the information, such as name, phone number,
    street address, city, state, and zip code for those businesses.
    
    `from lambdata_jmmiddour.dspt7_utilities import get_business_info`


Function #2 - `address_split`
    
    This function will take an address column with the number address and
    street name and split it into two seperate columns, (number, name). It will
    also split a column with city, state, and zip code into 3 seperate columns,
    (city, state, zipcode).
    
    Note: Once the columns are split,
        this function will remove the original columns.
        
    `from lambdata_jmmiddour.dspt7_utilities import address_split`
