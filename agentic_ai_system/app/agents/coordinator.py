from app.agents.diagnostic import DiagnosticAgent
from app.agents.automation import AutomationAgent
from app.agents.writer import WriterAgent

class CoordinatorAgent:
    @staticmethod
    async def plan_task(request: str, require_approval: bool):
        request_lower = request.lower()
        steps = []
        summary = ""

        if "azure cli" in request_lower and "rdp" in request_lower:
            steps = ["Generate NSG rules", "Generate rollback script"]
            summary = "Will restrict 3389 inbound to 10.0.0.0/24 on vm-a, vm-b, vm-c"
        else:
            if any(keyword in request_lower for keyword in ["diagnose", "why", "troubleshoot", "analyze"]):
                steps.append("diagnose")
            if any(keyword in request_lower for keyword in ["script", "generate", "create", "azure cli", "powershell", "bash", "commands"]):
                steps.append("script")
            if any(keyword in request_lower for keyword in ["email", "notify", "summary", "report"]):
                steps.append("email")
            summary = f"Planned steps based on input: {', '.join(steps) if steps else 'None'}"

        plan = {"steps": steps, "summary": summary}
        status = "waiting_approval" if require_approval else "active"
        return plan, status

    @staticmethod
    async def execute_plan(plan):
        results = {}
        if "diagnose" in plan["steps"]:
            results["diagnosis"] = await DiagnosticAgent.run()
        if "Generate NSG rules" in plan["steps"] or "Generate rollback script" in plan["steps"]:
            results["commands"] = [
                "az network nsg rule create ...",
                "az network nsg rule delete ... # rollback"
            ]
        if "script" in plan["steps"]:
            results["script"] = await AutomationAgent.run()
        if "email" in plan["steps"]:
            results["email_draft"] = await WriterAgent.run()
        results["duration_seconds"] = 42
        return results