# Generate player IDs

Amazon GameLift Servers uses a player session to represent a player connected to a game session. Amazon GameLift Servers
creates a player session each time a player connects to a game session using a game client
integrated with Amazon GameLift Servers. When a player leaves a game, the player session ends. Amazon GameLift Servers doesn't
reuse player sessions.

###### Important

When using FlexMatch matchmaking, if you create a new matchmaking request that contains a player ID that is already included in an existing active matchmaking request, the existing request is automatically cancelled. However, a `MatchmakingCancelled` event is not sent for the cancelled request. To monitor the status of existing matchmaking requests, use [DescribeMatchmaking](../../../gamelift/latest/apireference/API_DescribeMatchmaking.md "../../../gamelift/latest/apireference/API_DescribeMatchmaking.md") to poll the request status at infrequent intervals (30-60 seconds). The cancelled request will show a status of `CANCELLED` with the reason `Cancelled due to duplicate player`.

The following code example randomly generates unique player IDs:

```
bool includeBrackets = false;
bool includeDashes = true;
string playerId = AZ::Uuid::CreateRandom().ToString<string>(includeBrackets, includeDashes);
```

For more information about player sessions, see [Game and player sessions in
the Amazon GameLift Servers console](gamelift-console-game-player-sessions-metrics.md "gamelift-console-game-player-sessions-metrics.md").
