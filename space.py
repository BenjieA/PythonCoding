def getBert(string):
    array = (string.lower()).split("bert")

    if len(array) > 2:
        apple = "".join(array[1])
        return apple[::-1]
    else: 
        return ""
print(getBert("sdfhfffbertdolphinberthdfffs"))
