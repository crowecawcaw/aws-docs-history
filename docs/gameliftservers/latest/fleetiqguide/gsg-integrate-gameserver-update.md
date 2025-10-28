# Update game server status

Once a game server is registered, it should regularly report health and utilization
status in order to keep the state of server capacity in sync on Amazon GameLift Servers FleetIQ. Report health
and utilization status by calling [UpdateGameServer()](../../../gamelift/latest/apireference/API_UpdateGameServer.md "../../../gamelift/latest/apireference/API_UpdateGameServer.md"). In the example below, the game server is reporting that
it is healthy and is not currently occupied with hosting players or gameplay.

```
AWS gamelift update-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234 \
    --health-check HEALTHY \
    --utilization-status AVAILABLE
```

**Health status**

If your game server has a mechanism for tracking health status, you can use this
mechanism to trigger a game server health update to Amazon GameLift Servers FleetIQ.

**Utilization status**

Reporting game server utilization status keeps Amazon GameLift Servers FleetIQ informed on which game servers
are currently ideal and available for new game sessions. Your game server must have a
mechanism that triggers a utilization status update to Amazon GameLift Servers FleetIQ. For example, you might
trigger the update when players connect to the game server or when a game session
starts.

When starting a game session, client or matchmaking services claim an available game
server (by calling [ClaimGameServer()](../../../gamelift/latest/apireference/API_ClaimGameServer.md "../../../gamelift/latest/apireference/API_ClaimGameServer.md")), prompt players to connect to the game server, and
trigger the game server to start gameplay. This process is described in [Integrate Amazon GameLift Servers FleetIQ into a game client](gsg-integrate-gameclient.md "gsg-integrate-gameclient.md"). A
game server "claim" is valid for 60 seconds, and the game server must be able to update
utilization status withing this window. If utilization status is not updated, Amazon GameLift Servers FleetIQ
removes the claim, assumes that the game server is available, and may reserve the game
server for another client claim request.

```
AWS gamelift update-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234 \
    --health-check HEALTHY \
    --utilization-status UTILIZED
```
