import http.server
import socketserver
import os

# Thiết lập thư mục hiện tại thành thư mục chứa server.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cấu hình HTTP request handler để hỗ trợ gzip
class GzipHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Nếu là file .gz, thêm header Content-Encoding: gzip
        if self.path.endswith('.gz'):
            self.send_header('Content-Encoding', 'gzip')
        super().end_headers()

# Đặt cổng server (8080 hoặc 8000)
PORT = 8080

# Khởi tạo server với handler mới
Handler = GzipHTTPRequestHandler

# Khởi chạy server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
