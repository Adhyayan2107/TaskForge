import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


SYSTEM_PROMPT = """
You are TaskForge, a planning assistant.

Return ONLY valid JSON.

Format:
{
  "task": "string",
  "days": [
    {
      "day": 1,
      "goal": "string",
      "tasks": ["string"],
      "resources": ["string"]
    }
  ]
}

Rules:
- Keep output concise
- Max 3 tasks per day
- Max 2 resources per day
- No explanation text
"""


def generate_plan(task: str, duration: int):
    user_prompt = f"""
Task: {task}
Duration: {duration} days
Create a learning plan.
"""

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )

    content = completion.choices[0].message.content
    return json.loads(content)