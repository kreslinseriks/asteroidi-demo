#!/bin/bash

# Move to the directory containing naked.py
cd /home/s255/asteroidi-demo

# Run the naked.py program
/usr/bin/python3 /home/s255/asteroidi-demo/naked.py

chmod +x run_naked.sh

crontab -e

0 0 * * * /home/s255/asteroidi-demo/run_naked.sh
