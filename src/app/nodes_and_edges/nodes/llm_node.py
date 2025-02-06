from langchain_core.messages import AIMessage

from src.app.logic.llm import create_llm
from src.app.states.schemas import AgentState
import json,re


async def llm_node(state: AgentState):
    print("State in llm node:", state)
    llm = create_llm()

    if not state.get("messages"):
        state["messages"] = []

    state["messages"].append(state["prompt"])

    response = await llm.ainvoke(state["prompt"].messages)

    if "platform" in response.content:
        print('➡ response.content:', response.content)
        match = re.search(r'\[(.*?)\]', response.content)
        if match:
            # Extracted content between brackets
            content = match.group(1)
            
            # Convert to list by replacing ':' with ',' and treating it as key-value pairs
            content_list = [item for item in content.split(",")]
            
            print(content_list[0])
        print('➡ response_data:', content_list[0])
        #print('➡ response_data type:', type(response_data))
        #print('➡ response_data:', response_data)

        # Extract values correctly
        state["social_media"] = content_list[0]
        state["clear_query"] = content_list[1]


    state["messages"].append(AIMessage(content=response.content))
    state["answer"] = response.content
    print('➡ state["answer"]:', state["answer"])
    
    return state
