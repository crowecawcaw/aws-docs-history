# GAMEPERF07-BP02 Run a separate matchmaking service for each

gameplay mode and game hosting Region

If your game offers multiple gameplay modes for players to choose
from, you should separate the matchmaking systems for each of them
so that you can independently tune the performance for each
gameplay mode based on its unique requirements and reduce resource
contention. Each gameplay mode will likely have unique
requirements for acceptable latency, match size, as well as other
customize game-specific matchmaking logic. They will also likely
attract different types of players. Run each game mode's
matchmaking service as a separate software deployment so that you
can performance test and operate the game modes independently.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

For example, you might run these as separate Lambda functions for
each game mode, or you might operate them as separate
container-based service deployments.

Deploy your matchmaking services to multiple Regions near your
game server locations. Player traffic will take many routes, so it
is important for the matchmaking service to maintain an up-to-date
latency profile across multiple ISPs to improve the efficiency of
low latency game session placement. GameLift FlexMatch provides
additional guidance for selecting Regions for matchmakers, and
includes the ability to integrate your matchmakers with
[multi-Region
game session queues](../../../gamelift/latest/developerguide/queues-intro.md "../../../gamelift/latest/developerguide/queues-intro.md").
