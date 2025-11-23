# Amazon GameLift Servers FleetIQ API actions

The following operations allow you to manage your Amazon GameLift Servers FleetIQ resources, including game
server groups and game servers, in conjunction with Amazon EC2 and Amazon EC2 Auto Scaling groups.

## Manage game server groups

Use these operations to manage your game server deployments with FleetIQ
optimizations. A game server group controls how your game server processes are
launched on Amazon EC2 instances, sets up and Amazon EC2 Auto Scaling group, and defines how to apply FleetIQ
optimizations.

- [CreateGameServerGroup](../../../gamelift/latest/apireference/API_CreateGameServerGroup.md "../../../gamelift/latest/apireference/API_CreateGameServerGroup.md") – Create a new game server group
  and corresponding Amazon EC2 Auto Scaling group, and begin launching instances to host your
  game server. CLI command: [create-game-server-group](../../../cli/latest/reference/gamelift/create-game-server-group.md "../../../cli/latest/reference/gamelift/create-game-server-group.md")
- [ListGameServerGroups](../../../gamelift/latest/apireference/API_ListGameServerGroups.md "../../../gamelift/latest/apireference/API_ListGameServerGroups.md") – Get a list of all game server
  groups in a Amazon GameLift Servers region. CLI command: [list-game-server-groups](../../../cli/latest/reference/gamelift/list-game-server-groups.md "../../../cli/latest/reference/gamelift/list-game-server-groups.md")
- [DescribeGameServerGroup](../../../gamelift/latest/apireference/API_DescribeGameServerGroup.md "../../../gamelift/latest/apireference/API_DescribeGameServerGroup.md") – Retrieve metadata for a game
  server group. CLI command: [describe-game-server-group](../../../cli/latest/reference/gamelift/describe-game-server-group.md "../../../cli/latest/reference/gamelift/describe-game-server-group.md")
- [UpdateGameServerGroup](../../../gamelift/latest/apireference/API_UpdateGameServerGroup.md "../../../gamelift/latest/apireference/API_UpdateGameServerGroup.md") – Change game server group
  metadata. CLI command: [update-game-server-group](../../../cli/latest/reference/gamelift/update-game-server-group.md "../../../cli/latest/reference/gamelift/update-game-server-group.md")
- [DeleteGameServerGroup](../../../gamelift/latest/apireference/API_DeleteGameServerGroup.md "../../../gamelift/latest/apireference/API_DeleteGameServerGroup.md") – Permanently remove a game server
  group and terminate FleetIQ activity for the associated hosting resources. CLI
  command: [delete-game-server-group](../../../cli/latest/reference/gamelift/delete-game-server-group.md "../../../cli/latest/reference/gamelift/delete-game-server-group.md")
- [ResumeGameServerGroup](../../../gamelift/latest/apireference/API_ResumeGameServerGroup.md "../../../gamelift/latest/apireference/API_ResumeGameServerGroup.md") – Reinstate suspended FleetIQ
  activity for a game server group. CLI command: [resume-game-server-group](../../../cli/latest/reference/gamelift/resume-game-server-group.md "../../../cli/latest/reference/gamelift/resume-game-server-group.md")
- [SuspendGameServerGroup](../../../gamelift/latest/apireference/API_SuspendGameServerGroup.md "../../../gamelift/latest/apireference/API_SuspendGameServerGroup.md") – Temporarily stop FleetIQ activity
  for a game server group. CLI command: [suspend-game-server-group](../../../cli/latest/reference/gamelift/suspend-game-server-group.md "../../../cli/latest/reference/gamelift/suspend-game-server-group.md")

## Manage game servers

Use these operations to manage your game server deployments with FleetIQ
optimizations. A game server group controls how your game server processes are
launched on Amazon EC2 instances, sets up and Amazon EC2 Auto Scaling group, and defines how to apply FleetIQ
optimizations.

- [RegisterGameServer](../../../gamelift/latest/apireference/API_RegisterGameServer.md "../../../gamelift/latest/apireference/API_RegisterGameServer.md") – Call from a new game server to
  notify Amazon GameLift Servers FleetIQ that the game server is ready to host gameplay. CLI command:
  [register-game-server-group](../../../cli/latest/reference/gamelift/register-game-server.md "../../../cli/latest/reference/gamelift/register-game-server.md")
- [ListGameServers](../../../gamelift/latest/apireference/API_ListGameServers.md "../../../gamelift/latest/apireference/API_ListGameServers.md")
  – Call from a game client service to get a list of all game servers
  that are currently running in a game server group. CLI command: [list-game-servers](../../../cli/latest/reference/gamelift/list-game-servers.md "../../../cli/latest/reference/gamelift/list-game-servers.md")
- [ClaimGameServer](../../../gamelift/latest/apireference/API_ClaimGameServer.md "../../../gamelift/latest/apireference/API_ClaimGameServer.md")
  – Call from a game client service to locate and reserve a game server
  to host a new game session. CLI command: [claim-game-server](../../../cli/latest/reference/gamelift/claim-game-server.md "../../../cli/latest/reference/gamelift/claim-game-server.md")
- [DescribeGameServer](../../../gamelift/latest/apireference/API_DescribeGameServer.md "../../../gamelift/latest/apireference/API_DescribeGameServer.md") – Retrieve metadata for a game
  server. CLI command: [describe-game-server](../../../cli/latest/reference/gamelift/describe-game-server.md "../../../cli/latest/reference/gamelift/describe-game-server.md")
- [UpdateGameServer](../../../gamelift/latest/apireference/API_UpdateGameServer.md "../../../gamelift/latest/apireference/API_UpdateGameServer.md") – Change game server metadata, health
  status, or utilization status. CLI command: [update-game-server](../../../cli/latest/reference/gamelift/update-game-server.md "../../../cli/latest/reference/gamelift/update-game-server.md")
- [DeregisterGameServer](../../../gamelift/latest/apireference/API_DeregisterGameServer.md "../../../gamelift/latest/apireference/API_DeregisterGameServer.md") – Call from a terminating game
  server to prompt Amazon GameLift Servers FleetIQ to remove the game server from the game server
  group. CLI command: [deregister-game-server](../../../cli/latest/reference/gamelift/deregister-game-server.md "../../../cli/latest/reference/gamelift/deregister-game-server.md")
