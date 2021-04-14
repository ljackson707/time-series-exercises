# This is a loop that will take in a request and output all avalible pages.

def data_request_loop(url1, url2, item)
'''
This function takes in a mian request url == (url1), a secondary url == (url2),
and a specificed page name == (item). Then this fucntion runs a loop for each page to
acquire the data. Next the fucntion converts data dictonary into a data frame, then converts
data to csv for quicker access. THis function will return the stores_list and you will have a 
csv local file in your directory. 
'''

    list_of_data = [] 

    response = requests.get(url1)
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url2 = 'https://python.zach.lol/api/v1/stores?page='+str(i)
        response = requests.get(url2)
        data = response.json()
        page_items = data['payload'][item]
        list_of_data.append(page_items)
        list_of_data = list_of_data + page_items # This allows you to access the new list of items. 
        list_of_data = pd.DataFrame(data['payload'][item]) # Converts to Pandas DataFrame.
        list_of_data_csv = df.to_csv('list_of_data') # Creates a csv for quicker access to data.

        return stores_list