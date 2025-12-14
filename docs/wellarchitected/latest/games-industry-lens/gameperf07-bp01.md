# GAMEPERF07-BP01 Define network latency thresholds for your

game

When developing a multiplayer game, verify that your game
infrastructure does not introduce unnecessary latency for players.
If your game is sensitive to network latency, then you should set
latency thresholds in your matchmaking logic to prioritize placing
players on game server sessions that are hosted in nearby game
server locations or AWS Regions that meet your objective for ideal
player experience.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In many latency-sensitive games it is common to instrument the
game clients to ping each of the game's infrastructure locations
to gather performance data such as network latency, jitter, and
packet loss, and report this data to the metrics collection
backend so that it can be analyzed. When matching players into
game sessions, you can configure your game to incorporate the game
client's perceived network latency to your game server
infrastructure as one of the inputs used in your matchmaking
service logic.
