import asyncio
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
from contests import get_codeforces_contests
from bot import send_message
from db import already_sent, mark_sent

scheduler = BlockingScheduler()
print("✅ Scheduler started. Waiting for contests...")

# create ONE event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def check_contests():
    now = datetime.now()
    contests = get_codeforces_contests()

    for c in contests:
        diff = c["start_time"] - now
        name = c["name"]

        if timedelta(minutes=29) < diff < timedelta(minutes=31):
            if not already_sent(name, "30"):
                loop.run_until_complete(
                    send_message(f"⏰ Codeforces contest in 30 minutes\n\n{name}\n{c['link']}")
                )
                mark_sent(name, "30")

        if timedelta(minutes=9) < diff < timedelta(minutes=11):
            if not already_sent(name, "10"):
                loop.run_until_complete(
                    send_message(f"🔥 Codeforces contest in 10 minutes\n\n{name}\n{c['link']}")
                )
                mark_sent(name, "10")

scheduler.add_job(check_contests, "interval", minutes=1)
scheduler.start()

