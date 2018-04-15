def present_tense(stem):
    return[stem, stem+"t"]

f = open("stems.txt")
for line in f:
    print present_tense(line.strip())
f.close()



    # content = f.readlines()
# content = [present_tense(x.strip()) for x in content]
# print (content)
