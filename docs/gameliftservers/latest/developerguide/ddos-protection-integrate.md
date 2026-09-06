

# Integrate player gateway into a game
<a name="ddos-protection-integrate"></a>

After creating a player gateway-enabled fleet, you must update your game client and game backend to integrate with player gateway. Your game backend retrieves relay endpoints and player gateway tokens, then provides them to game clients. Game clients send all UDP traffic to these relay endpoints.

The integration follows this call path:

1. Your game backend calls the `GetPlayerConnectionDetails` API to retrieve relay endpoints and player gateway tokens for each player in a game session.

1. Your game backend sends the relay endpoints and player gateway tokens to the game client.

1. Your game client prepends the player gateway token to all outgoing UDP packets and sends the packets to the relay endpoints.

1. The relay network validates the player gateway token and routes the traffic to your game server.

1. Your game server sends traffic back to your game client through the same relay paths.

## Backend integration
<a name="ddos-protection-integrate-backend"></a>

Your game backend must call the `GetPlayerConnectionDetails` API to retrieve relay endpoints and player gateway tokens for players. The backend then provides this information to game clients.

### GetPlayerConnectionDetails API
<a name="ddos-protection-integrate-backend-api"></a>

The `GetPlayerConnectionDetails` API returns connection details for players in a game session:

Relay endpoints and tokens  
When player gateway is enabled and supported in the location, returns:  
+ **Relay endpoints** – Multiple relay endpoints (IP address and port) that vary across players
+ **Player gateway token** – Token that the client must prepend to all UDP packets (valid for at least 3 minutes)
+ **Expiration** – Player gateway token expiration timestamp

Direct connection  
When player gateway is not enabled or not supported in the location, returns the game server's IP address and port

Your game client should be designed to handle both connection types.

Example API call:

```
// C++ example using AWS SDK
Aws::GameLift::GameLiftClient client;
Aws::GameLift::Model::GetPlayerConnectionDetailsRequest request;
request.SetGameSessionId(gameSessionId);
request.SetPlayerIds(playerIds);  // Vector of player IDs

auto outcome = client.GetPlayerConnectionDetails(request);
if (outcome.IsSuccess()) {
    auto result = outcome.GetResult();
    auto connectionDetails = result.GetPlayerConnectionDetails();
    
    // Process each player's connection details
    for (const auto& detail : connectionDetails) {
        std::string playerId = detail.GetPlayerId();
        
        // Get relay endpoints (IP address and port)
        auto endpoints = detail.GetEndpoints();
        for (const auto& endpoint : endpoints) {
            std::string ipAddress = endpoint.GetIpAddress();
            int port = endpoint.GetPort();
        }
        
        // Get player gateway token
        auto token = detail.GetPlayerGatewayToken();
        
        // Get expiration time
        auto expiration = detail.GetExpiration();
        
        // Send endpoints and token to game client
    }
}
```

See [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetPlayerConnectionDetails.html) in the *Amazon GameLift Servers API Reference*.

### Refresh relay endpoints
<a name="ddos-protection-integrate-backend-refresh"></a>

Call `GetPlayerConnectionDetails` periodically to provide players with updated endpoints when relay endpoints become unhealthy. We recommend calling the API every 60 seconds for all players in a game session. To optimize API usage, batch multiple player IDs in a single API call.

**Important**  
Regular refresh calls are the primary mechanism for delivering updated endpoints to players. While player gateway tokens remain valid for at least 3 minutes, refreshing every 60 seconds ensures players receive updated endpoints regularly.

## Client integration
<a name="ddos-protection-integrate-client"></a>

Your game client must prepend player gateway tokens to all outgoing UDP packets and send the packets to the provided relay endpoints. The Amazon GameLift Servers client SDK for C\+\+, C\#, Unreal Engine, and Unity provides utilities to simplify this integration.

### Client requirements
<a name="ddos-protection-integrate-client-requirements"></a>

