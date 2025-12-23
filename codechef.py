import requests
from datetime import datetime

def get_codechef_contests():
    url = "https://www.codechef.com/api/list/contests/all"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    contests = []

    for c in data["future_contests"]:
        start_time = datetime.strptime(
            c["contest_start_date_iso"],
            "%Y-%m-%dT%H:%M:%S+05:30"
        )

        contests.append({
            "platform": "CodeChef",
            "name": c["contest_name"],
            "start_time": start_time,
            "link": "https://www.codechef.com/" + c["contest_code"]
        })

    return contests
