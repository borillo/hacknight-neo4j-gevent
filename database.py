from neo4j import GraphDatabase
 
# Create a database
db = GraphDatabase('/tmp/')

user_idx = db.node.indexes.create('users')
cafe_idx = db.node.indexes.create('cafes')
 
# All write operations happen in a transaction
with db.transaction:
   firstNode = db.node(name='usuario', node_type='user')
   secondNode = db.node(name='lungo', node_type='cafe')
 
   user_idx['name']['usuario'] = firstNode
   cafe_idx['name']['lungo'] = secondNode

   # Create a relationship with type 'knows'
   relationship = firstNode.toma(secondNode, cantidad=3)
 
# Always shut down your database when your application exits
db.shutdown()
