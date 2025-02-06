from langchain_core.messages import AIMessage

from app.logic.llm import create_llm
from app.states.scema import AgentState


async def llm_node(state: AgentState):
    print("State in llm node:", state)
    llm = create_llm()

    if not state.get("messages"):
        state["messages"] = []

    state["messages"].append(state["prompt"])

    response = await llm.ainvoke(state["prompt"].messages)

    state["messages"].append(AIMessage(content=response.content))
    state["answer"] = response.content
    print('➡ state["answer"]:', state["answer"])
    
    return state
