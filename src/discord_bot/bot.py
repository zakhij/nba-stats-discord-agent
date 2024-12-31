from discord import Client, Message, Intents
from typing import Optional
from src.agents.nba_agent import NBAAgent


class NBAStatsBot(Client):
    def __init__(self, nba_agent: NBAAgent):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.nba_agent = nba_agent
        self.message_handler = MessageHandler()

    async def setup_hook(self) -> None:
        """Called before the bot starts running"""
        # Initialize any background tasks
        pass

    async def on_ready(self):
        print(f"{self.user} is ready and online!")

    async def on_message(self, message: Message):
        if message.author == self.user:
            return

        await self.message_handler.handle(message, self.nba_agent)


class MessageHandler:
    async def handle(self, message: Message, agent: NBAAgent) -> Optional[str]:
        """Handle incoming Discord messages"""
        if not self._should_process(message):
            return None

        response = await agent.get_nba_response(message.content)
        await self._send_response(message.channel, response)

    def _should_process(self, message: Message) -> bool:
        # Add logic for when to respond (mentions, commands, etc)
        return True

    async def _send_response(self, channel, content: str):
        # Add formatting, embeds, etc.
        await channel.send(content)
