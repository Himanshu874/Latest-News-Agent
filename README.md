# AI News Summarizer & Analyzer Agent

A multi-agent system that fetches the latest AI news using real web search, analyzes and selects the top 5 stories, and generates catchy summaries using OpenAI's Agent SDK and GPT-4o.

## Features

- 🔍 **Real Web Search** - Uses DuckDuckGo to fetch latest AI news (no API key needed)
- 🤖 **Multi-Agent Architecture** - Specialized agents for search, analysis, and writing
- 🎯 Intelligently selects top 5 most impactful stories
- ✨ Generates catchy, engaging summaries
- 🛠️ Built with OpenAI Agent SDK and GPT-4o
- 🌐 Live internet access for current news

## Multi-Agent Architecture

### 1. Search Agent
- Searches the web for latest AI news
- Uses DuckDuckGo search (no API key required)
- Gathers comprehensive results from multiple queries

### 2. Analyst Agent
- Analyzes all found articles
- Evaluates based on relevance, impact, recency, and credibility
- Selects TOP 5 most important stories

### 3. Writer Agent
- Creates catchy, engaging summaries
- Writes in punchy, shareable style
- Explains why each story matters

## Tech Stack

- **Python 3.8+**
- **OpenAI Agent SDK** (Beta Assistants API)
- **GPT-4o** model
- **DuckDuckGo Search** - Real web search without API keys

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

3. Run the agent:
```bash
python ai_news_agent.py
```

## How It Works

### Phase 1: Web Search
- Search Agent queries DuckDuckGo for latest AI news
- Gathers 15+ recent articles from various sources
- Returns comprehensive results to orchestrator

### Phase 2: Analysis & Selection
- Analyst Agent evaluates all articles
- Ranks based on impact, relevance, and recency
- Selects TOP 5 most important stories

### Phase 3: Summary Generation
- Writer Agent creates catchy summaries
- Formats with emojis and engaging headlines
- Explains why each story matters

### Phase 4: Output
- Displays formatted news summaries
- Includes sources and links
- Ready to share!

## Customization

### Use Different Search Engines

Replace DuckDuckGo with other providers:
- **Google Custom Search API**
- **Bing News Search API**
- **NewsAPI.org**
- **Serper API**

### Modify Agent Behavior

Edit the `instructions` parameter in each agent class to change behavior:
- Search Agent: Change search strategies
- Analyst Agent: Adjust selection criteria
- Writer Agent: Modify writing style

### Change Model

Replace `"gpt-4o"` with other models like `"gpt-4-turbo"` or `"gpt-4o-mini"` based on your needs and budget.

## Example Output

```
📰 AI NEWS SUMMARY & ANALYSIS
================================================================================
Generated on: 2025-10-23 10:30:00

🚀 TOP 5 AI NEWS STORIES

1. 🧠 OpenAI Announces GPT-5 with Revolutionary Reasoning Capabilities
   The AI race heats up! OpenAI's GPT-5 brings unprecedented reasoning...

[Additional summaries...]
```

## License

MIT
