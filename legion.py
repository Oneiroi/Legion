#!/usr/bin/env python3
import os
import sys


def _pathAppend(aPath):
    """
        Appends a directory to sys.path if it exists.
        Args:
            aPath: complete directory path
        Returns:
            True on appended,
            None on allready appended or dir does nto exist.
    """
    if os.path.isdir(aPath) and (aPath not in sys.path):
        sys.path.append(aPath)
        print('Added',aPath)
        return True
    else:
        print('Failed',aPath)
        return None

if __name__ == '__main__':
    '''Append system paths for modules and libdir'''
    _pathAppend(os.path.join(sys.path[0],'modules'))
    _pathAppend(os.path.join(sys.path[0],'lib'))    
    _pathAppend(os.path.join(sys.path[0],'modules'))
