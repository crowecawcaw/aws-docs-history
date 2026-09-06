

# API limits reference
<a name="api-limits-common"></a>

The following table lists the default rate limits for Amazon GameLift Servers API operations. APIs marked with resource-level throttling may be subject to additional limits to prevent database hot key issues.


**API limits reference**  

| API action | Burst limit | Rate limit | Resource-level throttling | Notes | 
| --- | --- | --- | --- | --- | 
| AcceptMatch | 100 | 100 | No | Limit is per account. | 
| ClaimGameServer | 40 | 20 | No | Limit is per account. | 
| CreateAlias | 20 | 20 | No | Limit is per account. | 
| CreateBuild | 20 | 20 | No | Limit is per account. | 
| CreateContainerFleet | 4 | 1 | No | Limit is per account. | 
| CreateContainerGroupDefinition | 20 | 20 | No | Limit is per account. | 
| CreateFleet | 4 | 1 | No | Limit is per account. | 
| CreateFleetLocations | 20 | 20 | No | Limit is per account. | 
| CreateGameServerGroup | 20 | 20 | No | Limit is per account. | 
| CreateGameSession | 50 | 50 | No | Limit is per account. | 
| CreateGameSessionQueue | 20 | 20 | No | Limit is per account. | 
| CreateLocation | 20 | 20 | No | Limit is per account. | 
| CreateMatchmakingConfiguration | 20 | 20 | No | Limit is per account. | 
| CreateMatchmakingRuleSet | 20 | 20 | No | Limit is per account. | 
| CreatePlayerSession | 200 | 200 | No | Limit is per account. | 
| CreatePlayerSessions | 200 | 200 | No | Limit is per account. | 
| CreateScript | 20 | 20 | No | Limit is per account. | 
| CreateVpcPeeringAuthorization | 1 | 0.1 | No | Limit is per account. | 
| CreateVpcPeeringConnection | 1 | 0.1 | No | Limit is per account. | 
| DeleteAlias | 20 | 20 | No | Limit is per account. | 
| DeleteBuild | 20 | 20 | No | Limit is per account. | 
| DeleteContainerFleet | 20 | 20 | No | Limit is per account. | 
| DeleteContainerGroupDefinition | 20 | 20 | No | Limit is per account. | 
| DeleteFleet | 20 | 20 | No | Limit is per account. | 
| DeleteFleetLocations | 20 | 20 | No | Limit is per account. | 
| DeleteGameServerGroup | 20 | 20 | No | Limit is per account. | 
| DeleteGameSessionQueue | 20 | 20 | No | Limit is per account. | 
| DeleteLocation | 20 | 20 | No | Limit is per account. | 
| DeleteMatchmakingConfiguration | 20 | 20 | No | Limit is per account. | 
| DeleteMatchmakingRuleSet | 20 | 20 | No | Limit is per account. | 
| DeleteScalingPolicy | 20 | 20 | No | Limit is per account. | 
| DeleteScript | 20 | 20 | No | Limit is per account. | 
| DeleteVpcPeeringAuthorization | 1 | 0.1 | No | Limit is per account. | 
| DeleteVpcPeeringConnection | 1 | 0.1 | No | Limit is per account. | 
| DeregisterGameServer | 40 | 20 | No | Limit is per account. | 
| DeregisterCompute | 20 | 20 | No | Limit is per account. | 
| DescribeAlias | 30 | 30 | No | Limit is per account. | 
| DescribeBuild | 30 | 30 | No | Limit is per account. | 
| DescribeCompute | 30 | 30 | No | Limit is per account. | 
| DescribeContainerFleet | 30 | 30 | No | Limit is per account. | 
| DescribeContainerGroupDefinition | 30 | 30 | No | Limit is per account. | 
| DescribeContainerGroupPortMappings | 100 | 100 | No | Limit is per account. | 
| DescribeEC2InstanceLimits | 40 | 30 | No | Limit is per account. | 
| DescribeFleetAttributes | 30 | 30 | No | Limit is per account. | 
| DescribeFleetCapacity | 30 | 30 | No | Limit is per account. | 
| DescribeFleetDeployment | 30 | 30 | No | Limit is per account. | 
| DescribeFleetEvents | 30 | 30 | No | Limit is per account. | 
| DescribeFleetLocationAttributes | 30 | 30 | No | Limit is per account. | 
| DescribeFleetLocationCapacity | 30 | 30 | No | Limit is per account. | 
| DescribeFleetLocationUtilization | 30 | 30 | No | Limit is per account. | 
| DescribeFleetPortSettings | 30 | 30 | No | Limit is per account. | 
| DescribeFleetUtilization | 30 | 30 | No | Limit is per account. | 
| DescribeGameServer | 40 | 20 | No | Limit is per account. | 
| DescribeGameServerGroup | 30 | 30 | No | Limit is per account. | 
| DescribeGameServerInstances | 30 | 30 | No | Limit is per account. | 
| DescribeGameSessionDetails | 30 | 30 | No | Limit is per account. Consider using DescribeGameSessions instead as it has a higher default limit and supports resource level limits. | 
| DescribeGameSessionPlacement | 75 | 75 | Yes | Limit is per account. Subject to resource-level throttling. | 
| DescribeGameSessionQueues | 30 | 30 | No | Limit is per account. | 
| DescribeGameSessions | 20 | 20 | Yes | Limit is per account. Subject to resource-level throttling. | 
| DescribeInstances | 30 | 30 | No | Limit is per account. | 
| DescribeMatchmaking | 200 | 200 | Yes | Limit is per account. Subject to resource-level throttling. | 
| DescribeMatchmakingConfigurations | 30 | 30 | No | Limit is per account. | 
| DescribeMatchmakingRuleSets | 30 | 30 | No | Limit is per account. | 
| DescribePlayerSessions | 200 | 200 | Yes | Limit is per account. Subject to resource-level throttling. | 
| DescribeRuntimeConfiguration | 30 | 30 | No | Limit is per account. | 
| DescribeScalingPolicies | 30 | 30 | No | Limit is per account. | 
| DescribeScript | 30 | 30 | No | Limit is per account. | 
| DescribeVpcPeeringAuthorizations | 1 | 0.1 | No | Limit is per account. | 
| DescribeVpcPeeringConnections | 1 | 0.1 | No | Limit is per account. | 
| GetComputeAccess | 4 | 1 | No | Limit is per account. | 
| GetComputeAuthToken | 10 | 5 | No | Limit is per account. | 
| GetGameSessionLogUrl | 4 | 1 | No | Limit is per account. | 
| GetInstanceAccess | 4 | 1 | No | Limit is per account. | 
| ListAliases | 30 | 30 | No | Limit is per account. | 
| ListBuilds | 30 | 30 | No | Limit is per account. | 
| ListContainerFleets | 30 | 30 | No | Limit is per account. | 
| ListCompute | 30 | 30 | No | Limit is per account. | 
| ListContainerGroupDefinitions | 30 | 30 | No | Limit is per account. | 
| ListContainerGroupDefinitionVersions | 30 | 30 | No | Limit is per account. | 
| ListFleets | 30 | 30 | No | Limit is per account. | 
| ListFleetDeployments | 30 | 30 | No | Limit is per account. | 
| ListGameServerGroups | 30 | 30 | No | Limit is per account. | 
| ListGameServers | 30 | 30 | No | Limit is per account. | 
| ListLocations | 30 | 30 | No | Limit is per account. | 
| ListScripts | 30 | 30 | No | Limit is per account. | 
| ListTagsForResource | 30 | 30 | No | Limit is per account. | 
| PutScalingPolicy | 20 | 20 | No | Limit is per account. | 
| RegisterCompute | 20 | 20 | No | Limit is per account. | 
| RegisterGameServer | 40 | 20 | No | Limit is per account. | 
| RequestUploadCredentials | 4 | 1 | No | Limit is per account. | 
| ResolveAlias | 30 | 30 | No | Limit is per account. | 
| ResumeGameServerGroup | 1 | 0.1 | No | Limit is per account. | 
| SearchGameSessions | 30 | 30 | No | Limit is per account. | 
| StartFleetActions | 20 | 20 | No | Limit is per account. | 
| StartGameSessionPlacement | 75 | 75 | No | Limit is per account. | 
| StartMatchBackfill | 70 | 70 | No | Limit is per account. | 
| StartMatchmaking | 100 | 100 | No | Limit is per account. | 
| StopFleetActions | 20 | 20 | No | Limit is per account. | 
| StopGameSessionPlacement | 20 | 20 | No | Limit is per account. | 
| StopMatchmaking | 100 | 100 | No | Limit is per account. | 
| SuspendGameServerGroup | 1 | 0.1 | No | Limit is per account. | 
| TagResource | 30 | 30 | No | Limit is per account. | 
| TerminateGameSession | 20 | 20 | No | Limit is per account. | 
| UntagResource | 30 | 30 | No | Limit is per account. | 
| UpdateAlias | 20 | 20 | No | Limit is per account. | 
| UpdateBuild | 20 | 20 | No | Limit is per account. | 
| UpdateContainerGroupDefinition | 20 | 20 | No | Limit is per account. | 
| UpdateContainerFleet | 20 | 20 | No | Limit is per account. | 
| UpdateFleetAttributes | 20 | 20 | No | Limit is per account. | 
| UpdateFleetCapacity | 20 | 20 | No | Limit is per account. | 
| UpdateFleetPortSettings | 20 | 20 | No | Limit is per account. | 
| UpdateGameServer | 40 | 20 | No | Limit is per account. | 
| UpdateGameServerGroup | 20 | 20 | No | Limit is per account. | 
| UpdateGameSession | 20 | 20 | No | Limit is per account. | 
| UpdateGameSessionQueue | 20 | 20 | No | Limit is per account. | 
| UpdateMatchmakingConfiguration | 20 | 20 | No | Limit is per account. | 
| UpdateRuntimeConfiguration | 20 | 20 | No | Limit is per account. | 
| UpdateScript | 20 | 20 | No | Limit is per account. | 
| ValidateMatchmakingRuleSet | 30 | 30 | No | Limit is per account. | 