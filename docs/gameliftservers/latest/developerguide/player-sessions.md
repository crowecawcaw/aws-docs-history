# Look up player session data

If your game hosting solution uses player sessions and provides unique player IDs, you
can explore player-specific activity for past or present game sessions across multiple
fleets. Open the Player session lookup tool using either of the following methods:

- In the Amazon GameLift Servers console, open the left navigation pane and choose
  **Player session lookup** and select the filter type to
  use.
- When viewing a fleet's game session details, choose **View player
  sessions**. The lookup tool opens with the game session with the
  game session ID filter preselected and the game session value filled in.
  When using the lookup tool, you can provide any the following information:

- A player session ID to get information on a specific player session.
- A game session ID to get information on all player sessions for the requested
  game session. The results represent all players who reserved a slot or connected
  to the game session. You can optionally filter results by player session
  status.
- A player ID to get information on all player sessions for the requested
  player. The results represent all game sessions that the player participated
  in.

###### Note

The lookup tool searches for all player session activity across the currently
selected AWS Region. If you have multiple fleets in the Region, the results
include player session activity across all fleets. For multi-location fleets, the
results also include player session activity across the fleets' remote
locations.

The following player session data is collected for each game session:

- **Player session ID** – The identifier assigned to the
  player session.
- **Player ID** – A unique identifier for the player.
  Choose this ID to get additional player information.
- **Game session ID** – The identifier assigned to the
  game session.
- **Fleet ID** – The identifier assigned to the fleet
  that hosted the game session.
- **Status** – The status of the player session. The
  following are possible statuses:
  - **Reserved** – Player session has been
    reserved, but the players isn't connected.
  - **Active** – Player session is connected to
    the game server.
  - **Completed** – Player session has ended;
    player is no longer connected.
  - **Timed Out** – Player failed to
    connect.

- **Creation time** – The time the player connected to
  the game session.
- **Ending time** – The time the player disconnected
  from the game session.
- **Connection data** – IP address, DNS name and port
  that the player used to connect to the game session.
- **Player data** – Information about the player that
  was provided during player session creation.
