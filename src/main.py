import os
from dotenv import load_dotenv
import logging
import asyncio
from src.discord_bot.bot import NBAStatsBot

load_dotenv()

from src.services.claude_service import ClaudeService
from src.agents.nba_agent import NBAAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.tools.nba_tool_schema import nba_tools
from src.tools.evaluator_tool_schema import evaluator_tools


def setup_logging():

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    noisy_loggers = [
        "httpx",
        "anthropic",
        "urllib3",
        "requests",
        "httpcore",
        "requests_oauthlib",
        "oauthlib",
        "discord.gateway",
        "discord.http",
        "discord.client",
        "discord.webhook",
    ]

    for logger_name in noisy_loggers:
        logging.getLogger(logger_name).propagate = False

    app_logger = logging.getLogger("src")
    app_logger.setLevel(logging.DEBUG)


async def main():
    setup_logging()
    _logger = logging.getLogger(__name__)

    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY") or ""
    discord_token = os.getenv("DISCORD_TOKEN") or ""

    if not api_key or not discord_token:
        _logger.error("No API key or Discord token found in environment variables")
        return

    claude_service = ClaudeService(api_key)

    nba_agent = NBAAgent(
        claude_service=claude_service,
        tool_schemas=nba_tools,
        tool_module_path="src.tools.nba_tools",
    )
    evaluator_agent = EvaluatorAgent(
        claude_service=claude_service,
        tool_schemas=evaluator_tools,
        tool_module_path="src.tools.evaluator_tools",
    )
    _logger.info("Agents initialized successfully")

    bot = NBAStatsBot(
        nba_agent=nba_agent,
        evaluator_agent=evaluator_agent,
    )

    try:
        _logger.info("Starting bot...")
        await bot.start(discord_token)
    except Exception as e:
        _logger.error(f"Failed to start bot: {e}", exc_info=True)
    finally:
        if not bot.is_closed():
            await bot.close()


def run():
    """Entry point for the poetry script"""
    asyncio.run(main())


if __name__ == "__main__":
    run()
