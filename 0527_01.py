def div_name(name):
    return name[0], name[1:len(name)]

def div_name2(name):
    return name[0], name[1]+name[2]

print(div_name("기태연"))
print(div_name2("기태연"))