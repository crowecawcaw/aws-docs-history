# Set up a game server for FlexMatch

Game servers that are hosted with Amazon GameLift Servers must be integrated with the Amazon GameLift Servers server
SDK and have core functionality as described in [Add Amazon GameLift Servers to your game server](../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md "../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md").
This functionality makes it possible for your game server to run on Amazon GameLift Servers hosting resources
and communicate with the Amazon GameLift Servers service. The following instructions describe additional tasks
that you need to do to add FlexMatch functionality.

###### To add FlexMatch to your game server

1. **Use matchmaking data when starting game sessions.**
   Your game server implements a callback function called `onStartGameSession()`.
   After creating a match, Amazon GameLift Servers looks for an available game server process and calls this function
   to prompt it to start a game session for the match. This call includes a game session object
   ([GameSession](../apireference/API_GameSession.md "../apireference/API_GameSession.md")).
   Your game server uses the game session information, including matchmaker data, to
   start the game session. For more details on starting a game session, see [Start a game session](../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-startsession "../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-startsession"). For more on matchmaker data, see
   [About matchmaker data](match-server.md#match-server-data "match-server.md#match-server-data").
2. **Handle player connections.** When connecting to
   a matched game, a game client references a player ID and a player session ID
   (see [Validate a new player](../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-validateplayer "../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-validateplayer")). Set up your game server to use the player ID to
   associate an incoming player with player information in the matchmaker data.
   Matchmaker data identifies a player's team assignment and other
   information to represent the player in the game.
3. **Report when players leave a game.** Make sure
   that your game server calls the server SDK
   [RemovePlayerSession](../developerguide/integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-removeplayersession "../developerguide/integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-removeplayersession")
   to report a dropped player. This step is particularly important if you're
   using FlexMatch backfill to fill empty slots in existing games. Learn
   more about implementing FlexMatch backfill in [Backfill existing games with FlexMatch](match-backfill.md "match-backfill.md").
4. **Request new players to fill existing matches
   (optional).** Decide how you want to backfill your live matches.
   If your matchmaker has the backfill mode set to "manual", you might want to
   add backfill support to your game. If backfill mode is set to "automatic", you
   might need a way to turn it off for individual game sessions. For example, after
   a game session reaches a certain point in the game, you might want to stop backfilling.
   Learn more about how to implement match backfill in [Backfill existing games with FlexMatch](match-backfill.md "match-backfill.md").
