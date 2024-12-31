from discord import Client, Message, Intents
from typing import Optional
from src.agents.nba_agent import NBAAgent
from src.agents.evaluator_agent import EvaluatorAgent


class NBAStatsBot(Client):
    def __init__(self, nba_agent: NBAAgent, evaluator_agent: EvaluatorAgent):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.nba_agent = nba_agent
        self.evaluator_agent = evaluator_agent

    async def setup_hook(self) -> None:
        """Called before the bot starts running"""
        # Initialize any background tasks
        pass

    async def on_ready(self):
        print(f"{self.user} is ready and online!")

    async def on_message(self, message: Message):
        if message.author == self.user:
            return

        response = self.nba_agent.get_nba_response(message.content)
        if response:
            await self._send_response(message.channel, response)
