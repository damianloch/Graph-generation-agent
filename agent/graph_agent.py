from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .graph_code_execution import execute_graph_code

class GraphAgent:
    def __init__(self):
        self.prompt_template = """
        You are an AI that generates Python code to create a graph based on the user's input.
        The user input is: "{user_input}"
        Generate Python code using Plotly to create the graph.
        """
        
        # Load the tokenizer and model from Hugging Face (GPT-Neo)
        self.tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
        self.model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")
        
        # Set up the pipeline for text generation
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def handle_user_request(self, user_input: str):
        prompt = self.prompt_template.format(user_input=user_input)
        
        # Generate the Python code using the pipeline
        generated_code = self.pipeline(prompt, max_length=150)[0]['generated_text']
        
        # Execute the generated code to produce the graph
        graph_html = execute_graph_code(generated_code)
        return graph_html
