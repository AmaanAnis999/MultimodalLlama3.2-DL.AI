# Multimodal Use Case
# ⏳ Note (Kernel Starting): This notebook takes about 30 seconds to be ready to use. You may start and watch the video while you wait.

# import warnings
# warnings.filterwarnings('ignore')
# from utils import load_env
# load_env()
# Load helper functions
# from utils import llama32
# 💻   Access requirements.txt and utils.py files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# import base64
# ​
# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')
# def llama32pi(prompt, image_url, model_size=90):
#   messages = [
#     {
#       "role": "user",
#       "content": [
#         {"type": "text",
#           "text": prompt},
#         {"type": "image_url",
#           "image_url": {
#             "url": image_url}
#         }
#       ]
#     },
#   ]
# ​
#   result = llama32(messages, model_size)
#   return result
# OCR with receipts
# from utils import disp_image
# for i in range(1, 4):
#   disp_image(f"images/receipt-{i}.jpg")
# question = "What's the total charge in the receipt?"
# results = ""
# for i in range(1, 4):
#     base64_image = encode_image(f"images/receipt-{i}.jpg")
#     res = llama32pi(question, f"data:image/jpeg;base64,{base64_image}")
#     results = results + f"{res}\n"
# print(results)
# messages = [
#     {"role": "user",
#      "content": f"""What's the total charge of all the recipts below?
# {results}"""
#   }
# ]
# response = llama32(messages)
# print(response)
# Handling multiple images
# from utils import merge_images
# import matplotlib.pyplot as plt
# merged_image = merge_images("images/receipt-1.jpg",
#                             "images/receipt-2.jpg",
#                             "images/receipt-3.jpg")
# plt.imshow(merged_image)
# plt.axis('off')
# plt.show()
# from utils import resize_image
# resized_img = resize_image(merged_image)
# base64_image = encode_image("images/resized_image.jpg")
# question = "What's the total charge of all the recipts below?"
# result = llama32pi(question,
#                       f"data:image/jpeg;base64,{base64_image}")
# print(result)
# Choosing the right drink
# disp_image("images/drinks.png")
# question = "I am on a diet. Which drink should I drink?"
# base64_image = encode_image("images/drinks.png")
# result = llama32pi(question, f"data:image/png;base64,{base64_image}")
# print(result)
# question = ("Generete nurtrition facts of the two drinks " 
#             "in JSON format for easy comparison.")
# result = llama32pi(question, f"data:image/png;base64,{base64_image}")
# print(result)
# Understanding Llama MM model with code implementation
# disp_image("images/llama32mm.png")
# question = ("I see this diagram in the Llama 3 paper. "
#             "Summarize the flow in text and then return a "
#             "python script that implements the flow.")
# base64_image = encode_image("images/llama32mm.png")
# result = llama32pi(question, f"data:image/png;base64,{base64_image}")
# print(result)
# Llama 3.1 70B Instruct model speed
# disp_image("images/llama31speed.png")
# question = "Convert the chart to an HTML table."
# base64_image = encode_image("images/llama31speed.png")
# result = llama32pi(question, f"data:image/png;base64,{base64_image}")
# print(result)
# from IPython.display import HTML
# minified_html_table = "<table><thead><tr><th>Model</th><th>Output Tokens per Second</th></tr></thead><tbody><tr><td>Llama 2 1.5B</td><td>217</td></tr><tr><td>Google's PaLM 2 540B</td><td>214</td></tr><tr><td>Google's PaLM 2 540B</td><td>163</td></tr><tr><td>Meta's LLaMA 2 70B</td><td>133</td></tr><tr><td>Meta's LLaMA 2 70B</td><td>129</td></tr><tr><td>Google's T5 3.5B</td><td>123</td></tr><tr><td>OPT-6B</td><td>111</td></tr><tr><td>OPT-6B</td><td>75</td></tr><tr><td>ChatGPT-3.5</td><td>64</td></tr><tr><td>Google's T5 3.5B</td><td>62</td></tr><tr><td>Google's T5 3.5B</td><td>61</td></tr><tr><td>Meta's LLaMA 2 7B</td><td>68</td></tr><tr><td>Meta's LLaMA 2 7B</td><td>38</td></tr><tr><td>Meta's LLaMA 2 7B</td><td>38</td></tr><tr><td>Meta's LLaMA 2 7B</td><td>25</td></tr></tbody></table>"
# HTML(minified_html_table)
# Know your fridge
# disp_image("images/fridge-3.jpg")
# question = ("What're in the fridge? What kind of food can be made? Give "
#             "me 2 examples, based on only the ingredients in the fridge.")
# base64_image = encode_image("images/fridge-3.jpg")
# result = llama32pi(question, f"data:image/jpg;base64,{base64_image}")
# print(result)
# Asking a follow up question
# new_question = "is there banana in the fridge? where?"
# messages = [
#   {"role": "user", "content": [
#       {"type": "text", "text": question},
#       {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{base64_image}"}}
#   ]},
#   {"role": "assistant", "content": result},
#   {"role": "user", "content": new_question}
# ]
# result = llama32(messages)
# print(result)
# def llama32repi(question, image_url, result, new_question, model_size=90):
#     messages = [
#       {"role": "user", "content": [
#           {"type": "text", "text": question},
#           {"type": "image_url", "image_url": {"url": image_url}}
#       ]},
#       {"role": "assistant", "content": result},
#       {"role": "user", "content": new_question}
#     ]
#     result = llama32(messages, model_size)
#     return result
# Interior Design Assistant
# disp_image("images/001.jpeg")
# question = ("Describe the design, style, color, material and other "
#             "aspects of the fireplace in this photo. Then list all "
#             "the objects in the photo.")
# base64_image = encode_image("images/001.jpeg")
# result = llama32pi(question, f"data:image/jpeg;base64,{base64_image}")
# print(result)
# new_question = ("How many balls and vases are there? Which one is closer "
#                 "to the fireplace: the balls or the vases?")
# res = llama32repi(question, f"data:image/jpeg;base64,{base64_image}", result, new_question)
# print(res)
# disp_image("images/001.jpeg")
# Math grader
# disp_image("images/math_hw3.jpg")
# prompt = ("Check carefully each answer in a kid's math homework, first "
#           "do the calculation, then compare the result with the kid's "
#           "answer, mark correct or incorrect for each answer, and finally"
#           " return a total score based on all the problems answered.")
# base64_image = encode_image("images/math_hw3.jpg")
# result = llama32pi(prompt, f"data:image/jpg;base64,{base64_image}")
# print(result)
# Tool calling with image
# disp_image("images/golden_gate.png")
# question = ("Where is the location of the place shown in the picture?")
# base64_image = encode_image("images/golden_gate.png")
# result = llama32pi(question, f"data:image/png;base64,{base64_image}")
# print(result)
# weather_question = ("What is the current weather in the location "
#                  "mentioned in the text below: \n"  f"{result}")
# print(weather_question)
# from datetime import datetime
# ​
# current_date = datetime.now()
# formatted_date = current_date.strftime("%d %B %Y")
# ​
# messages = [
#     {"role": "system",
#      "content":  f"""
# Environment: ipython
# Tools: brave_search, wolfram_alpha
# Cutting Knowledge Date: December 2023
# Today Date: {formatted_date}
# """},
#     {"role": "user",
#      "content": weather_question}
#   ]
# print(llama32(messages))
# ​
# ​