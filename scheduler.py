import traceback

from contests import get_all_contests
from bot import send_message

def main():
    try:
        contests = get_all_contests()

        if not contests:
            print("No contests found. Exiting cleanly.")
            return

        for c in contests:
            if c.get("notify"):
                msg = (
                    "⏰ Contest Reminder!\n"
                    f"{c.get('name')}\n"
                    f"Starts at: {c.get('start_time')}"
                )
                send_message(msg)

        print("Scheduler run completed successfully.")

    except Exception as e:
        print("❌ ERROR OCCURRED (but workflow will not fail)")
        traceback.print_exc()

if __name__ == "__main__":
    main()
