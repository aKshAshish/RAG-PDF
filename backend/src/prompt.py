from langchain_core.prompts import PromptTemplate

PROMPT_TYPES = ['QUERY', 'SUMMARY']
PROMPTS = {
    'QUERY': '''Use the following pieces of context to answer the question at the end.
            If you don't know the answer, just say that you don't know, don't try to make up an answer.
            Use ten sentences maximum and keep the answer as concise as possible.

            {context}

            Question: {question}

            Helpful Answer:''',
    'SUMMARY': ''''''
}


def get_prompt_type(query):
    return PROMPT_TYPES[0]


def get_prompt(query):
    prompt_type = get_prompt_type(query)
    return PromptTemplate.from_template(PROMPTS[prompt_type])