import tornado.httpserver
import tornado.ioloop
from tornadows import soaphandler
from tornadows import webservices
from tornadows import xmltypes
from tornadows.soaphandler import webservice

class EchoService(soaphandler.SoapHandler):
	""" Echo Service """
	@webservice(_params=xmltypes.String,_returns=xmltypes.String)
  	def echo(self, message):
     		return 'Echo say : '+message

class CountService(soaphandler.SoapHandler):
	""" Service that counts the number of items in a list """
   	@webservice(_params=xmltypes.Array(xmltypes.String),_returns=xmltypes.Integer)
	def count(self, list_of_values):
		length = len(list_of_values)
		return length

class DivService(soaphandler.SoapHandler):
	""" Service that provides the division operation of two float numbers """
	@webservice(_params=[xmltypes.Float,xmltypes.Float],_returns=xmltypes.Float)
	def div(self, a, b):
		result = a/b
		return result

class FibonacciService(soaphandler.SoapHandler):
	""" Service that provides Fibonacci numbers """
	@webservice(_params=xmltypes.Integer,_returns=xmltypes.Array(xmltypes.Integer))
	def fib(self,n):
		a, b = 0, 1
		result = []
		while b < n:
			result.append(b)
			a, b = b, a + b
		return result

if __name__ == '__main__':
  	service = [('EchoService',EchoService),
        	   ('CountService',CountService),
             	   ('DivService',DivService),
             	   ('FibonacciService',FibonacciService)]
  	app = webservices.WebService(service)
  	ws  = tornado.httpserver.HTTPServer(app)
  	ws.listen(8080)
  	tornado.ioloop.IOLoop.instance().start()
