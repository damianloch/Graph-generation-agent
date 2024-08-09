import os
import logging
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from .graph_code_execution import execute_graph_code_safe

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
        You are an AI that generates Python code to create a graph based on the user's input. The user input is: "{user_input}" 
        Generate Python code using Plotly to create the graph. Ensure that the code does not attempt to load any resources from 
        local file paths (e.g., file://). All resources should be loaded via URLs using http:// or https://.

        Ensure that the code does not include any infinite loops or long-running operations.
        """
        
        # Use OpenAI as the LLM provider with the API key from the environment variable
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def handle_user_request(self, user_input: str):
        logging.info("Received user input: %s", user_input)
        
        # Prepare the prompt with the user's input
        prompt = self.prompt_template.format(user_input=user_input)
        
        # Generate the Python code using OpenAI API
        logging.info("Sending request to OpenAI API...")
        generated_code = self.llm(prompt)
        logging.info("Generated code:\n%s", generated_code)
        
        # Execute the generated code to produce the graph
        logging.info("Executing generated code...")
        try:
            graph_html = execute_graph_code_safe(generated_code)
            logging.info("Generated graph HTML: %s", graph_html)
            return graph_html
        except Exception as e:
            logging.error("Error during code execution: %s", str(e))
            return f"<p>Error executing graph code: {str(e)}</p>"
