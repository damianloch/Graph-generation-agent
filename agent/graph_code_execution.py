import plotly.graph_objects as go
import base64
import io

def execute_graph_code(generated_code: str):
    # Define a safe execution environment
    local_env = {}
    
    # Execute the generated Python code in this environment
    try:
        exec(generated_code, {"go": go}, local_env)
        
        # Assuming the code generates a Plotly figure and stores it in 'fig'
        fig = local_env.get("fig")
        if fig is None:
            raise ValueError("Generated code did not create a figure named 'fig'")
        
        # Convert the figure to HTML
        graph_html = fig.to_html(full_html=False)
        return graph_html
    
    except Exception as e:
        return f"<p>Error executing graph code: {str(e)}</p>"
