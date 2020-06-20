from cgi import parse_qs
from templatee import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	sum = d.get('sum', [''])[0]
	product = d.get('product', [''])[0]
	if '' not in [a,b]:
		a,b = int(a), int(b)
		sum = [a+b]	
		product = [a*b]
	response_body = html % {
		'sum' : sum,
		'product' : product,
	}
	start_response('200 ok', [
		('Content-Type', 'text/html'),
		('Content-Type', str(len(response_body)))
	])
	return [(response_body)]