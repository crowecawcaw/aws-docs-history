

# Actions, resources, and condition keys for Amazon EventBridge
<a name="list_eventbridge"></a>

Amazon EventBridge (service prefix: `events`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eventbridge/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eventbridge/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/events/events.json) for this service.

**Topics**
+ [API operations defined by Amazon EventBridge](#list_eventbridge-operations)
+ [Actions defined by Amazon EventBridge](#list_eventbridge-actions-as-permissions)
+ [Permission-only actions for Amazon EventBridge](#list_eventbridge-permission-only-actions)
+ [Resource types defined by Amazon EventBridge](#list_eventbridge-resources-for-iam-policies)
+ [Condition keys for Amazon EventBridge](#list_eventbridge-policy-keys)

## API operations defined by Amazon EventBridge
<a name="list_eventbridge-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_eventbridge-actions-as-permissions).




- **   CreateEventBus  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:CreateEventBus](#list_eventbridge-action-CreateEventBus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventSource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:CreateEventSource](#list_eventbridge-action-CreateEventSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSubscriber  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:CreateSubscriber](#list_eventbridge-action-CreateSubscriber)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   DeleteEventBus  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DeleteEventBus](#list_eventbridge-action-DeleteEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DeleteEventSource](#list_eventbridge-action-DeleteEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DeleteResourcePolicy](#list_eventbridge-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSubscriber  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DeleteSubscriber](#list_eventbridge-action-DeleteSubscriber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeEventBus  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DescribeEventBus](#list_eventbridge-action-DescribeEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventSource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DescribeEventSource](#list_eventbridge-action-DescribeEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSubscriber  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:DescribeSubscriber](#list_eventbridge-action-DescribeSubscriber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:GetResourcePolicy](#list_eventbridge-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEventBuses  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:ListEventBuses](#list_eventbridge-action-ListEventBuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventSources  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:ListEventSources](#list_eventbridge-action-ListEventSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcePolicies  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:ListResourcePolicies](#list_eventbridge-action-ListResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscribers  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:ListSubscribers](#list_eventbridge-action-ListSubscribers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:ListTagsForResource](#list_eventbridge-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutEvents  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:PutEvents](#list_eventbridge-action-PutEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRawEvents  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:PutRawEvents](#list_eventbridge-action-PutRawEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:PutResourcePolicy](#list_eventbridge-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RevokeResource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:RevokeResource](#list_eventbridge-action-RevokeResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:UntagResource](#list_eventbridge-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEventBus  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:UpdateEventBus](#list_eventbridge-action-UpdateEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventSource  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:UpdateEventSource](#list_eventbridge-action-UpdateEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriber  **
  - **SDK client:** eventbridgev2
  - **IAM action:**  [events:UpdateSubscriber](#list_eventbridge-action-UpdateSubscriber)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   ActivateEventSource  **
  - **SDK client:** events
  - **IAM action:**  [events:ActivateEventSource](#list_eventbridge-action-ActivateEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelReplay  **
  - **SDK client:** events
  - **IAM action:**  [events:CancelReplay](#list_eventbridge-action-CancelReplay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApiDestination  **
  - **SDK client:** events
  - **IAM action:**  [events:CreateApiDestination](#list_eventbridge-action-CreateApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateArchive  **
  - **SDK client:** events
  - **IAM action:**  [events:CreateArchive](#list_eventbridge-action-CreateArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnection  **
  - **SDK client:** events
  - **IAM action:**  [events:CreateConnection](#list_eventbridge-action-CreateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEndpoint  **
  - **SDK client:** events
  - **IAM action:**  [events:CreateEndpoint](#list_eventbridge-action-CreateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   CreateEventBus  **
  - **SDK client:** events
  - **IAM action:**  [events:CreateEventBus](#list_eventbridge-action-CreateEventBus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePartnerEventSource  **
  - **SDK client:** events
  - **IAM action:**  [events:CreatePartnerEventSource](#list_eventbridge-action-CreatePartnerEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeactivateEventSource  **
  - **SDK client:** events
  - **IAM action:**  [events:DeactivateEventSource](#list_eventbridge-action-DeactivateEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeauthorizeConnection  **
  - **SDK client:** events
  - **IAM action:**  [events:DeauthorizeConnection](#list_eventbridge-action-DeauthorizeConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApiDestination  **
  - **SDK client:** events
  - **IAM action:**  [events:DeleteApiDestination](#list_eventbridge-action-DeleteApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArchive  **
  - **SDK client:** events
  - **IAM action:**  [events:DeleteArchive](#list_eventbridge-action-DeleteArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **SDK client:** events
  - **IAM action:**  [events:DeleteConnection](#list_eventbridge-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **SDK client:** events
  - **IAM action:**  [events:DeleteEndpoint](#list_eventbridge-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventBus  **
  - **SDK client:** events
  - **IAM action:**  [events:DeleteEventBus](#list_eventbridge-action-DeleteEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartnerEventSource  **
  - **SDK client:** events
  - **IAM action:**  [events:DeletePartnerEventSource](#list_eventbridge-action-DeletePartnerEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **SDK client:** events
  - **IAM action:**  [events:DeleteRule](#list_eventbridge-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeApiDestination  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeApiDestination](#list_eventbridge-action-DescribeApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeArchive  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeArchive](#list_eventbridge-action-DescribeArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnection  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeConnection](#list_eventbridge-action-DescribeConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoint  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeEndpoint](#list_eventbridge-action-DescribeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventBus  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeEventBus](#list_eventbridge-action-DescribeEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventSource  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeEventSource](#list_eventbridge-action-DescribeEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePartnerEventSource  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribePartnerEventSource](#list_eventbridge-action-DescribePartnerEventSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplay  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeReplay](#list_eventbridge-action-DescribeReplay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRule  **
  - **SDK client:** events
  - **IAM action:**  [events:DescribeRule](#list_eventbridge-action-DescribeRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableRule  **
  - **SDK client:** events
  - **IAM action:**  [events:DisableRule](#list_eventbridge-action-DisableRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableRule  **
  - **SDK client:** events
  - **IAM action:**  [events:EnableRule](#list_eventbridge-action-EnableRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListApiDestinations  **
  - **SDK client:** events
  - **IAM action:**  [events:ListApiDestinations](#list_eventbridge-action-ListApiDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArchives  **
  - **SDK client:** events
  - **IAM action:**  [events:ListArchives](#list_eventbridge-action-ListArchives) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnections  **
  - **SDK client:** events
  - **IAM action:**  [events:ListConnections](#list_eventbridge-action-ListConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEndpoints  **
  - **SDK client:** events
  - **IAM action:**  [events:ListEndpoints](#list_eventbridge-action-ListEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventBuses  **
  - **SDK client:** events
  - **IAM action:**  [events:ListEventBuses](#list_eventbridge-action-ListEventBuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventSources  **
  - **SDK client:** events
  - **IAM action:**  [events:ListEventSources](#list_eventbridge-action-ListEventSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartnerEventSourceAccounts  **
  - **SDK client:** events
  - **IAM action:**  [events:ListPartnerEventSourceAccounts](#list_eventbridge-action-ListPartnerEventSourceAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartnerEventSources  **
  - **SDK client:** events
  - **IAM action:**  [events:ListPartnerEventSources](#list_eventbridge-action-ListPartnerEventSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReplays  **
  - **SDK client:** events
  - **IAM action:**  [events:ListReplays](#list_eventbridge-action-ListReplays) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleNamesByTarget  **
  - **SDK client:** events
  - **IAM action:**  [events:ListRuleNamesByTarget](#list_eventbridge-action-ListRuleNamesByTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRules  **
  - **SDK client:** events
  - **IAM action:**  [events:ListRules](#list_eventbridge-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** events
  - **IAM action:**  [events:ListTagsForResource](#list_eventbridge-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargetsByRule  **
  - **SDK client:** events
  - **IAM action:**  [events:ListTargetsByRule](#list_eventbridge-action-ListTargetsByRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutEvents  **
  - **SDK client:** events
  - **IAM action:**  [events:PutEvents](#list_eventbridge-action-PutEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPartnerEvents  **
  - **SDK client:** events
  - **IAM action:**  [events:PutPartnerEvents](#list_eventbridge-action-PutPartnerEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPermission  **
  - **SDK client:** events
  - **IAM action:**  [events:PutPermission](#list_eventbridge-action-PutPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRule  **
  - **SDK client:** events
  - **IAM action:**  [events:PutRule](#list_eventbridge-action-PutRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   PutTargets  **
  - **SDK client:** events
  - **IAM action:**  [events:PutTargets](#list_eventbridge-action-PutTargets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   RemovePermission  **
  - **SDK client:** events
  - **IAM action:**  [events:RemovePermission](#list_eventbridge-action-RemovePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RemoveTargets  **
  - **SDK client:** events
  - **IAM action:**  [events:RemoveTargets](#list_eventbridge-action-RemoveTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplay  **
  - **SDK client:** events
  - **IAM action:**  [events:StartReplay](#list_eventbridge-action-StartReplay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** events
  - **IAM action:**  [events:TagResource](#list_eventbridge-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestEventPattern  **
  - **SDK client:** events
  - **IAM action:**  [events:TestEventPattern](#list_eventbridge-action-TestEventPattern) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UntagResource  **
  - **SDK client:** events
  - **IAM action:**  [events:UntagResource](#list_eventbridge-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApiDestination  **
  - **SDK client:** events
  - **IAM action:**  [events:UpdateApiDestination](#list_eventbridge-action-UpdateApiDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateArchive  **
  - **SDK client:** events
  - **IAM action:**  [events:UpdateArchive](#list_eventbridge-action-UpdateArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnection  **
  - **SDK client:** events
  - **IAM action:**  [events:UpdateConnection](#list_eventbridge-action-UpdateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpoint  **
  - **SDK client:** events
  - **IAM action:**  [events:UpdateEndpoint](#list_eventbridge-action-UpdateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   UpdateEventBus  **
  - **SDK client:** events
  - **IAM action:**  [events:UpdateEventBus](#list_eventbridge-action-UpdateEventBus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon EventBridge
<a name="list_eventbridge-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ActivateEventSource.html)  **
  - **Description:** Grants permission to activate partner event sources
  - **Resource types (\*required):** [event-source\*](#list_eventbridge-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CancelReplay.html)  **
  - **Description:** Grants permission to cancel a replay
  - **Resource types (\*required):** [replay\*](#list_eventbridge-resource-replay)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateApiDestination.html)  **
  - **Description:** Grants permission to create a new api destination
  - **Resource types (\*required):** [api-destination\*](#list_eventbridge-resource-api-destination) / **Condition keys:**  
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateArchive.html)  **
  - **Description:** Grants permission to create a new archive
  - **Resource types (\*required):** [alias](#list_eventbridge-resource-alias) / **Condition keys:**  
  - **Resource types (\*required):** [archive\*](#list_eventbridge-resource-archive) / **Condition keys:**  
  - **Resource types (\*required):** [event-bus\*](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [key](#list_eventbridge-resource-key) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a new connection
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEndpoint.html)  **
  - **Description:** Grants permission to create an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_eventbridge-resource-endpoint)
  - **Condition keys:** [events:EventBusArn](#list_eventbridge-events_EventBusArn)
  - **Access level:** Write

- **   [CreateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html)  **
  - **Description:** Grants permission to create event buses
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventSource.html)  **
  - **Description:** Grants permission to create an event source that forwards events to an event bus
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:source](#list_eventbridge-events_source)
  - **Resource types (\*required):** [event-sourcev2\*](#list_eventbridge-resource-event-sourcev2) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:source](#list_eventbridge-events_source)
  - **Access level:** Write

- **   [CreatePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreatePartnerEventSource.html)  **
  - **Description:** Grants permission to create partner event sources
  - **Resource types (\*required):** [event-source\*](#list_eventbridge-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSubscriber](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateSubscriber.html)  **
  - **Description:** Grants permission to create a subscriber
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:ContentFilterPresent](#list_eventbridge-events_ContentFilterPresent)<br />[events:Metadata/${MetadataKey}](#list_eventbridge-events_Metadata___MetadataKey_)<br />[events:Metadata/${MetadataKey}/Matcher](#list_eventbridge-events_Metadata___MetadataKey__Matcher)
  - **Resource types (\*required):** [subscriber\*](#list_eventbridge-resource-subscriber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:ContentFilterPresent](#list_eventbridge-events_ContentFilterPresent)<br />[events:Metadata/${MetadataKey}](#list_eventbridge-events_Metadata___MetadataKey_)<br />[events:Metadata/${MetadataKey}/Matcher](#list_eventbridge-events_Metadata___MetadataKey__Matcher)
  - **Access level:** Write

- **   [DeactivateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeactivateEventSource.html)  **
  - **Description:** Grants permission to deactivate event sources
  - **Resource types (\*required):** [event-source\*](#list_eventbridge-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeauthorizeConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeauthorizeConnection.html)  **
  - **Description:** Grants permission to deauthorize a connection, deleting its stored authorization secrets
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteApiDestination.html)  **
  - **Description:** Grants permission to delete an api destination
  - **Resource types (\*required):** [api-destination\*](#list_eventbridge-resource-api-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteArchive.html)  **
  - **Description:** Grants permission to delete an archive
  - **Resource types (\*required):** [archive\*](#list_eventbridge-resource-archive)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_eventbridge-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventBus.html)  **
  - **Description:** Grants permission to delete event buses
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventSource.html)  **
  - **Description:** Grants permission to delete an event source
  - **Resource types (\*required):** [event-sourcev2\*](#list_eventbridge-resource-event-sourcev2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeletePartnerEventSource.html)  **
  - **Description:** Grants permission to delete partner event sources
  - **Resource types (\*required):** [event-source\*](#list_eventbridge-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy attached to an event bus
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:PolicyName](#list_eventbridge-events_PolicyName)
  - **Access level:** Permissions management, Write

- **   [DeleteRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteRule.html)  **
  - **Description:** Grants permission to delete rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Access level:** Write

- **   [DeleteSubscriber](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteSubscriber.html)  **
  - **Description:** Grants permission to delete a subscriber
  - **Resource types (\*required):** [subscriber\*](#list_eventbridge-resource-subscriber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeApiDestination.html)  **
  - **Description:** Grants permission to retrieve details about an api destination
  - **Resource types (\*required):** [api-destination\*](#list_eventbridge-resource-api-destination) / **Condition keys:**  
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection) / **Condition keys:**  
  - **Access level:** Read

- **   [DescribeArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeArchive.html)  **
  - **Description:** Grants permission to retrieve details about an archive
  - **Resource types (\*required):** [archive\*](#list_eventbridge-resource-archive)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeConnection.html)  **
  - **Description:** Grants permission to retrieve details about a conection
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEndpoint.html)  **
  - **Description:** Grants permission to retrieve details about an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_eventbridge-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventBus.html)  **
  - **Description:** Grants permission to retrieve details about event buses
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventSource.html)  **
  - **Description:** Grants permission to retrieve details about event sources
  - **Resource types (\*required):** [event-source](#list_eventbridge-resource-event-source) / **Condition keys:**  
  - **Resource types (\*required):** [event-sourcev2](#list_eventbridge-resource-event-sourcev2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribePartnerEventSource.html)  **
  - **Description:** Grants permission to retrieve details about partner event sources
  - **Resource types (\*required):** [event-source\*](#list_eventbridge-resource-event-source)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeReplay.html)  **
  - **Description:** Grants permission to retrieve the details of a replay
  - **Resource types (\*required):** [replay\*](#list_eventbridge-resource-replay)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeRule.html)  **
  - **Description:** Grants permission to retrieve details about rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Access level:** Read

- **   [DescribeSubscriber](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeSubscriber.html)  **
  - **Description:** Grants permission to retrieve details about a subscriber
  - **Resource types (\*required):** [subscriber\*](#list_eventbridge-resource-subscriber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html)  **
  - **Description:** Grants permission to disable rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Access level:** Write

- **   [EnableRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EnableRule.html)  **
  - **Description:** Grants permission to enable rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve the resource policy attached to an event bus
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:PolicyName](#list_eventbridge-events_PolicyName)
  - **Access level:** Read

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
  - **Resource types (\*required):** [event-source\*](#list_eventbridge-resource-event-source)
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

- **   [ListResourcePolicies](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListResourcePolicies.html)  **
  - **Description:** Grants permission to list the resource policies attached to an event bus
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
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

- **   [ListSubscribers](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListSubscribers.html)  **
  - **Description:** Grants permission to retrieve a list of subscribers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags associated with an Amazon EventBridge resource
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [event-sourcev2](#list_eventbridge-resource-event-sourcev2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [subscriber](#list_eventbridge-resource-subscriber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Access level:** List

- **   [ListTargetsByRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html)  **
  - **Description:** Grants permission to retrieve a list of targets defined for a rule
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Access level:** List

- **   [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)  **
  - **Description:** Grants permission to send custom events to Amazon EventBridge
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:detail-type](#list_eventbridge-events_detail-type)<br />[events:eventBusInvocation](#list_eventbridge-events_eventBusInvocation)<br />[events:source](#list_eventbridge-events_source)<br />[events:SystemMetadata/AwsDetailType](#list_eventbridge-events_SystemMetadata_AwsDetailType)<br />[events:SystemMetadata/AwsSource](#list_eventbridge-events_SystemMetadata_AwsSource)<br />[events:SystemMetadata/ContentType](#list_eventbridge-events_SystemMetadata_ContentType)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:detail-type](#list_eventbridge-events_detail-type)<br />[events:eventBusInvocation](#list_eventbridge-events_eventBusInvocation)<br />[events:source](#list_eventbridge-events_source)<br />[events:SystemMetadata/AwsDetailType](#list_eventbridge-events_SystemMetadata_AwsDetailType)<br />[events:SystemMetadata/AwsSource](#list_eventbridge-events_SystemMetadata_AwsSource)<br />[events:SystemMetadata/ContentType](#list_eventbridge-events_SystemMetadata_ContentType)
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

- **   [PutRawEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRawEvents.html)  **
  - **Description:** Grants permission to publish raw-format events with custom content types, metadata, binary payloads, and FIFO ordering to Amazon EventBridge
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:eventBusInvocation](#list_eventbridge-events_eventBusInvocation)<br />[events:Metadata/${MetadataKey}](#list_eventbridge-events_Metadata___MetadataKey_)<br />[events:SystemMetadata/AwsDetailType](#list_eventbridge-events_SystemMetadata_AwsDetailType)<br />[events:SystemMetadata/AwsSource](#list_eventbridge-events_SystemMetadata_AwsSource)<br />[events:SystemMetadata/ContentType](#list_eventbridge-events_SystemMetadata_ContentType)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to an event bus
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:PolicyName](#list_eventbridge-events_PolicyName)
  - **Access level:** Permissions management, Write

- **   [PutRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRule.html)  **
  - **Description:** Grants permission to create or updates rules
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:detail-type](#list_eventbridge-events_detail-type)<br />[events:detail.eventTypeCode](#list_eventbridge-events_detail.eventTypeCode)<br />[events:detail.service](#list_eventbridge-events_detail.service)<br />[events:detail.userIdentity.principalId](#list_eventbridge-events_detail.userIdentity.principalId)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)<br />[events:source](#list_eventbridge-events_source)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:detail-type](#list_eventbridge-events_detail-type)<br />[events:detail.eventTypeCode](#list_eventbridge-events_detail.eventTypeCode)<br />[events:detail.service](#list_eventbridge-events_detail.service)<br />[events:detail.userIdentity.principalId](#list_eventbridge-events_detail.userIdentity.principalId)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)<br />[events:source](#list_eventbridge-events_source)
  - **Access level:** Write

- **   [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html)  **
  - **Description:** Grants permission to add targets to a rule
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)<br />[events:TargetArn](#list_eventbridge-events_TargetArn)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)<br />[events:TargetArn](#list_eventbridge-events_TargetArn)
  - **Access level:** Write

- **   [RemovePermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html)  **
  - **Description:** Grants permission to revoke the permission of another AWS account to put events to your default event bus
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RemoveTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemoveTargets.html)  **
  - **Description:** Grants permission to removes targets from a rule
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)<br />[events:ManagedBy](#list_eventbridge-events_ManagedBy)
  - **Access level:** Write

- **   [RevokeResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RevokeResource.html)  **
  - **Description:** Grants permission to revoke a subscriber or an event source on an event bus
  - **Resource types (\*required):** [event-busv2\*](#list_eventbridge-resource-event-busv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_StartReplay.html)  **
  - **Description:** Grants permission to start a replay of an archive
  - **Resource types (\*required):** [archive\*](#list_eventbridge-resource-archive) / **Condition keys:**  
  - **Resource types (\*required):** [event-bus\*](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [replay\*](#list_eventbridge-resource-replay) / **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add a tag to an Amazon EventBridge resource
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [event-sourcev2](#list_eventbridge-resource-event-sourcev2) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [subscriber](#list_eventbridge-resource-subscriber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eventbridge-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Access level:** Tagging, Write

- **   [TestEventPattern](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TestEventPattern.html)  **
  - **Description:** Grants permission to test whether an event pattern matches the provided event
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an Amazon EventBridge resource
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [event-sourcev2](#list_eventbridge-resource-event-sourcev2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-custom-event-bus](#list_eventbridge-resource-rule-on-custom-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [rule-on-default-event-bus](#list_eventbridge-resource-rule-on-default-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Resource types (\*required):** [subscriber](#list_eventbridge-resource-subscriber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventbridge-aws_TagKeys)<br />[events:creatorAccount](#list_eventbridge-events_creatorAccount)
  - **Access level:** Tagging, Write

- **   [UpdateApiDestination](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateApiDestination.html)  **
  - **Description:** Grants permission to update an api destination
  - **Resource types (\*required):** [api-destination\*](#list_eventbridge-resource-api-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateArchive](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateArchive.html)  **
  - **Description:** Grants permission to update an archive
  - **Resource types (\*required):** [alias](#list_eventbridge-resource-alias) / **Condition keys:**  
  - **Resource types (\*required):** [archive\*](#list_eventbridge-resource-archive) / **Condition keys:**  
  - **Resource types (\*required):** [key](#list_eventbridge-resource-key) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateConnection.html)  **
  - **Description:** Grants permission to update a connection
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateEndpoint.html)  **
  - **Description:** Grants permission to update an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_eventbridge-resource-endpoint)
  - **Condition keys:** [events:EventBusArn](#list_eventbridge-events_EventBusArn)
  - **Access level:** Write

- **   [UpdateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateEventBus.html)  **
  - **Description:** Grants permission to update event buses
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateEventSource.html)  **
  - **Description:** Grants permission to update an event source
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:source](#list_eventbridge-events_source)
  - **Resource types (\*required):** [event-sourcev2\*](#list_eventbridge-resource-event-sourcev2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:source](#list_eventbridge-events_source)
  - **Access level:** Write

- **   [UpdateSubscriber](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateSubscriber.html)  **
  - **Description:** Grants permission to update a subscriber
  - **Resource types (\*required):** [event-busv2](#list_eventbridge-resource-event-busv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:ContentFilterPresent](#list_eventbridge-events_ContentFilterPresent)<br />[events:Metadata/${MetadataKey}](#list_eventbridge-events_Metadata___MetadataKey_)<br />[events:Metadata/${MetadataKey}/Matcher](#list_eventbridge-events_Metadata___MetadataKey__Matcher)
  - **Resource types (\*required):** [subscriber\*](#list_eventbridge-resource-subscriber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)<br />[events:ContentFilterPresent](#list_eventbridge-events_ContentFilterPresent)<br />[events:Metadata/${MetadataKey}](#list_eventbridge-events_Metadata___MetadataKey_)<br />[events:Metadata/${MetadataKey}/Matcher](#list_eventbridge-events_Metadata___MetadataKey__Matcher)
  - **Access level:** Write



## Permission-only actions for Amazon EventBridge
<a name="list_eventbridge-permission-only-actions"></a>

The following actions are defined by Amazon EventBridge but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html)  **
  - **Description:** Grants permission to configure vended log delivery for EventBridge
  - **Resource types (\*required):** [event-bus](#list_eventbridge-resource-event-bus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subscriber](#list_eventbridge-resource-subscriber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeApiDestination](https://docs.aws.amazon.com/eventbridge/latest/userguide/iam-identity-based-access-control-eventbridge.html)  **
  - **Description:** Grants permission to invoke an api destination
  - **Resource types (\*required):** [api-destination\*](#list_eventbridge-resource-api-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RetrieveConnectionCredentials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html)  **
  - **Description:** Grants permission to retrieve credentials from a connection
  - **Resource types (\*required):** [connection\*](#list_eventbridge-resource-connection)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon EventBridge
<a name="list_eventbridge-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html)  | arn:${Partition}:kms:${Region}:${Account}:alias/${Alias} |   | 
|  [api-destination](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:api-destination/${ApiDestinationName} |   | 
|  [archive](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:archive/${ArchiveName} |   | 
|  [connection](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:connection/${ConnectionName} |   | 
|  [create-snapshot](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/create-snapshot |   | 
|  [endpoint](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:endpoint/${EndpointName} |   | 
|  [event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:event-bus/${EventBusName} | [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_) | 
|  [event-busv2](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:event-busv2/${EventBusName}/${OpaqueId} | [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_) | 
|  [event-source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}::event-source/${EventSourceName} |   | 
|  [event-sourcev2](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:event-sourcev2/${SourceType}/${EventSourceName}/${OpaqueId} | [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_) | 
|  [key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)  | arn:${Partition}:kms:${Region}:${Account}:key/${KeyId} |   | 
|  [reboot-instance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/reboot-instance |   | 
|  [replay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:replay/${ReplayName} |   | 
|  [rule-on-custom-event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:rule/${EventBusName}/${RuleName} | [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_) | 
|  [rule-on-default-event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:rule/${RuleName} | [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_) | 
|  [stop-instance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/stop-instance |   | 
|  [subscriber](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:subscriber/${SubscriberName}/${OpaqueId} | [aws:ResourceTag/${TagKey}](#list_eventbridge-aws_ResourceTag___TagKey_) | 
|  [terminate-instance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format)  | arn:${Partition}:events:${Region}:${Account}:target/terminate-instance |   | 

## Condition keys for Amazon EventBridge
<a name="list_eventbridge-policy-keys"></a>

Amazon EventBridge defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags to event bus and rule actions | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource to event bus and rule actions | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tags in the request to event bus and rule actions | ArrayOfString | 
|   [events:ContentFilterPresent](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by whether a subscriber declares a payload-scope content filter to CreateSubscriber and UpdateSubscriber actions | Bool | 
|   [events:EventBusArn](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limiting-access-to-event-buses)  | Filters access by the ARN of the event buses that can be associated with an endpoint to CreateEndpoint and UpdateEndpoint actions | ArrayOfARN | 
|   [events:ManagedBy](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by AWS services. If a rule is created by an AWS service on your behalf, the value is the principal name of the service that created the rule | String | 
|   [events:Metadata/${MetadataKey}](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by a metadata key-value pair on the published event to PutRawEvents actions, or by the exact-match values declared for that key in a subscriber's metadata filter to CreateSubscriber and UpdateSubscriber actions | ArrayOfString | 
|   [events:Metadata/${MetadataKey}/Matcher](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by the match type declared for a metadata key in a subscriber's filter to CreateSubscriber and UpdateSubscriber actions | String | 
|   [events:PolicyName](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by the name of the resource policy specified in the request to resource policy actions | String | 
|   [events:SystemMetadata/AwsDetailType](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by the detail type recorded in the system metadata of an event forwarded onto an event bus to PutEvents and PutRawEvents actions | String | 
|   [events:SystemMetadata/AwsSource](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by the source recorded in the system metadata of an event forwarded onto an event bus to PutEvents and PutRawEvents actions | String | 
|   [events:SystemMetadata/ContentType](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html)  | Filters access by the content type declared on an event for PutRawEvents and for forwarded events authorized as PutEvents | String | 
|   [events:TargetArn](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limiting-access-to-targets)  | Filters access by the ARN of a target that can be put to a rule to PutTargets actions. TargetARN doesn't include DeadLetterConfigArn | ArrayOfARN | 
|   [events:creatorAccount](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-creator-account)  | Filters access by the account the rule was created in to rule actions | String | 
|   [events:detail-type](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-pattern-detail-type)  | Filters access by the literal string of the detail-type of the event to PutEvents and PutRule actions | ArrayOfString | 
|   [events:detail.eventTypeCode](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limit-rule-by-type-code)  | Filters access by the literal string for the detail.eventTypeCode field of the event to PutRule actions | String | 
|   [events:detail.service](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#limit-rule-by-service)  | Filters access by the literal string for the detail.service field of the event to PutRule actions | String | 
|   [events:detail.userIdentity.principalId](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#consume-specific-events)  | Filters access by the literal string for the detail.useridentity.principalid field of the event to PutRule actions | String | 
|   [events:eventBusInvocation](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-bus-invocation)  | Filters access to PutEvents and PutRawEvents by whether an event was forwarded from an event bus rather than published through a direct API call | String | 
|   [events:source](https://docs.aws.amazon.com/eventbridge/latest/userguide/policy-keys-eventbridge.html#events-limit-access-control)  | Filters access by the AWS service or AWS partner event source that generated the event to PutEvents and PutRule actions, or by the configured source of an event source to the CreateEventSource and UpdateEventSource actions. Matches the literal string of the source field of the event | ArrayOfString | 