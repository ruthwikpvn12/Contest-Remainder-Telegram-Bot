from mentorpick import get_mentorpick_contests

contests = get_mentorpick_contests()
for c in contests:
    print(c["name"], c["start_time"])
