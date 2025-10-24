import os
import json
import time
from datetime import datetime
from typing import List, Dict
from openai import OpenAI
from dotenv import load_dotenv
from duckduckgo_search import DDGS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def web_search(query: str, max_results: int = 20) -> List[Dict]:
    """
    Real web search using DuckDuckGo
    """
    print(f"Searching web for: '{query}'...")
    
    try:
        with DDGS() as ddgs:
            results = []
            for result in ddgs.news(query, max_results=max_results):
                results.append({
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "snippet": result.get("body", ""),
                    "source": result.get("source", "Unknown"),
                    "date": result.get("date", "")
                })
            
            print(f"Found {len(results)} articles\n")
            return results
    except Exception as e:
        print(f"Search error: {e}")
        return []


def search_and_summarize_september_news():
    """
    Search for September 2025 news and create summaries
    """
    print("=" * 80)
    print("SEARCHING: Latest News and Updates in September 2025")
    print("=" * 80 + "\n")
    
    
    search_query = "latest news and update in September 2025"
    articles = web_search(search_query, max_results=20)
    
    if not articles:
        print("No articles found for this search.")
        return
    
    print(f"Found {len(articles)} articles. Analyzing...\n")
    
    
    assistant = client.beta.assistants.create(
        name="September 2025 News Analyzer",
        instructions="""You are an expert news analyst. Your task is to:
        1. Analyze the provided news articles about September 2025
        2. Select the TOP 5 most interesting and impactful stories
        3. Create catchy, engaging summaries for each story
        
        Format each summary as:
        [Number]. [Emoji] [Catchy Headline]
        [2-3 sentence engaging summary]
         Why it matters: [1 sentence]
         Date: [date]
         Source: [source] - [url]
        
        Make it exciting and informative!""",
        model="gpt-4o"
    )

    thread = client.beta.threads.create()
    
    articles_text = json.dumps(articles, indent=2)
    

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"""Analyze these news articles about September 2025 and create summaries for the TOP 5 most interesting stories:

{articles_text}

Focus on the most impactful, interesting, and relevant news."""
    )
    
    
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    print("AI analyzing and creating summaries...\n")
    

    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        
        if run_status.status == "completed":
            break
        elif run_status.status == "failed":
            print(f"Analysis failed: {run_status.last_error}")
            return
        
        time.sleep(1)
    
    
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    
    print("=" * 80)
    print("TOP 5 NEWS STORIES - SEPTEMBER 2025")
    print("=" * 80)
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for msg in messages.data:
        if msg.role == "assistant":
            for content in msg.content:
                if content.type == "text":
                    print(content.text.value)
    
    print("\n" + "=" * 80)
    
    
    client.beta.assistants.delete(assistant.id)
    print("\nSearch and analysis complete!")


if __name__ == "__main__":
    search_and_summarize_september_news()
