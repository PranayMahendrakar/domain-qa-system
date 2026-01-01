"""feedback_learner module"""
from .base import LlamaClient
class FeedbackLearner:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are a domain-specific question answering expert."
    def process(self, query: str, context: str = "") -> str:
        return self.client.generate(f"Process: {query}\nContext: {context}\nProvide accurate, helpful response with sources.", self.system_prompt)
