# Data Engineering Career Intelligence Agent

A multi-agent AI system built with CrewAI that researches the current Data Engineering job market, identifies in-demand skills, designs portfolio projects, and generates a structured career roadmap for aspiring Data Engineers.

## Overview

Choosing what to learn for a Data Engineering career can be difficult because job requirements vary across companies and experience levels.

This project uses a team of specialized AI agents to analyze current job-market information and transform it into a practical learning roadmap.

The workflow is:

Job Market Research → Skill Gap Analysis → Project Recommendations → Career Roadmap

## Multi-Agent Architecture

The system consists of four specialized agents:

### 1. Job Market Researcher

**Role:** Data Engineering Job Market Researcher

Researches recent Data Engineering job postings and industry resources to identify:

- Programming languages
- Databases
- Technical skills
- Tools and frameworks
- Education requirements
- Frequently requested technologies

The agent uses web search and website scraping to gather information.

### 2. Skill Gap Analyst

**Role:** Data Engineering Skill Gap Analyst

Analyzes the job-market research and organizes the required skills into:

- Foundation
- Core Data Engineering
- Big Data
- Cloud

Skills are further organized by proficiency level:

- Beginner
- Intermediate
- Junior
- Senior

### 3. Project Architect

**Role:** Data Engineering Project Architect

Converts the identified skills into practical portfolio projects.

Projects are designed at three levels:

- Beginner
- Intermediate
- Advanced

Each project includes:

- Project name
- Technologies used
- Main workflow
- Skills demonstrated

### 4. Career Roadmap Planner

**Role:** Data Engineering Career Roadmap Planner

Combines the research, skill analysis, and project recommendations into a structured career roadmap.

The final roadmap includes:

- Learning phases
- Skills to learn
- Technologies to practice
- Practical projects
- Suggested timeline
- Progression toward job readiness

## Technologies

- Python
- CrewAI
- CrewAI Tools
- OpenAI GPT-4o-mini
- SerperDevTool
- ScrapeWebsiteTool
- LangChain
- Markdown

## Project Workflow

```text
                    ┌─────────────────────┐
                    │   Job Market        │
                    │     Researcher      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Skill Gap        │
                    │      Analyst        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Project           │
                    │     Architect       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Career Roadmap    │
                    │      Planner        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Engineering    │
                    │   Career Roadmap    │
                    └─────────────────────┘
