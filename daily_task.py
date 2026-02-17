from storage import load_plan
from datetime import date


def get_current_day_number():
    data = load_plan()

    start_date = date.fromisoformat(data["start_date"])
    today = date.today()

    return (today - start_date).days + 1


def get_today_plan():
    data = load_plan()
    plan = data["plan"]

    current_day = get_current_day_number()

    for day in plan["days"]:
        if day["day"] == current_day:
            return current_day, day

    return current_day, None