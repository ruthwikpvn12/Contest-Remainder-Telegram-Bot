from datetime import datetime, timedelta

def get_mentorpick_contests():
    contests = []

    now = datetime.now()

    # MentorPick rule:
    # Every Thursday at 21:00 (9 PM)
    target_weekday = 3  # Monday=0, Thursday=3
    target_hour = 21
    target_minute = 0

    days_ahead = target_weekday - now.weekday()
    if days_ahead < 0:
        days_ahead += 7

    contest_date = now + timedelta(days=days_ahead)
    contest_time = contest_date.replace(
        hour=target_hour,
        minute=target_minute,
        second=0,
        microsecond=0
    )

    # If today's Thursday and contest already passed, move to next week
    if contest_time <= now:
        contest_time += timedelta(days=7)

    contests.append({
        "platform": "MentorPick",
        "name": "MentorPick Weekly Contest",
        "start_time": contest_time,
        "link": "https://mentorpick.com"
    })

    return contests
