from utils.textsplitter import split

textpath = 'data/books/ARoomWithAView.txt'

data = split(open(textpath).read())[:100]