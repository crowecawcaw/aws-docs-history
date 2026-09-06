

# Enable player gateway on fleets
<a name="ddos-protection-enable"></a>

Enable player gateway when creating a fleet to route game traffic through relay endpoints that validate and rate limit incoming UDP traffic to your game servers.

## Prerequisites
<a name="ddos-protection-enable-prerequisites"></a>

Before enabling player gateway, verify the following requirements:
+ **Supported locations** – For a list of AWS locations that support player gateway, see [Amazon GameLift Servers service locations](gamelift-regions.md).
+ **Fleet type** – Player gateway supports Linux-based Managed EC2 fleets and Managed Container fleets.
+ **Server SDK** – Player gateway requires Amazon GameLift Servers Server SDK 5.0 or later.

## Player gateway modes
<a name="ddos-protection-enable-modes"></a>

Configure player gateway compatibility for your fleet using the `PlayerGatewayMode` property:

DISABLED (default)  
Fleet is not compatible with player gateway.

ENABLED  
Fleet is compatible with player gateway in locations where it is supported. Fleet locations that do not support the feature can still be added to the fleet but will not utilize player gateway, directly utilizing the game server IP address.

REQUIRED  
Fleet is compatible with player gateway. Fleet locations that do not support the feature cannot be added to the fleet.

## IPv4 and IPv6 compatibility
<a name="ddos-protection-enable-ip-protocol"></a>

Game clients must communicate with player gateway via IPv4. The player gateway relay network communicates with game servers using IPv6. Managed Container fleets automatically translate the IPv6 traffic to IPv4. For Managed EC2 fleets, configure how your fleet handles IPv6 traffic using the `GameServerIpProtocolSupported` property in `PlayerGatewayConfiguration`:

IPv4 (default)  
Your game server only accepts incoming IPv4 traffic. Lightweight IP translation software will be installed and executed on your instances to receive and transform the incoming IPv6 traffic to IPv4.

DUAL\_STACK  
Your game server is compatible with incoming IPv6 traffic. IP translation software will not be installed or executed on your instances. Game servers that support IPv6 natively may have slightly higher performance.