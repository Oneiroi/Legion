import re

"""
compilation of regex items is done here so that they occur @ import,
and not on every execution of a method.
"""

#todo: Expand this to return all items, not just ip,url,resp code,bytes
rCombined = re.compile('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s-\s[^\]]+\]\s"(.*)"\s([0-9]+)\s(-|[0-9]+)')

def combined(line):
    """
        Parses a single line in the apache combined format, and returns a list of parse items.
        Args:
            line: single line from an apache combined log
        Returns:
            List on successfull parse, None on failed
    """
    return rCombined.split(line)
