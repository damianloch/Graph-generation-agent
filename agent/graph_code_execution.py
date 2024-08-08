import multiprocessing

def execute_target(code: str, result):
    try:
        # Define a local context to capture the output
        local_context = {}
        exec(code, {}, local_context)
        result['output'] = local_context.get('output', "<p>No output generated</p>")
    except Exception as e:
        result['error'] = str(e)

def execute_graph_code_safe(code: str) -> str:
    manager = multiprocessing.Manager()
    result = manager.dict()
    process = multiprocessing.Process(target=execute_target, args=(code, result,))
    
    process.start()
    process.join(timeout=10)  # Timeout after 10 seconds
    
    if process.is_alive():
        process.terminate()
        raise TimeoutError("Code execution timed out.")

    if 'error' in result:
        raise RuntimeError(result['error'])

    return result.get('output', "<p>No output generated</p>")
