class DiagnosticAgent:
    @staticmethod
    async def run():
        return {
            "root_cause": "Wsappx runaway process",
            "evidence": ["perfmon shows high kernel time ..."],
            "solutions": [
                {"title": "Disable Superfetch", "confidence": "high"},
                {"title": "Install KB500XYZ", "confidence": "medium"}
            ]
        }