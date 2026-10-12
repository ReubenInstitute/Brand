#!/usr/bin/env python3
import os
from pathlib import Path

CSS_URL = '/@@'
FONT_URL = '/@@'

DATA_FOLDER = '/usr/share/reubeninstitute'
CSS_FOLDER = '/usr/share/reubeninstitute/@@'
FONT_FOLDER = '/usr/share/reubeninstitute/@@'
CACHE_FOLDER = Path.home() / '.reubeninstitute' / 'cache'

if os.environ.get('DATA_FOLDER'):
	DATA_FOLDER = os.environ.get('DATA_FOLDER')
if os.environ.get('CSS_FOLDER'):
	CSS_FOLDER = os.environ.get('CSS_FOLDER')
if os.environ.get('FONT_FOLDER'):
	FONT_FOLDER = os.environ.get('FONT_FOLDER')
