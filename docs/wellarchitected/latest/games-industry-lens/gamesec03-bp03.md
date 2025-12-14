# GAMESEC03-BP03 Use your game backend service to validate player

requests to join a multiplayer game

Typically, in multiplayer games, a player will join a game session
by selecting an option directly from a list of available sessions,
or they will submit a request to find a match. The latter approach
places the responsibility on the game developer to locate an
eligible game session and provide the connection information
(usually an IP address and port number) back to the player's game
client. The implementation may vary depending on the genre of game
you are developing, but regardless, it is a security best practice
to perform server-side validation of a player's request to join a
game.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

For example, in a session-based multiplayer game, a request from a
player to join a game session should be validated by your game
server software with your game backend matchmaking service before
authorizing their connection to the server. When a player requests
to join a game session, the game server should check the request
for a unique identifier, such as a player session ID and
server-generated ticket that was previously provided to the game
client by your game backend matchmaking service.

Upon initiating the connection to the game server, your
server-side software can use this information to verify with the
matchmaking service that the player's connection request is valid
and verify that the player is not joining a spot that was
previously reserved in the game session for another player. 

For games that are hosted on Amazon GameLift, see
[Game
client/server interactions with Amazon GameLift Servers](../../../gamelift/latest/developerguide/gamelift-sdk-interactions.md "../../../gamelift/latest/developerguide/gamelift-sdk-interactions.md") for
an example of how this type of server-side validation can be
implemented.

**Customer example**

During AnyCompany Games' initial beta launch, they discovered that
players were bypassing their matchmaking system by directly
connecting to game servers, leading to serious competitive
integrity issues. When highly-ranked players found that they could
share server IP addresses with friends, they began circumventing
the skill-based matchmaking system, resulting in experienced
players joining novice matches and creating a frustrating
experience for new players. AnyCompany Games responded by
implementing a server-side validation system that generated unique
session tickets for each matchmaking request. The system required
both the player IDs and matchmaking request tickets and verified
connection attempts against their backend matchmaking service.

### Implementation steps

- Validate player join requests server-side using unique
  identifiers like player session IDs and server-generated
  tickets.
- Confirm the validity of connection requests with the
  matchmaking service to block unauthorized access.
- Verify that reserved spots in game sessions are not accessed
  by unauthorized players during the validation process.
