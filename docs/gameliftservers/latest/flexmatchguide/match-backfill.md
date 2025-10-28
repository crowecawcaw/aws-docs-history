# Backfill existing games with FlexMatch

Match backfill uses your FlexMatch mechanisms to find new players for existing matched game
sessions. Although you can always add players to any game (see [Join a
player to a game session](../../../gamelift/latest/developerguide/gamelift-sdk-client-api.md#gamelift-sdk-client-api-join "../../../gamelift/latest/developerguide/gamelift-sdk-client-api.md#gamelift-sdk-client-api-join")), match backfill ensures that new players meet the same
match criteria as current players. In addition, match backfill assigns the new players to
teams, manages player acceptance, and sends updated match information to the game server.
Learn more about match backfill in [FlexMatch matchmaking process](gamelift-match-howitworks.md "gamelift-match-howitworks.md").

###### Note

FlexMatch backfill is not currently available for games using Amazon GameLift Servers Realtime.

There are two types of backfill mechanisms:

- Enable automatic backfill to fill game sessions that start with fewer than the maximum allowed players.
  Automatic backfill doesn't backfill players who join the game and then drop out.
- Set up a manual backfill mechanism to replace players who drop out of a game session in progress.
  This mechanism must be able to detect an open slot and generate a backfill request to fill it.
