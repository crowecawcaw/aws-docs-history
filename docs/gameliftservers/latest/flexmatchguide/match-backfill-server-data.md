# Update match data on the game

server

No matter how you initiate match backfill requests in your game, your game server must
be able to handle the game session updates that Amazon GameLift Servers delivers as a result of match
backfill requests.

When Amazon GameLift Servers completes a match backfill request—successfully or not—it
calls your game server using the callback function `onUpdateGameSession`.
This call has three input parameters: a match backfill ticket ID, a status message , and
a GameSession object containing the most up-to-date matchmaking data including player
information. You need to add the following code to your game server as part of your game
server integration:

1. Implement the `onUpdateGameSession` function. This function must be
   able to handle the following status messages (`updateReason`):
   - MATCHMAKING_DATA_UPDATED – New players were successfully
     matched to the game session. The `GameSession` object
     contains updated matchmaker data, including player data on existing
     players and newly matched players.
   - BACKFILL_FAILED – The match backfill attempt failed due to an
     internal error. The `GameSession` object is unchanged.
   - BACKFILL_TIMED_OUT – The matchmaker failed to find a backfill
     match within the time limit. The `GameSession` object is
     unchanged.
   - BACKFILL_CANCELLED – The match backfill request was canceled by
     a call to StopMatchmaking (client) or StopMatchBackfill (server). The
     `GameSession` object is unchanged.

2. For successful backfill matches, use the updated matchmaker data to handle the
   new players when they connect to the game session. At a minimum, you'll need to
   use the team assignments for the new player(s), as well as other player
   attributes that are required to get the player started in the game.
3. In your game server's call to the Server SDK action [ProcessReady()](../../../gamelift/latest/developerguide/integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processready "../../../gamelift/latest/developerguide/integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processready"), add the `onUpdateGameSession` callback
   method name as a process parameter.
