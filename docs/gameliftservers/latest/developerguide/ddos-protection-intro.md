# DDoS protection with Amazon GameLift Servers

Amazon GameLift Servers player gateway is a relay-based network that routes UDP traffic between game
clients and game servers hosted on Amazon GameLift Servers. Player gateway provides proactive DDoS protection
by validating traffic before it reaches game servers, rate limiting player traffic, hiding
game server IP addresses from the public, and providing updated endpoints when relay endpoints
become unhealthy. This feature helps protect your game servers from volumetric attacks with
negligible added latency.

Player gateway requires game servers to run on Linux-based Amazon GameLift Servers Managed EC2 fleets
or Container Fleets. You must enable player gateway during fleet creation and update your
game client and game backend to use this feature.

## Key benefits

Player gateway provides the following security and operational benefits:

- **Hide game server IP addresses** – Game clients
  connect through relay endpoints instead of directly to game servers, hiding your game
  server addresses from the public.
- **Validate traffic** – All traffic through player gateway requires a player gateway token, allowing only traffic from authenticated players to reach your game servers.
- **Dynamic endpoint replacement** – When relay endpoints become unhealthy, Amazon GameLift Servers quickly replaces the endpoints and provides updated healthy endpoints on the next call to refresh player connection details.
- **Distribute player traffic** – Relay endpoints vary across players, reducing the impact of a single unhealthy relay endpoint to other players within the same game session.
