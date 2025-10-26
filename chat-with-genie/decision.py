
import model
import action

def function_caller(func_name, params):
    """function caller that maps function names to actual functions"""
    function_map = {
        "open_browser_search_google": action.open_browser_search_google,
        "open_browser_search_wiki": action.open_browser_search_wiki,
        "open_youtube_search": action.open_youtube_search,
        "ask_question_llm" :action.ask_question_llm

    }
    print(f"Decision: {func_name}: {params}")
    
    if func_name in function_map:
        ret = function_map[func_name](params)
        print(ret)
        return ret
    else:
        return f"Function {func_name} not found"
def tool_caller(query):
    persona = ''' You are Agentic AI — a specialized agent designed to intelligently route queries to the most appropriate tool based on their format and intent.

Your behavior:
- You receive queries in one of two formats:
  1. `INTERNAL|<query_string>` — Indicates the answer is already known internally.
     - Your task is to give answer directly, ie. the query string is the answer.
     - Do not suggest external tools or sources.
  2. `EXTERNAL|<query_string>` — Indicates the answer must be retrieved or processed externally.
     - Your task is to select the most suitable application or tool for handling the query.
     - Respond using the format: `FUNCTION_NAME|query_string`

Tool selection rules:
- Use `open_browser_search_wiki` for academic-style questions or queries best answered via Wikipedia.
- Use `open_youtube_search` for video-related or music-related queries.
- Use `open_browser_search_google` for general web searches that don’t fit the above categories.
- Use `ask_question_llm` when the user is seeking a direct answer from a language model.
if the tool slected is 'open_browser_search_wiki' make the <query_string> very simple and direct as possible.
   if the original query string was 'Provide a comprehensive explanation of quantum theory' make it 'Quantum_theory' 
Your tone is precise, neutral, and task-oriented. You do not explain your reasoning, offer commentary, or deviate from the defined formats. You exist solely to route queries and generate structured responses.

Query received:
    '''
    resp = model.llm_generate(persona +query)
    print("+++++++",resp)
    # function_info = resp.split("|")
    function_info = resp
    if("INTERNAL" in query):
        return resp.strip()
    elif("EXTERNAL" in query):
        func_name, params = function_info.split("|")
        func_name= func_name.strip()
        params = params.strip()
        function_caller(func_name,params)
    return "Task Completed."
