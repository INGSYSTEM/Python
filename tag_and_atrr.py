# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class CustumerHtmlParse(HTMLParser):
    def handle_starttag(self, etiquetas, atributos):
        print(etiquetas)
        
        for a,v in atributos:
            print(f'-> {a} > {v}')

if __name__ == '__main__':
    N = int(input())
    html = ''
    
    for _ in range(N):
        html += input()
        
    parse = CustumerHtmlParse()
    parse.feed(html)
