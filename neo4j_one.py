from py2neo import Graph,Node,Relationship,NodeSelector

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="12345"
)

#删除全部

graph.run("match(n) detach delete n")

#创建节点
a=Node("Person",name="李嘉诚",born=1928,age=90)
b=Node("Person",name="李泽钜",born=1964,age=52)
c=Node("Person",name="李泽楷",born=1966,age=52)
d=Node("Person",name="李长治",born=2009,age=9)
graph.create(a)
graph.create(b)
graph.create(c)
graph.create(d)

#建立节点间的关系
a_b=Relationship(a,'长子',b)
graph.create(a_b)
a_c=Relationship(a,'次子',c)
graph.create(a_c)
a_d=Relationship(a,'孙子',d)
graph.create(a_d)
b_a=Relationship(b,'父亲',a)
graph.create(b_a)
b_c=Relationship(b,'兄弟',c)
graph.create(b_c)
b_d=Relationship(b,'大伯',d)
graph.create(b_d)

#查询全部
sum=graph.find(label="Person")
for i in sum:
    print(i)
print("--------------------------------------")

#查询
node=graph.find_one(label='Person', property_key='name', property_value="李嘉诚")
print(node)
print("------------------------")
so=NodeSelector(graph)
find_man=so.select("Person",name="李泽楷")
print(list(find_man))

#更新节点属性
node1 = graph.find_one(label='Person', property_key='name', property_value="李泽钜")
node1['age'] = 54
graph.push(node1)

#删除单条关系，用run方法
graph.run('MATCH (a)-[r:兄弟]-(b) where a.name="李泽钜" and b.name="李泽楷"  delete r;')

#修改单条关系
graph.run('MATCH (a)-[:兄弟]-(b) where a.name="李泽钜" and b.name="李泽楷" merge(a)-[:弟弟]->(b);')

#删除节点及其关系，采用run方法
graph.run('match(nonde2:Person{name:"李长治"}) detach delete nonde2')

#查询全部
print("------------------------------")
sum=graph.find(label="Person")
for i in sum:
    print(i)

#查找关系
print("----------------------------------")
fr = graph.match_one(start_node=node,end_node=node1)
print(fr)
