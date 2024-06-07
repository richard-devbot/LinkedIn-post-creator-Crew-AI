# LinkedIn-post-creator-Crew-AI

Project Overview
This project is a Streamlit application that utilizes various AI models and tools to scrape LinkedIn posts, research topics, and generate engaging LinkedIn posts. The application is designed to be user-friendly and provides a comprehensive interface for users to interact with the AI agents.

Components
AI Models
Groq_llm: A Langchain Groq model used for natural language processing tasks.
Gemini_llm: A Langchain Google Generative AI model used for natural language processing tasks.
Tools
ScrapeWebsiteTool: A tool used for scraping websites.
SerperDevTool: A tool used for searching and researching topics.
ScrapeLinkedInPostsTool: A tool used for scraping LinkedIn posts.
Agents
LinkedIn Post Scraper: An agent responsible for scraping LinkedIn posts.
Web Researcher: An agent responsible for researching topics and providing relevant information.
LinkedIn Post Creator: An agent responsible for generating engaging LinkedIn posts based on the scraped posts and researched topics.
Functionality
Streamlit Interface
The application provides a Streamlit interface that allows users to interact with the AI agents. The interface includes:

A topic input field for users to enter the topic they want to research.
A button to trigger the AI agents to start working on the topic.
A display area to show the progress and output of the AI agents.
AI Agent Workflow
The AI agents work together to achieve the following workflow:

The LinkedIn Post Scraper agent scrapes LinkedIn posts related to the user-input topic.
The Web Researcher agent researches the topic and provides relevant information.
The LinkedIn Post Creator agent generates an engaging LinkedIn post based on the scraped posts and researched information.
Setup and Configuration
Environment Variables
The application requires the following environment variables to be set:

GROQ_API_KEY: The API key for the Groq model.
GEMINI_API_KEY: The API key for the Gemini model.
Installation
To install the required dependencies, run the following command:

Copy code
pip install -r requirements.txt
Running the Application
To run the application, execute the following command:

Copy code
streamlit run app.py
License
This project is licensed under the MIT License. See LICENSE for details.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

Acknowledgments
This project utilizes the following open-source libraries and tools:

Langchain
Streamlit
CrewAI
dotenv
We acknowledge the contributions of the developers and maintainers of these projects.
