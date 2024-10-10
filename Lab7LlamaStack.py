# Lab 7: Llama Stack
# ⏳ Note (Kernel Starting): This notebook takes about 30 seconds to be ready to use. You may start and watch the video while you wait.

# import warnings
# warnings.filterwarnings('ignore')
# from dotenv import load_dotenv
# import os
# _ = load_dotenv() #loads 'TOGETHER_API_KEY'
# #!pip install llama-stack==0.0.36 llama-stack-client==0.0.35
# 💻   Access requirements.txt and utils.py files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# !llama stack build --list-templates
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | Template Name               | Providers                           | Description                                                                      |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | local-bedrock-conda-example | {                                   | Use Amazon Bedrock APIs.                                                         |
# |                             |   "inference": "remote::bedrock",   |                                                                                  |
# |                             |   "memory": "meta-reference",       |                                                                                  |
# |                             |   "safety": "meta-reference",       |                                                                                  |
# |                             |   "agents": "meta-reference",       |                                                                                  |
# |                             |   "telemetry": "meta-reference"     |                                                                                  |
# |                             | }                                   |                                                                                  |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | local                       | {                                   | Use code from `llama_stack` itself to serve all llama stack APIs                 |
# |                             |   "inference": "meta-reference",    |                                                                                  |
# |                             |   "memory": "meta-reference",       |                                                                                  |
# |                             |   "safety": "meta-reference",       |                                                                                  |
# |                             |   "agents": "meta-reference",       |                                                                                  |
# |                             |   "telemetry": "meta-reference"     |                                                                                  |
# |                             | }                                   |                                                                                  |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | local-fireworks             | {                                   | Use Fireworks.ai for running LLM inference                                       |
# |                             |   "inference": "remote::fireworks", |                                                                                  |
# |                             |   "memory": "meta-reference",       |                                                                                  |
# |                             |   "safety": "meta-reference",       |                                                                                  |
# |                             |   "agents": "meta-reference",       |                                                                                  |
# |                             |   "telemetry": "meta-reference"     |                                                                                  |
# |                             | }                                   |                                                                                  |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | local-ollama                | {                                   | Like local, but use ollama for running LLM inference                             |
# |                             |   "inference": "remote::ollama",    |                                                                                  |
# |                             |   "memory": "meta-reference",       |                                                                                  |
# |                             |   "safety": "meta-reference",       |                                                                                  |
# |                             |   "agents": "meta-reference",       |                                                                                  |
# |                             |   "telemetry": "meta-reference"     |                                                                                  |
# |                             | }                                   |                                                                                  |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | local-tgi                   | {                                   | Use TGI (local or with Hugging Face Inference Endpoints for running LLM          |
# |                             |   "inference": "remote::tgi",       | inference. When using HF Inference Endpoints, you must provide the name of the   |
# |                             |   "memory": "meta-reference",       | endpoint).                                                                       |
# |                             |   "safety": "meta-reference",       |                                                                                  |
# |                             |   "agents": "meta-reference",       |                                                                                  |
# |                             |   "telemetry": "meta-reference"     |                                                                                  |
# |                             | }                                   |                                                                                  |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# | local-together              | {                                   | Use Together.ai for running LLM inference                                        |
# |                             |   "inference": "remote::together",  |                                                                                  |
# |                             |   "memory": "meta-reference",       |                                                                                  |
# |                             |   "safety": "remote::together",     |                                                                                  |
# |                             |   "agents": "meta-reference",       |                                                                                  |
# |                             |   "telemetry": "meta-reference"     |                                                                                  |
# |                             | }                                   |                                                                                  |
# +-----------------------------+-------------------------------------+----------------------------------------------------------------------------------+
# !llama stack list-apis
# +--------------+
# | API          |
# +--------------+
# | inference    |
# +--------------+
# | safety       |
# +--------------+
# | agents       |
# +--------------+
# | memory       |
# +--------------+
# | telemetry    |
# +--------------+
# | models       |
# +--------------+
# | shields      |
# +--------------+
# | memory_banks |
# +--------------+
# Llama Stack Inference
# LLAMA_STACK_API_TOGETHER_URL="https://llama-stack.together.ai"
# LLAMA31_8B_INSTRUCT = "Llama3.1-8B-Instruct"
# ​
# from llama_stack_client import LlamaStackClient
# from llama_stack_client.lib.inference.event_logger import EventLogger
# from llama_stack_client.types import UserMessage
# ​
# async def run_main():
#     client = LlamaStackClient(
#         base_url=LLAMA_STACK_API_TOGETHER_URL,
#     )
# ​
#     iterator = client.inference.chat_completion(
#         messages=[
#             UserMessage(
#                 content="Who wrote the book Innovator's Dilemma? How about Charlotte's Web?",
#                 role="user",
#             ),
# ​
#             UserMessage(
#                 content="which book was published first?",
#                 role="user",
#             ),
#         ],
#         model=LLAMA31_8B_INSTRUCT,
#         stream=True
#     )
# ​
#     async for log in EventLogger().log(iterator):
#         log.print()
#         #print("?")
# ​
# await run_main()
# Assistant> "Charlotte's Web" was written by E.B. White and published in 1952. 

# "The Innovator's Dilemma" was written by Clayton M. Christensen and published in 1997.
# Llama Stack Agent
# import asyncio
# from typing import List, Optional, Dict
# ​
# from llama_stack_client import LlamaStackClient
# from llama_stack_client.lib.agents.event_logger import EventLogger
# ​
# from llama_stack_client.types import SamplingParams, UserMessage
# from llama_stack_client.types.agent_create_params import AgentConfig
# ​
# class Agent:
#     def __init__(self):
#         self.client = LlamaStackClient(
#             base_url=LLAMA_STACK_API_TOGETHER_URL,
#         )
# ​
#     def create_agent(self, agent_config: AgentConfig):
#         agent = self.client.agents.create(
#             agent_config=agent_config,
#         )
#         self.agent_id = agent.agent_id
#         session = self.client.agents.sessions.create(
#             agent_id=agent.agent_id,
#             session_name="example_session",
#         )
#         self.session_id = session.session_id
# ​
#     async def execute_turn(self, content: str):
#         response = self.client.agents.turns.create(
#             agent_id=self.agent_id,
#             session_id=self.session_id,
#             messages=[
#                 UserMessage(content=content, role="user"),
#             ],
#             stream=True,
#         )
# ​
#         for chunk in response:
#             if chunk.event.payload.event_type != "turn_complete":
#                 yield chunk
# ​
# ​
# async def run_main():
#     agent_config = AgentConfig(
#         model=LLAMA31_8B_INSTRUCT,
#         instructions="You are a helpful assistant",
#         enable_session_persistence=False,
#     )
# ​
#     agent = Agent()
#     agent.create_agent(agent_config)
# ​
#     prompts = [
#         "Who wrote the book Charlotte's Web?",
#         "Three best quotes?",
#     ]
# ​
#     for prompt in prompts:
#         print(f"User> {prompt}")
#         response = agent.execute_turn(content=prompt)
#         async for log in EventLogger().log(response):
#             if log is not None:
#                 log.print()
# ​
# await run_main()
# User> Who wrote the book Charlotte's Web?
# inference> The author of the book 'Charlotte's Web' is E.B. White. The novel was first published in 1952.
# User> Three best quotes?
# inference> Here are three notable quotes from 'Charlotte's Web':

# 1. "Alone, alone, alone. What a thing it is to be alone." 

# However,  Another famous one is: 
# 2. "Where's the harm in putting the words together a little funny?"

# But the most famous one may be: 
# 3. "Some people are worth melting for."
# Llama Stack with Llama 3.2 vision model
# from PIL import Image
# import matplotlib.pyplot as plt
# ​
# def display_image(path):
#   img = Image.open(path)
#   plt.imshow(img)
#   plt.axis('off')
#   plt.show()
# ​
# display_image("./content/Llama_Repo.jpeg")

# import base64
# ​
# from llama_stack_client import LlamaStackClient
# from llama_stack_client.types import agent_create_params
# ​
# LLAMA32_11B_INSTRUCT = "Llama3.2-11B-Vision-Instruct"
# ​
# def encode_image(image_path):
#   with open(image_path, "rb") as img:
#     return base64.b64encode(img.read()).decode('utf-8')
# ​
# class Agent:
#     def __init__(self):
#         self.client = LlamaStackClient(
#             base_url=LLAMA_STACK_API_TOGETHER_URL,
#         )
# ​
#     def create_agent(self, agent_config: AgentConfig):
#         agent = self.client.agents.create(
#             agent_config=agent_config,
#         )
#         self.agent_id = agent.agent_id
#         session = self.client.agents.sessions.create(
#             agent_id=agent.agent_id,
#             session_name="example_session",
#         )
#         self.session_id = session.session_id
# ​
#     async def execute_turn(self, prompt: str, image_path: str):
#         base64_image = encode_image(image_path)
# ​
#         messages = [{
#             "role": "user",
#             "content": [
#               {
#                 "image": {
#                   "uri": f"data:image/jpeg;base64,{base64_image}"
#                 }
#               },
#               prompt,
#             ]
#         }]
# ​
#         response = self.client.agents.turns.create(
#             agent_id=self.agent_id,
#             session_id=self.session_id,
#             messages = messages,
#             stream=True,
#         )
# ​
#         for chunk in response:
#             if chunk.event.payload.event_type != "turn_complete":
#                 yield chunk
# async def run_main(image_path, prompt):
#     agent_config = AgentConfig(
#         model=LLAMA32_11B_INSTRUCT,
#         instructions="You are a helpful assistant",
#         enable_session_persistence=False,
#     )
# ​
#     agent = Agent()
#     agent.create_agent(agent_config)
# ​
#     print(f"User> {prompt}")
#     response = agent.execute_turn(prompt=prompt, image_path=image_path)
#     async for log in EventLogger().log(response):
#         if log is not None:
#             log.print()
# ​
# ​
# await run_main("./content/Llama_Repo.jpeg",
#          "How many different colors are those llamas?\
#          What are those colors?")
# User> How many different colors are those llamas?         What are those colors?
# inference> 
