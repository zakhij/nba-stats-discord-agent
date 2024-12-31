from src.agents.base_agent import BaseAgent


class EvaluatorAgent(BaseAgent):
    SYSTEM_PROMPT = """
    You are a professional social media expert specializing in NBA content.
    Your role is to evaluate the NBA information for relevance to the original question.
    """

    def evaluate_nba_response(self, user_message: str, nba_response: str) -> str:
        """Evaluate the NBA response for relevance to the original question"""
        # Implement your evaluation logic here
        return "TEST!!!"
