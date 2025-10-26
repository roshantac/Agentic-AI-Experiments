import subprocess
import model
# basic import 
# from mcp.server.fastmcp import FastMCP, Image
# from mcp.server.fastmcp.prompts import base
# from mcp.types import TextContent
# from mcp import types

# mcp = FastMCP("Calculator")

# @mcp.tool()
def open_browser_search_google(query: str) -> None:
    query = query.replace(" ", "+")
    # Run the AppleScript using osascript
    apple_script = f'''
tell application "Safari"
    activate
    open location "https://www.google.com/search?q={query}"
end tell
'''
    process = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
    print(f'AppleScript output:\n{process.stdout}')
    print(f'AppleScript error:\n{process.stderr}')

# @mcp.tool()
def open_browser_search_wiki(query: str) -> None:
    query = query.replace(" ", "_")
    # Run the AppleScript using osascript
    apple_script = f'''
tell application "Safari"
    activate
    open location "https://en.wikipedia.org/wiki/{query}"
end tell
'''
    process = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
    print(f'AppleScript output:\n{process.stdout}')
    print(f'AppleScript error:\n{process.stderr}')

# @mcp.tool()
def open_youtube_search(query: str) -> None:
    query = query.replace(" ", "+")
    # Run the AppleScript using osascript
    apple_script = f'''
tell application "Safari"
    activate
    open location "https://www.youtube.com/results?search_query={query}"
end tell
'''
    process = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
    print(f'AppleScript output:\n{process.stdout}')
    print(f'AppleScript error:\n{process.stderr}')

# @mcp.tool()
def ask_question_llm(query:str)->str:
    return model.llm_generate(query)
# open_browser_search_google("hello")
