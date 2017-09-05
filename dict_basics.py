info = {
    "name": "Lex",
    "age": 55,
    "home_town": "Bainbridge Island",
    "pet_name": "Thumbelina"
    }

def print_info(dictio):
    for key in dictio:
        print "My {} is {}".format(key, dictio[key])

print_info(info)
