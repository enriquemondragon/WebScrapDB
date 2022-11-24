import sys
import codecs
from html.parser import HTMLParser

class Parser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.recording = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.recording = True
        else:
            self.recording = False
            
    def handle_data(self, data):
        if self.recording:
            print(f"Found data for tag: {repr(data)}")
            self.recording = False


def main(argv):
    print(argv)
    f = codecs.open(argv, 'r')
    doc = f.read()
    print(doc)

    p = Parser()
    p.feed(doc)
    

if __name__=='__main__':
    try:
        main(sys.argv[1])
    except IndexError: print('\nMissing HTML to parse\n')