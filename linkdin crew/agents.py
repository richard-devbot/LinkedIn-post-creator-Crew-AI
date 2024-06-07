import os
from textwrap import dedent
import streamlit as st
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import scrape_linkedin_posts_tool

load_dotenv()


Groq_llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192")

# gemini_llm = ChatGoogleGenerativeAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     model="gemini-pro")


gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0,
    google_api_key="AIzaSyAU97ZxASlUERhrK3MJ2IlIEYLL5lzxm4Y",
)


def streamlit_callback(step_output):
    # This function will be called after each step of the agent's execution
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)

scrape_website_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()

def create_agents(topic):
    
    linkedin_scraper = Agent(
        role="LinkedIn Post Scraper",
        goal="""Your goal is to efficiently and effectively scrape a LinkedIn profile to get a comprehensive 
                list of posts from the given profile, ensuring the highest level of accuracy and completeness.""",
        tools=[scrape_linkedin_posts_tool],
        backstory=dedent(
            """
            You are a highly skilled and experienced programmer, renowned for your exceptional web scraping abilities.
            You have a proven track record of successfully scraping various websites, including LinkedIn, 
            with unparalleled precision and speed. 
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=Groq_llm,
        step_callback=streamlit_callback,
    )

    web_researcher = Agent(
        role="Web Researcher",
        goal="""Your goal is to search for the most relevant and high-quality content about the user-requested topic: {topic},
                ensuring the results are comprehensive, accurate, and up-to-date.""",
        tools=[scrape_website_tool, search_tool],
        backstory=dedent(
            """
            You are a proficient and meticulous web researcher, known for your ability to find the most valuable 
            and informative content on any given topic. Your expertise lies in your ability to sift through vast 
            amounts of data and select only the most relevant and high-quality sources.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    writer = Agent(
        role="LinkedIn Post Creator",
        goal="""You will create a LinkedIn post about the user-requested topic:{topic}, 
                observed in the LinkedIn posts scraped by the LinkedIn Post Scraper, ensuring the post is engaging, 
                informative, and accurately reflects the style and tone of the original posts.""",
        backstory=dedent(
            """
            You are a highly skilled and creative writer, specializing in crafting LinkedIn posts that replicate 
            the style and tone of any influencer. Your ability to capture the essence of an influencer's voice 
            and translate it into engaging and informative posts has earned you a reputation as a master of your craft.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=Groq_llm,
        step_callback=streamlit_callback,
    )
    
    return linkedin_scraper, web_researcher, writer
    
