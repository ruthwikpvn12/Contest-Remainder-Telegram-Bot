import requests
from datetime import datetime, timezone

def get_leetcode_contests():
    url = "https://leetcode.com/graphql"

    payload = {
        "query": """
        query getContestList {
          allContests {
            title
            titleSlug
            startTime
            duration
          }
        }
        """
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    contests = []

    if "data" not in data or "allContests" not in data["data"]:
        return contests

    now = datetime.now(timezone.utc).timestamp()

    for c in data["data"]["allContests"]:
        # only FUTURE contests
        if c["startTime"] > now:
            start_time = datetime.fromtimestamp(
                c["startTime"], tz=timezone.utc
            ).astimezone()

            contests.append({
                "platform": "LeetCode",
                "name": c["title"],
                "start_time": start_time,
                "link": "https://leetcode.com/contest/" + c["titleSlug"]
            })

    return contests
