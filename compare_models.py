from llm_utils import query_openai, query_claude

def compare(prompt):
    oai = query_openai(prompt)
    claude = query_claude(prompt)
    return {"OpenAI": oai, "Claude": claude}