import os
import logging
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    filename='generated_code.log',  # Log to a file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

class GraphAgent:
    def __init__(self):
        self.prompt_template = """
        You are an AI that generates JSX/JavaScript code for creating charts using Shadcn components in a React application.
        The user input is: "{user_input}"
        Generate the JSX/JavaScript code using the Shadcn charts library.
        Ensure that the code is well-formatted and can be directly used in a React component.
        """
        
        # Use OpenAI as the LLM provider with the API key from the environment variable
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def handle_user_request(self, user_input: str):
        logging.info("Received user input: %s", user_input)
        
        # Prepare the prompt with the user's input
        prompt = self.prompt_template.format(user_input=user_input)
        
        # Generate the JSX/JavaScript code using OpenAI API
        logging.info("Sending request to OpenAI API...")
        generated_code = self.llm(prompt)
        
        # Log the generated code to the file and console
        logging.info("Generated code:\n%s", generated_code)
        
        # Return the generated JSX/JavaScript code
        return generated_code
