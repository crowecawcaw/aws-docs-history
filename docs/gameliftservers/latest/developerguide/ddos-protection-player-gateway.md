# Amazon GameLift Servers player gateway

Amazon GameLift Servers player gateway is a relay-based network that routes UDP traffic between game
clients and game servers hosted on Amazon GameLift Servers. Player gateway provides proactive DDoS protection
by validating traffic before it reaches game servers, rate limiting player traffic, hiding
game server IP addresses from the public, and providing updated endpoints when relay endpoints
become unhealthy. This feature helps protect your game servers from volumetric attacks with
negligible added latency.

Player gateway is provided at no additional charge when you use Amazon GameLift Servers. It requires
game servers to run on Linux-based Amazon GameLift Servers Managed EC2 fleets or Container Fleets. You must
enable player gateway during fleet creation and update your game client and game backend
to use this feature.

## Key benefits

Player gateway provides the following security and operational benefits beyond
the baseline DDoS protection:

- **Hide game server IP addresses** – Game clients
  connect through relay endpoints instead of directly to game servers, hiding your game
  server addresses from the public.
- **Validate traffic** – All traffic through
  player gateway requires a player gateway token, allowing only traffic from
  authenticated players to reach your game servers.
- **Dynamic endpoint replacement** – When relay
  endpoints become unhealthy, Amazon GameLift Servers quickly replaces the endpoints and provides updated
  healthy endpoints on the next call to refresh player connection details.
- **Distribute player traffic** – Relay endpoints
  vary across players, reducing the impact of a single unhealthy relay endpoint to other
  players within the same game session.
- **No additional cost** – Player gateway is
  included at no additional charge with Amazon GameLift Servers.

## Prerequisites

To use player gateway, you need the following:

- Game servers running on Linux-based Amazon GameLift Servers Managed EC2 fleets or Container
  Fleets.
- Player gateway enabled during fleet creation.
- Game client and game backend updated to use player gateway tokens and relay
  endpoints.

For details on how player gateway works, see
[How player gateway works](ddos-protection-howitworks.md "ddos-protection-howitworks.md"). To get started with integration, see
[Enable player gateway on fleets](ddos-protection-enable.md "ddos-protection-enable.md") and
[Integrate player gateway into a game](ddos-protection-integrate.md "ddos-protection-integrate.md").
