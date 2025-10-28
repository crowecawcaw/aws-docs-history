# Register game servers

When a game server process is launched and ready to host live gameplay, it must
register with Amazon GameLift Servers FleetIQ by calling [RegisterGameServer()](../../../gamelift/latest/apireference/API_RegisterGameServer.md "../../../gamelift/latest/apireference/API_RegisterGameServer.md"). Registering allows Amazon GameLift Servers FleetIQ to respond to matchmaking
systems or other client services when they request information on server capacity or
claim a game server. When registering, the game server can provide Amazon GameLift Servers FleetIQ with
relevant game server data and connection information, including the port and IP address
that it uses for inbound client connections.

```
AWS gamelift register-game-server \
    --game-server-id UniqueId-1234 \
    --game-server-group-name MyLiveGroup \
    --instance-id i-1234567890 \
    --connection-info "1.2.3.4:123" \
    --game-server-data "{\"key\": \"value\"}"
```
