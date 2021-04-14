# This is a loop that will take in a request and output all avalible pages.

def data_request_loop(url_1, url_2, item)
'''
This function takes in a mian request url == (url1), a secondary url == (url2),
and a specificed page name == (item). Then this fucntion runs a loop for each page to
acquire the data. Next the fucntion converts data dictonary into a data frame, then converts
data to csv for quicker access. THis function will return the stores_list and you will have a 
csv local file in your directory. 
'''

    list_of_data = [] 

    response = requests.get(url_1) # request inital url
    data = response.json() # sets data equal to the response from request inital url in json format
    n = data['payload']['max_page'] # Goes into payload and looks at the max page

    for i in range(1,n+1): # For loop 
        url2 = 'https://python.zach.lol/api/v1/stores?page='+str(i) # Page number as the string
        response = requests.get(url_2) # Request json data for url_2
        data = response.json() # sets data = to the respones to the request for json data.
        page_items = data['payload'][item] 
        list_of_data.append(page_items) # Appends the list_of_data to the page items. 
        list_of_data = list_of_data + page_items # This allows you to access the new list of items. 
    
    list_of_data = pd.DataFrame(data['payload'][item]) # Converts to Pandas DataFrame.
    list_of_data_csv = df.to_csv('list_of_data') # Creates a csv for quicker access to data.

    return stores_list

#-----------------------------------------------------------------------------------------------------------------

def merge_data(items, stores, sales):

    sales = sales.rename(columns={"store": "store_id"})
    sales = sales.rename(columns={"item": "item_id"})

    items_stores_sales = stores.merge(sales, how='inner', on='store_id')
    items_stores_sales = items_stores_sales.merge(sales, how='inner', on='item_id')
    return items_stores_sales
    
    items_stores_sales = df.to_csv('items_stores_sales')
    
#-----------------------------------------------------------------------------------------------------------------

def pull_csv(url):

        req = requests.get(url)
        data = StringIO(req.text)
        df = pd.read_csv(data)
        df = pd.DataFrame(df)
    df_csv = df.to_csv('Open_Power_Systems_Data')    
    return df

#-----------------------------------------------------------------------------------------------------------------