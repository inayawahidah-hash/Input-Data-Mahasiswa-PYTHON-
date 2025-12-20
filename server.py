from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8010

class SimpleHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path== "/" or self.path=="/index.html":
			self.send_response(200)
			self.send_header("Content type", "text/html")
			self.end_headers()
			
			with open("index.html", "rb") as file:
				self.wfile.write(file.read())
				
		elif self.path=="/about.html":
			self.send_response(200)
			self.send_header("Content type", "text/html")
			self.end_headers()
			
			with open("about.html", "rb") as file:
				self.wfile.write(file.read())
		else:
			self.send_response(404)
			self.end_headers()
			self.wfile.write(b"404 - Halaman tidak ada")
			
	def load_page(self, filename):
		self.send_response(200)
		self.send_header("Content type", "text/html")
		self.end_headers()
			
		with open(filename, "rb") as file:
			self.wfile.write(file.read())
	
if __name__=="__main__":
	server = HTTPServer((HOST, PORT), SimpleHandler)
	print(f"server berjalan di http://{HOST}:{PORT}")
	server.serve_forever()