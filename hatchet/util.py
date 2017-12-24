import json
from pygments import highlight, lexers, formatters


def pretty_json_dumps(json_object):
    formatted_json = json.dumps(json_object, sort_keys=False, indent=4)
    colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    return colorful_json
