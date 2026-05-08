import time as t
import json as js

with open(r"D:\Data Disk D\Gezimi's folder\Cacttus\2025-2026\Gjuhe skriptuse\Ushtrime\Java_6\suspicious_logins.json",
          'r') as f:
    data = js.load(f)

previous_count = len(data)

while True:
    print("Simple Monitoring .....")

    with open(r"D:\Data Disk D\Gezimi's folder\Cacttus\2025-2026\Gjuhe skriptuse\Ushtrime\Java_6\suspicious_logins.json",'r') as f:
        data = js.load(f)

    actual_count = len(data)

    if actual_count > previous_count:

        new_data = data[previous_count:actual_count]  # 0 - 10

        print(f"{actual_count-previous_count} new logins detected")

        for login in new_data:
            print(login)


        previous_count = actual_count


    t.sleep(10)

