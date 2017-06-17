from cgi import parse_qs
import json

def application(environ, start_response):

    try:
	request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
	request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    s = str(d.get('s', [''])[0])
    c = str(d.get('c', [''])[0])

    length = len(s)
    if len(c)==1:
        count = s.count(c)
    else:
	count = 0
    status = '200 OK'
    response_body = json.dumps({'length': length, 'count': count})

    response_headers = [
	('Content-Type', 'application/json'),
	('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]
