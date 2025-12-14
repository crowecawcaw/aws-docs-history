# Game hosting for real-time synchronous gameplay

Real-time synchronous gameplay allows for two or more players to
participate and interact in a game simultaneously where the state
of the gameplay is shared between the connected players to create
as close to a real-time experience as possible. Examples of
synchronous games include first-person shooters, massively
multiplayer online games (MMOG), sports and action games, or an
online game where two or more players must be connected to share
the play experience in near real time.

Characteristics of real-time synchronous gameplay architectures
include:

- Some games may be hosted as game sessions through game server
  processes that run on dedicated servers. Some games may use
  P2P-like architectures that employ lighter-weight Session
  Traversal Utilities for NAT (STUN) or Traversal Using Relays
  around NAT (TURN) servers. Regardless of the type of server
  involved, game servers are hosted in multiple data centers and
  AWS Regions globally.
- Game clients can join a game session either by requesting a
  match from a centralized matchmaking service hosted in the
  game backend system or by selecting a match from a predefined
  list of available game servers. The game client is provided
  with an IP address and port to connect to.
- Many synchronous games are latency sensitive, like
  first-person shooters and massively multiplayer online games.
  They will likely include algorithms like rewind and time
  dilation to minimize lag effects but may also have a
  pre-defined latency tolerance that is carefully measured and
  optimized to reduce the lag experience that can sometimes
  occur for players in high-latency situations. This latency
  information is determined by instrumenting game clients to
  ping the available game server AWS Regions to capture metrics
  such as latency, network jitter, and other important metrics
  for the gameplay experience. These metrics are sent to a
  central metrics collection service in the game backend system
  so that live operation streams can monitor game health. During
  the matchmaking process, game clients provide their current
  latency data as one of the request parameters when requesting
  a match, and the matchmaking service can use that latency data
  as one of the variables when selecting a game server to host
  the player.
- Typically, the gameplay is conducted over a mix of protocols
  (like game servers using faster UDP-based messaging with
  matchmaking, authentication, and other client-server traffic
  using HTTPS).
- Game servers employ algorithms and design to minimize
  client-server traffic like transform streaming, deltas, and
  data compression.
- Game servers are frequent targets for malicious activities and
  should be protected with a DDoS protection solution like AWS Shield Advanced.
