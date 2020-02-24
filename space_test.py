def getBert(string):
    ting = (string.lower()).split("bert")
    
    if len(ting) > 2:
        return "".join(ting[1])
    else: 
        return ""
print(getBert("sdfhbertkjberthds"))
