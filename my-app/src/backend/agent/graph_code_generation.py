import plotly.graph_objects as go
import base64
import io

def generate_graph_code(data):
    # Example code to generate a bar graph using Plotly
    fig = go.Figure(data=[go.Bar(x=data['x'], y=data['y'])])
    
    # Convert the Plotly graph to HTML
    graph_html = fig.to_html(full_html=False)
    
    return graph_html
