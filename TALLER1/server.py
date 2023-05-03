from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function under a different name
    def adder_function(x):
        s = xmlrpc.client.ServerProxy('http://localhost:8000') #IP RECEPTOR
        sum = (7 + x)
        ans = s.add(sum)
        return ans

    server.register_function(adder_function, 'add')

    server.serve_forever()