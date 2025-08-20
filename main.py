from dotenv import load_dotenv
import os
from agent1 import Agent
from openai import OpenAI

load_dotenv()
client = OpenAI()

def generate_html(prompt):
  response = client.responses.create(
    model="gpt-5",
    input=prompt
  )
  output_html = response.output_text
  return output_html

def generate_css(html_code, prompt_design):
  response = client.responses.create(
    model="gpt-5",
    input=f"""
    ${html_code}
    Above is a complete end to end html code, for which you, a design assistant with expertise in matching exactly what the stylistic prompt asks for, have to generate a comprehensive CSS code ONLY. Below is the design prompt for you to generate the CSS off:
    ${prompt_design}
    """
  )
  output_css = response.output_text
  return output_css

agent = Agent(client=client, tools_list={
    "generate_html": generate_html,
    "generate_css": generate_css
})
agent("Make me a beautiful landing page for my cat nursery")
