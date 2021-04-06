#!/usr/bin/env python3


import argparse


def gendiff():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.accumulate(args.integers))

gendiff()
