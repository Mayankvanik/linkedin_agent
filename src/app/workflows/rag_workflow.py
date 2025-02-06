from langgraph.graph import END, StateGraph

from app.nodes_and_edges.nodes.llm_node import llm_node
from app.nodes_and_edges.nodes.prompt_node import prompt_node , first_prompt_node
from app.nodes_and_edges.nodes.retrieval_node import retrieve_node
from app.states.schemas import AgentState

from tavily import TavilyClient
import os, re
from dotenv import load_dotenv
load_dotenv()


# Initialize Tavily client
#tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_online(state: AgentState):  # Default search depth if not specified
    """this is search tool which take latest information from the internet."""
    print("State in searchhh node:", state['question'])
    try:
        # Perform the search using Tavily API
        result = tavily_client.get_search_context(
            query=state['question'],
            max_tokens=1000  # Adjust as needed
        )
        #print(result)
        cleaned_result = re.sub(r'[\\"]+', '', result)
        cleaned_result = cleaned_result.strip("'[]")
        state["context"]=cleaned_result
        return state#{"result": cleaned_result}
    except Exception as e:
        return {'error': 'Search failed', 'details': str(e)}


def create_rag_graph():
    workflow = StateGraph(AgentState)

    #workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("first_social-media_prompt",first_prompt_node)
    workflow.add_node("llm_node", llm_node)
    workflow.add_node("searching_online", search_online)
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("generate_prompt", prompt_node)

    workflow.add_edge("retrieve", "generate_prompt")
    workflow.add_edge("generate_prompt", "llm_node")
    workflow.add_edge("llm_node", END)

    workflow.set_entry_point("retrieve")
    return workflow.compile()
