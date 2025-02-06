from langchain_core.prompts import ChatPromptTemplate

def social_media_prompt_template(question: str) -> ChatPromptTemplate:
    template = """you have to make more clear query and also find out query ask related for which social media platform ex(instagram , twitter , linkedin)
    answer formate in json should be like below formate
    answer:{"generated_query":"your created more clea query", "platform":"instagram"}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

def create_chat_prompt_template(context: str, question: str) -> ChatPromptTemplate:
    template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

