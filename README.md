# NBA Stats Discord Agent 

An agentic Discord bot that answers NBA-related statistical queries. Uses Anthropic's SDK to build agents empowered with tools related to the [NBA Stats API Library](https://github.com/swar/nba_api).


## How it works (WIP)

The project uses two main agents:
- `NBAAgent`: The "basketball expert" equipped with tools that map to NBA Stats API endpoints. When a query comes in, it selects and executes the appropriate tools and returns the NBA statistical data.
- `EvaluatorAgent`: Takes the data returned by the NBA agent, sanity-checks it as an LLM judge, and then tweets out the response.






