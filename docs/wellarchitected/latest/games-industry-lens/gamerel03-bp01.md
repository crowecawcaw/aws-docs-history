# GAMEREL03-BP01 Monitor game server disruptions, and use the

data to improve hosting architecture to achieve reliability
goals

Monitor game server metrics and the impact of failures or
degradations in performance, such as increased latency under load,
on player behavior over time so that you can adjust your game
server hosting strategy to meet your game's reliability
requirements. Game server infrastructure to be degraded should be
removed from service immediately if it is impacting players or
proactively replaced when there are no active player sessions
hosted on the server.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For scenarios where games are hosted as REST APIs, system
reliability can be managed like traditional web application
architectures, where traffic can be load balanced across multiple
servers in a distributed manner to mitigate the risk of server
failures.

For real-time synchronous gameplay, a game session is usually
hosted on a game server process running on a virtual machine, or
game server instance, since gameplay state needs to be maintained
in a performant manner and replicated to connected game clients.
This implementation means that a player's experience is tightly
coupled to the performance and reliability of the game server
process that hosts their game session. This type of architecture
makes managing the reliability of game servers more complex than
traditional approaches.

To mitigate the impact of a game server failure, configure your
game to continuously perform asynchronous updates of a player's
game state to a highly-available cache or database such
as [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/ "https://aws.amazon.com/elasticache/redis/")
or [Amazon MemoryDB](https://aws.amazon.com/memorydb/ "https://aws.amazon.com/memorydb/"). If a server failure occurs, the
player's last saved game state can be fetched from the external
data store, and their session can be restored on a new game server
instance.

However, this approach adds additional cost and complexity to
manage this external state, and may not be suitable for fast-paced
or competitive games where the state changes are so frequent and
happening at such a significant scale that introducing even a
performant in-memory cache data store would result in replication
lag that is too significant to be useful to restore a session
from. For games of this nature, the optimal approach is to accept
the loss of the server and send the player back to a game lobby to
find another session or you can automatically redirect them into
another game session.

Capture as much useful log data about what caused the server
disruption so that you can investigate the issue later. Amazon
GameLift provides guidance
for [debugging
fleet issues](../../../gamelift/latest/developerguide/fleets-creating-debug.md "../../../gamelift/latest/developerguide/fleets-creating-debug.md") and provides the ability
to [remotely
access Amazon GameLift fleet instances](../../../gamelift/latest/developerguide/fleets-remote-access.md "../../../gamelift/latest/developerguide/fleets-remote-access.md") .

### Implementation steps

- Monitor game server metrics for performance degradations,
  and remove or replace degraded servers as necessary to
  maintain reliability.
- Use Amazon ElastiCache or MemoryDB for asynchronous game
  state updates to enable session recovery after server
  failures when feasible.
- Capture detailed log data on server disruptions for
  investigation and debugging, leveraging tools like Amazon
  GameLift for fleet monitoring and remote access.
