<<<<<<< HEAD
=======
# AIAutopilot_Agentic_AI

>>>>>>> 1938c852ea9f9cd5decd4f65789ffa6c87b062af
# 🛡️ Agentic AI System for IT Requests

This project is a FastAPI-based microservice that intelligently handles natural-language IT support requests using an agentic AI architecture. It simulates LLM-powered agents to perform diagnostics, generate automation scripts, and draft emails, with built-in support for approval flows and task status tracking.

---

## 📌 What This Project Does

- Accepts a free-form IT request (e.g., “Diagnose high CPU usage and generate a script”)
- Determines what actions are needed using a CoordinatorAgent
- Executes the correct agents:
  - DiagnosticAgent: Analyzes root cause
  - AutomationAgent: Generates a script (PowerShell, Bash, Azure CLI)
  - WriterAgent: Drafts summary or email
- Supports approval before execution if required
- Returns structured output in JSON
- Includes status tracking via task ID

---

## 🧱 Tech Stack

- Python 3.8+
- FastAPI (API server)
- Uvicorn (ASGI server)
- Pytest (unit testing)
- curl or Postman for testing
- [LLM stubs are simulated but ready for OpenAI/GPT integration]

---

## 🗂️ Folder Structure

```
agentic_ai_system/
├── app/
│   ├── agents/              # Coordinator, Diagnostic, Automation, Writer Agents
│   ├── utils/               # TaskManager for tracking state
│   ├── tests/               # Pytest test cases
│   └── main.py              # FastAPI API server
├── architecture_diagram.png
<<<<<<< HEAD
├── postman_collection.json
=======
>>>>>>> 1938c852ea9f9cd5decd4f65789ffa6c87b062af
└── README.md
```

---

## 🚀 How to Run the Project

1. Clone this repository:
```bash
git clone https://github.com/your-username/agentic-ai-system.git
cd agentic_ai_system
```

2. Create a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install fastapi uvicorn pytest httpx
```

4. Start the API server:
```bash
uvicorn app.main:app --reload
```

5. Open your browser and go to:
```
http://127.0.0.1:8000/docs
```

---

## 🔄 API Endpoints

| Method | Endpoint                            | Description                          |
|--------|-------------------------------------|--------------------------------------|
| POST   | `/api/v1/execute`                   | Submit a new IT task                 |
| POST   | `/api/v1/plans/{task_id}/approve`   | Approve a task awaiting approval     |
| POST   | `/api/v1/plans/{task_id}/reject`    | Reject a pending task plan           |
| GET    | `/api/v1/tasks/{task_id}`           | Get status and output of a task      |

---

## 🧪 Example Use Cases

### ✅ Example A — No Approval
Request:
```json
{
  "request": "Diagnose why Windows Server is slow and generate script and email",
  "require_approval": false
}
```
Expected Response:
```json
{
  "status": "completed",
  "diagnosis": { ... },
  "script": { ... },
  "email_draft": "...",
  "duration_seconds": 42
}
```

---

### ✅ Example B — Approval Flow
Step 1: Request
```json
{
  "request": "Create Azure CLI commands to lock RDP (3389) to 10.0.0.0/24 on all prod VMs",
  "require_approval": true
}
```
Initial Response:
```json
{
  "task_id": "1234...",
  "status": "waiting_approval",
  "plan": {
    "steps": ["Generate NSG rules", "Generate rollback script"],
    "summary": "Will restrict 3389 inbound on all VMs"
  }
}
```

Step 2: Approve it using curl
```bash
curl -X POST http://127.0.0.1:8000/api/v1/plans/1234/approve
```

Final Response:
```json
{
  "status": "completed",
  "commands": [
    "az network nsg rule create ...",
    "az network nsg rule delete ... # rollback"
  ]
}
```

---

## 🧪 Run Unit Tests

```bash
pytest app/tests
```

Covers:
- Happy path (all agents)
- Approval flow
- Retry handling
- Script syntax check

---

## 🗺️ Architecture Diagram

<<<<<<< HEAD
See included architecture_diagram.png file or embed the Mermaid diagram in README:

```mermaid
=======
![Architecture](https://github.com/user-attachments/assets/683f1289-b5fb-4553-b341-a2f02ebc8a9b)

>>>>>>> 1938c852ea9f9cd5decd4f65789ffa6c87b062af
graph TD
    A[User Request] --> B[FastAPI API Layer]
    B --> C[CoordinatorAgent]
    C --> D{Determine Steps}
    D --> E[DiagnosticAgent]
    D --> F[AutomationAgent]
    D --> G[WriterAgent]
    C --> H[Approval Workflow]
    C --> I[TaskManager]
    I --> J[Task Status Storage]
    C --> K[Merge Results]
    K --> L[Return JSON Response]
```

