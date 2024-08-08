from .data_retrieval import retrieve_data
from .graph_generation import generate_graph_code

class GraphAgent:
    def handle_user_request(self, user_input: str):
        data = retrieve_data(user_input)
        graph_code = generate_graph_code(data)
        return graph_code
