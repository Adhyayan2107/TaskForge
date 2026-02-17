from fastapi import FastAPI
from Planner import generate_plan
from storage import save_plan
from send_today import format_email
from mailer import send_email

app = FastAPI()


@app.get("/")
def home():
    return {"status": "TaskForge running"}


@app.post("/create-plan")
def create_plan(task: str, duration: int):
    plan = generate_plan(task, duration)
    save_plan(plan)
    return plan


@app.post("/send-day")
def send_day(day: int):
    from daily_task import get_day_plan

    day_plan = get_day_plan(day)

    if not day_plan:
        return {"error": "Day not found"}

    body = format_email(day_plan)
    send_email(f"TaskForge — Day {day}", body)

    return {"status": "email sent"}