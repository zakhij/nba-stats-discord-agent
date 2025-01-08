from discord.ext import commands
from discord import Intents, app_commands, Interaction
from src.agents.nba_agent import NBAAgent
from src.agents.evaluator_agent import EvaluatorAgent
import logging

logger = logging.getLogger(__name__)


class NBAStatsBot(commands.Bot):
    def __init__(self, nba_agent: NBAAgent, evaluator_agent: EvaluatorAgent):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="*", intents=intents)

        self.nba_agent = nba_agent
        self.evaluator_agent = evaluator_agent

    async def setup_hook(self):
        """Called when the bot is ready"""
        self.tree.add_command(
            app_commands.Command(
                name="asknba",
                description="Ask any NBA-related question",
                callback=self.ask_nba,
            )
        )

        await self.tree.sync()
        print(f"{self.user} is ready and online!")

    async def ask_nba(self, interaction: Interaction, question: str):
        """Slash command handler for NBA questions"""
        await interaction.response.defer(thinking=True)

        try:
            response = await self.nba_agent.get_nba_response(question)
            if response:
                curated_response = await self.evaluator_agent.evaluate_nba_response(
                    question, response
                )
                await interaction.followup.send(
                    f"{interaction.user.mention} {curated_response}"
                )
            else:
                await interaction.followup.send(
                    f"{interaction.user.mention} I couldn't process your NBA question."
                )
        except Exception as e:
            logger.error(f"Error processing NBA question: {e}", exc_info=True)
            await interaction.followup.send(
                f"{interaction.user.mention} Sorry, something went wrong processing your question."
            )