To route traffic through player gateway, your game client must:
+ **Prepend player gateway tokens** – Prepend the player gateway token to all outgoing UDP packets. Player gateway tokens must not be encrypted and must appear at the beginning of each packet. Packets without a valid player gateway token will be dropped.
+ **Send to relay endpoints** – Send all UDP packets to the provided relay endpoints.
+ **Maintain connection activity** – Ensure that either the game client sends a packet to the game server, or the game server sends a packet to the player, at least once every 30 seconds. This activity maintains the connection through the relay network.
+ **Handle endpoint updates** – Accept updated relay endpoints and player gateway tokens from your backend (recommended every 60 seconds) and transition to new endpoints without dropping the connection.

### Client SDK
<a name="ddos-protection-integrate-client-sdk"></a>

The Amazon GameLift Servers client SDK for C\+\+, C\#, Unreal Engine, and Unity provides utilities to simplify player gateway integration:
+ **Token management** – Prepends player gateway tokens to all outgoing UDP packets.
+ **Endpoint selection** – Routes traffic to relay endpoints using a configurable algorithm.
+ **Endpoint refresh** – Schedules periodic callbacks to retrieve updated relay endpoints and player gateway tokens from your backend.

### Endpoint selection algorithms
<a name="ddos-protection-integrate-client-algorithms"></a>

The client SDK provides two built-in algorithms for selecting which relay endpoint to use:

Fallback algorithm  
Uses one endpoint until it becomes unhealthy, then switches to another endpoint. Best for menus, lobbies, and turn-based games where brief interruptions are acceptable. During endpoint failover, packets may be lost for the configured timeout period (default: 2 seconds).

Predictive rotation algorithm  
Continuously rotates through all available endpoints and predicts failures before they occur. Best for real-time gameplay such as first-person shooters and racing games where consistent packet delivery is critical. Requires the game server to send messages at a consistent frequency.

You can also implement custom algorithms by extending the SDK's base algorithm class.

### Client SDK resources
<a name="ddos-protection-integrate-client-resources"></a>

For complete integration instructions and sample code, see the following resources:

C\+\+  
A client SDK for C\+\+ is available at [Amazon GameLift Servers client SDK for C\+\+](https://github.com/amazon-gamelift/amazon-gamelift-servers-client-sdk-for-cpp).

C\#  
A client SDK for C\# is available at [Amazon GameLift Servers client SDK for C\#](https://github.com/amazon-gamelift/amazon-gamelift-servers-client-sdk-for-csharp).

Unreal Engine  
A plugin for Unreal Engine is available at [Amazon GameLift Servers client SDK for Unreal Engine](https://github.com/amazon-gamelift-for-unreal/amazon-gamelift-servers-client-sdk-for-unreal). Access requires membership in the Epic Games organization on GitHub. See [Unreal Engine on GitHub](https://www.unrealengine.com/en-US/ue-on-github) for details.

Unity  
A client SDK for Unity is available at [Amazon GameLift Servers client SDK for Unity](https://github.com/amazon-gamelift/amazon-gamelift-servers-client-sdk-for-unity).

## Test your integration
<a name="ddos-protection-integrate-testing"></a>

Before deploying to a fleet, test your player gateway integration locally using the player gateway testing tool. This tool simulates the player gateway UDP proxy infrastructure and helps you verify that your game client correctly prepends player gateway tokens, routes traffic through multiple endpoints, and handles network degradation.

For setup and usage instructions, see the [player gateway testing app](https://github.com/amazon-gamelift/amazon-gamelift-toolkit/tree/main/player-gateway-testing-app) on GitHub.

## Best practices
<a name="ddos-protection-integrate-best-practices"></a>

Follow these best practices when integrating player gateway:
+ **Refresh endpoints every 60 seconds** – Call `GetPlayerConnectionDetails` every 60 seconds to ensure players receive updated endpoints regularly.
+ **Batch API calls** – When calling `GetPlayerConnectionDetails` for multiple players in the same game session, batch the calls together to reduce API overhead.
+ **Maintain connection activity** – Ensure that traffic flows between the game client and game server at least once every 30 seconds. This can be either client-to-server or server-to-client traffic.
+ **Handle endpoint updates gracefully** – When your game client receives updated endpoints from the backend, transition to the new endpoints without dropping the player's connection.
+ **Choose the right algorithm** – Select the endpoint selection algorithm that best matches your game's requirements. Use the fallback algorithm for turn-based games and the predictive rotation algorithm for real-time games.