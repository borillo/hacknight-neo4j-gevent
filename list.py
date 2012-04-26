from neo4j import GraphDatabase
 
# Create a database  
db = GraphDatabase('/tmp/')

user_idx = db.node.indexes.users
print user_idx['name']['usuario'].single
 
# Always shut down your database when your application exits
db.shutdown()
