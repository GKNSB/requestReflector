from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE'])
def reflect_request(path):
    # Get the request method and path, including the query string if it exists
    query_string = request.query_string.decode("utf-8")
    full_path = f"/{path}" + (f"?{query_string}" if query_string else "")
    request_line = f"{request.method} {full_path} HTTP/{request.environ.get('SERVER_PROTOCOL').split('/')[1]}"
    
    # Get the headers
    headers = "\n".join([f"{header}: {value}" for header, value in request.headers.items()])

    # Get the body
    body = request.get_data(as_text=True)

    # Combine all parts into the final output
    full_request = f"{request_line}\n{headers}\n\n{body}"
    
    return Response(full_request, content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
