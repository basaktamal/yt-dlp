#!/usr/bin/env python3

# Execute with
# $ python -m yt_dlp

import sys

if __package__ is None and not getattr(sys, 'frozen', False):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import yt_dlp

def abcd():
        return yt_dlp.YoutubeDL({}).extract_info('https://www.youtube.com/watch?v=CJDEtfA33VI', False)

if __name__ == '__main__':
    # yt_dlp.main()
    abcd()
    
