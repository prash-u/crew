# 1) Scaffold a modern Next.js app IN THIS FOLDER (no prompts)
npx create-next-app@latest . \
  --ts \
  --eslint \
  --tailwind \
  --src-dir \
  --app \
  --use-npm \
  --import-alias "@/*"

# 2) Create portfolio + agents structure
mkdir -p projects/pokemon-scanner projects/eeg-visualisation projects/metabolism-sim
echo "v0.1 — skeleton scaffolded" > projects/pokemon-scanner/changelog.md
echo "v0.1 — skeleton scaffolded" > projects/eeg-visualisation/changelog.md
echo "v0.1 — skeleton scaffolded" > projects/metabolism-sim/changelog.md

mkdir -p public/models
mkdir -p agents crew

# 3) Python requirements (CrewAI etc.)
cat > requirements.txt <<'PYREQ'
crewai
langchain
pydantic
PyGithub
litellm
PYREQ

# 4) Minimal agents (placeholders you can extend)
cat > agents/content_agent.py <<'PY'
from crewai import Agent
ContentAgent = Agent(
    role="Content Agent",
    goal="Draft and improve project blurbs and update changelog.",
    backstory="Writes short, clear summaries in markdown for each project.",
    allow_delegation=False,
    verbose=True
)
PY

cat > agents/media_agent.py <<'PY'
from crewai import Agent
MediaAgent = Agent(
    role="Media Agent",
    goal="Generate thumbnails/OG images and keep assets optimized.",
    backstory="Turns text into clean visuals with consistent branding.",
    allow_delegation=False,
    verbose=True
)
PY

cat > agents/qa_agent.py <<'PY'
from crewai import Agent
QAAgent = Agent(
    role="QA Agent",
    goal="Run performance, accessibility and PWA checks; suggest fixes.",
    backstory="Acts like a quality gate with practical, concrete patches.",
    allow_delegation=False,
    verbose=True
)
PY

# 5) Orchestrator (simple, project-centric)
cat > crew/orchestrator.py <<'PY'
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
PY

# 6) Example env file for local LLM via Ollama (CodeLlama)
cat > .env.example <<'ENV'
# For running agents locally with Ollama (OpenAI-compatible endpoint)
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_API_KEY=ollama
LLM_MODEL=openai/codellama
ENV

# 7) Solid .gitignore for Next.js + Python + macOS
cat > .gitignore <<'GI'
# Node
node_modules/
.next/
out/
dist/
.cache/
*.log
npm-debug.log*
yarn-error.log*

# Env & local
.env
.env.local
.DS_Store

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/

# Misc
*.icloud
GI