from crewai import Agent
from crewai_tools.tools import  EXASearchTool

search_tool = EXASearchTool()

class Agents():
    def __init__(self, llm_model = None):
        self.llm_model = llm_model
    def researcher(self):
        return Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments in AI and data science',
            backstory="""You work at a leading tech think tank.
            Your expertise lies in identifying emerging trends.
            You have a knack for dissecting complex data and presenting
            actionable insights.""",
            verbose=True,
            llm=self.llm_model,
            allow_delegation=False,
            tools=[
                search_tool
            ]
        )
    
    def writer(self):
        return Agent(
            role='Technical Writer',
            goal='Create a comprehensive report on AI and data science trends',
            backstory="""You are a seasoned technical writer with a passion for
            translating complex ideas into accessible content.
            You have a keen eye for detail and a knack for distilling
            information into clear, concise prose.""",
            verbose=True,
            llm=self.llm_model,
            allow_delegation=False
        )
    
    def reviewer(self):
        return Agent(
            role='Review and Editing Specialist',
            goal='Review athe report for clarity, grammatical accuracy, and consistency and refine it to ensure perfection',
            backstory="""You are a subject matter expert in AI and data science.
            Your insights are highly valued in the tech community.
            You have a critical eye and a deep understanding of the
            latest developments in the field, ensuring every piece of content is clear, engaging, 
            and grammatically perfect.""",
            verbose=True,
            llm=self.llm_model,
            tools=[
                search_tool
            ],
            allow_delegation=False
        )