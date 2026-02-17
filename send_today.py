from daily_task import get_today_plan
from mailer import send_email


def format_email(day_plan):
    body = f"Goal: {day_plan['goal']}\n\n"

    body += "Tasks:\n"
    for t in day_plan["tasks"]:
        body += f"- {t}\n"

    body += "\nResources:\n"
    for r in day_plan["resources"]:
        body += f"- {r}\n"

    return body


if __name__ == "__main__":
    current_day, day_plan = get_today_plan()

    if day_plan:
        body = format_email(day_plan)
        send_email(f"TaskForge — Day {current_day}", body)
    else:
        print("No tasks scheduled for today.")