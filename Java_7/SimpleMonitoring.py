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
    else:
        print("No new logins detected")

    t.sleep(10)




# 1. Read JSON file
# 2. Remember previous number of logins
# 3. Every 10 seconds check if new logins were added
# 4. Analyze only the new logins
# 5. If status is FAILED, count failed attempts per user
# 6. If user reaches 5 failed attempts in 60 seconds, print alert - brute force
# 7. def create_alert(alert_type, severity, message, event=None):
