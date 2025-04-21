from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

import json

with open("menu.json","r") as file:
    menu = json.load(file)



load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are very expert in hospitality and scholar in dealing customers",
    instructions=["Greet the customer",f"If asked about the available items, respond with the following menu {menu}"],
    markdown=True
)

while True:
    inp = input("Enter the prompt : ")

    if inp == "exit":
        exit()
    else :
        agent.print_response(inp)
        print("\n")