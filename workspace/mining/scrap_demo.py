from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = '''
    <html><head><title>this is a title</title></head>
    '''

    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.string)