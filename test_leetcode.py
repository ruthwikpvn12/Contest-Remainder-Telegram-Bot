from leetcode import get_leetcode_contests

contests = get_leetcode_contests()
print("Total contests:", len(contests))

for c in contests:
    print(c["name"], c["start_time"])
