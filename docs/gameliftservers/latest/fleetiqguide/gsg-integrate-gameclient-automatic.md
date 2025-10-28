# Let Amazon GameLift Servers FleetIQ choose a game

server

To have Amazon GameLift Servers FleetIQ choose an available game server, call [ClaimGameServer()](../../../gamelift/latest/apireference/API_ClaimGameServer.md "../../../gamelift/latest/apireference/API_ClaimGameServer.md") without
specifying a game server ID. In this scenario, Amazon GameLift Servers FleetIQ does exercise its logic to find
a game server on an instance that is viable for game hosting and optimized for automatic
scaling.

```
AWS gamelift claim-game-server \
    --game-server-group-name MyLiveGroup
```

In response to a claim request, Amazon GameLift Servers FleetIQ identifies the `GameServer`
resource, connection information, and game data, which clients can use to connect to the
game server. The game server's claim status is set to CLAIMED for 60 seconds. Either
your game server or client service needs to update the game server's status on Amazon GameLift Servers FleetIQ
after players connect or gameplay starts. This ensures that Amazon GameLift Servers FleetIQ does not provide
this game server in response to subsequent requests for game server capacity. Update
game server status by calling [UpdateGameServer()](../../../gamelift/latest/apireference/API_UpdateGameServer.md "../../../gamelift/latest/apireference/API_UpdateGameServer.md").

```
AWS gamelift update-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234 \
    --health-check HEALTHY \
    --utilization-status UTILIZED
```
