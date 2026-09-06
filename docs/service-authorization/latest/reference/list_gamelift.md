

# Actions, resources, and condition keys for Amazon GameLift Servers
<a name="list_gamelift"></a>

Amazon GameLift Servers (service prefix: `gamelift`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-intro.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/gameliftservers/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/gamelift/gamelift.json) for this service.

**Topics**
+ [API operations defined by Amazon GameLift Servers](#list_gamelift-operations)
+ [Actions defined by Amazon GameLift Servers](#list_gamelift-actions-as-permissions)
+ [Resource types defined by Amazon GameLift Servers](#list_gamelift-resources-for-iam-policies)
+ [Condition keys for Amazon GameLift Servers](#list_gamelift-policy-keys)

## API operations defined by Amazon GameLift Servers
<a name="list_gamelift-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_gamelift-actions-as-permissions).




- **   AcceptMatch  **
  - **IAM action:**  [gamelift:AcceptMatch](#list_gamelift-action-AcceptMatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ClaimGameServer  **
  - **IAM action:**  [gamelift:ClaimGameServer](#list_gamelift-action-ClaimGameServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAlias  **
  - **IAM action:**  [gamelift:CreateAlias](#list_gamelift-action-CreateAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateBuild  **
  - **IAM action:**  [gamelift:CreateBuild](#list_gamelift-action-CreateBuild)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateBuild](#list_gamelift-action-CreateBuild)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   CreateContainerFleet  **
  - **IAM action:**  [gamelift:CreateContainerFleet](#list_gamelift-action-CreateContainerFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateContainerFleet](#list_gamelift-action-CreateContainerFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   CreateContainerGroupDefinition  **
  - **IAM action:**  [gamelift:CreateContainerGroupDefinition](#list_gamelift-action-CreateContainerGroupDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateContainerGroupDefinition](#list_gamelift-action-CreateContainerGroupDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFleet  **
  - **IAM action:**  [gamelift:CreateFleet](#list_gamelift-action-CreateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateFleet](#list_gamelift-action-CreateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   CreateFleetLocations  **
  - **IAM action:**  [gamelift:CreateFleetLocations](#list_gamelift-action-CreateFleetLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGameServerGroup  **
  - **IAM action:**  [gamelift:CreateGameServerGroup](#list_gamelift-action-CreateGameServerGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateGameServerGroup](#list_gamelift-action-CreateGameServerGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   CreateGameSession  **
  - **IAM action:**  [gamelift:CreateGameSession](#list_gamelift-action-CreateGameSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGameSessionQueue  **
  - **IAM action:**  [gamelift:CreateGameSessionQueue](#list_gamelift-action-CreateGameSessionQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateGameSessionQueue](#list_gamelift-action-CreateGameSessionQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLocation  **
  - **IAM action:**  [gamelift:CreateLocation](#list_gamelift-action-CreateLocation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMatchmakingConfiguration  **
  - **IAM action:**  [gamelift:CreateMatchmakingConfiguration](#list_gamelift-action-CreateMatchmakingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateMatchmakingConfiguration](#list_gamelift-action-CreateMatchmakingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMatchmakingRuleSet  **
  - **IAM action:**  [gamelift:CreateMatchmakingRuleSet](#list_gamelift-action-CreateMatchmakingRuleSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateMatchmakingRuleSet](#list_gamelift-action-CreateMatchmakingRuleSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePlayerSession  **
  - **IAM action:**  [gamelift:CreatePlayerSession](#list_gamelift-action-CreatePlayerSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePlayerSessions  **
  - **IAM action:**  [gamelift:CreatePlayerSessions](#list_gamelift-action-CreatePlayerSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateScript  **
  - **IAM action:**  [gamelift:CreateScript](#list_gamelift-action-CreateScript)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:CreateScript](#list_gamelift-action-CreateScript)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   CreateVpcPeeringAuthorization  **
  - **IAM action:**  [gamelift:CreateVpcPeeringAuthorization](#list_gamelift-action-CreateVpcPeeringAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVpcPeeringConnection  **
  - **IAM action:**  [gamelift:CreateVpcPeeringConnection](#list_gamelift-action-CreateVpcPeeringConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAlias  **
  - **IAM action:**  [gamelift:DeleteAlias](#list_gamelift-action-DeleteAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBuild  **
  - **IAM action:**  [gamelift:DeleteBuild](#list_gamelift-action-DeleteBuild) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContainerFleet  **
  - **IAM action:**  [gamelift:DeleteContainerFleet](#list_gamelift-action-DeleteContainerFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContainerGroupDefinition  **
  - **IAM action:**  [gamelift:DeleteContainerGroupDefinition](#list_gamelift-action-DeleteContainerGroupDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleet  **
  - **IAM action:**  [gamelift:DeleteFleet](#list_gamelift-action-DeleteFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleetLocations  **
  - **IAM action:**  [gamelift:DeleteFleetLocations](#list_gamelift-action-DeleteFleetLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGameServerGroup  **
  - **IAM action:**  [gamelift:DeleteGameServerGroup](#list_gamelift-action-DeleteGameServerGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGameSessionQueue  **
  - **IAM action:**  [gamelift:DeleteGameSessionQueue](#list_gamelift-action-DeleteGameSessionQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLocation  **
  - **IAM action:**  [gamelift:DeleteLocation](#list_gamelift-action-DeleteLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMatchmakingConfiguration  **
  - **IAM action:**  [gamelift:DeleteMatchmakingConfiguration](#list_gamelift-action-DeleteMatchmakingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMatchmakingRuleSet  **
  - **IAM action:**  [gamelift:DeleteMatchmakingRuleSet](#list_gamelift-action-DeleteMatchmakingRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScalingPolicy  **
  - **IAM action:**  [gamelift:DeleteScalingPolicy](#list_gamelift-action-DeleteScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScript  **
  - **IAM action:**  [gamelift:DeleteScript](#list_gamelift-action-DeleteScript) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcPeeringAuthorization  **
  - **IAM action:**  [gamelift:DeleteVpcPeeringAuthorization](#list_gamelift-action-DeleteVpcPeeringAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcPeeringConnection  **
  - **IAM action:**  [gamelift:DeleteVpcPeeringConnection](#list_gamelift-action-DeleteVpcPeeringConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterCompute  **
  - **IAM action:**  [gamelift:DeregisterCompute](#list_gamelift-action-DeregisterCompute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterGameServer  **
  - **IAM action:**  [gamelift:DeregisterGameServer](#list_gamelift-action-DeregisterGameServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAlias  **
  - **IAM action:**  [gamelift:DescribeAlias](#list_gamelift-action-DescribeAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBuild  **
  - **IAM action:**  [gamelift:DescribeBuild](#list_gamelift-action-DescribeBuild) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCompute  **
  - **IAM action:**  [gamelift:DescribeCompute](#list_gamelift-action-DescribeCompute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContainerFleet  **
  - **IAM action:**  [gamelift:DescribeContainerFleet](#list_gamelift-action-DescribeContainerFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContainerGroupDefinition  **
  - **IAM action:**  [gamelift:DescribeContainerGroupDefinition](#list_gamelift-action-DescribeContainerGroupDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContainerGroupPortMappings  **
  - **IAM action:**  [gamelift:DescribeContainerGroupPortMappings](#list_gamelift-action-DescribeContainerGroupPortMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEC2InstanceLimits  **
  - **IAM action:**  [gamelift:DescribeEC2InstanceLimits](#list_gamelift-action-DescribeEC2InstanceLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetAttributes  **
  - **IAM action:**  [gamelift:DescribeFleetAttributes](#list_gamelift-action-DescribeFleetAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetCapacity  **
  - **IAM action:**  [gamelift:DescribeFleetCapacity](#list_gamelift-action-DescribeFleetCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetDeployment  **
  - **IAM action:**  [gamelift:DescribeFleetDeployment](#list_gamelift-action-DescribeFleetDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetEvents  **
  - **IAM action:**  [gamelift:DescribeFleetEvents](#list_gamelift-action-DescribeFleetEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetLocationAttributes  **
  - **IAM action:**  [gamelift:DescribeFleetLocationAttributes](#list_gamelift-action-DescribeFleetLocationAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetLocationCapacity  **
  - **IAM action:**  [gamelift:DescribeFleetLocationCapacity](#list_gamelift-action-DescribeFleetLocationCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetLocationUtilization  **
  - **IAM action:**  [gamelift:DescribeFleetLocationUtilization](#list_gamelift-action-DescribeFleetLocationUtilization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetPortSettings  **
  - **IAM action:**  [gamelift:DescribeFleetPortSettings](#list_gamelift-action-DescribeFleetPortSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetUtilization  **
  - **IAM action:**  [gamelift:DescribeFleetUtilization](#list_gamelift-action-DescribeFleetUtilization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameServer  **
  - **IAM action:**  [gamelift:DescribeGameServer](#list_gamelift-action-DescribeGameServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameServerGroup  **
  - **IAM action:**  [gamelift:DescribeGameServerGroup](#list_gamelift-action-DescribeGameServerGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameServerInstances  **
  - **IAM action:**  [gamelift:DescribeGameServerInstances](#list_gamelift-action-DescribeGameServerInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameSessionDetails  **
  - **IAM action:**  [gamelift:DescribeGameSessionDetails](#list_gamelift-action-DescribeGameSessionDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameSessionPlacement  **
  - **IAM action:**  [gamelift:DescribeGameSessionPlacement](#list_gamelift-action-DescribeGameSessionPlacement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameSessionQueues  **
  - **IAM action:**  [gamelift:DescribeGameSessionQueues](#list_gamelift-action-DescribeGameSessionQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGameSessions  **
  - **IAM action:**  [gamelift:DescribeGameSessions](#list_gamelift-action-DescribeGameSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstances  **
  - **IAM action:**  [gamelift:DescribeInstances](#list_gamelift-action-DescribeInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMatchmaking  **
  - **IAM action:**  [gamelift:DescribeMatchmaking](#list_gamelift-action-DescribeMatchmaking) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMatchmakingConfigurations  **
  - **IAM action:**  [gamelift:DescribeMatchmakingConfigurations](#list_gamelift-action-DescribeMatchmakingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMatchmakingRuleSets  **
  - **IAM action:**  [gamelift:DescribeMatchmakingRuleSets](#list_gamelift-action-DescribeMatchmakingRuleSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePlayerSessions  **
  - **IAM action:**  [gamelift:DescribePlayerSessions](#list_gamelift-action-DescribePlayerSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuntimeConfiguration  **
  - **IAM action:**  [gamelift:DescribeRuntimeConfiguration](#list_gamelift-action-DescribeRuntimeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScalingPolicies  **
  - **IAM action:**  [gamelift:DescribeScalingPolicies](#list_gamelift-action-DescribeScalingPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScript  **
  - **IAM action:**  [gamelift:DescribeScript](#list_gamelift-action-DescribeScript) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVpcPeeringAuthorizations  **
  - **IAM action:**  [gamelift:DescribeVpcPeeringAuthorizations](#list_gamelift-action-DescribeVpcPeeringAuthorizations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVpcPeeringConnections  **
  - **IAM action:**  [gamelift:DescribeVpcPeeringConnections](#list_gamelift-action-DescribeVpcPeeringConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComputeAccess  **
  - **IAM action:**  [gamelift:GetComputeAccess](#list_gamelift-action-GetComputeAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComputeAuthToken  **
  - **IAM action:**  [gamelift:GetComputeAuthToken](#list_gamelift-action-GetComputeAuthToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGameSessionLogUrl  **
  - **IAM action:**  [gamelift:GetGameSessionLogUrl](#list_gamelift-action-GetGameSessionLogUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstanceAccess  **
  - **IAM action:**  [gamelift:GetInstanceAccess](#list_gamelift-action-GetInstanceAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlayerConnectionDetails  **
  - **IAM action:**  [gamelift:GetPlayerConnectionDetails](#list_gamelift-action-GetPlayerConnectionDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAliases  **
  - **IAM action:**  [gamelift:ListAliases](#list_gamelift-action-ListAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBuilds  **
  - **IAM action:**  [gamelift:ListBuilds](#list_gamelift-action-ListBuilds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCompute  **
  - **IAM action:**  [gamelift:ListCompute](#list_gamelift-action-ListCompute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContainerFleets  **
  - **IAM action:**  [gamelift:ListContainerFleets](#list_gamelift-action-ListContainerFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContainerGroupDefinitionVersions  **
  - **IAM action:**  [gamelift:ListContainerGroupDefinitionVersions](#list_gamelift-action-ListContainerGroupDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContainerGroupDefinitions  **
  - **IAM action:**  [gamelift:ListContainerGroupDefinitions](#list_gamelift-action-ListContainerGroupDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFleetDeployments  **
  - **IAM action:**  [gamelift:ListFleetDeployments](#list_gamelift-action-ListFleetDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFleets  **
  - **IAM action:**  [gamelift:ListFleets](#list_gamelift-action-ListFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGameServerGroups  **
  - **IAM action:**  [gamelift:ListGameServerGroups](#list_gamelift-action-ListGameServerGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGameServers  **
  - **IAM action:**  [gamelift:ListGameServers](#list_gamelift-action-ListGameServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLocations  **
  - **IAM action:**  [gamelift:ListLocations](#list_gamelift-action-ListLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScripts  **
  - **IAM action:**  [gamelift:ListScripts](#list_gamelift-action-ListScripts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [gamelift:ListTagsForResource](#list_gamelift-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutScalingPolicy  **
  - **IAM action:**  [gamelift:PutScalingPolicy](#list_gamelift-action-PutScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterCompute  **
  - **IAM action:**  [gamelift:RegisterCompute](#list_gamelift-action-RegisterCompute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterGameServer  **
  - **IAM action:**  [gamelift:RegisterGameServer](#list_gamelift-action-RegisterGameServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RequestUploadCredentials  **
  - **IAM action:**  [gamelift:RequestUploadCredentials](#list_gamelift-action-RequestUploadCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResolveAlias  **
  - **IAM action:**  [gamelift:ResolveAlias](#list_gamelift-action-ResolveAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResumeGameServerGroup  **
  - **IAM action:**  [gamelift:ResumeGameServerGroup](#list_gamelift-action-ResumeGameServerGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchGameSessions  **
  - **IAM action:**  [gamelift:SearchGameSessions](#list_gamelift-action-SearchGameSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartFleetActions  **
  - **IAM action:**  [gamelift:StartFleetActions](#list_gamelift-action-StartFleetActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartGameSessionPlacement  **
  - **IAM action:**  [gamelift:StartGameSessionPlacement](#list_gamelift-action-StartGameSessionPlacement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMatchBackfill  **
  - **IAM action:**  [gamelift:StartMatchBackfill](#list_gamelift-action-StartMatchBackfill) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMatchmaking  **
  - **IAM action:**  [gamelift:StartMatchmaking](#list_gamelift-action-StartMatchmaking) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopFleetActions  **
  - **IAM action:**  [gamelift:StopFleetActions](#list_gamelift-action-StopFleetActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopGameSessionPlacement  **
  - **IAM action:**  [gamelift:StopGameSessionPlacement](#list_gamelift-action-StopGameSessionPlacement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMatchmaking  **
  - **IAM action:**  [gamelift:StopMatchmaking](#list_gamelift-action-StopMatchmaking) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SuspendGameServerGroup  **
  - **IAM action:**  [gamelift:SuspendGameServerGroup](#list_gamelift-action-SuspendGameServerGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [gamelift:TagResource](#list_gamelift-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TerminateGameSession  **
  - **IAM action:**  [gamelift:TerminateGameSession](#list_gamelift-action-TerminateGameSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [gamelift:UntagResource](#list_gamelift-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [gamelift:UntagResource](#list_gamelift-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateAlias  **
  - **IAM action:**  [gamelift:UpdateAlias](#list_gamelift-action-UpdateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBuild  **
  - **IAM action:**  [gamelift:UpdateBuild](#list_gamelift-action-UpdateBuild) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContainerFleet  **
  - **IAM action:**  [gamelift:UpdateContainerFleet](#list_gamelift-action-UpdateContainerFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContainerGroupDefinition  **
  - **IAM action:**  [gamelift:UpdateContainerGroupDefinition](#list_gamelift-action-UpdateContainerGroupDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleetAttributes  **
  - **IAM action:**  [gamelift:UpdateFleetAttributes](#list_gamelift-action-UpdateFleetAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleetCapacity  **
  - **IAM action:**  [gamelift:UpdateFleetCapacity](#list_gamelift-action-UpdateFleetCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleetPortSettings  **
  - **IAM action:**  [gamelift:UpdateFleetPortSettings](#list_gamelift-action-UpdateFleetPortSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGameServer  **
  - **IAM action:**  [gamelift:UpdateGameServer](#list_gamelift-action-UpdateGameServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGameServerGroup  **
  - **IAM action:**  [gamelift:UpdateGameServerGroup](#list_gamelift-action-UpdateGameServerGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   UpdateGameSession  **
  - **IAM action:**  [gamelift:UpdateGameSession](#list_gamelift-action-UpdateGameSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGameSessionQueue  **
  - **IAM action:**  [gamelift:UpdateGameSessionQueue](#list_gamelift-action-UpdateGameSessionQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMatchmakingConfiguration  **
  - **IAM action:**  [gamelift:UpdateMatchmakingConfiguration](#list_gamelift-action-UpdateMatchmakingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuntimeConfiguration  **
  - **IAM action:**  [gamelift:UpdateRuntimeConfiguration](#list_gamelift-action-UpdateRuntimeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScript  **
  - **IAM action:**  [gamelift:UpdateScript](#list_gamelift-action-UpdateScript)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gamelift.amazonaws.com / **Access level:** Write

- **   ValidateMatchmakingRuleSet  **
  - **IAM action:**  [gamelift:ValidateMatchmakingRuleSet](#list_gamelift-action-ValidateMatchmakingRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon GameLift Servers
<a name="list_gamelift-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptMatch](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AcceptMatch.html)  **
  - **Description:** Grants permission to register player acceptance or rejection of a proposed FlexMatch match
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ClaimGameServer](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ClaimGameServer.html)  **
  - **Description:** Grants permission to locate and reserve a game server to host a new game session
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAlias](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateAlias.html)  **
  - **Description:** Grants permission to define a new alias for a fleet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBuild](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateBuild.html)  **
  - **Description:** Grants permission to create a new game build using files stored in an Amazon S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContainerFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateContainerFleet.html)  **
  - **Description:** Grants permission to create a new container fleet of computing resources to run your game servers
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateContainerGroupDefinition.html)  **
  - **Description:** Grants permission to create a new container group definition using images stored in an Amazon ECR repository
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateFleet.html)  **
  - **Description:** Grants permission to create a new fleet of computing resources to run your game servers
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFleetLocations](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateFleetLocations.html)  **
  - **Description:** Grants permission to specify additional locations for a fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameServerGroup.html)  **
  - **Description:** Grants permission to create a new game server group, set up a corresponding Auto Scaling group, and launche instances to host game servers
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSession.html)  **
  - **Description:** Grants permission to start a new game session on a specified fleet
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGameSessionQueue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSessionQueue.html)  **
  - **Description:** Grants permission to set up a new queue for processing game session placement requests
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocation](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateLocation.html)  **
  - **Description:** Grants permission to define a new location for a fleet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMatchmakingConfiguration](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateMatchmakingConfiguration.html)  **
  - **Description:** Grants permission to create a new FlexMatch matchmaker
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMatchmakingRuleSet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateMatchmakingRuleSet.html)  **
  - **Description:** Grants permission to create a new matchmaking rule set for FlexMatch
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePlayerSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreatePlayerSession.html)  **
  - **Description:** Grants permission to reserve an available game session slot for a player
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePlayerSessions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreatePlayerSessions.html)  **
  - **Description:** Grants permission to reserve available game session slots for multiple players
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateScript](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateScript.html)  **
  - **Description:** Grants permission to create a new Realtime Servers script
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVpcPeeringAuthorization](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateVpcPeeringAuthorization.html)  **
  - **Description:** Grants permission to allow GameLift to create or delete a peering connection between a GameLift fleet VPC and a VPC on another AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVpcPeeringConnection](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateVpcPeeringConnection.html)  **
  - **Description:** Grants permission to establish a peering connection between your GameLift fleet VPC and a VPC on another account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAlias](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteAlias.html)  **
  - **Description:** Grants permission to delete an alias
  - **Resource types (\*required):** [alias\*](#list_gamelift-resource-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBuild](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteBuild.html)  **
  - **Description:** Grants permission to delete a game build
  - **Resource types (\*required):** [build\*](#list_gamelift-resource-build)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContainerFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteContainerFleet.html)  **
  - **Description:** Grants permission to delete a container fleet
  - **Resource types (\*required):** [containerFleet\*](#list_gamelift-resource-containerFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContainerGroupDefinition](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteContainerGroupDefinition.html)  **
  - **Description:** Grants permission to delete a container group definition
  - **Resource types (\*required):** [containerGroupDefinition\*](#list_gamelift-resource-containerGroupDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteFleet.html)  **
  - **Description:** Grants permission to delete an empty fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleetLocations](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteFleetLocations.html)  **
  - **Description:** Grants permission to delete locations for a fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteGameServerGroup.html)  **
  - **Description:** Grants permission to permanently delete a game server group and terminate FleetIQ activity for the corresponding Auto Scaling group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGameSessionQueue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteGameSessionQueue.html)  **
  - **Description:** Grants permission to delete an existing game session queue
  - **Resource types (\*required):** [gameSessionQueue\*](#list_gamelift-resource-gameSessionQueue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLocation](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteLocation.html)  **
  - **Description:** Grants permission to delete a location
  - **Resource types (\*required):** [location\*](#list_gamelift-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMatchmakingConfiguration](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteMatchmakingConfiguration.html)  **
  - **Description:** Grants permission to delete an existing FlexMatch matchmaker
  - **Resource types (\*required):** [matchmakingConfiguration\*](#list_gamelift-resource-matchmakingConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMatchmakingRuleSet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteMatchmakingRuleSet.html)  **
  - **Description:** Grants permission to delete an existing FlexMatch matchmaking rule set
  - **Resource types (\*required):** [matchmakingRuleSet\*](#list_gamelift-resource-matchmakingRuleSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScalingPolicy](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteScalingPolicy.html)  **
  - **Description:** Grants permission to delete a set of auto-scaling rules
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScript](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteScript.html)  **
  - **Description:** Grants permission to delete a Realtime Servers script
  - **Resource types (\*required):** [script\*](#list_gamelift-resource-script)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVpcPeeringAuthorization](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteVpcPeeringAuthorization.html)  **
  - **Description:** Grants permission to cancel a VPC peering authorization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVpcPeeringConnection](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteVpcPeeringConnection.html)  **
  - **Description:** Grants permission to remove a peering connection between VPCs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeregisterCompute.html)  **
  - **Description:** Grants permission to deregister a compute against a fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterGameServer](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeregisterGameServer.html)  **
  - **Description:** Grants permission to remove a game server from a game server group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAlias](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeAlias.html)  **
  - **Description:** Grants permission to retrieve properties for an alias
  - **Resource types (\*required):** [alias\*](#list_gamelift-resource-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBuild](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeBuild.html)  **
  - **Description:** Grants permission to retrieve properties for a game build
  - **Resource types (\*required):** [build\*](#list_gamelift-resource-build)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeCompute.html)  **
  - **Description:** Grants permission to retrieve information for a compute in a fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeContainerFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerFleet.html)  **
  - **Description:** Grants permission to retrieve the properties of an existing container fleet
  - **Resource types (\*required):** [containerFleet\*](#list_gamelift-resource-containerFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerGroupDefinition.html)  **
  - **Description:** Grants permission to retrieve the properties of an existing container group definition
  - **Resource types (\*required):** [containerGroupDefinition\*](#list_gamelift-resource-containerGroupDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeContainerGroupPortMappings](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerGroupPortMappings.html)  **
  - **Description:** Grants permission to retrieve container port mappings for a container fleet
  - **Resource types (\*required):** [containerFleet\*](#list_gamelift-resource-containerFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEC2InstanceLimits](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeEC2InstanceLimits.html)  **
  - **Description:** Grants permission to retrieve the maximum allowed and current usage for EC2 instance types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetAttributes](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetAttributes.html)  **
  - **Description:** Grants permission to retrieve general properties, including status, for fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetCapacity](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetCapacity.html)  **
  - **Description:** Grants permission to retrieve the current capacity settings for managed fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetDeployment](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetDeployment.html)  **
  - **Description:** Grants permission to retrieve the properties of an existing fleet deployment
  - **Resource types (\*required):** [containerFleet\*](#list_gamelift-resource-containerFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetEvents](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetEvents.html)  **
  - **Description:** Grants permission to retrieve entries from a fleet's event log
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetLocationAttributes](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetLocationAttributes.html)  **
  - **Description:** Grants permission to retrieve general properties, including statuses, for a fleet's locations
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetLocationCapacity.html)  **
  - **Description:** Grants permission to retrieve the current capacity setting for a fleet's location
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetLocationUtilization](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetLocationUtilization.html)  **
  - **Description:** Grants permission to retrieve utilization statistics for fleet's location
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetPortSettings](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetPortSettings.html)  **
  - **Description:** Grants permission to retrieve the inbound connection permissions for a fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetUtilization](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetUtilization.html)  **
  - **Description:** Grants permission to retrieve utilization statistics for fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGameServer](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameServer.html)  **
  - **Description:** Grants permission to retrieve properties for a game server
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameServerGroup.html)  **
  - **Description:** Grants permission to retrieve properties for a game server group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGameServerInstances](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameServerInstances.html)  **
  - **Description:** Grants permission to retrieve the status of EC2 instances in a game server group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGameSessionDetails](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionDetails.html)  **
  - **Description:** Grants permission to retrieve properties for game sessions in a fleet, including the protection policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionPlacement.html)  **
  - **Description:** Grants permission to retrieve details of a game session placement request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGameSessionQueues](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionQueues.html)  **
  - **Description:** Grants permission to retrieve properties for game session queues
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGameSessions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessions.html)  **
  - **Description:** Grants permission to retrieve properties for game sessions in a fleet
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInstances](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeInstances.html)  **
  - **Description:** Grants permission to retrieve information about instances in a managed fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMatchmaking](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeMatchmaking.html)  **
  - **Description:** Grants permission to retrieve details of matchmaking tickets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMatchmakingConfigurations](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeMatchmakingConfigurations.html)  **
  - **Description:** Grants permission to retrieve properties for FlexMatch matchmakers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMatchmakingRuleSets](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeMatchmakingRuleSets.html)  **
  - **Description:** Grants permission to retrieve properties for FlexMatch matchmaking rule sets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePlayerSessions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribePlayerSessions.html)  **
  - **Description:** Grants permission to retrieve properties for player sessions in a game session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRuntimeConfiguration](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeRuntimeConfiguration.html)  **
  - **Description:** Grants permission to retrieve the current runtime configuration for a fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeScalingPolicies](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeScalingPolicies.html)  **
  - **Description:** Grants permission to retrieve all scaling policies that are applied to a fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeScript](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeScript.html)  **
  - **Description:** Grants permission to retrieve properties for a Realtime Servers script
  - **Resource types (\*required):** [script\*](#list_gamelift-resource-script)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVpcPeeringAuthorizations](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeVpcPeeringAuthorizations.html)  **
  - **Description:** Grants permission to retrieve valid VPC peering authorizations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVpcPeeringConnections](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeVpcPeeringConnections.html)  **
  - **Description:** Grants permission to retrieve details on active or pending VPC peering connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetComputeAccess](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAccess.html)  **
  - **Description:** Grants permission to retrieve credentials to remotely access a compute in a managed fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComputeAuthToken](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAuthToken.html)  **
  - **Description:** Grants permission to retrieve an authentication token that allows processes on a compute to send requests to the Amazon GameLift service
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGameSessionLogUrl](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetGameSessionLogUrl.html)  **
  - **Description:** Grants permission to retrieve the location of stored logs for a game session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInstanceAccess](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetInstanceAccess.html)  **
  - **Description:** Grants permission to request remote access to a specified fleet instance
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetPlayerConnectionDetails.html)  **
  - **Description:** Grants permission to retrieve player connection endpoints and player gateway tokens for a game session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAliases](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListAliases.html)  **
  - **Description:** Grants permission to retrieve all aliases that are defined in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBuilds](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListBuilds.html)  **
  - **Description:** Grants permission to retrieve all game build in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListCompute.html)  **
  - **Description:** Grants permission to retrieve all compute resources in the current Region
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListContainerFleets](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerFleets.html)  **
  - **Description:** Grants permission to retrieve the properties of all existing container fleets in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerGroupDefinitionVersions.html)  **
  - **Description:** Grants permission to retrieve the properties of all versions of an existing container group definition
  - **Resource types (\*required):** [containerGroupDefinition\*](#list_gamelift-resource-containerGroupDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerGroupDefinitions.html)  **
  - **Description:** Grants permission to retrieve the properties of all existing container group definitions in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFleetDeployments](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListFleetDeployments.html)  **
  - **Description:** Grants permission to retrieve the properties of all existing fleet deployments in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFleets](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListFleets.html)  **
  - **Description:** Grants permission to retrieve a list of fleet IDs for all fleets in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGameServerGroups](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListGameServerGroups.html)  **
  - **Description:** Grants permission to retrieve all game server groups that are defined in the current Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGameServers](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListGameServers.html)  **
  - **Description:** Grants permission to retrieve all game servers that are currently running in a game server group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLocations](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListLocations.html)  **
  - **Description:** Grants permission to retrieve all locations in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScripts](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListScripts.html)  **
  - **Description:** Grants permission to retrieve properties for all Realtime Servers scripts in the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve tags for GameLift resources
  - **Resource types (\*required):** [alias](#list_gamelift-resource-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [build](#list_gamelift-resource-build) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [containerGroupDefinition](#list_gamelift-resource-containerGroupDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [gameServerGroup](#list_gamelift-resource-gameServerGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [gameSessionQueue](#list_gamelift-resource-gameSessionQueue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [location](#list_gamelift-resource-location) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [matchmakingConfiguration](#list_gamelift-resource-matchmakingConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [matchmakingRuleSet](#list_gamelift-resource-matchmakingRuleSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [script](#list_gamelift-resource-script) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutScalingPolicy](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PutScalingPolicy.html)  **
  - **Description:** Grants permission to create or update a fleet auto-scaling policy
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html)  **
  - **Description:** Grants permission to register a compute against a fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterGameServer](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterGameServer.html)  **
  - **Description:** Grants permission to notify GameLift FleetIQ when a new game server is ready to host gameplay
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RequestUploadCredentials](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RequestUploadCredentials.html)  **
  - **Description:** Grants permission to retrieve fresh upload credentials to use when uploading a new game build
  - **Resource types (\*required):** [build\*](#list_gamelift-resource-build)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ResolveAlias](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ResolveAlias.html)  **
  - **Description:** Grants permission to retrieve the fleet ID associated with an alias
  - **Resource types (\*required):** [alias\*](#list_gamelift-resource-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ResumeGameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ResumeGameServerGroup.html)  **
  - **Description:** Grants permission to reinstate suspended FleetIQ activity for a game server group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchGameSessions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SearchGameSessions.html)  **
  - **Description:** Grants permission to retrieve game sessions that match a set of search criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartFleetActions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartFleetActions.html)  **
  - **Description:** Grants permission to resume auto-scaling activity on a fleet after it was suspended with StopFleetActions()
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartGameSessionPlacement.html)  **
  - **Description:** Grants permission to send a game session placement request to a game session queue
  - **Resource types (\*required):** [gameSessionQueue\*](#list_gamelift-resource-gameSessionQueue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMatchBackfill](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartMatchBackfill.html)  **
  - **Description:** Grants permission to request FlexMatch matchmaking to fill available player slots in an existing game session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMatchmaking](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartMatchmaking.html)  **
  - **Description:** Grants permission to request FlexMatch matchmaking for one or a group of players and initiate game session placement
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopFleetActions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StopFleetActions.html)  **
  - **Description:** Grants permission to suspend auto-scaling activity on a fleet
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StopGameSessionPlacement.html)  **
  - **Description:** Grants permission to cancel a game session placement request that is in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopMatchmaking](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StopMatchmaking.html)  **
  - **Description:** Grants permission to cancel a matchmaking or match backfill request that is in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SuspendGameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SuspendGameServerGroup.html)  **
  - **Description:** Grants permission to temporarily stop FleetIQ activity for a game server group
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag GameLift resources
  - **Resource types (\*required):** [alias](#list_gamelift-resource-alias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [build](#list_gamelift-resource-build) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [containerGroupDefinition](#list_gamelift-resource-containerGroupDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [gameServerGroup](#list_gamelift-resource-gameServerGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [gameSessionQueue](#list_gamelift-resource-gameSessionQueue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [location](#list_gamelift-resource-location) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [matchmakingConfiguration](#list_gamelift-resource-matchmakingConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [matchmakingRuleSet](#list_gamelift-resource-matchmakingRuleSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [script](#list_gamelift-resource-script) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gamelift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_TerminateGameSession.html)  **
  - **Description:** Grants permission to shut down an existing game session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag GameLift resources
  - **Resource types (\*required):** [alias](#list_gamelift-resource-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [build](#list_gamelift-resource-build) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [containerGroupDefinition](#list_gamelift-resource-containerGroupDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [gameServerGroup](#list_gamelift-resource-gameServerGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [gameSessionQueue](#list_gamelift-resource-gameSessionQueue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [location](#list_gamelift-resource-location) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [matchmakingConfiguration](#list_gamelift-resource-matchmakingConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [matchmakingRuleSet](#list_gamelift-resource-matchmakingRuleSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Resource types (\*required):** [script](#list_gamelift-resource-script) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gamelift-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAlias](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateAlias.html)  **
  - **Description:** Grants permission to update the properties of an existing alias
  - **Resource types (\*required):** [alias\*](#list_gamelift-resource-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBuild](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateBuild.html)  **
  - **Description:** Grants permission to update an existing build's metadata
  - **Resource types (\*required):** [build\*](#list_gamelift-resource-build)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContainerFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateContainerFleet.html)  **
  - **Description:** Grants permission to update an existing container fleet 
  - **Resource types (\*required):** [containerFleet\*](#list_gamelift-resource-containerFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateContainerGroupDefinition.html)  **
  - **Description:** Grants permission to update the properties of an existing container group definition
  - **Resource types (\*required):** [containerGroupDefinition\*](#list_gamelift-resource-containerGroupDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleetAttributes](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateFleetAttributes.html)  **
  - **Description:** Grants permission to update the general properties of an existing fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleetCapacity](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateFleetCapacity.html)  **
  - **Description:** Grants permission to adjust a managed fleet's capacity settings
  - **Resource types (\*required):** [containerFleet](#list_gamelift-resource-containerFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_gamelift-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleetPortSettings](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateFleetPortSettings.html)  **
  - **Description:** Grants permission to adjust a fleet's port settings
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGameServer](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameServer.html)  **
  - **Description:** Grants permission to change game server properties, health status, or utilization status
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameServerGroup.html)  **
  - **Description:** Grants permission to update properties for game server group, including allowed instance types
  - **Resource types (\*required):** [gameServerGroup\*](#list_gamelift-resource-gameServerGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSession.html)  **
  - **Description:** Grants permission to update the properties of an existing game session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGameSessionQueue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSessionQueue.html)  **
  - **Description:** Grants permission to update properties of an existing game session queue
  - **Resource types (\*required):** [gameSessionQueue\*](#list_gamelift-resource-gameSessionQueue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMatchmakingConfiguration](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateMatchmakingConfiguration.html)  **
  - **Description:** Grants permission to update properties of an existing FlexMatch matchmaking configuration
  - **Resource types (\*required):** [matchmakingConfiguration\*](#list_gamelift-resource-matchmakingConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuntimeConfiguration](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateRuntimeConfiguration.html)  **
  - **Description:** Grants permission to update how server processes are configured on instances in an existing fleet
  - **Resource types (\*required):** [fleet\*](#list_gamelift-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateScript](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateScript.html)  **
  - **Description:** Grants permission to update the metadata and content of an existing Realtime Servers script
  - **Resource types (\*required):** [script\*](#list_gamelift-resource-script)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateMatchmakingRuleSet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ValidateMatchmakingRuleSet.html)  **
  - **Description:** Grants permission to validate the syntax of a FlexMatch matchmaking rule set
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon GameLift Servers
<a name="list_gamelift-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alias](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-aliases.html)  | arn:${Partition}:gamelift:${Region}::alias/${AliasId} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [build](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-builds.html)  | arn:${Partition}:gamelift:${Region}:${Account}:build/${BuildId} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [containerFleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-intro.html)  | arn:${Partition}:gamelift:${Region}:${Account}:containerfleet/${FleetId} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [containerGroupDefinition](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-intro.html)  | arn:${Partition}:gamelift:${Region}:${Account}:containergroupdefinition/${Name} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-fleets.html)  | arn:${Partition}:gamelift:${Region}:${Account}:fleet/${FleetId} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [gameServerGroup](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup.html)  | arn:${Partition}:gamelift:${Region}:${Account}:gameservergroup/${GameServerGroupName} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [gameSessionQueue](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-console.html)  | arn:${Partition}:gamelift:${Region}:${Account}:gamesessionqueue/${GameSessionQueueName} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [location](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-creating-anywhere.html#fleet-anywhere-location)  | arn:${Partition}:gamelift:${Region}:${Account}:location/${LocationId} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [matchmakingConfiguration](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-configuration.html)  | arn:${Partition}:gamelift:${Region}:${Account}:matchmakingconfiguration/${MatchmakingConfigurationName} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [matchmakingRuleSet](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets.html)  | arn:${Partition}:gamelift:${Region}:${Account}:matchmakingruleset/${MatchmakingRuleSetName} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 
|  [script](https://docs.aws.amazon.com/gameliftservers/latest/realtimeguide/realtime-intro.html)  | arn:${Partition}:gamelift:${Region}:${Account}:script/${ScriptId} | [aws:ResourceTag/${TagKey}](#list_gamelift-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon GameLift Servers
<a name="list_gamelift-policy-keys"></a>

Amazon GameLift Servers defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 