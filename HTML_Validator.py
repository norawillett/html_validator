#!/bin/python3


def validate_html(html):
    '''
        This function performs a limited
        version of html validation by checking
        whether every opening tag has a corresponding closing tag.
        >>> validate_html('<strong>example</strong>')
        True
        >>> validate_html('<strong>example')
        False
    '''
    tagged = _extract_tags(html)
    index = 0
    stack = []
    balanced = True
    if len(tagged) == 0:
        return False
    if len(html) == 0:
        return True
    while index < len(tagged) and balanced:
        tag = tagged[index]
        tagname = tag[1:-1]
        if '/' not in html:
            stack.append()
        else:
            if len(stack) == 0:
                return False
            else:
                lasttag = stack.pop()
                if lasttag != tagname[1:-1]:
                    balanced = False
        index += 1


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that
    are not meant to be used directly by the user are
    prefixed with an underscore.
    This function returns a list of all the html tags
    contained in the input string,stripping out all text
    not contained within angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    import re
    tags = re.findall(r'<[^>]+>', html)
    return tags
