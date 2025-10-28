# Choose your own game server

With the "list and pick" method, your game client or matchmaker requests a list of
available game servers by calling [ListGameServers()](../../../gamelift/latest/apireference/API_ListGameServers.md "../../../gamelift/latest/apireference/API_ListGameServers.md"). You might want to use game server data to provide
additional information that players or your matchmaker can use when selecting a game
server. To control how results are returned, you can request paginated results and sort
game servers by registration date. The following request returns 20 active and available
game servers in the specified game server group, sorted by registration time with the
newest game servers listed first.

```
AWS gamelift list-game-servers \
    --game-server-group-name MyLiveGroup \
    --limit 20 \
    --sort-order DESCENDING
```

Based on the list of available game servers, the client or matchmaking service selects
a game server and claims it by calling [ClaimGameServer()](../../../gamelift/latest/apireference/API_ClaimGameServer.md "../../../gamelift/latest/apireference/API_ClaimGameServer.md") with the specific game server ID. In this scenario,
Amazon GameLift Servers FleetIQ does not exercise any of its instance type optimization logic, as described in
[Amazon GameLift Servers FleetIQ logic](gsg-howitworks-logic.md "gsg-howitworks-logic.md").

```
AWS gamelift claim-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234
```
