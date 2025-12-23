import requests
from datetime import datetime

def get_codeforces_contests():
    url = "https://codeforces.com/api/contest.list"
    data = requests.get(url).json()

    contests = []
    for c in data["result"]:
        if c["phase"] == "BEFORE":
            start = datetime.fromtimestamp(c["startTimeSeconds"])
            contests.append({
                "name": c["name"],
                "start_time": start,
                "link": f"https://codeforces.com/contest/{c['id']}"
            })
    return contests
