from dotenv import load_dotenv
from crewai import Crew
from tasks import Tasks
from agents import Agents
from langchain_openai import AzureChatOpenAI

import os
def main():
    load_dotenv()
    
    print("## Welcome to the AI Research Crew")
    print('-------------------------------')
    topic = input("What AI topic are you interesting in today?\n")

    llm = None
    if os.environ.get("USE_AZURE"):
        llm = AzureChatOpenAI(
            azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
        )


    tasks = Tasks()
    agents = Agents(llm)
    
    # create agents
    research_agent = agents.researcher()
    writer_agent = agents.writer()
    reviewer_agent = agents.reviewer()

    
    # create tasks
    research_task = tasks.research_task(research_agent, topic)
    writing_task = tasks.writing_task(writer_agent, topic)
    reviewing_task = tasks.reviewing_task(reviewer_agent, topic)
    
    
    crew = Crew(
      agents=[
        research_agent,
        writer_agent,
        reviewer_agent,
      ],
      tasks=[
        research_task,
        writing_task,
        reviewing_task,
      ]
    )
    
    result = crew.kickoff()
    
    print(result)
    
if __name__ == "__main__":
    main()