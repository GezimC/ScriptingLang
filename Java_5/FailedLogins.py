import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")

args = parser.parse_args()

if args.file:
    with open(args.file) as f:
        data = json.load(f)

counter = 0
for event in data:
    if event['status']=='FAILED':
        counter+=1

print("Number of failed logins for give file is: ",counter)

