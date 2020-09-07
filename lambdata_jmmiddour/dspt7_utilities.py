# Function #1:
def get_business_info(business, city, state):
    '''
    This function  will scrape the yellowpages website and
    will return a list of the information, such as name, phone number,
    street address, city, state, and zip code for those businesses.

    Parameters:
    -----------
      business : type or name of business
      city : name of the city where the business is located
      state : the 2 character abbrivation for the state in which the
        business is located.

    Returns:
    --------
      DataFrame with information scraped from the yellowpages website, 
        based on the parameters entered into the function.
    '''
    # Import libraries needed:
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    # Set the url to pull the data from:
    url = f'https://www.yellowpages.com/search?search_terms={business}&geo_location_terms={city}%2C+{state}&s=distance'

    # Create a get request:
    response = requests.get(url)

    # Check the status code to verify it is 200. This lets you know if there is
    #   an error reaching the website based on the code:
    if response.status_code == 200:

        # Use beautiful soup to parse everything:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the data from the location within the webpage:
        information = soup.find_all('div', class_="info")
        data = {'Name': [], 'Phone_No': [], 'Street': [], 'City_State_Zip': []}

        for info in information:
            # Get all the attribrutes we need:
            name = info.find('a', class_="business-name").span
            name = name.text if name else 'none'
            phone = info.find('div', class_='phones phone primary')
            phone = phone.text if phone else 'none'
            street = info.find('div', class_='street-address')
            street = street.text if street else 'none'
            area = info.find('div', class_='locality')
            area = area.text if area else 'none'

            # Store the values in a data object:
            data['Name'].append(name)
            data['Phone_No'].append(phone)
            data['Street'].append(street)
            data['City_State_Zip'].append(area)

    # Turn data collected into a pandas dataframe:
    business_info = pd.DataFrame(data, columns=['Name', 'Phone_No', 'Street',
                                                'City_State_Zip'])
    return business_info


# Function #2:
def address_split(df, col1, col2):
    '''
    This function will take an address column with the number address and
    street name and split it into two seperate columns. It will
    also split a column with city, state, and zip code into 3 seperate columns.

    Parameters:
    -----------
      df : The name of your DataFrame
      col1 : The column with the address you want to split.
      col2 : The column with the city, state, and zip code.
    
    Returns:
    --------
      DataFrame with 3 more columns. There will be 5 columns total with address
        values.
      Once the columns are split,
        this function will also remove the original columns.
    '''
    # Split the address column into 2 seperate columns:
    df[['Address_No', 'Street_Name']] = df[col1].str.split(n=1, expand=True)

    # Split the city, state, and zip into 3 seperate columns:
    df[['City', 'State', 'Zip_Code']] = df[col2].str.rsplit(n=2, expand=True)

    # Remove , from city column:
    df['City'] = df['City'].str.replace(',', '')

    # Remove the orginal columns to create a clean dataframe:
    df.drop(columns=[col1, col2], inplace=True)

    return df


if __name__ == "__main__":
    df = get_business_info('fast food', 'jacksonville', 'fl')
    print(f'DataFrame after running function 1:\n', df.head(), '\n')

    df2 = address_split(df, 'Street', 'City_State_Zip')
    print(f'DataFrame after running function 2:\n', df2.head())