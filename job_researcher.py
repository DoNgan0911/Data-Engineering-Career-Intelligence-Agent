# Import the libraries
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from IPython.display import display, Markdown
from langchain_openai import ChatOpenAI


# #tools to perform web searches
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Agent 1: Job Market Researcher
research_agent = Agent(
    role = "Data Engineering Job Market Researcher",
    goal = "Research current Data Engineering job postings to identify commonly required qualifications, technical skills, experience requirements",
    backstory = "You are a job market researcher focused on Data Engineering. You gather information from reliable real job postings "
    "and industry resources from 2025 onward, identify ongoing requirements, and organize these information into structured findings. " \
    "Distinguish frequently required skills from occasionall skills.",
    llm = "gpt-4o-mini",
    tools = [search_tool, scrape_tool],
    verbose = True
)
# Agent 2: Skill Gap Analyst
analyst_agent = Agent(
    role = "Data Engineering Skill Gap Analyst",
    goal = "Analyze the job market research to find the core skills and technologies required for entry-level Data Engineering roles and organize them by proficiency level.",
    backstory = "You are an experienced Data Engineering skills analyst. You transform job-market research into a structured skill framework. " \
    "Compare the frequency and importance of technologies, group related skills into categories, and distinguish foundational skills from intermediate and advanced skills. " \
    "Base your analysis on the research evidence rather than assumptions.",
    llm = "gpt-4o-mini",
    verbose = True
)
# Agent 3: Project Architect
architect_agent = Agent(
    role = "Data Engineering Project Architect",
    goal = "Design practical projects that demonstrate the skills identified by the Skill Gap Analyst and reflect realistic Data Engineering workflows.",
    backstory = "You are a Data Engineering project architect who designs projects for aspiring Data Engineers. Translate required skills into practical projects that progressively increase in complexity. Each project should have a clear objective, technology stack, data source, pipeline architecture, expected deliverables, and skills demonstrated.",
    llm = "gpt-4o-mini",
    verbose = True
)
# Agent 4: Career Roadmap Planner
plan_agent = Agent(
    role = "Data Engineering Career Roadmap Planner",
    goal = "Create a structured learning roadmap that prioritizes the skills and projects needed to prepare for entry-level Data Engineering roles.",
    backstory = "You are an experienced career roadmap planner specializing in Data Engineering. Combine job-market evidence, skill-gap analysis, and project recommendations into a realistic progression from foundational knowledge to job readiness. Organize the roadmap by learning phases and explain why each skill or project appears at that stage.",
    llm = "gpt-4o-mini",
    verbose = True
)

# Task 1: Searching job postings
searching_task = Task(
    description = 'Research recent Data Engineering job postings and reliable industry resources, focusing on entry-level and higher roles. Identify the most ' \
    'common programming languages, databases, technical skills, tools, frameworks ,education requirements. Organize the findings so it can be used by a Skill Gap Analyst.',
    expected_output = 'A structured research report containing: \n' \
    '1. Common Programming languages \n' \
    '2. Common Databases \n' \
    '3. Common Technical Skills \n' \
    '4. Common Tools and Frameworkds \n' \
    '5. Education requirements \n' \
    '6. The approximate number of sources mentioning each major skill when available \n' \
    '7. A coherent summary of the most frequently required skills',
    agent = research_agent
)

# Task 2: Analyzing SKill Gap
analyzing_task = Task(
    description = 'Analyze the research report from Task 1. Organize the requested skills into:' \
    '1. Foundation \n' \
    '2. Core Data Engineering \n' \
    '3. Big Data \n' \
    '4. Cloud \n' \
    'And for each category, organize the skills into: \n' \
    'Beginner -> Intermedia -> Junior -> Senior.',
    expected_output = 'A clear and structured Data Engineering skill roadmap.',
    agent = analyst_agent,
    context = [searching_task]
)

# Task 3: Design projects
designing_task = Task(
    description = 'Design practical Data Engineering porfolio projects using the skill analysis from Task 2. \n' \
    'Create projects for: \n' \
    'Beginner, Intermediate, Advanced. \n' \
    'For each project, include: \n' \
    'Project name, Tenologies used, Main workflow, Skills demonstrated.',
    expected_output = 'A structured project roadmap with Beginner, Intermediate, Advanced Data Engineering projects. \n' \
    'Each project should clearly show which required skills it helps demonstrate.',
    agent = architect_agent,
    context = [analyzing_task]
)

# Task 4: Roadmap
roadmap_task = Task(
    description="""
    Combine the outputs from the previous tasks to create a
    Data Engineering career roadmap.

    Organize the roadmap into learning phases with:
    - Skills to learn
    - Technologies to practice
    - A project for each phase
    - Suggested timeline

    Start with foundational skills and progress toward
    job-ready and advanced skills.
    """,

    expected_output="""
    A structured Data Engineering career roadmap containing:

    1. Learning phases
    2. Skills and technologies for each phase
    3. A practical project for each phase
    4. Suggested timeline
    5. A clear path from beginner to job-ready and advanced
    """,

    agent=plan_agent,
    context=[searching_task, analyzing_task, designing_task]
)



# Assemble a team of AI Agents
#Create the AI team for job market research
crew = Crew(
    agents = [research_agent, analyst_agent, architect_agent, plan_agent],
    tasks = [searching_task, analyzing_task, designing_task, roadmap_task],
    verbose = True,
    process = Process.sequential
)

result = crew.kickoff()



# Save final output in a readable Markdown file
with open("research_output.md", "w", encoding="utf-8") as f:
    f.write("# Data Engineering Career Roadmap\n\n")
    f.write("Generated using a CrewAI multi-agent workflow.\n\n")
    f.write("---\n\n")
    f.write(str(result))

print("Output saved to research_output.md")
