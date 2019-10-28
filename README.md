# Honeypot

This is a very simple multiport honeypot that outputs to the terminal and to a log file to the same directory as the script called honeypot.log.

# Requirements

python 3+, uses the following imports:

    import datetime
    
    import fileinput
    
    import os
    
    import socket
    
    import sys
    
    import time
    
    import threading


# Usage

This is multithreaded and can take multiple port arguments, however it cannot bind to a port if it's already bound:

python .\honeypot.py 8888 8887 443 22

    Listening on Port: 8888
    Listening on Port: 8887
    Listening on Port: 443
    Listening on Port: 22
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 22
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 443
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 8887
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 8888
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 8888
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 8887
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 443
    Mon Oct 28 10:05:09 2019 : connection from: x.x.x.x on port: 22
    
# This will constantly run due to while loop

Keyboard interrupt does not work for this loop, you will need to kill the python process to close this, been trying to fix this.
