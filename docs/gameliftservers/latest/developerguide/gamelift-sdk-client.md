# Integrate your game client

withAmazon GameLift Servers

The topics in this section describe the managed Amazon GameLift Servers functionality that you can add
to a backend service. A backend service handles the following tasks:

- Requests information about active game sessions from Amazon GameLift Servers.
- Joins a player to an existing game session.
- Creates a new game session and joins players to it.
- Changes metadata for an existing game session.
  For more information about how game clients interact with
  Amazon GameLift Servers
  and game servers running on Amazon GameLift Servers, see [Game client/server interactions with
  Amazon GameLift Servers](gamelift-sdk-interactions.md "gamelift-sdk-interactions.md").

###### Prerequisites

- An AWS account.
- A game server build uploaded to Amazon GameLift Servers.
- A fleet for hosting your games.

###### Topics

- [Add Amazon GameLift Servers to your game client](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md")
- [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md")
