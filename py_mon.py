import pymongo
#本机地址
client = pymongo.MongoClient("mongodb://localhost:27017/")
#连接数据库
mydb = client["test"]
con = mydb["form"]

#删除集合里的全部数据
con.delete_many({})

#向集合中插入一条数据(可指定id）
con.insert({"name":'people',"age":32,"add":'Cleveland'})

#插入多条数据
more=[
    {"_id":1,"name":'man',"age":30,"add":'Cleveland'},
    {"_id":2,"name":'woman',"age":28,"add":'China'},
    {"_id":3,"name":'boy',"age":13,"add":'USA'},
    {"_id":4,"name":'sun',"age":12,"add":'England'},
    {"_id":5,"name":'girl',"age":18,"add":'France'},
    {"_id":6,"name":'李峰',"age":23,"add":'Chian'}
]
con.insert_many(more)

#实现更新一整个数据
con.update({"name":'people'},{"name":'Tom',"age":18})

#查询数据库里全部数据
print("集合里的所有数据有")
for item in con.find():
    print(item)
print("--------------------------------------")

#按条件查询
y={"name":"man"}
x=con.find_one(y)
print("其中一个名字为man的人：")
print(x)

#按条件删除其中一条
myquery = {"name": "Tom"}
con.delete_one(myquery)
print("name为Tom的数据已经被删除")
print("--------------------------------------")

#按指定删除多条数据
myquery = {"age": 30}
con.delete_many(myquery)
print("age为32数据的已经全部被删除")
print("--------------------------------------")
print("现在集合里的所有数据有")
for item in con.find():
    print(item)

#用正则表达式来查询
y = { "name": { "$regex": "^李" } }
x=con.find(y)
print("用正则表达式查询到姓李的数据：")
for item in x:
    print(item)

#按指定条数返回
y = con.find().limit(3)
print("按指定条数查询：")
for x in y:
  print(x)
print("--------------------------------------")

#按指定字段查询输出
y=con.find({},{ "_id": 0,"name": 1,"age":1 })
print("按指定字段输出name和age：")
for x in y:
  print(x)
print("---------------------------------------")

#修改数据单个选项
x = {"name": "sun"}
print("修改前：")
print(con.find_one(x))
y = {"$set": {"name": "shun","age":15}}
con.update_one(x,y)
w={"name":"shun"}
print("修改后：")
print(con.find_one(w))
print("-----------------------------------")

#按升降序排序输出
x = con.find().sort("age")
print("升序：")
for y in x:
  print(y)
print("------------------------------------")
x = con.find().sort("age",-1)
print("降序：")
for y in x:
  print(y)

#删除集合里全部数据
con.delete_many({})

#用drop方法删除集合
con.drop()