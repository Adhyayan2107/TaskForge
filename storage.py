import json
from datetime import date


def save_plan(plan):
    data = {
        "start_date": str(date.today()),
        "plan": plan
    }

    with open("plan.json", "w") as f:
        json.dump(data, f, indent=2)


def load_plan():
    with open("plan.json", "r") as f:
        return json.load(f)