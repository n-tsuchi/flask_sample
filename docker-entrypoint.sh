#!/bin/sh
set -e

cd /app
pip install -r requirements.txt
python server.py
