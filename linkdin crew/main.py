from crewai import Crew
from dotenv import load_dotenv
from agents import create_agents
import streamlit as st
from tasks import create_tasks

load_dotenv()

def main():
    st.set_page_config(
        page_title="LinkedIn Post Creator",
        page_icon="dd.jpg",  # Replace with the path to your image
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items=None
    )

    st.subheader("🏖️ Craft Your Captivating LinkedIn Post: Turn Your Thoughts into LinkedIn Gold: The AI-Agents Post Creator 🏆",
                 divider="rainbow", anchor=False)

    st.title("Let's Talk LinkedIn: Craft Compelling Posts with the Power of AI-Agents 🗣️")
    st.image("dd.jpg", width=None)

    topic = st.text_input("Enter the topic for your LinkedIn post:")

    if st.button("Create Post"):
        # Create the agents and tasks
        linkedin_scraper, web_researcher, writer = create_agents(topic)
        scrape_linkedin_task, web_research_task, create_linkedin_post_task = create_tasks(topic=topic)

        # Create a Crew and run the tasks
        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
            with st.container(height=500, border=False):
                crew = Crew(
                    agents=[linkedin_scraper, web_researcher, writer],
                    tasks=[scrape_linkedin_task, web_research_task, create_linkedin_post_task],
                    # topic=topic
                )
                result = crew.kickoff()
            status.update(label="✅ Post Created!",
                          state="complete", expanded=False)

        st.subheader("Here is your LinkedIn Post", anchor=False, divider="rainbow")
        st.markdown(result)

if __name__ == "__main__":
    main()