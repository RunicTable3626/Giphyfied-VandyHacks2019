import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import json
import requests
def GiphyRetriever(key_word):
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
    q = key_word # str | Search query term or prhase.
    limit = 3 # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g' # str | Filters results by specified rating. (optional)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

    try: 
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q,
                                                    limit=limit,
                                                    offset=offset,
                                                    rating=rating,
                                                    lang=lang,
                                                    fmt=fmt)
        giphy_dict_array = api_response.data
        image_url_array = []
        for image in giphy_dict_array:
            image_url_array.append(image.images.original.url)
        i = 0
        for uri in image_url_array:
            with open('GIFS\\' + q + str(i) + '.gif', 'wb') as f:
                f.write(requests.get(uri).content)
            i+=1
    
    ##    pprint(image_url_array[0])
            
            
    ##    print(type(api_response))
    ##    json_string = api_response.read()
    ##    my_dict = json.loads(json_string)
    ##    
    ##    images_array = []
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
PATH_TO_JSON = 'C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/aeneastest/output/'+"lalala"+'.json' 
    # read existing json to memory. you do this to preserve whatever existing data. 
with open(PATH_TO_JSON,'r') as jsonfile:
    json_content = json.load(jsonfile) # this is now in memory! you can use it outside 'open'
    i = 0
for json_entry in json_content['fragments']:
    GiphyRetriever(json_entry['key_word'])
        

    


