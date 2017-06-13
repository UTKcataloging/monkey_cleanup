import xmltodict
import json
import os


def get_transcript(x):
    number_of_dictionaries = 0
    number_of_lists = 0
    other = 0
    for record in os.walk(x):
        for y in record[2]:
            f = open("{0}{1}".format(x, y))
            text = f.read()
            new_string = json.dumps(xmltodict.parse(text))
            the_stuff = json.loads(new_string)
            try:
                if type(the_stuff['mods']['note']) != str:
                    if(type(the_stuff['mods']['note'])) is dict:
                        number_of_dictionaries += 1
                        new_ocr = open('../ocr/{0}'.format(y), 'w')
                        new_ocr.write(the_stuff['mods']['note']['#text'])
                        new_ocr.close()
                    elif(type(the_stuff['mods']['note'])) is list:
                        for thing in the_stuff['mods']['note']:
                            if(type(thing)) is dict:
                                number_of_lists += 1
                                new_ocr = open('../ocr/{0}'.format(y), 'w')
                                new_ocr.write(thing['#text'])
                                new_ocr.close()
            except KeyError:
                pass
    print("Totals:\n\n\tDictionaries: {0}\n\n\tLists: {1}".format(number_of_dictionaries, number_of_lists))

if __name__ == "__main__":
    path = '../modsxml/'
    get_transcript(path)
