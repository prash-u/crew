# crew/orchestrator.py
from crewai import Agent, Task, Crew, LLM

# ---- LLM: force Ollama (local) ----
# If your Ollama listens on 127.0.0.1:11434 (default), this is correct.
# The api_key is ignored by Ollama but some stacks expect a value.
ollama_llm = LLM(
    model="codellama",
    provider="ollama",
    base_url="http://127.0.0.1:11434",
    api_key="ollama",
    temperature=0.2,
)

# ---- Agents: define them here with llm=ollama_llm ----
content_agent = Agent(
    role="Content Agent",
    goal="Draft and improve project blurbs and update changelog.",
    backstory="Writes short, clear summaries in markdown for each project.",
    allow_delegation=False,
    verbose=True,
    llm=ollama_llm,
)

media_agent = Agent(
    role="Media Agent",
    goal="Propose thumbnails/OG copy and keep assets consistent.",
    backstory="Turns text into clean visuals with consistent branding.",
    allow_delegation=False,
    verbose=True,
    llm=ollama_llm,
)

qa_agent = Agent(
    role="QA Agent",
    goal="List concrete perf/a11y/PWA checks and fixes.",
    backstory="Acts like a quality gate with practical, concrete patches.",
    allow_delegation=False,
    verbose=True,
    llm=ollama_llm,
)

# ---- Tasks: (optionally) also pin llm per task for belt-and-braces ----
tasks = [
    Task(
        description=(
            "Create a 100–120 word blurb for Pokémon Scanner: "
            "what it does, key tech, and the next step."
        ),
        expected_output=(
            "A concise markdown paragraph saved to "
            "projects/pokemon-scanner/blurb.md"
        ),
        agent=content_agent,
        llm=ollama_llm,
    ),
    Task(
        description=(
            "Propose a thumbnail concept and OG image copy for Pokémon Scanner "
            "(title, subtitle, alt text)."
        ),
        expected_output=(
            "A short markdown saved to projects/pokemon-scanner/media_notes.md"
        ),
        agent=media_agent,
        llm=ollama_llm,
    ),
    Task(
        description=(
            "List concrete performance, accessibility and PWA checks to run on "
            "the Pokémon Scanner page once implemented."
        ),
        expected_output=(
            "A checklist markdown saved to projects/pokemon-scanner/qa_checklist.md"
        ),
        agent=qa_agent,
        llm=ollama_llm,
    ),
]

# ---- Crew: no surprises, but we still pass llm here too ----
crew = Crew(
    agents=[content_agent, media_agent, qa_agent],
    tasks=tasks,
    llm=ollama_llm,
    verbose=True,
)

if __name__ == "__main__":
    crew.kickoff()