from crewai import Task
from textwrap import dedent
from agents import create_agents

def create_tasks(topic):
    linkedin_scraper, web_researcher, writer = create_agents(topic)

    scrape_linkedin_task = Task(
        description=dedent(
            """Scrape a LinkedIn profile to get a comprehensive list of relevant posts, 
            ensuring the highest level of accuracy and completeness."""
        ),
        expected_output=dedent(
            """A comprehensive list of LinkedIn posts obtained from the LinkedIn profile, with each post containing all relevant 
            information, such as the post's content, date, and engagement metrics."""
        ),
        agent=linkedin_scraper,
    )

    web_research_task = Task(
        description=dedent(
            """Get the most relevant and high-quality web information about the user-requested 
            topic:{topic}, ensuring the results are comprehensive, accurate, and up-to-date."""
        ),
        expected_output=dedent(
            """A well-organized and informative summary of the most relevant and high-quality web information about the user-requested topic:{topic},
              including articles, blog posts, and other relevant sources."""
        ),
        agent=web_researcher,
    )

    create_linkedin_post_task = Task(
        description=dedent(
            """Create a high-quality and engaging LinkedIn post about the user-requested topic:{topic}, 
            observed in the LinkedIn posts scraped by the LinkedIn Post Scraper, 
            ensuring the post is engaging, informative, and accurately reflects the style 
            and tone of the original posts."""
        ),
        expected_output=dedent(
            """A high-quality and engaging LinkedIn post about the user-requested topic:{topic}, written in the style and tone of the 
            original LinkedIn posts, and containing accurate and informative content."""
        ),
        agent=writer,
    )

    create_linkedin_post_task.context = [scrape_linkedin_task, web_research_task]

    return scrape_linkedin_task, web_research_task, create_linkedin_post_task