# x = ["BMW", "Porshe", "www6"]
finaldata= [
    {
        "id": 4,
        "title": "Hello world",
        "completed": True,
        "created_at": "13-07-2026 23:37",
        "due_date": "2-2-2026"
    },
    {
        "id": 5,
        "title": "BMW",
        "completed": False,
        "created_at": "17-09-2026 23:25",
        "due_date": "05-02-2026"
    },
    {
        "id": 6,
        "title": "Car wash",
        "completed": False,
        "created_at": "22-09-2026 19:22",
        "due_date": "23-09-2026"
    },
    {
        "id": 7,
        "title": "say hi",
        "completed": True,
        "created_at": "22-09-2026 19:25",
        "due_date": "22-09-2026"
    }
]
st = "Hello"

for item in finaldata: 
    if st in item["title"]:


        print (item)

# y= {
#     "title":"hello",
#     "id":"2",
#     "features":{
#         "f1":"Black",
#         "f2":"red"
#     }
#     }
# st = "Black"
# for item, value in y.items(): 
#     # if st in item["f1"]:

#         print (value)
#         print (type(item))