from crewai import Agent
QAAgent = Agent(
    role="QA Agent",
    goal="Run performance, accessibility and PWA checks; suggest fixes.",
    backstory="Acts like a quality gate with practical, concrete patches.",
    allow_delegation=False,
    verbose=True
)
