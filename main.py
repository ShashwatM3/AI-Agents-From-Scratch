from dotenv import load_dotenv
from serpapi import GoogleSearch
import os
from agent1 import Agent
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

load_dotenv()
client = OpenAI()

def generate_html(prompt):
  response = client.responses.create(
    model="gpt-5",
    input=prompt + """
    Only produce HTML code. No CSS. However, add specific IDs or anything that could help with the styling.
    """
  )
  output_html = response.output_text
  return output_html

def generate_css(html_code, prompt_design):
  response = client.responses.create(
    model="gpt-5",
    input=f"""
    {html_code}
    Above is a complete end to end html code, for which you, a design assistant with expertise in matching exactly what the stylistic prompt asks for, have to generate a comprehensive CSS code ONLY. Below is the design prompt for you to generate the CSS off:
    {prompt_design}
    Your output must be ONLY CSS CODE, and must adhere to the request
    """
  )
  output_css = response.output_text
  return output_css

def get_web_results(query, max_results):
  def general_LLM_call(promptCallLLM):
    response = client.responses.create(
      model="gpt-5",
      input=promptCallLLM
    )
    outp = response.output_text
    return outp
  
  params = {
      "q": query,
      "api_key": os.getenv("SERPAPI_KEY"),
      "num": max_results
  }
  search = GoogleSearch(params)
  results = search.get_dict()
  
  links = []
  for result in results.get("organic_results", [])[:max_results]:
      link = result.get("link")
      if link:
          links.append(link)

  combined_text = ""
  for i, url in enumerate(links):
      try:
          response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
          soup = BeautifulSoup(response.text, "html.parser")

          for tag in soup(["script", "style", "nav", "footer", "header", "form", "noscript"]):
              tag.decompose()

          text = soup.get_text(separator="\n")
          lines = [line.strip() for line in text.splitlines() if line.strip()]
          cleaned_text = "\n".join(lines[:50])  # limit to first 50 lines

          combined_text += f"--- Source {i+1} ---\n{cleaned_text}\n\n"

      except Exception as e:
          combined_text += f"--- Source {i+1} ---\nFailed to scrape {url}: {e}\n\n"

  summary = general_LLM_call(f"""You are given some URLs and their respective scraped info which were retrieved from the query: {query}. You will analyze all the 3 URLs, and produce a concise summary of the information without compromising on any value. 

  Scraped info: {combined_text}
  """)

  return summary

tools_list = {
   "generate_html": {
      "function": generate_html,
      "description": "Generates a complete HTML structure based on prompt",
      "parameters_descriptions": "prompt: string - A prompt specifying the complete HTML structure to generate"
   },
    "generate_css": {
      "function": generate_css,
      "description": "Generates CSS styling for HTML code based on design requirements",
      "parameters_descriptions": "html_code: string - The HTML code to style, prompt_design: string - Design requirements for styling"
   },
    "get_web_results": {
      "function": get_web_results,
      "description": "Searches the web for information and provides a summary",
      "parameters_descriptions": "query: string - The search query, max_results: int - Maximum number of results to analyze (generally around 3-4)"
   }
}

agent = Agent(
   client = client,
   tools_list = tools_list,
   role = "Recipe website producer",
   backstory = "You are an assistant who will help the user cook their preferred recipes within a cuisine by producing a website for them with those recipes"
)

agent("I want to make indo-chinese food today. Give me a website with 3 recipes for today")
