from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

cert_info = ssl._ssl._test_decode_cert("Filename or path to your self signed certificate")

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #Respond to the get request from the client. Use the following methods to set the correct HTTP headers.
        #Our response data is in the response variable. We should tell the client the content type in the headers
        
        #send_response()
        #send_header()
        #end_headers()

        expiry = cert_info['notAfter']
        response = (f"""
        <html>
            <body style="text-align:center;">
                <h1>HTTPS Works!</h1>
                <p>Certificate expires at:</p>
                <b>{expiry}</b>
            </body>
        </html>
        """)
        #write our response into the wfile
        self.wfile.write()


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="Filename or path to your self signed certificate ", keyfile="Filename or path to your private key")

#httpd = HTTPServer(address, MyHandler)
#httpd.socket = context.wrap_socket(,) https://docs.python.org/3/library/http.server.html

print(f"Serving on {httpd.server_address}")
httpd.serve_forever()