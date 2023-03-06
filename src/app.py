import http.server
import http


class request_handle(http.server.SimpleHTTPRequestHandler):
    """
    自定义请求处理类
    """

    def do_GET(self):
        print('client_address:', self.client_address)
        print('headers:', self.headers)
        print('path:', self.path)
        print("command:", self.command)
        attrs = self.path.split('?')[1]
        print(attrs)
        self.send_response(200, "do_get")
        self.end_headers()
        self.wfile.write('hello world'.encode('UTF-8'))

    def do_POST(self):
        print('client_address:', self.client_address)
        print('headers:', self.headers)
        print('path:', self.path)
        print("command:", self.command)

        self.send_response(200)
        self.end_headers()
        self.wfile.write("i get your message by post".encode("utf-8"))


def my_server():
    addr = "127.0.0.1"
    port = 8080
    server_o = (addr, port)
    httpd = http.server.HTTPServer(server_o, request_handle)
    return httpd


def info():
    print('http...')


if __name__ == '__main__':
    info()
    my_server().serve_forever()
