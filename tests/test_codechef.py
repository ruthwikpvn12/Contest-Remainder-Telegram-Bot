from codechef import get_codechef_contests

contests = get_codechef_contests()
for c in contests[:3]:
    print(c["name"], c["start_time"])
