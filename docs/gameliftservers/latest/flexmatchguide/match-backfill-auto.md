# Turn on automatic backfill

With automatic match backfill, Amazon GameLift Servers automatically triggers a backfill request
whenever a game session starts with one or more unfilled player slots. This feature
allows games to start as soon as the minimum number of matched players is found and fill
remaining slots later as additional players are matched. You can opt to stop automatic
backfill at any time.

As an example, consider a game that can hold six to ten players. FlexMatch initially
locates six players, forms the match, and starts a new game session. With automatic
backfill, the new game session can immediately request an additional four players.
Depending on the game style, we might want to allow new players to join at any time
during the game session. Alternatively, we might want to stop automatic backfill after
initial setup phase and before gameplay starts.

To add automatic backfill to your game, make the following updates to your
game.

1. **Enable automatic backfill.** Automatic backfill
   is managed in a matchmaking configuration. When enabled, it is used with all
   matched game sessions that are created with that matchmaker. Amazon GameLift Servers begins
   generating backfill requests for a non-full game session as soon as the game
   session starts up on a game server.

To turn on automatic backfill, open a match configuration and set the backfill
mode to "AUTOMATIC". For more details, see [Create a matchmaking configuration](match-create-configuration.md "match-create-configuration.md") 2. **Turn on backfill prioritization**. Customize
your matchmaking process to prioritize filling backfill requests before creating
new matches. In your matchmaking rule set, add an algorithm component and set
backfill priority to "high". For more details, see [Customize the match
algorithm](match-rulesets-components-algorithm.md "match-rulesets-components-algorithm.md"). 3. **Update game session with new matchmaker data.**
Amazon GameLift Servers updates your game server with match information using the Server SDK
callback function `onUpdateGameSession` (see [Initialize the server process](../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-initialize "../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-initialize")). Add code to your game server to
handle updated game session objects as a result of backfill activity. Learn more
in [Update match data on the game
server](match-backfill-server-data.md "match-backfill-server-data.md"). 4. **Turn off automatic backfill for a game
session.** You can opt to stop automatic backfill at any point
during an individual game session. To stop automatic backfill, add code to your
game client or game server to make the Amazon GameLift Servers API call [StopMatchmaking](../../../gamelift/latest/apireference/API_StopMatchmaking.md "../../../gamelift/latest/apireference/API_StopMatchmaking.md"). This
call requires a ticket ID. Use the backfill ticket ID from the latest backfill
request. You can get this information from the game session matchmaking data,
which is updated as described in the previous step.
