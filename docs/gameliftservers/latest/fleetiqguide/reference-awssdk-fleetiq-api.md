

# Amazon GameLift Servers FleetIQ API actions
<a name="reference-awssdk-fleetiq-api"></a>

The following operations allow you to manage your Amazon GameLift Servers FleetIQ resources, including game server groups and game servers, in conjunction with Amazon EC2 and Auto Scaling groups.

## Manage game server groups
<a name="reference-awssdk-fleetiq-api-gsg"></a>

Use these operations to manage your game server deployments with FleetIQ optimizations. A game server group controls how your game server processes are launched on Amazon EC2 instances, sets up an Auto Scaling group, and defines how to apply FleetIQ optimizations.
+ [CreateGameServerGroup](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateGameServerGroup.html) – Create a new game server group and corresponding Auto Scaling group, and begin launching instances to host your game server. CLI command: [create-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/create-game-server-group.html)
+ [ListGameServerGroups](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListGameServerGroups.html) – Get a list of all game server groups in an Amazon GameLift Servers region. CLI command: [list-game-server-groups](https://docs.aws.amazon.com/cli/latest/reference/gamelift/list-game-server-groups.html)
+ [DescribeGameServerGroup](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameServerGroup.html) – Retrieve metadata for a game server group. CLI command: [describe-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-game-server-group.html)
+ [UpdateGameServerGroup](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameServerGroup.html) – Change game server group metadata. CLI command: [update-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/update-game-server-group.html)
+ [DeleteGameServerGroup](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteGameServerGroup.html) – Permanently remove a game server group and terminate FleetIQ activity for the associated hosting resources. CLI command: [delete-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/delete-game-server-group.html)
+ [ResumeGameServerGroup](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ResumeGameServerGroup.html) – Reinstate suspended FleetIQ activity for a game server group. CLI command: [resume-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/resume-game-server-group.html)
+ [SuspendGameServerGroup](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SuspendGameServerGroup.html) – Temporarily stop FleetIQ activity for a game server group. CLI command: [suspend-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/suspend-game-server-group.html)

## Manage game servers
<a name="reference-awssdk-fleetiq-api-gs"></a>

Use these operations to manage your game server deployments with FleetIQ optimizations. A game server group controls how your game server processes are launched on Amazon EC2 instances, sets up an Auto Scaling group, and defines how to apply FleetIQ optimizations.
+ [RegisterGameServer](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RegisterGameServer.html) – Call from a new game server to notify Amazon GameLift Servers FleetIQ that the game server is ready to host gameplay. CLI command: [register-game-server-group](https://docs.aws.amazon.com/cli/latest/reference/gamelift/register-game-server.html)
+ [ListGameServers](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListGameServers.html) – Call from a game client service to get a list of all game servers that are currently running in a game server group. CLI command: [list-game-servers](https://docs.aws.amazon.com/cli/latest/reference/gamelift/list-game-servers.html)
+ [ClaimGameServer](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ClaimGameServer.html) – Call from a game client service to locate and reserve a game server to host a new game session. CLI command: [claim-game-server](https://docs.aws.amazon.com/cli/latest/reference/gamelift/claim-game-server.html)
+ [DescribeGameServer](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameServer.html) – Retrieve metadata for a game server. CLI command: [describe-game-server](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-game-server.html)
+ [UpdateGameServer](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameServer.html) – Change game server metadata, health status, or utilization status. CLI command: [update-game-server](https://docs.aws.amazon.com/cli/latest/reference/gamelift/update-game-server.html)
+ [DeregisterGameServer](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeregisterGameServer.html) – Call from a terminating game server to prompt Amazon GameLift Servers FleetIQ to remove the game server from the game server group. CLI command: [deregister-game-server](https://docs.aws.amazon.com/cli/latest/reference/gamelift/deregister-game-server.html)