from Planner import generate_plan
from storage import save_plan
import json

def main():
    task = input("Enter your task: ")
    duration = int(input("Enter duration (days): "))

    plan = generate_plan(task, duration)

    save_plan(plan)

    print("\nPlan generated and saved!\n")
    # print(json.dumps(plan, indent=2))


if __name__ == "__main__":
    main()