from langchain_core.prompts import ChatPromptTemplate

def social_media_prompt_template(question: str) -> ChatPromptTemplate:
    template = """you have to make more clear query and also find out query ask related for which social media platform ex(instagram , twitter , linkedin)
    answer formate is only be like below formate
    answer:["generated_query":"your created more clea query", "platform":"instagram"]
    query: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

def create_chat_prompt_template(context: str, question: str, social_media: str) -> ChatPromptTemplate:
    template = """Generate blog or tweet or post related content based on platform based on the following context:
    {context}
    make content which following platform formate
    platform: {social_media}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

