#!/usr/bin/env python

from neo4j import GraphDatabase
import urllib

def post2dic(data):
    data = data.decode()
    result = {}
    for atributo in data.split('&'):
        print "ATRIBUTO: %s" % atributo
        name = atributo.split('=')[0]
        value = atributo.split('=')[1]
        result[name] = value
    return result
  
def addUser(usuario):
    
    # Create a database
    db = GraphDatabase('/tmp/')
    user_idx = db.node.indexes.get('users')
    cafe_idx = db.node.indexes.get('cafes')

    # All write operations happen in a transaction
    with db.transaction:
        firstNode = db.node(name=usuario, type_record='user')
        user_idx['name'][usuario] = firstNode

        secondNode = cafe_idx['name']['lungo'].single
 
        # Create a relationship with type 'knows'
        relationship = firstNode.toma(secondNode, cantidad=3) 
 
    # Always shut down your database when your application exits
    db.shutdown()

def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])

    if env['PATH_INFO'] == '/':
       return open('front.html', 'r').readlines()
   
    if env['PATH_INFO'] == '/user':
       post_data = post2dic(env['wsgi.input'].readline().decode())
       addUser(post_data['usuario'])
       return ["Hello, World!"]

if __name__ == "__main__":
    from gevent.wsgi import WSGIServer
    
    address = "localhost", 8080
    server = WSGIServer(address, application)
    try:
        print "Server running on port %s:%d. Ctrl+C to quit" % address
        server.serve_forever()
    except KeyboardInterrupt:
        server.stop()
        print "Bye bye"

