from textwrap import dedent
from crewai import Task

class Tasks():
  def research_task(self, agent, topic):
    return Task(
      description=dedent(f"""\
        Conduct a comprehensive analysis of the latest advancements in AI in 2024 related to the topic
                  the topic described below.
                  Identify key trends, breakthrough technologies, and potential industry impacts.
                  Your final answer MUST be a full analysis report.
                                  
                  Topic: {topic}"""),
      expected_output="Full analysis report about the latest advancements in AI in 2024",
      agent=agent,
    )
    
  def writing_task(self, agent, topic):
    return Task(
			description=dedent(f"""\
          "Using the insights provided, develop an engaging report
                  that highlights the most significant AI advancements related to the topic described below.
                  Your report should be informative yet accessible, catering to a tech-savvy audience.
                  Make it sound cool, avoid complex words so it doesn't sound like AI.
                        
                  Topic: {topic}"""),
      expected_output="Fullreport of at least 4 sections about the latest advancements in AI in 2024",
      agent=agent
    )
    
  def reviewing_task(self, agent, topic):
    return Task(
			description=dedent(f"""\
          Review the draft report for the topic defined below. Check for clarity, engagement, grammatical accuracy,
                  Edit and refine the content, ensuring it doesn't sound like AI.

                  Topic: {topic}"""),
      expected_output="A polished, error-free report that is engaging, clear, and free of grammatical.",
      output_file=f'outputs/{topic}.md',
      agent=agent
    )
      