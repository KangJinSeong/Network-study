'''
Date: 2022.06.17
Title: 
By: Kang Jin Seong
'''
#HTTP GET 서버 프로그램

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

#다중 query를 딕셔너리로 분해한다.
def query_parse(query):
    a = query.split('&')
    temp = []
    for item in a:
        temp.append(item.split('='))
    for i in range(len(temp)):
        if len(temp[i]) == 1:
            temp[i].append('')
    return dict(temp)

class SimpleHTTPRequestHandelr(BaseHTTPRequestHandler):
    #GEt request를 처리한다.
    def do_GET(self):
        parsed_path = parse.urlparse(self.path) #URL 분해
        msg = parsed_path.query #URL 에서 query를 찾는다.
        if msg == '':
            return
        
        #query를 딕셔너리로 분해한다.
        parsed_query = query_parse(msg)
        resp = "Fault"  #허용되지 않은 query를 받았을 때 전송 메세지
        #query를 분석하여 응답 메시지를 구성한다.
        try:
            if parsed_query["led"] == "on":
                resp = "the led is on"
            elif parsed_query["led"] == "off":
                resp = "the led is off"
        except:
            pass

        #헤더 전송
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset = utf-8')
        self.end_headers()

        #응답 전송
        self.wfile.write(resp.encode())

httpd = HTTPServer(('192.168.0.144', 8080), SimpleHTTPRequestHandelr)
httpd.serve_forever()