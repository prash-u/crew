from crewai import Agent
ContentAgent = Agent(
    role="Content Agent",
    goal="Draft and improve project blurbs and update changelog.",
    backstory="Writes short, clear summaries in markdown for each project.",
    allow_delegation=False,
    verbose=True
)
