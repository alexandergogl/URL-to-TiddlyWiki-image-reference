"""
Alfred script: Convert an image url to a tiddly url.
"""

import sys


def url_to_tiddly_imgref(Text, Delimiter=' '):
    splitted = Text.split(Delimiter, 1)

    # Format URL
    imgref = '[img[%s]]' % splitted[0]

    # Format caption
    if len(splitted) > 1:
        caption = "<figcaption>\n%s\n</figcaption>" % splitted[1]
        # Remove line breaks
        caption = caption.replace("\n", " ")

        # Compose TiddlyWiki entry
        entry = "%s\n%s" % (imgref, caption)
    else:
        # Compose TiddlyWiki entry
        entry = "%s" % imgref

    return entry


input = sys.argv[1]
entry = url_to_tiddly_imgref(input)
print(entry)
