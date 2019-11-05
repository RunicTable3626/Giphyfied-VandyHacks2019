from google.cloud import language_v1
from google.cloud.language_v1 import enums
import json
import os
import pprint


def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)
    # Loop through entitites returned from the API
    for entity in response.entities:
        return entity.name
##        print(u"Representative name for the entity: {}".format(entity.name))
##        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
##        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
##        # Get the salience score associated with the entity in the [0, 1.0] range
##        print(u"Salience score: {}".format(entity.salience))
##        # Loop over the metadata associated with entity. For many known entities,
##        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
##        # Some entity types may have additional metadata, e.g. ADDRESS entities
##        # may have metadata for the address street_name, postal_code, et al.
##        for metadata_name, metadata_value in entity.metadata.items():
##            print(u"{}: {}".format(metadata_name, metadata_value))
##
##        # Loop over the mentions of this entity in the input document.
##        # The API currently supports proper noun mentions.
##        for mention in entity.mentions:
##            print(u"Mention text: {}".format(mention.text.content))
##            # Get the mention type, e.g. PROPER for proper noun
##            print(
##                u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
##            )
        

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
##    print(u"Language of the text: {}".format(response.language))

# first, get the absolute path to json file
def nlpKeyWordGen(song_name):
    print('Generating key words from lyrics...')
    PATH_TO_JSON = 'C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/aeneastest/output/'+song_name+'.json' 
    # read existing json to memory. you do this to preserve whatever existing data. 
    with open(PATH_TO_JSON,'r') as jsonfile:
        json_content = json.load(jsonfile) # this is now in memory! you can use it outside 'open'
        i = 0
    for json_entry in json_content['fragments']:
    # add the id key-value pair (rmbr that it already has the "name" key value)
            json_content['fragments'][i]["key_word"] = sample_analyze_entities(json_entry['lines'][0])
            if (json_content['fragments'][i]["key_word"] == None):
                json_content['fragments'][i]["key_word"] = json_content['fragments'][i-1]["key_word"]
            i+=1
    with open(PATH_TO_JSON,'w') as jsonfile:
        json.dump(json_content, jsonfile, indent = 4) # you decide the indentation level
    print('Key words generated from lyrics')

    
