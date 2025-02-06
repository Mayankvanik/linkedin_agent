from langchain_core.messages import AIMessage

from src.app.logic.llm import create_llm
from src.app.states.schemas import AgentState


async def llm_node(state: AgentState):
    print("State in llm node:", state)
    llm = create_llm()

    if not state.get("messages"):
        state["messages"] = []

    state["messages"].append(state["prompt"])

    response = await llm.ainvoke(state["prompt"].messages)

    if "platform" in response.content:
        print('➡ response.content:', response.content)
        state["social_media"] = response.content['answer'][0]['platform']
        state['clear_query'] = response.content['answer'][0]['generated_query']

    state["messages"].append(AIMessage(content=response.content))
    state["answer"] = response.content
    print('➡ state["answer"]:', state["answer"])
    
    return state
