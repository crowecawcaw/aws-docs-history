# Monitoring

| GAMEPERF04 — How do you design your matchmaking service to optimize performance? |
| -------------------------------------------------------------------------------- |
|                                                                                  |

**GAMEPERF_BP09 - Define network latency thresholds for your game.**

When developing a multiplayer game, ensure that your game infrastructure does not
introduce unnecessary latency for players. If your game is sensitive to network latency,
then you should set latency thresholds in your matchmaking logic to prioritize placing
players on game server instances that are hosted in Regions where their connection to
the game session meets your objective for ideal player experience.

In many latency-sensitive games it is common to instrument the game clients to ping
each of the game's infrastructure Regions to gather performance data such as network
latency, jitter, and packet loss, and report this data to your metrics collection
backend so that it can be analyzed. When matching players into game sessions, you can
configure your game to incorporate the game client's perceived network latency to your
game server infrastructure as one of the inputs used in your matchmaking service when
selecting a game for a player.

**GAMEPERF_BP10 - Run a separate matchmaking service for each gameplay mode and game hosting Region.**

If your game offers multiple gameplay modes for players to choose from, you should
separate the matchmaking systems for each of them so that you can independently tune the
performance for each gameplay mode based on its unique requirements, and reduce resource
contention. Each gameplay mode will likely have unique requirements for acceptable
latency, match size, as well as other customize game-specific matchmaking logic. They
will also likely attract different types of players. Run each game mode's matchmaking
service as a separate software deployment so that you can more easily performance test
and operate the game modes independently. For example, you might run these as separate
Lambda functions for each game mode, or you might operate them as separate
container-based service deployments.

Deploy your matchmaking services to multiple Regions, preferably the same Regions that
you host your game servers, so that players can be routed to a matchmaking service that
is closest to them which can improve the efficiency of finding game servers with low
latency. Amazon GameLift Servers FlexMatch provides additional guidance for selecting Regions for
matchmakers, and includes the ability to integrate your matchmakers with [multi-Region game session queues](../../../gamelift/latest/developerguide/queues-intro.md "../../../gamelift/latest/developerguide/queues-intro.md").

**GAMEPERF_BP11 - Regularly monitor matchmaking performance.**

One of the most effective ways to optimize the performance of a game for players is to reduce the time that they must wait before they can enter into a game session. Long wait times can cause players to lose interest and lead to attrition, so it is important to consider this when designing your matchmaking solution.

When you are designing your game matchmaking configuration for your game, you will need to create rules that determine the conditions that are applied in order to form a match. You should consider the impact that these rules will have on the performance of the system, particularly the wait times for players. Before deploying changes to your matchmaking implementation, such as the addition of new matchmaking conditions or filters, you should properly test this beforehand, or consider releasing this change gradually to a small sample population of players as a canary or A/B test to gather performance metrics before introducing this change to the entire player population.

Configure your matchmaking service to generate detailed logs that can help you to
understand what conditions or rules were applied to each matchmaking request so that you
review and adjust matchmaking implement as necessary. For example, Amazon [Amazon GameLift Servers
FlexMatch](../../../gamelift/latest/flexmatchguide/match-intro.md "../../../gamelift/latest/flexmatchguide/match-intro.md") provides a fully-managed matchmaking service which can be used as a
standalone service with your own game server hosting or used with game servers hosted on
Amazon GameLift Servers. FlexMatch can generate event notifications to Amazon EventBridge (formerly
CloudWatch Events) and Amazon Simple Notification Service (Amazon SNS) in JSON format so
that you can automatically process and store this data for analysis to help you improve
matchmaking performance.

Setup metrics to track how long your matchmaking service takes to find a suitable
game session for players. Regularly review matchmaking duration metrics and correlate
these times with player behavior and community sentiment in order to develop suitable
thresholds for matchmaking timeouts that you can include in your matchmaking rule
configuration. For example, Amazon GameLift Servers FlexMatch provides support for defining
matchmaking request timeouts as well as creating matchmaking rules that can [allow requirements to relax over time](../../../gamelift/latest/flexmatchguide/match-design-ruleset.md#match-rulesets-components-expansion "../../../gamelift/latest/flexmatchguide/match-design-ruleset.md#match-rulesets-components-expansion"). This feature allows you to create
matchmaking that can adapt to make it easier to create matches and place players into
game sessions when matches are difficult to find.
