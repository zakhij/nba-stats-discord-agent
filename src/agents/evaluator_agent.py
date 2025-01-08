from src.agents.base_agent import BaseAgent
import asyncio


class EvaluatorAgent(BaseAgent):
    SYSTEM_PROMPT = """
    Your role is to evaluate the NBA information for relevance to the original question and
    output a concise, neutral message to the user based on the NBA response.
    If the NBA response is not relevant, output "Sorry, I can't help with that. I only answer questions about the NBA."
    """

    async def evaluate_nba_response(
        self, original_message: str, nba_response: str
    ) -> str:
        messages = [
            {
                "role": "user",
                "content": f"""
                Original Question: {original_message}
                NBA Response: {nba_response}
                """,
            }
        ]

        # Run Claude service in executor, it does not support async natively
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: self.claude_service.create_message(
                system_prompt=self.SYSTEM_PROMPT,
                messages=messages,
                tools=self.tool_schemas,
                tool_choice={"type": "any"},
            ),
        )

        if response.stop_reason == "tool_use":
            tool_use = next(
                block for block in response.content if block.type == "tool_use"
            )
            output_message = self.execute_tool(tool_use.name, tool_use.input)
            if output_message:
                return output_message
        return "Sorry, I can't help with that."
