from crewai import Agent
MediaAgent = Agent(
    role="Media Agent",
    goal="Generate thumbnails/OG images and keep assets optimized.",
    backstory="Turns text into clean visuals with consistent branding.",
    allow_delegation=False,
    verbose=True
)
