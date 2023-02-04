#!/bin/python3


import re


def validate_html(html):
    '''

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    extags = _extract_tags(html)
    if len(html) > 0 and len(extags) <= 1:
        return False
    for i in range(len(extags)):
        if '/' not in extags[i]:
            stack.append(extags[i])
        else:
            if len(stack) == 0:
                return False
            if stack[-1][1:] in extags[i]:
                stack.pop()
            else:
                return False
    return(len(stack)) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.

    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    xs = re.findall("<([^ >]+)", html)
    return list(map((lambda x: "<" + x + ">"), xs))
