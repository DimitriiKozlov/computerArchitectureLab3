from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
from operations import create, read, update, delete, read_all

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="http://example.com/sample.wsdl", prefix="ns0",
    trace=True,
    ns=True)

dispatcher.register_function('Create', create, returns={'Node': str}, args={'name': str, 'surname': str})
dispatcher.register_function('Read', read, returns={'Node': str}, args={'st_id': int})
dispatcher.register_function('Update', update, returns={'Node': str}, args={'st_id': int, 'name': str, 'surname': str})
dispatcher.register_function('Delete', delete, returns={'Node': str}, args={'st_id': int})
dispatcher.register_function('Read_all', read_all, returns={'Node': list}, args={})

print "Starting server..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()