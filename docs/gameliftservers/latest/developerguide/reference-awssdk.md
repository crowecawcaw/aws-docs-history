# Service API for Amazon GameLift Servers

Use this task-based list to find API operations when building your Amazon GameLift Servers game hosting
solutions and other features. The AWS SDK includes these operations in the
`aws.gamelift` namespace. [Download the AWS SDK](https://aws.amazon.com/developer/tools/#SDKs "https://aws.amazon.com/developer/tools/#SDKs") or [view the Amazon GameLift Servers API reference
documentation](../apireference/Welcome.md "../apireference/Welcome.md"). You can also use the API with the AWS command line interface
(AWS CLI), as documented in the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html").

The API includes two sets of operations for managed game hosting:

- [Manage Amazon GameLift Servers hosting resources](#reference-awssdk-resources "#reference-awssdk-resources")
- [Start game sessions and join players](#reference-awssdk-sessions "#reference-awssdk-sessions")
  The Amazon GameLift Servers Service API also contains operations for use with other Amazon GameLift Servers tools and
  solutions. For a list of FleetIQ APIs, see [FleetIQ API operations](../../../gamelift/latest/fleetiqguide/reference-awssdk-fleetiq.md "../../../gamelift/latest/fleetiqguide/reference-awssdk-fleetiq.md"). For a list
  of FlexMatch APIs for matchmaking, see [FlexMatch API operations](../../../gamelift/latest/flexmatchguide/reference-awssdk-flex.md "../../../gamelift/latest/flexmatchguide/reference-awssdk-flex.md").

## Manage Amazon GameLift Servers hosting resources

Call these operations to configure hosting resources for your game servers, scale
capacity to meet player demand, get performance and usage metrics, and more. Use these
API operations when hosting game servers with Amazon GameLift Servers, including Amazon GameLift Servers Realtime. You can also work
in [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/") for most resource management tasks, or you can make calls with the
AWS Command Line Interface (AWS CLI) tool.

### Prepare game servers for

deployment

Upload and configure your game's game server code in preparation for deployment
and launching on hosting resources.

**Manage custom game server builds**

- [upload-build](../../../cli/latest/reference/gamelift/upload-build.md "../../../cli/latest/reference/gamelift/upload-build.md")
  – Upload build files from a local path and create a new Amazon GameLift Servers build
  resource. This operation, available as an AWS CLI command, is the most common
  way to upload game server builds.
- [CreateBuild](../../../gamelift/latest/apireference/API_CreateBuild.md "../../../gamelift/latest/apireference/API_CreateBuild.md") –
  Create a new build using files stored in an Amazon S3 bucket.
- [ListBuilds](../../../gamelift/latest/apireference/API_ListBuilds.md "../../../gamelift/latest/apireference/API_ListBuilds.md") –
  Get a list of all builds uploaded to an Amazon GameLift Servers region.
- [DescribeBuild](../../../gamelift/latest/apireference/API_DescribeBuild.md "../../../gamelift/latest/apireference/API_DescribeBuild.md")
  – Retrieve information associated with a build.
- [UpdateBuild](../../../gamelift/latest/apireference/API_UpdateBuild.md "../../../gamelift/latest/apireference/API_UpdateBuild.md") –
  Change build metadata, including build name and version.
- [DeleteBuild](../../../gamelift/latest/apireference/API_DeleteBuild.md "../../../gamelift/latest/apireference/API_DeleteBuild.md") –
  Remove a build from Amazon GameLift Servers.

**Manage Amazon GameLift Servers Realtime configuration scripts**

- [CreateScript](../../../gamelift/latest/apireference/API_CreateScript.md "../../../gamelift/latest/apireference/API_CreateScript.md")
  – Upload JavaScript files and create a new Amazon GameLift Servers script
  resource.
- [ListScripts](../../../gamelift/latest/apireference/API_ListScripts.md "../../../gamelift/latest/apireference/API_ListScripts.md") –
  Get a list of all Realtime scripts uploaded to an Amazon GameLift Servers region.
- [DescribeScript](../../../gamelift/latest/apireference/API_DescribeScript.md "../../../gamelift/latest/apireference/API_DescribeScript.md")
  – Retrieve information associated with a Realtime script.
- [UpdateScript](../../../gamelift/latest/apireference/API_UpdateScript.md "../../../gamelift/latest/apireference/API_UpdateScript.md")
  – Change script metadata and upload revised script content.
- [DeleteScript](../../../gamelift/latest/apireference/API_DeleteScript.md "../../../gamelift/latest/apireference/API_DeleteScript.md")
  – Remove a Realtime script from Amazon GameLift Servers.

### Set up computing resources for

hosting

Configure hosting resources and deploy them with your game server build or
Realtime configuration script.

**Create and manage fleets**

- [CreateFleet](../../../gamelift/latest/apireference/API_CreateFleet.md "../../../gamelift/latest/apireference/API_CreateFleet.md") –
  Configure and deploy a new Amazon GameLift Servers fleet of computing resources to run your
  game servers. Once deployed, game servers are automatically launched as
  configured and ready to host game sessions.
- [ListFleets](../../../gamelift/latest/apireference/API_ListFleets.md "../../../gamelift/latest/apireference/API_ListFleets.md") –
  Get a list of all fleets in an Amazon GameLift Servers region.
- [DeleteFleet](../../../gamelift/latest/apireference/API_DeleteFleet.md "../../../gamelift/latest/apireference/API_DeleteFleet.md") –
  Remove a fleet that's no longer running game servers or hosting
  players.
- View / update fleet locations.
  - [CreateFleetLocations](../../../gamelift/latest/apireference/API_CreateFleetLocations.md "../../../gamelift/latest/apireference/API_CreateFleetLocations.md") – Add remote locations to
    an existing fleet that supports multiple locations
  - [DescribeFleetLocationAttributes](../../../gamelift/latest/apireference/API_DescribeFleetLocationAttributes.md "../../../gamelift/latest/apireference/API_DescribeFleetLocationAttributes.md") – Get a list of
    all remote locations for a fleet and view the current status of each
    location.
  - [DeleteFleetLocations](../../../gamelift/latest/apireference/API_DeleteFleetLocations.md "../../../gamelift/latest/apireference/API_DeleteFleetLocations.md") – Remove remote locations
    from a fleet that supports multiple locations.

- View / update fleet configurations.
  - [DescribeFleetAttributes](../../../gamelift/latest/apireference/API_DescribeFleetAttributes.md "../../../gamelift/latest/apireference/API_DescribeFleetAttributes.md") / [UpdateFleetAttributes](../../../gamelift/latest/apireference/API_UpdateFleetAttributes.md "../../../gamelift/latest/apireference/API_UpdateFleetAttributes.md") – View or change a fleet's
    metadata and settings for game session protection and resource
    creation limits.
  - [DescribeFleetPortSettings](../../../gamelift/latest/apireference/API_DescribeFleetPortSettings.md "../../../gamelift/latest/apireference/API_DescribeFleetPortSettings.md") / [UpdateFleetPortSettings](../../../gamelift/latest/apireference/API_UpdateFleetPortSettings.md "../../../gamelift/latest/apireference/API_UpdateFleetPortSettings.md") – View or change the
    inbound permissions (IP address and port setting ranges) allowed for
    a fleet.
  - [DescribeRuntimeConfiguration](../../../gamelift/latest/apireference/API_DescribeRuntimeConfiguration.md "../../../gamelift/latest/apireference/API_DescribeRuntimeConfiguration.md") / [UpdateRuntimeConfiguration](../../../gamelift/latest/apireference/API_UpdateRuntimeConfiguration.md "../../../gamelift/latest/apireference/API_UpdateRuntimeConfiguration.md") – View or change what
    server processes (and how many) to run on each instance in a
    fleet.

**Manage fleet capacity**

- [DescribeEC2InstanceLimits](../../../gamelift/latest/apireference/API_DescribeEC2InstanceLimits.md "../../../gamelift/latest/apireference/API_DescribeEC2InstanceLimits.md") – Retrieve maximum number of
  instances allowed for the current AWS account and the current usage
  level.
- [DescribeFleetCapacity](../../../gamelift/latest/apireference/API_DescribeFleetCapacity.md "../../../gamelift/latest/apireference/API_DescribeFleetCapacity.md") – Retrieve the current capacity
  settings for a fleet's home Region.
- [DescribeFleetLocationCapacity](../../../gamelift/latest/apireference/API_DescribeFleetLocationCapacity.md "../../../gamelift/latest/apireference/API_DescribeFleetLocationCapacity.md") – Retrieve the current
  capacity settings for each location a multi-location fleet.
- [UpdateFleetCapacity](../../../gamelift/latest/apireference/API_UpdateFleetCapacity.md "../../../gamelift/latest/apireference/API_UpdateFleetCapacity.md") – Manually adjust capacity settings
  for a fleet.
- Set up :
  - [PutScalingPolicy](../../../gamelift/latest/apireference/API_PutScalingPolicy.md "../../../gamelift/latest/apireference/API_PutScalingPolicy.md") – Turn on target-based
    auto scaling or create a custom auto scaling policy, or update an
    existing policy.
  - [DescribeScalingPolicies](../../../gamelift/latest/apireference/API_DescribeScalingPolicies.md "../../../gamelift/latest/apireference/API_DescribeScalingPolicies.md") – Retrieve an existing
    auto scaling policy.
  - [DeleteScalingPolicy](../../../gamelift/latest/apireference/API_DeleteScalingPolicy.md "../../../gamelift/latest/apireference/API_DeleteScalingPolicy.md") – Delete an auto scaling
    policy and stop it from affecting a fleet's capacity.
  - [StartFleetActions](../../../gamelift/latest/apireference/API_StartFleetActions.md "../../../gamelift/latest/apireference/API_StartFleetActions.md") – Restart a fleet's
    auto scaling policies.
  - [StopFleetActions](../../../gamelift/latest/apireference/API_StopFleetActions.md "../../../gamelift/latest/apireference/API_StopFleetActions.md") – Suspend a fleet's
    auto scaling policies.

**Monitor fleet activity.**

- [DescribeFleetUtilization](../../../gamelift/latest/apireference/API_DescribeFleetUtilization.md "../../../gamelift/latest/apireference/API_DescribeFleetUtilization.md") – Retrieve statistics on the
  number of server processes, game sessions, and players that are currently
  active on a fleet.
- [DescribeFleetLocationUtilization](../../../gamelift/latest/apireference/API_DescribeFleetLocationUtilization.md "../../../gamelift/latest/apireference/API_DescribeFleetLocationUtilization.md") – Retrieve utilization
  statistics for each location in a multi-location fleet.
- [DescribeFleetEvents](../../../gamelift/latest/apireference/API_DescribeFleetEvents.md "../../../gamelift/latest/apireference/API_DescribeFleetEvents.md") – View logged events for a fleet
  during a specified time span.
- [DescribeGameSessions](../../../gamelift/latest/apireference/API_DescribeGameSessions.md "../../../gamelift/latest/apireference/API_DescribeGameSessions.md") – Retrieve game session metadata,
  including a game's running time and current player count.

### Set up queues for game session

placement

Set up multi-fleet, multi-region queues to place game sessions with the best
available hosting resources for cost, latency, and resiliency.

- [CreateGameSessionQueue](../../../gamelift/latest/apireference/API_CreateGameSessionQueue.md "../../../gamelift/latest/apireference/API_CreateGameSessionQueue.md") – Create a queue for use when
  processing requests for game session placements.
- [DescribeGameSessionQueues](../../../gamelift/latest/apireference/API_DescribeGameSessionQueues.md "../../../gamelift/latest/apireference/API_DescribeGameSessionQueues.md") – Retrieve game session queues
  defined in an Amazon GameLift Servers region.
- [UpdateGameSessionQueue](../../../gamelift/latest/apireference/API_UpdateGameSessionQueue.md "../../../gamelift/latest/apireference/API_UpdateGameSessionQueue.md") – Change the configuration of a
  game session queue.
- [DeleteGameSessionQueue](../../../gamelift/latest/apireference/API_DeleteGameSessionQueue.md "../../../gamelift/latest/apireference/API_DeleteGameSessionQueue.md") – Remove a game session queue
  from the region.

### Manage aliases

Use aliases to represent your fleets or create a terminal alternative destination.
Aliases are useful when transitioning game activity from one fleet to another, such
as during game server build updates.

- [CreateAlias](../../../gamelift/latest/apireference/API_CreateAlias.md "../../../gamelift/latest/apireference/API_CreateAlias.md") –
  Define a new alias and optionally assign it to a fleet.
- [ListAliases](../../../gamelift/latest/apireference/API_ListAliases.md "../../../gamelift/latest/apireference/API_ListAliases.md") –
  Get all fleet aliases defined in an Amazon GameLift Servers region.
- [DescribeAlias](../../../gamelift/latest/apireference/API_DescribeAlias.md "../../../gamelift/latest/apireference/API_DescribeAlias.md")
  – Retrieve information on an existing alias.
- [UpdateAlias](../../../gamelift/latest/apireference/API_UpdateAlias.md "../../../gamelift/latest/apireference/API_UpdateAlias.md") –
  Change settings for an alias, such as redirecting it from one fleet to
  another.
- [DeleteAlias](../../../gamelift/latest/apireference/API_DeleteAlias.md "../../../gamelift/latest/apireference/API_DeleteAlias.md") –
  Remove an alias from the region.
- [ResolveAlias](../../../gamelift/latest/apireference/API_ResolveAlias.md "../../../gamelift/latest/apireference/API_ResolveAlias.md")
  – Get the fleet ID that a specified alias points to.

### Connect to managed hosting

instances

View information on individual instances in a fleet, or request remote access to a
specified fleet instance for troubleshooting.

- [DescribeInstances](../../../gamelift/latest/apireference/API_DescribeInstances.md "../../../gamelift/latest/apireference/API_DescribeInstances.md") – Get information on each instance in
  a fleet, including instance ID, IP address, location, and status.
- [GetInstanceAccess](../../../gamelift/latest/apireference/API_GetInstanceAccess.md "../../../gamelift/latest/apireference/API_GetInstanceAccess.md") – Request access credentials needed to
  remotely connect to a specified instance in a fleet.

### Set up VPC peering

Create and manage VPC peering connections between your Amazon GameLift Servers hosting resources and
other AWS resources.

- [CreateVpcPeeringAuthorization](../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md") – Authorize a peering
  connection to one of your VPCs.
- [DescribeVpcPeeringAuthorizations](../../../gamelift/latest/apireference/API_DescribeVpcPeeringAuthorizations.md "../../../gamelift/latest/apireference/API_DescribeVpcPeeringAuthorizations.md") – Retrieve valid
  peering connection authorizations.
- [DeleteVpcPeeringAuthorization](../../../gamelift/latest/apireference/API_DeleteVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_DeleteVpcPeeringAuthorization.md") – Delete a peering
  connection authorization.
- [CreateVpcPeeringConnection](../../../gamelift/latest/apireference/API_CreateVpcPeeringConnection.md "../../../gamelift/latest/apireference/API_CreateVpcPeeringConnection.md") – Establish a peering
  connection between the VPC for an Amazon GameLift Servers fleet and one of your VPCs.
- [DescribeVpcPeeringConnections](../../../gamelift/latest/apireference/API_DescribeVpcPeeringConnections.md "../../../gamelift/latest/apireference/API_DescribeVpcPeeringConnections.md") – Retrieve information on
  active or pending VPC peering connections with an Amazon GameLift Servers fleet.
- [DeleteVpcPeeringConnection](../../../gamelift/latest/apireference/API_DeleteVpcPeeringConnection.md "../../../gamelift/latest/apireference/API_DeleteVpcPeeringConnection.md") – Delete a VPC peering
  connection with an Amazon GameLift Servers fleet.

## Start game sessions and join players

Call these operations from a backend service to start new game sessions, get
information on existing game sessions, and join players to game sessions. These
operations are for use with custom game servers that are hosted on Amazon GameLift Servers. If you're
using Amazon GameLift Servers Realtime, manage game sessions using the
[Amazon GameLift Servers Realtime client API (C#)](../realtimeguide/realtime-sdk-csharp-ref.md "../realtimeguide/realtime-sdk-csharp-ref.md").

- **Start new game sessions for one or more
  players.**
  - [StartGameSessionPlacement](../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md") – Ask Amazon GameLift Servers to find the
    best available hosting resources and start a new game session. This is
    the preferred method for creating new game sessions. It relies on game
    session queues to track hosting availability across multiple regions,
    and uses FleetIQ algorithms to prioritize placements based on player
    latency, hosting cost, location, etc.
  - [DescribeGameSessionPlacement](../../../gamelift/latest/apireference/API_DescribeGameSessionPlacement.md "../../../gamelift/latest/apireference/API_DescribeGameSessionPlacement.md") – Get details and
    status on a placement request.
  - [StopGameSessionPlacement](../../../gamelift/latest/apireference/API_StopGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StopGameSessionPlacement.md") – Cancel a placement
    request.
  - [CreateGameSession](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md") – Start a new, empty game session
    on a specific fleet location. This operation gives you greater control
    over where to start the game session, instead of using FleetIQ to evaluate
    placement options. You must add players to the new game session in a
    separate step.

- **Get players into existing game sessions.** Find
  running game sessions with available player slots and reserve them for new
  players.
  - [CreatePlayerSession](../../../gamelift/latest/apireference/API_CreatePlayerSession.md "../../../gamelift/latest/apireference/API_CreatePlayerSession.md") – Reserve an open slot for a
    player to join a game session.
  - [CreatePlayerSessions](../../../gamelift/latest/apireference/API_CreatePlayerSessions.md "../../../gamelift/latest/apireference/API_CreatePlayerSessions.md") – Reserve open slots for
    multiple players to join a game session.

- **Work with game session and player session
  data.** Manage information on game sessions and player
  sessions.
  - [SearchGameSessions](../../../gamelift/latest/apireference/API_SearchGameSessions.md "../../../gamelift/latest/apireference/API_SearchGameSessions.md") – Request a list of active game
    sessions based on a set of search criteria.
  - [DescribeGameSessions](../../../gamelift/latest/apireference/API_DescribeGameSessions.md "../../../gamelift/latest/apireference/API_DescribeGameSessions.md") – Retrieve metadata for
    specific game sessions, including length of time active and current
    player count.
  - [DescribeGameSessionDetails](../../../gamelift/latest/apireference/API_DescribeGameSessionDetails.md "../../../gamelift/latest/apireference/API_DescribeGameSessionDetails.md") – Retrieve metadata,
    including the game session protection setting, for one or more game
    sessions.
  - [DescribePlayerSessions](../../../gamelift/latest/apireference/API_DescribePlayerSessions.md "../../../gamelift/latest/apireference/API_DescribePlayerSessions.md") – Get details on player
    activity, including status, playing time, and player data.
  - [UpdateGameSession](../../../gamelift/latest/apireference/API_UpdateGameSession.md "../../../gamelift/latest/apireference/API_UpdateGameSession.md") – Change game session settings,
    such as maximum player count and join policy.
  - [GetGameSessionLogUrl](../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md "../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md") – Get the location of saved
    logs for a game session.
