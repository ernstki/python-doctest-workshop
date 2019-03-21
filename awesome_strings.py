"""
A super awesome string manipulation library
"""
import re

class AwesomeStringInputIsNone(Exception): pass


def ALLCAPSBRO(s):
    """
    >>> ALLCAPSBRO('this is a test')
    'THIS IS A TEST'
    >>> ALLCAPSBRO()
    Traceback (most recent call last):
      ...
    TypeError: ALLCAPSBRO() missing 1 required positional argument: 's'
    >>> ALLCAPSBRO()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      ...
    TypeError: <<< anything here, doesn't matter >>>
    """
    return s.upper()


def StUdLyCaPs(s):
    """
    >>> StUdLyCaPs('some test string')
    'SoMe tEsT StRiNg'
    >>> StUdLyCaPs()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError: <<whatever>>
    >>> StUdLyCaPs(None)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    AwesomeStringInputIsNone: 
    """

    if s is None:
        raise AwesomeStringInputIsNone("OH NOES")

    result = []
    for i in range(0,len(s)):
        if i % 2 == 0:
            result.append(s[i].upper())
        else:
            result.append(s[i].lower())
    return ''.join(result)




def CamelCase(s):
    pass


def kebab_case(s):
    pass


def snake_case(s):
    pass


def reverse_string(s):
    pass


def ap_title(s):
    """
    Return properly title-cased version of input string according to AP style
    guide rules.

    The AP stylebook says:
    - capitalize the principal words, including prepositions and
      conjunctions of four or more letters.
    - capitalize an article – the, a, an – or words of fewer than four
      letters if it is the first or last word in a title.

    (source: https://writers.stackexchange.com/a/4622)

    Here's how you use the 'ap_title' function:

    >>> ap_title('the the')  # British post-punk band
    'The The'

    >>> ap_title('the cat in the hat')  # simple book title
    'The Cat in the Hat'

    >>> ap_title('over the hills and through the woods')  # ≥ 4 char prep.
    'Over the Hills and Through the Woods'

    >>> ap_title('you and the horse you rode in on')  # preposition at end
    'You and the Horse You Rode in On'

    >>> ap_title('you and the horse you rode in on!')  # punctuation at end
    'You and the Horse You Rode in On!'

    >>> ap_title('to boldly go, but, then again...')  # preposition w/ comma
    'To Boldly Go, but, Then Again...'

    >>> ap_title('to boldly go, but, then again...')  # doctest: +ELLIPSIS
    'To Boldly Go, but...'

    >>> ap_title()
    Traceback (most recent call last):
      ... # <<< Exceptions are handled specially, anything here is ignored >>
    TypeError: ap_title() missing 1 required positional argument: 's'

    >>> ap_title()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError: <<< absolutely anything here, but exception type must match>>>

    """
    ARTS  = ['a', 'an', 'the']

    # source: https://en.wikibooks.org/wiki/English_in_Use
    #                  /Prepositions,_Conjunctions,_and_Interjections
    PREPS = ['about', 'above', 'across', 'after', 'against', 'along', 'amid',
            'amidst', 'among', 'around', 'at', 'before', 'behind', 'below',
            'beneath', 'beside', 'besides', 'between', 'beyond', 'during',
            'except', 'for', 'from', 'in', 'into', 'of', 'off', 'on',
            'outside', 'over', 'past', 'through', 'throughout', 'to', 'toward',
            'towards', 'under', 'underneath', 'until', 'with', 'within',
            'without']

    CONJS = ['although', 'and', 'as', 'because', 'both', 'but', 'either',
            'even', 'except', 'for', 'however', 'if', 'lest', 'neither',
            'nevertheless', 'nor', 'notwithstanding', 'or', 'provided', 'save',
            'seeing', 'since', 'so', 'than', 'that', 'then', 'though',
            'unless', 'whereas', 'whether', 'yet']

    # see https://writers.stackexchange.com/a/4622
    AP_CAP_IF_THIS_LONG = 4  # AP stylebook says capitalize if >=4 characters

    words = []
    preps = [p for p in PREPS if len(p) < AP_CAP_IF_THIS_LONG]
    conjs = [c for c in CONJS if len(c) < AP_CAP_IF_THIS_LONG]
    # for Chicago Manual of of Style, this would be:
    # excludes = ARTS + PREPS + CONJS
    excludes = ARTS + preps + conjs

    for word in s.split():
        bareword = re.sub('[^\w]', '', word)  # remove punctuation
        words.append(word if bareword in excludes else word.capitalize())

    # always capitalize the first and last words, regardless:
    words[-1] = words[-1].capitalize()
    words[0] = words[0].capitalize()

    return ' '.join(words)
