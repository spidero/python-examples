#!/usr/bin/python

# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='description')

parser.add_argument("--verbose",
                    help='Set verbosity level',
                    choices=['DEBUG', 'INFO', 'WARNING', 'CRITICAL'],
                    default='CRITICAL'
                    )
                    
parser.add_argument('--param1',
                    help='''description
                    multiline''',
                    required=True
                    )
                  
parser.add_argument('--param2', default='defaults')
