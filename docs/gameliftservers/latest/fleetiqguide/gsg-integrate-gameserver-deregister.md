

# Deregister game servers
<a name="gsg-integrate-gameserver-deregister"></a>

When a game concludes, the game server must deregister from Amazon GameLift Servers FleetIQ using [DeregisterGameServer()](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeregisterGameServer.html).

```
AWS gamelift deregister-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234
```