import json

new={"name" :{"firstname" :[" ramya"," soumya"] } ,"address":{"PA":["NA,AMERICA"],"PIN":1234}}
print(new)
print(json.dumps(new))
print(new["name"]["firstname"])
for i in new:
    print(i)
    print(new[i]["firstname"])