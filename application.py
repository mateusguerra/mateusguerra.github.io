from wsgiref.simple_server import make_server
import os


def application(environ, start_response):
    path = environ['PATH_INFO']

    if path == '/':
        file = 'index.html'
    else:
        file = path[1:]

    name, ext = os.path.splitext(file)
    if ext == '.html':
        mime = 'text/html'
    else:
        mime = 'text/css'

    response = ''

    try:
        with open(file) as f:
            response = f.read()
        status = '200 OK'
        headers = [('Content-type', mime)]
    except FileNotFoundError:
        status = '404 NOT FOUND'
        headers = [('Content-type', mime)]

    start_response(status, headers)
    return [response.encode()]


if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
