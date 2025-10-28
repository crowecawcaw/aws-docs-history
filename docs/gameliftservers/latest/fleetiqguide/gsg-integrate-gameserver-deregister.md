# Deregister game servers

When a game concludes, the game server must deregister from Amazon GameLift Servers FleetIQ using [DeregisterGameServer()](../../../gamelift/latest/apireference/API_DeregisterGameServer.md "../../../gamelift/latest/apireference/API_DeregisterGameServer.md").

```
AWS gamelift deregister-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234
```
