

# Actions, resources, and condition keys for Amazon EventBridge
<a name="list_events"></a>

Amazon EventBridge (service prefix: `events`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eventbridge/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eventbridge/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/events/events.json) for this service.

**Topics**
+ [API operations defined by Amazon EventBridge](#list_events-operations)
+ [Actions defined by Amazon EventBridge](#list_events-actions-as-permissions)
+ [Permission-only actions for Amazon EventBridge](#list_events-permission-only-actions)
+ [Resource types defined by Amazon EventBridge](#list_events-resources-for-iam-policies)
+ [Condition keys for Amazon EventBridge](#list_events-policy-keys)

## API operations defined by Amazon EventBridge
<a name="list_events-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_events-actions-as-permissions).




- **   ActivateEventSource  **
  - **IAM action:**  [events:ActivateEventSource](#list_events-action-ActivateEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelReplay  **
  - **IAM action:**  [events:CancelReplay](#list_events-action-CancelReplay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApiDestination  **
  - **IAM action:**  [events:CreateApiDestination](#list_events-action-CreateApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateArchive  **
  - **IAM action:**  [events:CreateArchive](#list_events-action-CreateArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnection  **
  - **IAM action:**  [events:CreateConnection](#list_events-action-CreateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEndpoint  **
  - **IAM action:**  [events:CreateEndpoint](#list_events-action-CreateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   CreateEventBus  **
  - **IAM action:**  [events:CreateEventBus](#list_events-action-CreateEventBus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_events-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePartnerEventSource  **
  - **IAM action:**  [events:CreatePartnerEventSource](#list_events-action-CreatePartnerEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeactivateEventSource  **
  - **IAM action:**  [events:DeactivateEventSource](#list_events-action-DeactivateEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeauthorizeConnection  **
  - **IAM action:**  [events:DeauthorizeConnection](#list_events-action-DeauthorizeConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApiDestination  **
  - **IAM action:**  [events:DeleteApiDestination](#list_events-action-DeleteApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArchive  **
  - **IAM action:**  [events:DeleteArchive](#list_events-action-DeleteArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [events:DeleteConnection](#list_events-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **IAM action:**  [events:DeleteEndpoint](#list_events-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventBus  **
  - **IAM action:**  [events:DeleteEventBus](#list_events-action-DeleteEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartnerEventSource  **
  - **IAM action:**  [events:DeletePartnerEventSource](#list_events-action-DeletePartnerEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [events:DeleteRule](#list_events-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeApiDestination  **
  - **IAM action:**  [events:DescribeApiDestination](#list_events-action-DescribeApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeArchive  **
  - **IAM action:**  [events:DescribeArchive](#list_events-action-DescribeArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnection  **
  - **IAM action:**  [events:DescribeConnection](#list_events-action-DescribeConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoint  **
  - **IAM action:**  [events:DescribeEndpoint](#list_events-action-DescribeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventBus  **
  - **IAM action:**  [events:DescribeEventBus](#list_events-action-DescribeEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventSource  **
  - **IAM action:**  [events:DescribeEventSource](#list_events-action-DescribeEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePartnerEventSource  **
  - **IAM action:**  [events:DescribePartnerEventSource](#list_events-action-DescribePartnerEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplay  **
  - **IAM action:**  [events:DescribeReplay](#list_events-action-DescribeReplay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRule  **
  - **IAM action:**  [events:DescribeRule](#list_events-action-DescribeRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableRule  **
  - **IAM action:**  [events:DisableRule](#list_events-action-DisableRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableRule  **
  - **IAM action:**  [events:EnableRule](#list_events-action-EnableRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListApiDestinations  **
  - **IAM action:**  [events:ListApiDestinations](#list_events-action-ListApiDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArchives  **
  - **IAM action:**  [events:ListArchives](#list_events-action-ListArchives) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnections  **
  - **IAM action:**  [events:ListConnections](#list_events-action-ListConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEndpoints  **
  - **IAM action:**  [events:ListEndpoints](#list_events-action-ListEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventBuses  **
  - **IAM action:**  [events:ListEventBuses](#list_events-action-ListEventBuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventSources  **
  - **IAM action:**  [events:ListEventSources](#list_events-action-ListEventSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartnerEventSourceAccounts  **
  - **IAM action:**  [events:ListPartnerEventSourceAccounts](#list_events-action-ListPartnerEventSourceAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartnerEventSources  **
  - **IAM action:**  [events:ListPartnerEventSources](#list_events-action-ListPartnerEventSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReplays  **
  - **IAM action:**  [events:ListReplays](#list_events-action-ListReplays) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleNamesByTarget  **
  - **IAM action:**  [events:ListRuleNamesByTarget](#list_events-action-ListRuleNamesByTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRules  **
  - **IAM action:**  [events:ListRules](#list_events-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [events:ListTagsForResource](#list_events-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargetsByRule  **
  - **IAM action:**  [events:ListTargetsByRule](#list_events-action-ListTargetsByRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutEvents  **
  - **IAM action:**  [events:PutEvents](#list_events-action-PutEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPartnerEvents  **
  - **IAM action:**  [events:PutPartnerEvents](#list_events-action-PutPartnerEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPermission  **
  - **IAM action:**  [events:PutPermission](#list_events-action-PutPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRule  **
  - **IAM action:**  [events:PutRule](#list_events-action-PutRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_events-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   PutTargets  **
  - **IAM action:**  [events:PutTargets](#list_events-action-PutTargets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   RemovePermission  **
  - **IAM action:**  [events:RemovePermission](#list_events-action-RemovePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RemoveTargets  **
  - **IAM action:**  [events:RemoveTargets](#list_events-action-RemoveTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplay  **
  - **IAM action:**  [events:StartReplay](#list_events-action-StartReplay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [events:TagResource](#list_events-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestEventPattern  **
  - **IAM action:**  [events:TestEventPattern](#list_events-action-TestEventPattern) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UntagResource  **
  - **IAM action:**  [events:UntagResource](#list_events-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApiDestination  **
  - **IAM action:**  [events:UpdateApiDestination](#list_events-action-UpdateApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateArchive  **
  - **IAM action:**  [events:UpdateArchive](#list_events-action-UpdateArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnection  **
  - **IAM action:**  [events:UpdateConnection](#list_events-action-UpdateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpoint  **
  - **IAM action:**  [events:UpdateEndpoint](#list_events-action-UpdateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   UpdateEventBus  **
  - **IAM action:**  [events:UpdateEventBus](#list_events-action-UpdateEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon EventBridge
<a name="list_events-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ActivateEventSource.html)  **
  - **Description:** Grants permission to activate partner event sources
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CancelReplay.html)  **
  - **Description:** Grants permission to cancel a replay
  - **Resource types (\*required):** [replay\*](#list_events-resource-replay)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateApiDestination.html)  **
  - **Description:** Grants permission to create a new api destination
  - **Resource types (\*required):** [api-destination\*](#list_events-resource-api-destination) / **Condition keys:**  
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateArchive.html)  **
  - **Description:** Grants permission to create a new archive
  - **Resource types (\*required):** [alias](#list_events-resource-alias) / **Condition keys:**  
  - **Resource types (\*required):** [archive\*](#list_events-resource-archive) / **Condition keys:**  
  - **Resource types (\*required):** [event-bus\*](#list_events-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [key](#list_events-resource-key) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a new connection
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEndpoint.html)  **
  - **Description:** Grants permission to create an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_events-resource-endpoint)
  - **Condition keys:** [events:EventBusArn](#list_events-events_EventBusArn)
  - **Access level:** Write

- **   [CreateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html)  **
  - **Description:** Grants permission to create event buses
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_events-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreatePartnerEventSource.html)  **
  - **Description:** Grants permission to create partner event sources
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeactivateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeactivateEventSource.html)  **
  - **Description:** Grants permission to deactivate event sources
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeauthorizeConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeauthorizeConnection.html)  **
  - **Description:** Grants permission to deauthorize a connection, deleting its stored authorization secrets
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteApiDestination.html)  **
  - **Description:** Grants permission to delete an api destination
  - **Resource types (\*required):** [api-destination\*](#list_events-resource-api-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteArchive.html)  **
  - **Description:** Grants permission to delete an archive
  - **Resource types (\*required):** [archive\*](#list_events-resource-archive)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_events-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventBus.html)  **
  - **Description:** Grants permission to delete event buses
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeletePartnerEventSource.html)  **
  - **Description:** Grants permission to delete partner event sources
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteRule.html)  **
  - **Description:** Grants permission to delete rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Access level:** Write

- **   [DescribeApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeApiDestination.html)  **
  - **Description:** Grants permission to retrieve details about an api destination
  - **Resource types (\*required):** [api-destination\*](#list_events-resource-api-destination) / **Condition keys:**  
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection) / **Condition keys:**  
  - **Access level:** Read

- **   [DescribeArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeArchive.html)  **
  - **Description:** Grants permission to retrieve details about an archive
  - **Resource types (\*required):** [archive\*](#list_events-resource-archive)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeConnection.html)  **
  - **Description:** Grants permission to retrieve details about a conection
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEndpoint.html)  **
  - **Description:** Grants permission to retrieve details about an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_events-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventBus.html)  **
  - **Description:** Grants permission to retrieve details about event buses
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventSource.html)  **
  - **Description:** Grants permission to retrieve details about event sources
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribePartnerEventSource.html)  **
  - **Description:** Grants permission to retrieve details about partner event sources
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeReplay.html)  **
  - **Description:** Grants permission to retrieve the details of a replay
  - **Resource types (\*required):** [replay\*](#list_events-resource-replay)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeRule.html)  **
  - **Description:** Grants permission to retrieve details about rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Access level:** Read

- **   [DisableRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html)  **
  - **Description:** Grants permission to disable rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Access level:** Write

- **   [EnableRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EnableRule.html)  **
  - **Description:** Grants permission to enable rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Access level:** Write

- **   [ListApiDestinations](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListApiDestinations.html)  **
  - **Description:** Grants permission to retrieve a list of api destinations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArchives](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListArchives.html)  **
  - **Description:** Grants permission to retrieve a list of archives
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnections](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListConnections.html)  **
  - **Description:** Grants permission to retrieve a list of connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEndpoints](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEndpoints.html)  **
  - **Description:** Grants permission to retrieve a list of endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventBuses](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventBuses.html)  **
  - **Description:** Grants permission to retrieve a list of the event buses in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventSources](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventSources.html)  **
  - **Description:** Grants permission to to retrieve a list of event sources shared with this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPartnerEventSourceAccounts](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListPartnerEventSourceAccounts.html)  **
  - **Description:** Grants permission to retrieve a list of AWS account IDs associated with an event source
  - **Resource types (\*required):** [event-source\*](#list_events-resource-event-source)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPartnerEventSources](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListPartnerEventSources.html)  **
  - **Description:** Grants permission to retrieve a list partner event sources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReplays](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListReplays.html)  **
  - **Description:** Grants permission to retrieve a list of replays
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRuleNamesByTarget](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRuleNamesByTarget.html)  **
  - **Description:** Grants permission to retrieve a list of the names of the rules associated with a target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRules](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRules.html)  **
  - **Description:** Grants permission to retrieve a list of the Amazon EventBridge rules in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags associated with an Amazon EventBridge resource
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Access level:** List

- **   [ListTargetsByRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html)  **
  - **Description:** Grants permission to retrieve a list of targets defined for a rule
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Access level:** List

- **   [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)  **
  - **Description:** Grants permission to send custom events to Amazon EventBridge
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:detail-type](#list_events-events_detail-type)<br />[events:eventBusInvocation](#list_events-events_eventBusInvocation)<br />[events:source](#list_events-events_source)
  - **Access level:** Write

- **   [PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)  **
  - **Description:** Grants permission to sends custom events to Amazon EventBridge
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutPermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html)  **
  - **Description:** Grants permission to use the PutPermission action to grants permission to another AWS account to put events to your default event bus
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRule.html)  **
  - **Description:** Grants permission to create or updates rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_events-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:detail-type](#list_events-events_detail-type)<br />[events:detail.eventTypeCode](#list_events-events_detail.eventTypeCode)<br />[events:detail.service](#list_events-events_detail.service)<br />[events:detail.userIdentity.principalId](#list_events-events_detail.userIdentity.principalId)<br />[events:ManagedBy](#list_events-events_ManagedBy)<br />[events:source](#list_events-events_source)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_events-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:detail-type](#list_events-events_detail-type)<br />[events:detail.eventTypeCode](#list_events-events_detail.eventTypeCode)<br />[events:detail.service](#list_events-events_detail.service)<br />[events:detail.userIdentity.principalId](#list_events-events_detail.userIdentity.principalId)<br />[events:ManagedBy](#list_events-events_ManagedBy)<br />[events:source](#list_events-events_source)
  - **Access level:** Write

- **   [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html)  **
  - **Description:** Grants permission to add targets to a rule
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)<br />[events:TargetArn](#list_events-events_TargetArn)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)<br />[events:TargetArn](#list_events-events_TargetArn)
  - **Access level:** Write

- **   [RemovePermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html)  **
  - **Description:** Grants permission to revoke the permission of another AWS account to put events to your default event bus
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RemoveTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemoveTargets.html)  **
  - **Description:** Grants permission to removes targets from a rule
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_events-events_creatorAccount)<br />[events:ManagedBy](#list_events-events_ManagedBy)
  - **Access level:** Write

- **   [StartReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_StartReplay.html)  **
  - **Description:** Grants permission to start a replay of an archive
  - **Resource types (\*required):** [archive\*](#list_events-resource-archive) / **Condition keys:**  
  - **Resource types (\*required):** [event-bus\*](#list_events-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [replay\*](#list_events-resource-replay) / **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add a tag to an Amazon EventBridge resource
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_events-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_events-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_events-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Access level:** Tagging, Write

- **   [TestEventPattern](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TestEventPattern.html)  **
  - **Description:** Grants permission to test whether an event pattern matches the provided event
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an Amazon EventBridge resource
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_events-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_events-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_events-aws_TagKeys)<br />[events:creatorAccount](#list_events-events_creatorAccount)
  - **Access level:** Tagging, Write

- **   [UpdateApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateApiDestination.html)  **
  - **Description:** Grants permission to update an api destination
  - **Resource types (\*required):** [api-destination\*](#list_events-resource-api-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateArchive.html)  **
  - **Description:** Grants permission to update an archive
  - **Resource types (\*required):** [alias](#list_events-resource-alias) / **Condition keys:**  
  - **Resource types (\*required):** [archive\*](#list_events-resource-archive) / **Condition keys:**  
  - **Resource types (\*required):** [key](#list_events-resource-key) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateConnection.html)  **
  - **Description:** Grants permission to update a connection
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateEndpoint.html)  **
  - **Description:** Grants permission to update an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_events-resource-endpoint)
  - **Condition keys:** [events:EventBusArn](#list_events-events_EventBusArn)
  - **Access level:** Write

- **   [UpdateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateEventBus.html)  **
  - **Description:** Grants permission to update event buses
  - **Resource types (\*required):** [event-bus](#list_events-resource-event-bus)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon EventBridge
<a name="list_events-permission-only-actions"></a>

The following actions are defined by Amazon EventBridge but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html)  **
  - **Description:** Grants permission to configure vended log delivery for EventBridge
  - **Resource types (\*required):** [event-bus\*](#list_events-resource-event-bus)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeApiDestination](https://docs.aws.amazon.com/eventbridge/latest/userguide/iam-identity-based-access-control-eventbridge.html)  **
  - **Description:** Grants permission to invoke an api destination
  - **Resource types (\*required):** [api-destination\*](#list_events-resource-api-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RetrieveConnectionCredentials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html)  **
  - **Description:** Grants permission to retrieve credentials from a connection
  - **Resource types (\*required):** [connection\*](#list_events-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon EventBridge
<a name="list_events-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html)  | arn:${Partition}:kms:${Region}:${Account}:alias/${Alias} |   | 
|  [api-destination](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:api-destination/${ApiDestinationName} |   | 
|  [archive](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:archive/${ArchiveName} |   | 
|  [connection](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:connection/${ConnectionName} |   | 
|  [create-snapshot](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/create-snapshot |   | 
|  [endpoint](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:endpoint/${EndpointName} |   | 
|  [event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:event-bus/${EventBusName} | [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_) | 
|  [event-source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}::event-source/${EventSourceName} |   | 
|  [key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)  | arn:${Partition}:kms:${Region}:${Account}:key/${KeyId} |   | 
|  [reboot-instance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/reboot-instance |   | 
|  [replay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:replay/${ReplayName} |   | 
|  [rule-on-custom-event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:rule/${EventBusName}/${RuleName} | [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_) | 
|  [rule-on-default-event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:rule/${RuleName} | [aws:ResourceTag/${TagKey}](#list_events-aws_ResourceTag___TagKey_) | 
|  [stop-instance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/stop-instance |   | 
|  [terminate-instance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/terminate-instance |   | 

## Condition keys for Amazon EventBridge
<a name="list_events-policy-keys"></a>

Amazon EventBridge defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags to event bus and rule actions | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource to event bus and rule actions | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tags in the request to event bus and rule actions | ArrayOfString | 
|   [events:EventBusArn](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limiting-access-to-event-buses)  | Filters access by the ARN of the event buses that can be associated with an endpoint to CreateEndpoint and UpdateEndpoint actions | ArrayOfARN | 
|   [events:ManagedBy](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by AWS services. If a rule is created by an AWS service on your behalf, the value is the principal name of the service that created the rule | String | 
|   [events:TargetArn](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limiting-access-to-targets)  | Filters access by the ARN of a target that can be put to a rule to PutTargets actions. TargetARN doesn't include DeadLetterConfigArn | ArrayOfARN | 
|   [events:creatorAccount](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-creator-account)  | Filters access by the account the rule was created in to rule actions | String | 
|   [events:detail-type](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-pattern-detail-type)  | Filters access by the literal string of the detail-type of the event to PutEvents and PutRule actions | ArrayOfString | 
|   [events:detail.eventTypeCode](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limit-rule-by-type-code)  | Filters access by the literal string for the detail.eventTypeCode field of the event to PutRule actions | String | 
|   [events:detail.service](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limit-rule-by-service)  | Filters access by the literal string for the detail.service field of the event to PutRule actions | String | 
|   [events:detail.userIdentity.principalId](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#consume-specific-events)  | Filters access by the literal string for the detail.useridentity.principalid field of the event to PutRule actions | String | 
|   [events:eventBusInvocation](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-bus-invocation)  | Filters access by whether the event was generated via API or cross-account bus invocation to PutEvents actions | String | 
|   [events:source](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-limit-access-control)  | Filters access by the AWS service or AWS partner event source that generated the event to PutEvents and PutRule actions. Matches the literal string of the source field of the event | ArrayOfString | 