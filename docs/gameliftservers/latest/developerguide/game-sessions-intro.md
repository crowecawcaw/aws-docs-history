# How players connect to games

A _game session_ is an instance of your game running on
Amazon GameLift Servers. To play your game, a player can either find and join an existing game session or
create a new game session and join it. A player joins by creating a _player session_ for the game session. If the game session is open for
players, then Amazon GameLift Servers reserves a slot for the player and provides connection information. The
player can then connect to the game session and claim the reserved slot.

For detailed information about creating and managing game sessions and player sessions
with custom game servers, see [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md"). For information about connecting players to
Amazon GameLift Servers Realtime, see [Integrating a game client for Amazon GameLift Servers Realtime](realtime-client.md "realtime-client.md").

Amazon GameLift Servers provides several features related to game and player sessions.

**Host game sessions on best available resources across
multiple locations**

Choose from multiple options when configuring how Amazon GameLift Servers selects resources to
host new game sessions. If you're running fleets in multiple locations, then you
can design **game session queues** that place new
game sessions on any fleet regardless of location.
Use UDP ping beacons to calculate latency data, which the queue
automatically uses to prioritize placement locations.

**Control player access to game sessions**

Configure game sessions to allow or deny join requests from new players,
regardless of the number of players connected.

**Use custom game and player data**

Add custom data to game session objects and player session objects. Amazon GameLift Servers
passes game session data to a game server when starting a new game session.
Amazon GameLift Servers passes player session data to the game server when a player connects to
the game session.

**Filter and sort available game sessions**

Use session search and sort to find the best possible match for a prospective
player, or let player choose from a list of available game sessions. Use session
search and sort to find game sessions based on session characteristics . You can
also search and sort based on your own custom game data.

**Track game and player usage data**

Automatically have logs stored for completed game sessions. You can set up
log storage when integrating Amazon GameLift Servers into your game servers. For more
information, see [Logging server messages in Amazon GameLift Servers](logging-server-messages.md "logging-server-messages.md").

Use the Amazon GameLift Servers console to view detailed information about game sessions,
including session metadata, settings, and player session data. For more
information, see [Game and player sessions in
the Amazon GameLift Servers console](gamelift-console-game-player-sessions-metrics.md "gamelift-console-game-player-sessions-metrics.md") and [Metrics](gamelift-console-fleets-metrics.md#fleets-metrics-tab "gamelift-console-fleets-metrics.md#fleets-metrics-tab").
