import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True )
parser.add_argument("--username")
parser.add_argument("--country")

args = parser.parse_args()

with open(args.file) as f:
    data = json.load(f)

filtered = data

if args.country:
   filtered = [row  for row in filtered if row['country'] == args.country ]
   print('****** Filtered by country ***********')
   for row in filtered:
       print(row)

if args.username:
   filtered = [row  for row in filtered if row['username'] == args.username]
   print('****** Filtered by username ***********')
   for row in filtered:
       print(row)

counter = 0
for event in filtered:
    if event['status']=='FAILED':
        counter+=1

print("Number of failed logins for give file is: ",counter)


# convert to functions,
# load_dataset,
# filter_logs(events, country=None, user=None, status=None, failed_only=False),
# show_events(events)   -- print events
# summarize_by_ip(events)   -- print attempts per ip
# summarize_by_user(events)   -- print attempts per user
#detect_suspicious_ips(events, threshold)  -- print attempts with more than threshold attempts
#detect_suspicious_users(events, threshold)  -- print attempts with more than threshold attempts
# detect_bruteforce(events, threshold=5, window_seconds=60)
# export_to_csv(events, output_file)

# python analyzer.py --file suspicious_logins.json --failed          (onl failed)
# python analyzer.py --file suspicious_logins.json --failed --country Germany --show     show failed from germay
# python analyzer.py --file suspicious_logins.json --ip-summary      summary by ip
# python analyzer.py --file suspicious_logins.json --suspicious-user-threshold 2     detect by user
# python analyzer.py --file suspicious_logins.json --failed --country Germany --export report.csv


