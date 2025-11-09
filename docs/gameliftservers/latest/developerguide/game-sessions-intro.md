# Amazon GameLift Servers and the player experience

Players expect fast, fair, and reliable multiplayer gaming experiences. Amazon GameLift Servers delivers these experiences by providing game developers with tools that directly enhance how players connect and engage with multiplayer games. This topic outlines the key player benefits Amazon GameLift Servers features provide.

## Provide fast gameplay to players globally

Players want to connect to nearby servers with minimal lag. Amazon GameLift Servers ensures optimal connection experiences through intelligent placement and global infrastructure:

- **Players experience consistent performance
  globally** – Host games in AWS Regions and Local Zones
  available globally to minimize the distance between players and game servers
  (see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md")). You
  can choose from a wide range of Amazon EC2 instance types in these locations to find
  the best computing resources to host your game workloads.
- **Players connect to the best available servers**
  – Amazon GameLift Servers places players in game sessions with the lowest possible latency
  by gathering game client network data and searching for available servers across
  multiple locations. Use UDP ping beacons to collect accurate latency data.
  Configure latency policies to balance connection quality with acceptable wait
  times for players.
- **Players from different regions can play together** – Game session placements can balance game sessions with players from regional player pools while maintaining acceptable latency. Players from less-populated regions can find matches without sacrificing connection quality.

## Help players join games quickly

Players want fast access to games regardless of demand. Amazon GameLift Servers provides a range of capacity scaling tools that help you ensure that players can find games during peak and quiet periods:

- **Players can easily find available servers**
  – With automatic scaling tools, you can ensure that hosting resources are
  ready when they're needed. Target tracking manages a flexible buffer of capacity
  to anticipate player demand patterns for your game and scale proactively.
- **Players experience smooth performance during special
  events** – Combine auto-scaling with manual scaling
  techniques to handle sudden influxes after planned events, such as game updates,
  marketing campaigns, or tournaments.
- **Players don't have to wait for servers to start
  up** – On every game hosting resource, game servers are
  pre-warmed so that they're always ready to host new sessions as soon as players
  join.

## Build creative ways to group players for game sessions

Players want to compete or collaborate with others in fair, balanced ways. Amazon GameLift Servers offers a number of options for grouping players into game sessions:

- **Players are grouped to optimize player
  experience** – You can manage player grouping to best suit
  your game using a range of features. Let players search or browse game sessions
  or group player requests when they arrive based on skill level, latency, and
  other attributes. You can manage player grouping on your own or you can
  implement FlexMatch matchmaking with customizable match rules.
- **Players can join active matches** – Build player groups to start new game sessions, or use player sessions to track available slots in existing sessions and add new players. With FlexMatch, automatically backfill sessions with well-matched players.
- **Friends can play together as a team** – Player party support lets groups of friends play together. Game sessions can fill remaining slots with other players or restrict access. With FlexMatch, friends can form teams.
- **Players can bring custom data to game sessions** – Include game and player information in requests for game sessions and player sessions. The information gets passed on to the game server for use in a game session.
- **Players don't wait indefinitely for perfect matches** – With FlexMatch, you can relax match requirements over time to prevent player frustration from excessive queuing. Create progressive relaxation rules that prioritize the most important aspects of match quality.
- **Players can choose to accept or decline matches** – With FlexMatch, you can customize workflows for letting players accept or reject prospective matches.

## Deliver reliable connections throughout gameplay

Players expect consistent gameplay without interruptions or disconnections. Amazon GameLift Servers
provides comprehensive session management and protection:

- **Players enjoy high-quality performance on AWS
  Cloud** – With hosting managed by Amazon GameLift Servers, players get fast,
  reliable game servers that run on AWS computing infrastructure.
- **Validate players when they connect** –
  When you enable player sessions for your game, you can have Amazon GameLift Serversreserve player
  slots in game sessions and validate players on connection.
- **Players can reconnect and maintain game
  progress** – Amazon GameLift Servers supports reconnection for both server-side
  and client-side interruptions.
- **Players' games are protected from termination**
  – Optional game session protection feature prevents active sessions from
  being terminated during scaling events or other interruptions.

## Improve player experience based on real-world data

Players expect games to work consistently and get better over time. Amazon GameLift Servers provides comprehensive monitoring and analytics that help optimize the player experience:

- **Players experience fewer disruptions** –
  Real-time monitoring of fleet performance, game sessions, and player activity
  can identify issues before they significantly impact gameplay Customize graceful
  game session shutdowns and migrations.
- **Players benefit from proactive server health monitoring** – Amazon GameLift Servers provides continuous server health monitoring and automatically replaces unhealthy game servers to minimize hardware or software failure impact. Configure health check parameters to support different game requirements.
- **Players get data-driven improvements in gameplay** – Take advantage of game session logs and detailed analytics to reveal patterns in player behavior and server performance. Add custom logging support for game-specific events.

## Integrate enhanced game features with other AWS services

Players want integrated features like voice chat, secure authentication, and persistent progress. Amazon GameLift Servers can be integrated with other AWS services to provide comprehensive gaming experiences:

- **Players get streamlined authentication** – Amazon Cognito integration supports various identity providers and authentication methods while maintaining secure player identities across game sessions, with streamlined login processes for returning players.
- **Players can persist their game progress across
  sessions** – Amazon DynamoDB integration can be used to store
  player progression, inventories, and persistent data with high-performance
  access that ensures minimal gameplay impact while supporting cross-session
  continuity.
- **Players benefit from analytic insights**
  – Amazon Kinesis and Amazon Simple Storage Service (Amazon S3) integration processes game analytics to gather
  insights on player behavior and preferences, enabling real-time analytics that
  help developers adapt to changing player patterns and keep games fresh and
  engaging.
