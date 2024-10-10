# Tool Calling Use Cases
# ⏳ Note (Kernel Starting): This notebook takes about 30 seconds to be ready to use. You may start and watch the video while you wait.

# import warnings
# warnings.filterwarnings('ignore')
# Get API keys
# from utils import get_tavily_api_key
# TAVILY_API_KEY = get_tavily_api_key()
# Load helper functions
# from utils import llama31
# from utils import cprint
# import json
# 💻   Access requirements.txt and utils.py files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# Define tool system prompt
# from datetime import datetime
# ​
# current_date = datetime.now()
# formatted_date = current_date.strftime("%d %B %Y")
# print(formatted_date)
# tool_system_prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
# ​
# Environment: ipython
# Tools: brave_search, wolfram_alpha
# Cutting Knowledge Date: December 2023
# Today Date: {formatted_date}
# """
# The brave_search built-in tool
# prompt = tool_system_prompt + f"""<|eot_id|><|start_header_id|>user<|end_header_id|>
# ​
# What is the current weather in Menlo Park, California?
# ​
# <|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
# response = llama31(prompt)
# print(response)
# no_tool_call_prompt = tool_system_prompt + f"""<|eot_id|><|start_header_id|>user<|end_header_id|>
# ​
# What is the population of California?
# ​
# <|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
# no_tool_call_response = llama31(no_tool_call_prompt)
# print(no_tool_call_response)
# Calling the search API
# from tavily import TavilyClient
# tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
# ​
# result = tavily_client.search("current weather in Menlo Park, California")
# cprint(result)
# Reprompting Llama with search tool response
# search_result = result["results"][0]["content"]
# print(search_result)
# prompt = tool_system_prompt + f"""<|eot_id|><|start_header_id|>user<|end_header_id|>
# What is the current weather in Menlo Park, California?
# ​
# <|eot_id|><|start_header_id|>assistant<|end_header_id|>
# ​
# <|python_tag|>{response}<|eom_id|>
# <|start_header_id|>ipython<|end_header_id|>
# ​
# {search_result}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
# """
# print(prompt)
# response = llama31(prompt)
# print(response)
# Using the higher-level message
# system_prompt_content = f"""
# Environment: ipython
# Tools: brave_search, wolfram_alpha
# Cutting Knowledge Date: December 2023
# Today Date: {formatted_date}
# """
# messages = [
#     {"role": "system", "content":  system_prompt_content},
#     {"role": "user",   "content": "What is the current weather in Menlo Park, California?"}
#   ]
# response = llama31(messages)
# print(response)
# messages = [
#     {"role": "system",     "content":  system_prompt_content},
#     {"role": "user",       "content": "What is the current weather in Menlo Park, California?"},
#     {"role": "assistant",  "content": response},
#     {"role": "ipython",    "content": search_result}
#   ]
# response = llama31(messages)
# print(response)
# The Wolfram Alpha tool
# math_problem = "Can you help me solve this equation: x^3 - 2x^2 - x + 2 = 0?"
# messages = [
#     {"role": "system",  "content": system_prompt_content},
#     {"role": "user",    "content": math_problem}
# ]
# response = llama31(messages)
# print(response)
# Calling the Wolfram Alpha tool
# from utils import wolfram_alpha
# tool_result = wolfram_alpha("solve x^3 - 2x^2 - x + 2 = 0")
# print(tool_result)
# Checking the result
# from sympy import symbols, Eq, solve
# ​
# x = symbols('x')                           # Define the variable
# equation = Eq(x**3 - 2*x**2 - 1*x + 2, 0) # Define the equation
# solution = solve(equation, x)              # Solve the equation
# ​
# print(solution)
# Reprompting Llama with Wolfram Alpha tool response
# messages = [
#     {"role": "system", "content": system_prompt_content},
#     {"role": "user",      "content": math_problem},
#     {"role": "assistant", "content": response},
#     {"role": "ipython",   "content": tool_result}
# ]
# response = llama31(messages)
# print(response)
# The code interpreter built-in tool
# loan_question = (
#     "How much is the monthly payment, total payment, "
#     "and total interest paid for a 30 year mortgage of $1M "
#     "at a fixed rate of 6% with a 20% down payment?"
# )
# messages = [
#     {"role": "system",     "content": system_prompt_content},
#     {"role": "user",       "content": loan_question},
#   ]
# response = llama31(messages)
# print(response)
# Calculate loan payments
# from utils import calculate_loan
# monthly_payment, total_payment, total_interest_paid = calculate_loan(
#     loan_amount = 1000000, 
#     annual_interest_rate = 0.06, 
#     loan_term = 30, 
#     down_payment = 200000)
# ​
# print(f"Monthly payment: ${(monthly_payment)}")
# print(f"Total payment: ${(total_payment)}")
# print(f"Total interest paid: ${(total_interest_paid)}")
# Generating the code in Java
# messages = [
#     {"role":    "system",     
#      "content": system_prompt_content + "\nGenerate the code in Java."},
#     {"role":    "user",       "content": loan_question},
#   ]
# response = llama31(messages)
# print(response)
# Reprompting Llama with Code Interpreter tool response
# code_interpreter_tool_response="""
# Monthly payment: $4796
# Total payment: $1726705
# Total interest paid: $926705
# """
# messages = [
#     {"role": "system", "content":  system_prompt_content},
#     {"role": "user",      "content": loan_question},
#     {"role": "assistant", "content": response},
#     {"role": "ipython",   "content": code_interpreter_tool_response}
#   ]
# response = llama31(messages)
# print(response)
# Llama 3.1 custom tool calling
# from utils import trending_songs, get_boiling_point
# ​
# country = "US"
# top_num = 5
# top_songs = trending_songs(country, top_num)
# print(f"Top {top_num} trending songs in {country}:")
# print(top_songs)
# 💻   Access trending_songs() in utils.py files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# Prompt Llama 3.1 for custom tool call
# user_prompt = """
# Answer the user's question by using the following functions if needed.
# If none of the functions can be used, please say so.
# Functions (in JSON format):
# {
#     "type": "function", "function": {
#         "name": "get_boiling_point",
#         "description": "Get the boiling point of a liquid",
#         "parameters": {
#             "type": "object", "properties": [
#                 {"liquid_name": {"type": "object", "description": "name of the liquid"}},
#                 {"celsius": {"type": "object", "description": "whether to use celsius"}}
#             ], "required": ["liquid_name"]
#         }
#     }
# }
# {
#     "type": "function", "function": {
#         "name": "trending_songs",
#         "description": "Returns the trending songs on a Music site",
#         "parameters": {
#             "type": "object", "properties": [
#                 {"country": {"type": "object", "description": "country to return trending songs for"}},
#                 {"n": {"type": "object", "description": "The number of songs to return"}}
#             ], "required": ["country"]
#         }
#     }
# }
# ​
# Question: Can you check the top 5 trending songs in US?
# """
# messages = [
#     {
#       "role": "system", "content":  f"""
# Environment: ipython
# Cutting Knowledge Date: December 2023
# Today Date: {formatted_date}
# """},
#     {"role": "user", "content": user_prompt}
#   ]
# result = llama31(messages,405)
# print(result)
# Calling the custom tool
# custom_tools = {"trending_songs": trending_songs,
#                 "get_boiling_point": get_boiling_point}
# res = json.loads(result)
# function_name = res['name']
# parameters = list(res['parameters'].values())
# function_name, parameters
# tool_result = custom_tools[function_name](*parameters)
# tool_result
# Reprompting Llama with custom tool call result
# messages = [
#     {
#       "role": "system", "content":  f"""
# Environment: ipython
# Cutting Knowledge Date: December 2023
# Today Date: {formatted_date}
# """},
#     {"role": "user", "content": user_prompt},
#     {"role": "assistant", "content": result},
#     {"role": "ipython", "content": ','.join(tool_result)}
#   ]
# response = llama31(messages, 70)
# print(response)