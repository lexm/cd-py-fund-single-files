def lists_to_dict(arr1, arr2):
    result = {}
    for i in range(len(arr1)):
        result[arr1[i]] = arr2[i]
    return result

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print lists_to_dict(name, favorite_animal)
