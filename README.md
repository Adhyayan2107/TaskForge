# TaskForge

TaskForge is a lightweight **agentic task-planning tool** that converts a high-level goal into a structured day-by-day execution plan and sends daily task reminders via email.

It’s designed as a **personal AI productivity system** that helps break down learning goals, projects, or study plans into manageable daily steps.

Example input:
```
Study agentic AI in 4 days
```

Example output:
- A structured daily plan
- Learning resource recommendations
- Automated daily email reminders

---

## How TaskForge Works

TaskForge follows a simple workflow pipeline:

```
User Task Input
      ↓
Planner (LLM via Groq)
      ↓
Structured Plan (JSON)
      ↓
Saved Locally (plan.json)
      ↓
Auto Day Tracking
      ↓
Daily Task Extractor
      ↓
Email Sender (SMTP)
      ↓
Daily Task Email
```

Simplified workflow:

```
Input → Plan → Store → Track → Email
```

---

## Running TaskForge Locally

### 1. Install dependencies
```
pip install -r requirements.txt
```

---

### 2. Create a `.env` file
```
GROQ_API_KEY=your_key
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_app_password
```

Use a Gmail **App Password**, not your normal password.

---

### 3. Generate a plan
```
python main.py
```

Enter:
```
Task
Duration (days)
```

This creates:
```
plan.json
```

---

### 4. Send today's tasks
```
python send_today.py
```

You’ll receive the daily task email.

---

## Core Idea

TaskForge turns:

```
"I want to do this"
```

into:

```
"Here’s exactly what to do today."
```

using an **LLM planner + automated daily execution reminders**.

---

## Author

Adhyayan Gupta
