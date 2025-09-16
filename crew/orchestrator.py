from crewai import Crew, Task
from agents.content_agent import ContentAgent
from agents.media_agent import MediaAgent
from agents.qa_agent import QAAgent

# Example: iterate Pokemon Scanner through v0.2
tasks = [
    Task(
        description="Create a 100-120 word blurb for Pokémon Scanner: what it does, key tech, and next step.",
        agent=ContentAgent,
        expected_output="A concise markdown paragraph saved to projects/pokemon-scanner/blurb.md"
    ),
    Task(
        description="Propose a thumbnail concept and OG image copy for Pokémon Scanner.",
        agent=MediaAgent,
        expected_output="A short markdown with title, subtitle, and alt text saved to projects/pokemon-scanner/media_notes.md"
    ),
    Task(
        description="List concrete perf/a11y checks to run on the Pokémon Scanner page once implemented.",
        agent=QAAgent,
        expected_output="A checklist markdown saved to projects/pokemon-scanner/qa_checklist.md"
    ),
]

crew = Crew(
    agents=[ContentAgent, MediaAgent, QAAgent],
    tasks=tasks,
    verbose=True
)

if __name__ == "__main__":
    crew.kickoff()
