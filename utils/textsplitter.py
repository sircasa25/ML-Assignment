from nltk import tokenize

def split(text):
    '''
    Splits text into separate lines.

    Args:
        text: String to be split into sentences
    
    Returns:
        sentences: Array of sentences
    '''
    sentences = tokenize.sent_tokenize(text)
    return sentences