import json
import argparse
import csv
import datetime as d
import time as t

def load_dataset(file):
    with open(file) as f:
        return json.load(f)


def filter_logs(events, country=None, user=None, status=None):
    filtered = events
    if country:
        filtered = [row for row in filtered if row['country'] == country]
    if user:
        filtered = [row for row in filtered if row['username'] == user]
    if status:
        filtered = [row for row in filtered if row['status'] == status]

    return filtered


def count_failed_logins(events):
    counter = 0
    for event in events:
        if event['status'] == 'FAILED':
            counter += 1
    print("Number of failed logins for given file is: ", counter)


def summarize_by_ip(events):
    counter_ip = {}

    for login in events:
        ip_add = login['ip_address']
        if ip_add in counter_ip.keys():
            counter_ip[ip_add] += 1
        else:
            counter_ip[ip_add] = 1

    return counter_ip


def summarize_by_user(events):
    counter_user = {}
    for login in events:
        user = login['username']
        if user in counter_user.keys():
            counter_user[user] += 1
        else:
            counter_user[user] = 1

    return counter_user


def show_events(events):
    for event in events:
        print(event)


def show_summarized(input_dictionary):
    print('Summary:')
    for key, value in input_dictionary.items():
        print(f"{key} --> {value}")


def export_to_csv(events, output_file):
    with open(output_file, "w", newline="") as f:
        fieldnames = events[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"File {output_file} created.")


def detect_suspicious_ips(events, threshold):
    counter_ip = summarize_by_ip(events)
    print(f"Detected suspicious ips with threshold {threshold}"
          f" for given file is : \n")
    for ip, counter in counter_ip.items():
        if counter >= threshold:
            print(f"{ip} --> {counter}")


def detect_suspicious_users(events, threshold):
    counter_user = summarize_by_user(events)
    print(f"Detected suspicious users with threshold {threshold}"
          f" for given file is : \n")
    for user, counter in counter_user.items():
        if counter >= threshold:
            print(f"{user} --> {counter}")


def find_failed_timestamps_for_user(events):
    user_timestamps = {}
    for login in events:
        user = login['username']
        if login['status'] == 'FAILED':
            if user in user_timestamps.keys():
                user_timestamps[user].append(login['timestamp'])
            else:
                user_timestamps[user] = [login['timestamp']]

    return user_timestamps


def detect_bruteforce(events, threshold=5, window_seconds=60):
    # find failed timestamps for user
    failed_timestamps = find_failed_timestamps_for_user(events)

    for user, timestamps in failed_timestamps.items():
        timestamps.sort()

        found_bruteforce = False

        for index in range(len(timestamps) - threshold + 1):
            start = d.datetime.strptime(timestamps[index], "%Y-%m-%dT%H:%M:%S")
            end = d.datetime.strptime(timestamps[index + threshold - 1], "%Y-%m-%dT%H:%M:%S")

            diff = ((end - start).total_seconds())

            if diff <= window_seconds:
                found_bruteforce = True
                print(f"{user} --> Potential brute force")
                break

        if found_bruteforce:
            continue




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--username")
    parser.add_argument("--country")
    parser.add_argument("--status")
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--ip", action="store_true")
    parser.add_argument("--showUser", action="store_true")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--bruteforce", action="store_true")


    args = parser.parse_args()

    events = None
    try:
        events = load_dataset(args.file)
    except FileNotFoundError:
        print("File not found")
    else:
        print("Loaded dataset")


    filtered = filter_logs(events, args.country, args.username, args.status)

    if args.show:
        show_events(filtered)

    if args.ip:
        result = summarize_by_ip(events)
        show_summarized(result)

    if args.showUser:
        result = summarize_by_user(events)
        show_summarized(result)

    if args.csv:
        export_to_csv(filtered, args.file+"_filtered")

    if args.bruteforce:
        while True:
            print("Monitoring bruteforce")

            new_events = load_dataset(args.file)
            detect_bruteforce(new_events, threshold=4, window_seconds=60)

            t.sleep(15)

if __name__ == '__main__':
    main()

# convert to functions,
# load_dataset,
# filter_logs(events, country=None, user=None, status=None, failed_only=False),
#    -- print events
# summarize_by_ip(events)   -show_events(events)- print attempts per ip
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


