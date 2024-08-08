import plotly.graph_objects as go

def generate_graph_code(data):
    fig = go.Figure(data=[go.Bar(x=data['x'], y=data['y'])])
    graph_html = fig.to_html(full_html=False)
    return graph_html
