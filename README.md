# NBA Stats Discord Agent 

An agentic Discord bot that answers NBA-related statistical queries. Uses Anthropic's SDK to build agents empowered with tools related to the [NBA Stats API Library](https://github.com/swar/nba_api).


## How it works

The project uses two main agents:
- `NBAAgent`: The "basketball expert" equipped with tools that map to NBA Stats API endpoints using the `nba_api` library. When a query comes in, it selects and executes the appropriate tools with the appropriate parameters and returns the relevant NBA statistical information.
- `EvaluatorAgent`: Takes the data returned by the NBA agent, sanity-checks it as an LLM judge, and then produces a final output message to be sent to the user.


## NBA Stats API Endpoints

The effectiveness of the Discord agent bot is directly tied to the breadth of NBA Stats API endpoint tools it is equipped with. One endpoint, one tool. All available endpoints can be found listed in the [NBA Stats API Library documentation](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints).

Currently supported endpoints are found in the `docs/implemented_endpoints` folder. Endpoints that were tested but found problematic are found in the `docs/problematic_endpoints` folder, which is described in [Problematic Endpoints Analysis](docs/problematic_endpoints_analysis.md). Regardless, more work must be done to test and implement more endpoints as tools.



