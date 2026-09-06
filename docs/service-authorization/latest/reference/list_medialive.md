

# Actions, resources, and condition keys for AWS Elemental MediaLive
<a name="list_medialive"></a>

AWS Elemental MediaLive (service prefix: `medialive`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/medialive/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/medialive/latest/apireference/what-is.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/medialive/latest/ug/setting-up.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/medialive/medialive.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaLive](#list_medialive-operations)
+ [Actions defined by AWS Elemental MediaLive](#list_medialive-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaLive](#list_medialive-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaLive](#list_medialive-policy-keys)

## API operations defined by AWS Elemental MediaLive
<a name="list_medialive-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_medialive-actions-as-permissions).




- **   AcceptInputDeviceTransfer  **
  - **IAM action:**  [medialive:AcceptInputDeviceTransfer](#list_medialive-action-AcceptInputDeviceTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDelete  **
  - **IAM action:**  [medialive:BatchDelete](#list_medialive-action-BatchDelete) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchStart  **
  - **IAM action:**  [medialive:BatchStart](#list_medialive-action-BatchStart) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchStop  **
  - **IAM action:**  [medialive:BatchStop](#list_medialive-action-BatchStop) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateSchedule  **
  - **IAM action:**  [medialive:BatchUpdateSchedule](#list_medialive-action-BatchUpdateSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelInputDeviceTransfer  **
  - **IAM action:**  [medialive:CancelInputDeviceTransfer](#list_medialive-action-CancelInputDeviceTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ClaimDevice  **
  - **IAM action:**  [medialive:ClaimDevice](#list_medialive-action-ClaimDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [medialive:CreateChannel](#list_medialive-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medialive.amazonaws.com / **Access level:** Write

- **   CreateChannelPlacementGroup  **
  - **IAM action:**  [medialive:CreateChannelPlacementGroup](#list_medialive-action-CreateChannelPlacementGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCloudWatchAlarmTemplate  **
  - **IAM action:**  [medialive:CreateCloudWatchAlarmTemplate](#list_medialive-action-CreateCloudWatchAlarmTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCloudWatchAlarmTemplateGroup  **
  - **IAM action:**  [medialive:CreateCloudWatchAlarmTemplateGroup](#list_medialive-action-CreateCloudWatchAlarmTemplateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCluster  **
  - **IAM action:**  [medialive:CreateCluster](#list_medialive-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medialive.amazonaws.com / **Access level:** Write

- **   CreateEventBridgeRuleTemplate  **
  - **IAM action:**  [medialive:CreateEventBridgeRuleTemplate](#list_medialive-action-CreateEventBridgeRuleTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventBridgeRuleTemplateGroup  **
  - **IAM action:**  [medialive:CreateEventBridgeRuleTemplateGroup](#list_medialive-action-CreateEventBridgeRuleTemplateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInput  **
  - **IAM action:**  [medialive:CreateInput](#list_medialive-action-CreateInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medialive.amazonaws.com / **Access level:** Write

- **   CreateInputSecurityGroup  **
  - **IAM action:**  [medialive:CreateInputSecurityGroup](#list_medialive-action-CreateInputSecurityGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMultiplex  **
  - **IAM action:**  [medialive:CreateMultiplex](#list_medialive-action-CreateMultiplex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMultiplexProgram  **
  - **IAM action:**  [medialive:CreateMultiplexProgram](#list_medialive-action-CreateMultiplexProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNetwork  **
  - **IAM action:**  [medialive:CreateNetwork](#list_medialive-action-CreateNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNode  **
  - **IAM action:**  [medialive:CreateNode](#list_medialive-action-CreateNode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNodeRegistrationScript  **
  - **IAM action:**  [medialive:CreateNodeRegistrationScript](#list_medialive-action-CreateNodeRegistrationScript) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePartnerInput  **
  - **IAM action:**  [medialive:CreatePartnerInput](#list_medialive-action-CreatePartnerInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSdiSource  **
  - **IAM action:**  [medialive:CreateSdiSource](#list_medialive-action-CreateSdiSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSignalMap  **
  - **IAM action:**  [medialive:CreateSignalMap](#list_medialive-action-CreateSignalMap)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTags  **
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteChannel  **
  - **IAM action:**  [medialive:DeleteChannel](#list_medialive-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannelPlacementGroup  **
  - **IAM action:**  [medialive:DeleteChannelPlacementGroup](#list_medialive-action-DeleteChannelPlacementGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudWatchAlarmTemplate  **
  - **IAM action:**  [medialive:DeleteCloudWatchAlarmTemplate](#list_medialive-action-DeleteCloudWatchAlarmTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudWatchAlarmTemplateGroup  **
  - **IAM action:**  [medialive:DeleteCloudWatchAlarmTemplateGroup](#list_medialive-action-DeleteCloudWatchAlarmTemplateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [medialive:DeleteCluster](#list_medialive-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventBridgeRuleTemplate  **
  - **IAM action:**  [medialive:DeleteEventBridgeRuleTemplate](#list_medialive-action-DeleteEventBridgeRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventBridgeRuleTemplateGroup  **
  - **IAM action:**  [medialive:DeleteEventBridgeRuleTemplateGroup](#list_medialive-action-DeleteEventBridgeRuleTemplateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInput  **
  - **IAM action:**  [medialive:DeleteInput](#list_medialive-action-DeleteInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInputSecurityGroup  **
  - **IAM action:**  [medialive:DeleteInputSecurityGroup](#list_medialive-action-DeleteInputSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMultiplex  **
  - **IAM action:**  [medialive:DeleteMultiplex](#list_medialive-action-DeleteMultiplex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMultiplexProgram  **
  - **IAM action:**  [medialive:DeleteMultiplexProgram](#list_medialive-action-DeleteMultiplexProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNetwork  **
  - **IAM action:**  [medialive:DeleteNetwork](#list_medialive-action-DeleteNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNode  **
  - **IAM action:**  [medialive:DeleteNode](#list_medialive-action-DeleteNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReservation  **
  - **IAM action:**  [medialive:DeleteReservation](#list_medialive-action-DeleteReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchedule  **
  - **IAM action:**  [medialive:DeleteSchedule](#list_medialive-action-DeleteSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSdiSource  **
  - **IAM action:**  [medialive:DeleteSdiSource](#list_medialive-action-DeleteSdiSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSignalMap  **
  - **IAM action:**  [medialive:DeleteSignalMap](#list_medialive-action-DeleteSignalMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [medialive:DeleteTags](#list_medialive-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DescribeAccountConfiguration  **
  - **IAM action:**  [medialive:DescribeAccountConfiguration](#list_medialive-action-DescribeAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChannel  **
  - **IAM action:**  [medialive:DescribeChannel](#list_medialive-action-DescribeChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChannelPlacementGroup  **
  - **IAM action:**  [medialive:DescribeChannelPlacementGroup](#list_medialive-action-DescribeChannelPlacementGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCluster  **
  - **IAM action:**  [medialive:DescribeCluster](#list_medialive-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInput  **
  - **IAM action:**  [medialive:DescribeInput](#list_medialive-action-DescribeInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInputDevice  **
  - **IAM action:**  [medialive:DescribeInputDevice](#list_medialive-action-DescribeInputDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInputDeviceThumbnail  **
  - **IAM action:**  [medialive:DescribeInputDeviceThumbnail](#list_medialive-action-DescribeInputDeviceThumbnail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInputSecurityGroup  **
  - **IAM action:**  [medialive:DescribeInputSecurityGroup](#list_medialive-action-DescribeInputSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMultiplex  **
  - **IAM action:**  [medialive:DescribeMultiplex](#list_medialive-action-DescribeMultiplex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMultiplexProgram  **
  - **IAM action:**  [medialive:DescribeMultiplexProgram](#list_medialive-action-DescribeMultiplexProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNetwork  **
  - **IAM action:**  [medialive:DescribeNetwork](#list_medialive-action-DescribeNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNode  **
  - **IAM action:**  [medialive:DescribeNode](#list_medialive-action-DescribeNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOffering  **
  - **IAM action:**  [medialive:DescribeOffering](#list_medialive-action-DescribeOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservation  **
  - **IAM action:**  [medialive:DescribeReservation](#list_medialive-action-DescribeReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSchedule  **
  - **IAM action:**  [medialive:DescribeSchedule](#list_medialive-action-DescribeSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSdiSource  **
  - **IAM action:**  [medialive:DescribeSdiSource](#list_medialive-action-DescribeSdiSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThumbnails  **
  - **IAM action:**  [medialive:DescribeThumbnails](#list_medialive-action-DescribeThumbnails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudWatchAlarmTemplate  **
  - **IAM action:**  [medialive:GetCloudWatchAlarmTemplate](#list_medialive-action-GetCloudWatchAlarmTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudWatchAlarmTemplateGroup  **
  - **IAM action:**  [medialive:GetCloudWatchAlarmTemplateGroup](#list_medialive-action-GetCloudWatchAlarmTemplateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventBridgeRuleTemplate  **
  - **IAM action:**  [medialive:GetEventBridgeRuleTemplate](#list_medialive-action-GetEventBridgeRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventBridgeRuleTemplateGroup  **
  - **IAM action:**  [medialive:GetEventBridgeRuleTemplateGroup](#list_medialive-action-GetEventBridgeRuleTemplateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSignalMap  **
  - **IAM action:**  [medialive:GetSignalMap](#list_medialive-action-GetSignalMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAlerts  **
  - **IAM action:**  [medialive:ListAlerts](#list_medialive-action-ListAlerts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChannelPlacementGroups  **
  - **IAM action:**  [medialive:ListChannelPlacementGroups](#list_medialive-action-ListChannelPlacementGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChannels  **
  - **IAM action:**  [medialive:ListChannels](#list_medialive-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudWatchAlarmTemplateGroups  **
  - **IAM action:**  [medialive:ListCloudWatchAlarmTemplateGroups](#list_medialive-action-ListCloudWatchAlarmTemplateGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudWatchAlarmTemplates  **
  - **IAM action:**  [medialive:ListCloudWatchAlarmTemplates](#list_medialive-action-ListCloudWatchAlarmTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusterAlerts  **
  - **IAM action:**  [medialive:ListClusterAlerts](#list_medialive-action-ListClusterAlerts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [medialive:ListClusters](#list_medialive-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventBridgeRuleTemplateGroups  **
  - **IAM action:**  [medialive:ListEventBridgeRuleTemplateGroups](#list_medialive-action-ListEventBridgeRuleTemplateGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventBridgeRuleTemplates  **
  - **IAM action:**  [medialive:ListEventBridgeRuleTemplates](#list_medialive-action-ListEventBridgeRuleTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInputDeviceTransfers  **
  - **IAM action:**  [medialive:ListInputDeviceTransfers](#list_medialive-action-ListInputDeviceTransfers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInputDevices  **
  - **IAM action:**  [medialive:ListInputDevices](#list_medialive-action-ListInputDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInputSecurityGroups  **
  - **IAM action:**  [medialive:ListInputSecurityGroups](#list_medialive-action-ListInputSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInputs  **
  - **IAM action:**  [medialive:ListInputs](#list_medialive-action-ListInputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultiplexAlerts  **
  - **IAM action:**  [medialive:ListMultiplexAlerts](#list_medialive-action-ListMultiplexAlerts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultiplexPrograms  **
  - **IAM action:**  [medialive:ListMultiplexPrograms](#list_medialive-action-ListMultiplexPrograms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultiplexes  **
  - **IAM action:**  [medialive:ListMultiplexes](#list_medialive-action-ListMultiplexes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworks  **
  - **IAM action:**  [medialive:ListNetworks](#list_medialive-action-ListNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNodes  **
  - **IAM action:**  [medialive:ListNodes](#list_medialive-action-ListNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOfferings  **
  - **IAM action:**  [medialive:ListOfferings](#list_medialive-action-ListOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReservations  **
  - **IAM action:**  [medialive:ListReservations](#list_medialive-action-ListReservations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSdiSources  **
  - **IAM action:**  [medialive:ListSdiSources](#list_medialive-action-ListSdiSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSignalMaps  **
  - **IAM action:**  [medialive:ListSignalMaps](#list_medialive-action-ListSignalMaps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [medialive:ListTagsForResource](#list_medialive-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVersions  **
  - **IAM action:**  [medialive:ListVersions](#list_medialive-action-ListVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PurchaseOffering  **
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [medialive:PurchaseOffering](#list_medialive-action-PurchaseOffering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RebootInputDevice  **
  - **IAM action:**  [medialive:RebootInputDevice](#list_medialive-action-RebootInputDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectInputDeviceTransfer  **
  - **IAM action:**  [medialive:RejectInputDeviceTransfer](#list_medialive-action-RejectInputDeviceTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestartChannelPipelines  **
  - **IAM action:**  [medialive:RestartChannelPipelines](#list_medialive-action-RestartChannelPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartChannel  **
  - **IAM action:**  [medialive:StartChannel](#list_medialive-action-StartChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDeleteMonitorDeployment  **
  - **IAM action:**  [medialive:StartDeleteMonitorDeployment](#list_medialive-action-StartDeleteMonitorDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInputDevice  **
  - **IAM action:**  [medialive:StartInputDevice](#list_medialive-action-StartInputDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInputDeviceMaintenanceWindow  **
  - **IAM action:**  [medialive:StartInputDeviceMaintenanceWindow](#list_medialive-action-StartInputDeviceMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMonitorDeployment  **
  - **IAM action:**  [medialive:StartMonitorDeployment](#list_medialive-action-StartMonitorDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMultiplex  **
  - **IAM action:**  [medialive:StartMultiplex](#list_medialive-action-StartMultiplex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartUpdateSignalMap  **
  - **IAM action:**  [medialive:StartUpdateSignalMap](#list_medialive-action-StartUpdateSignalMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopChannel  **
  - **IAM action:**  [medialive:StopChannel](#list_medialive-action-StopChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopInputDevice  **
  - **IAM action:**  [medialive:StopInputDevice](#list_medialive-action-StopInputDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMultiplex  **
  - **IAM action:**  [medialive:StopMultiplex](#list_medialive-action-StopMultiplex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TransferInputDevice  **
  - **IAM action:**  [medialive:TransferInputDevice](#list_medialive-action-TransferInputDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccountConfiguration  **
  - **IAM action:**  [medialive:UpdateAccountConfiguration](#list_medialive-action-UpdateAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannel  **
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [medialive:UpdateChannel](#list_medialive-action-UpdateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medialive.amazonaws.com / **Access level:** Write

- **   UpdateChannelClass  **
  - **IAM action:**  [medialive:UpdateChannelClass](#list_medialive-action-UpdateChannelClass) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannelPlacementGroup  **
  - **IAM action:**  [medialive:UpdateChannelPlacementGroup](#list_medialive-action-UpdateChannelPlacementGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCloudWatchAlarmTemplate  **
  - **IAM action:**  [medialive:UpdateCloudWatchAlarmTemplate](#list_medialive-action-UpdateCloudWatchAlarmTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCloudWatchAlarmTemplateGroup  **
  - **IAM action:**  [medialive:UpdateCloudWatchAlarmTemplateGroup](#list_medialive-action-UpdateCloudWatchAlarmTemplateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCluster  **
  - **IAM action:**  [medialive:UpdateCluster](#list_medialive-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventBridgeRuleTemplate  **
  - **IAM action:**  [medialive:UpdateEventBridgeRuleTemplate](#list_medialive-action-UpdateEventBridgeRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventBridgeRuleTemplateGroup  **
  - **IAM action:**  [medialive:UpdateEventBridgeRuleTemplateGroup](#list_medialive-action-UpdateEventBridgeRuleTemplateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInput  **
  - **IAM action:**  [medialive:UpdateInput](#list_medialive-action-UpdateInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medialive.amazonaws.com / **Access level:** Write

- **   UpdateInputDevice  **
  - **IAM action:**  [medialive:UpdateInputDevice](#list_medialive-action-UpdateInputDevice)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medialive.amazonaws.com / **Access level:** Write

- **   UpdateInputSecurityGroup  **
  - **IAM action:**  [medialive:CreateTags](#list_medialive-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [medialive:UpdateInputSecurityGroup](#list_medialive-action-UpdateInputSecurityGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateMultiplex  **
  - **IAM action:**  [medialive:UpdateMultiplex](#list_medialive-action-UpdateMultiplex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMultiplexProgram  **
  - **IAM action:**  [medialive:UpdateMultiplexProgram](#list_medialive-action-UpdateMultiplexProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetwork  **
  - **IAM action:**  [medialive:UpdateNetwork](#list_medialive-action-UpdateNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNode  **
  - **IAM action:**  [medialive:UpdateNode](#list_medialive-action-UpdateNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNodeState  **
  - **IAM action:**  [medialive:UpdateNodeState](#list_medialive-action-UpdateNodeState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReservation  **
  - **IAM action:**  [medialive:UpdateReservation](#list_medialive-action-UpdateReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSdiSource  **
  - **IAM action:**  [medialive:UpdateSdiSource](#list_medialive-action-UpdateSdiSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elemental MediaLive
<a name="list_medialive-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptInputDeviceTransfer](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to accept an input device transfer
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDelete](https://docs.aws.amazon.com/medialive/latest/ug/editing-deleting-channel.html)  **
  - **Description:** Grants permission to delete channels, inputs, input security groups, and multiplexes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchStart](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to start channels and multiplexes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchStop](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to stop channels and multiplexes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchUpdateSchedule](https://docs.aws.amazon.com/medialive/latest/ug/submitting-batch-command.html)  **
  - **Description:** Grants permission to add and remove actions from a channel's schedule
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelInputDeviceTransfer](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to cancel an input device transfer
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ClaimDevice](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to claim an input device
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/medialive/latest/ug/creating-channel-scratch.html)  **
  - **Description:** Grants permission to create a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [input\*](#list_medialive-resource-input) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateChannelPlacementGroup](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to create a cluster
  - **Resource types (\*required):** [channel-placement-group\*](#list_medialive-resource-channel-placement-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCloudWatchAlarmTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html)  **
  - **Description:** Grants permission to create a cloudwatch alarm template
  - **Resource types (\*required):** [cloudwatch-alarm-template\*](#list_medialive-resource-cloudwatch-alarm-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cloudwatch-alarm-template-group\*](#list_medialive-resource-cloudwatch-alarm-template-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCloudWatchAlarmTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html)  **
  - **Description:** Grants permission to create a cloudwatch alarm template group
  - **Resource types (\*required):** [cloudwatch-alarm-template-group\*](#list_medialive-resource-cloudwatch-alarm-template-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to create a cluster
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventBridgeRuleTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html)  **
  - **Description:** Grants permission to create a eventbridge rule template
  - **Resource types (\*required):** [eventbridge-rule-template\*](#list_medialive-resource-eventbridge-rule-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [eventbridge-rule-template-group\*](#list_medialive-resource-eventbridge-rule-template-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventBridgeRuleTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html)  **
  - **Description:** Grants permission to create a eventbridge rule template group
  - **Resource types (\*required):** [eventbridge-rule-template-group\*](#list_medialive-resource-eventbridge-rule-template-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInput](https://docs.aws.amazon.com/medialive/latest/ug/creating-input.html)  **
  - **Description:** Grants permission to create an input
  - **Resource types (\*required):** [input\*](#list_medialive-resource-input) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [input-security-group\*](#list_medialive-resource-input-security-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInputSecurityGroup](https://docs.aws.amazon.com/medialive/latest/ug/working-with-input-security-groups.html)  **
  - **Description:** Grants permission to create an input security group
  - **Resource types (\*required):** [input-security-group\*](#list_medialive-resource-input-security-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMultiplex](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-create.html)  **
  - **Description:** Grants permission to create a multiplex
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMultiplexProgram](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-create.html)  **
  - **Description:** Grants permission to create a multiplex program
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNetwork](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to create a network
  - **Resource types (\*required):** [network\*](#list_medialive-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNode](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to create a node
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [node\*](#list_medialive-resource-node) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNodeRegistrationScript](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to create a node registration script
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePartnerInput](https://docs.aws.amazon.com/medialive/latest/ug/input-create-cdi-partners.html)  **
  - **Description:** Grants permission to create a partner input
  - **Resource types (\*required):** [input\*](#list_medialive-resource-input)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSdiSource](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to create a SDI source
  - **Resource types (\*required):** [sdi-source\*](#list_medialive-resource-sdi-source)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSignalMap](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html)  **
  - **Description:** Grants permission to create a signal map
  - **Resource types (\*required):** [signal-map\*](#list_medialive-resource-signal-map)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTags](https://docs.aws.amazon.com/medialive/latest/ug/tagging.html)  **
  - **Description:** Grants permission to create tags for channels, inputs, input security groups, multiplexes, reservations, nodes, networks, clusters, channel placement groups, signal maps, SDI sources, template groups, and templates
  - **Resource types (\*required):** [channel](#list_medialive-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [channel-placement-group](#list_medialive-resource-channel-placement-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cloudwatch-alarm-template](#list_medialive-resource-cloudwatch-alarm-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cloudwatch-alarm-template-group](#list_medialive-resource-cloudwatch-alarm-template-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_medialive-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [eventbridge-rule-template](#list_medialive-resource-eventbridge-rule-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [eventbridge-rule-template-group](#list_medialive-resource-eventbridge-rule-template-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [input](#list_medialive-resource-input) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [input-security-group](#list_medialive-resource-input-security-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [multiplex](#list_medialive-resource-multiplex) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_medialive-resource-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [node](#list_medialive-resource-node) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [reservation](#list_medialive-resource-reservation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [sdi-source](#list_medialive-resource-sdi-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [signal-map](#list_medialive-resource-signal-map) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteChannel](https://docs.aws.amazon.com/medialive/latest/ug/editing-deleting-channel.html)  **
  - **Description:** Grants permission to delete a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannelPlacementGroup](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to delete a cluster
  - **Resource types (\*required):** [channel-placement-group\*](#list_medialive-resource-channel-placement-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCloudWatchAlarmTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)  **
  - **Description:** Grants permission to delete a cloudwatch alarm template
  - **Resource types (\*required):** [cloudwatch-alarm-template\*](#list_medialive-resource-cloudwatch-alarm-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCloudWatchAlarmTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)  **
  - **Description:** Grants permission to delete a cloudwatch alarm template group
  - **Resource types (\*required):** [cloudwatch-alarm-template-group\*](#list_medialive-resource-cloudwatch-alarm-template-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to delete a cluster
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventBridgeRuleTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html)  **
  - **Description:** Grants permission to delete a eventbridge rule template
  - **Resource types (\*required):** [eventbridge-rule-template\*](#list_medialive-resource-eventbridge-rule-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventBridgeRuleTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html)  **
  - **Description:** Grants permission to delete a eventbridge rule template group
  - **Resource types (\*required):** [eventbridge-rule-template-group\*](#list_medialive-resource-eventbridge-rule-template-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInput](https://docs.aws.amazon.com/medialive/latest/ug/delete-input.html)  **
  - **Description:** Grants permission to delete an input
  - **Resource types (\*required):** [input\*](#list_medialive-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInputSecurityGroup](https://docs.aws.amazon.com/medialive/latest/ug/delete-input-security-group.html)  **
  - **Description:** Grants permission to delete an input security group
  - **Resource types (\*required):** [input-security-group\*](#list_medialive-resource-input-security-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMultiplex](https://docs.aws.amazon.com/medialive/latest/ug/delete-multiplex-program.html)  **
  - **Description:** Grants permission to delete a multiplex
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMultiplexProgram](https://docs.aws.amazon.com/medialive/latest/ug/delete-multiplex-program.html)  **
  - **Description:** Grants permission to delete a multiplex program
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetwork](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to delete a network
  - **Resource types (\*required):** [network\*](#list_medialive-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNode](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to delete a node
  - **Resource types (\*required):** [node\*](#list_medialive-resource-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReservation](https://docs.aws.amazon.com/medialive/latest/ug/deleting-reservations.html)  **
  - **Description:** Grants permission to delete an expired reservation
  - **Resource types (\*required):** [reservation\*](#list_medialive-resource-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchedule](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-console-delete.html)  **
  - **Description:** Grants permission to delete all schedule actions for a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSdiSource](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to delete a SDI source
  - **Resource types (\*required):** [sdi-source\*](#list_medialive-resource-sdi-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSignalMap](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html)  **
  - **Description:** Grants permission to delete a signal map
  - **Resource types (\*required):** [signal-map\*](#list_medialive-resource-signal-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/medialive/latest/ug/tagging.html)  **
  - **Description:** Grants permission to delete tags from channels, inputs, input security groups, multiplexes, reservations, nodes, clusters, networks, channel placement groups, SDI source, signal maps, template groups, and templates
  - **Resource types (\*required):** [channel](#list_medialive-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [channel-placement-group](#list_medialive-resource-channel-placement-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cloudwatch-alarm-template](#list_medialive-resource-cloudwatch-alarm-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cloudwatch-alarm-template-group](#list_medialive-resource-cloudwatch-alarm-template-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_medialive-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [eventbridge-rule-template](#list_medialive-resource-eventbridge-rule-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [eventbridge-rule-template-group](#list_medialive-resource-eventbridge-rule-template-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [input](#list_medialive-resource-input) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [input-security-group](#list_medialive-resource-input-security-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [multiplex](#list_medialive-resource-multiplex) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_medialive-resource-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [node](#list_medialive-resource-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [reservation](#list_medialive-resource-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [sdi-source](#list_medialive-resource-sdi-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [signal-map](#list_medialive-resource-signal-map) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DescribeAccountConfiguration](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to view the account configuration of the customer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeChannel](https://docs.aws.amazon.com/medialive/latest/ug/viewing-channel-configuration.html)  **
  - **Description:** Grants permission to get details about a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeChannelPlacementGroup](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-create.html)  **
  - **Description:** Grants permission to describe a channel placement group
  - **Resource types (\*required):** [channel-placement-group\*](#list_medialive-resource-channel-placement-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCluster](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-create.html)  **
  - **Description:** Grants permission to describe a cluster
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInput](https://docs.aws.amazon.com/medialive/latest/ug/edit-input.html)  **
  - **Description:** Grants permission to describe an input
  - **Resource types (\*required):** [input\*](#list_medialive-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInputDevice](https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html)  **
  - **Description:** Grants permission to describe an input device
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInputDeviceThumbnail](https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html)  **
  - **Description:** Grants permission to describe an input device thumbnail
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInputSecurityGroup](https://docs.aws.amazon.com/medialive/latest/ug/edit-input-security-group.html)  **
  - **Description:** Grants permission to describe an input security group
  - **Resource types (\*required):** [input-security-group\*](#list_medialive-resource-input-security-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMultiplex](https://docs.aws.amazon.com/medialive/latest/ug/edit-multiplex-program-channel.html)  **
  - **Description:** Grants permission to describe a multiplex
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMultiplexProgram](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-multiplex-console.html)  **
  - **Description:** Grants permission to describe a multiplex program
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNetwork](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-networks.html)  **
  - **Description:** Grants permission to describe a network
  - **Resource types (\*required):** [network\*](#list_medialive-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNode](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-nodes-create.html)  **
  - **Description:** Grants permission to describe a node
  - **Resource types (\*required):** [node\*](#list_medialive-resource-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOffering](https://docs.aws.amazon.com/medialive/latest/ug/purchasing-reservations.html)  **
  - **Description:** Grants permission to get details about a reservation offering
  - **Resource types (\*required):** [offering\*](#list_medialive-resource-offering)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReservation](https://docs.aws.amazon.com/medialive/latest/ug/view-reservations.html)  **
  - **Description:** Grants permission to get details about a reservation
  - **Resource types (\*required):** [reservation\*](#list_medialive-resource-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSchedule](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-console-view.html)  **
  - **Description:** Grants permission to view a list of actions scheduled on a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSdiSource](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-create.html)  **
  - **Description:** Grants permission to describe a SDI source
  - **Resource types (\*required):** [sdi-source\*](#list_medialive-resource-sdi-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeThumbnails](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to view the thumbnails for a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudWatchAlarmTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)  **
  - **Description:** Grants permission to get a cloudwatch alarm template
  - **Resource types (\*required):** [cloudwatch-alarm-template\*](#list_medialive-resource-cloudwatch-alarm-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudWatchAlarmTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)  **
  - **Description:** Grants permission to get a cloudwatch alarm template group
  - **Resource types (\*required):** [cloudwatch-alarm-template-group\*](#list_medialive-resource-cloudwatch-alarm-template-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventBridgeRuleTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html)  **
  - **Description:** Grants permission to get a eventbridge rule template
  - **Resource types (\*required):** [eventbridge-rule-template\*](#list_medialive-resource-eventbridge-rule-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventBridgeRuleTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html)  **
  - **Description:** Grants permission to get a eventbridge rule template group
  - **Resource types (\*required):** [eventbridge-rule-template-group\*](#list_medialive-resource-eventbridge-rule-template-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSignalMap](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-view.html)  **
  - **Description:** Grants permission to get a signal map
  - **Resource types (\*required):** [signal-map\*](#list_medialive-resource-signal-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAlerts](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-alerts-channels.html)  **
  - **Description:** Grants permission to list channel alerts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListChannelPlacementGroups](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to list channel placement groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListChannels](https://docs.aws.amazon.com/medialive/latest/ug/viewing-channel-configuration.html)  **
  - **Description:** Grants permission to list channels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCloudWatchAlarmTemplateGroups](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)  **
  - **Description:** Grants permission to list cloudwatch alarm template groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCloudWatchAlarmTemplates](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)  **
  - **Description:** Grants permission to list cloudwatch alarm templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClusterAlerts](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-alerts-cluster.html)  **
  - **Description:** Grants permission to list cluster alerts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to list clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventBridgeRuleTemplateGroups](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html)  **
  - **Description:** Grants permission to list eventbridge rule template groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventBridgeRuleTemplates](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html)  **
  - **Description:** Grants permission to list eventbridge rule templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInputDeviceTransfers](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to list input device transfers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInputDevices](https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html)  **
  - **Description:** Grants permission to list input devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInputSecurityGroups](https://docs.aws.amazon.com/medialive/latest/ug/edit-input-security-group.html)  **
  - **Description:** Grants permission to list input security groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInputs](https://docs.aws.amazon.com/medialive/latest/ug/edit-input.html)  **
  - **Description:** Grants permission to list inputs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMultiplexAlerts](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-alerts-channels.html)  **
  - **Description:** Grants permission to list multiplex alerts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMultiplexPrograms](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-multiplex-console.html)  **
  - **Description:** Grants permission to list multiplex programs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMultiplexes](https://docs.aws.amazon.com/medialive/latest/ug/edit-multiplex-program-channel.html)  **
  - **Description:** Grants permission to list multiplexes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNetworks](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to list networks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNodes](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to list nodes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOfferings](https://docs.aws.amazon.com/medialive/latest/ug/purchasing-reservations.html)  **
  - **Description:** Grants permission to list reservation offerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReservations](https://docs.aws.amazon.com/medialive/latest/ug/view-reservations.html)  **
  - **Description:** Grants permission to list reservations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSdiSources](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to list SDI sources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSignalMaps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-view.html)  **
  - **Description:** Grants permission to list signal maps
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/medialive/latest/ug/tagging.html)  **
  - **Description:** Grants permission to list tags for channels, inputs, input security groups, multiplexes, reservations, nodes, clusters, networks, channel placement groups, SDI sources, signal maps, template groups, and templates
  - **Resource types (\*required):** [channel](#list_medialive-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [channel-placement-group](#list_medialive-resource-channel-placement-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloudwatch-alarm-template](#list_medialive-resource-cloudwatch-alarm-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloudwatch-alarm-template-group](#list_medialive-resource-cloudwatch-alarm-template-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_medialive-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventbridge-rule-template](#list_medialive-resource-eventbridge-rule-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventbridge-rule-template-group](#list_medialive-resource-eventbridge-rule-template-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [input](#list_medialive-resource-input) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [input-security-group](#list_medialive-resource-input-security-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [multiplex](#list_medialive-resource-multiplex) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [network](#list_medialive-resource-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [node](#list_medialive-resource-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [reservation](#list_medialive-resource-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sdi-source](#list_medialive-resource-sdi-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [signal-map](#list_medialive-resource-signal-map) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVersions](https://docs.aws.amazon.com/medialive/latest/ug/medialive-versions.html)  **
  - **Description:** Grants permission to list available versions of MediaLive
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PollAnywhere](https://docs.aws.amazon.com/medialive/latest/ug/about-emla.html)  **
  - **Description:** Grants permission to the node to poll the cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PurchaseOffering](https://docs.aws.amazon.com/medialive/latest/ug/purchasing-reservations.html)  **
  - **Description:** Grants permission to purchase a reservation offering
  - **Resource types (\*required):** [offering\*](#list_medialive-resource-offering) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Resource types (\*required):** [reservation\*](#list_medialive-resource-reservation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [RebootInputDevice](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to reboot an input device
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectInputDeviceTransfer](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to reject an input device transfer
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RestartChannelPipelines](https://docs.aws.amazon.com/medialive/latest/ug/maintenance-user-initiated.html)  **
  - **Description:** Grants permission to restart pipelines on a running channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartChannel](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to start a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDeleteMonitorDeployment](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html)  **
  - **Description:** Grants permission to start deletion of a signal map's monitor
  - **Resource types (\*required):** [signal-map\*](#list_medialive-resource-signal-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartInputDevice](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to start an input device attached to a MediaConnect flow
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartInputDeviceMaintenanceWindow](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to start a maintenance window for an input device
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMonitorDeployment](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-deploy.html)  **
  - **Description:** Grants permission to start a signal map monitor deployment
  - **Resource types (\*required):** [signal-map\*](#list_medialive-resource-signal-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMultiplex](https://docs.aws.amazon.com/medialive/latest/ug/start-multiplex.html)  **
  - **Description:** Grants permission to start a multiplex
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartUpdateSignalMap](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-update.html)  **
  - **Description:** Grants permission to start a signal map update
  - **Resource types (\*required):** [signal-map\*](#list_medialive-resource-signal-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopChannel](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to stop a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopInputDevice](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to stop an input device attached to a MediaConnect flow
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopMultiplex](https://docs.aws.amazon.com/medialive/latest/ug/stop-multiplex.title.html)  **
  - **Description:** Grants permission to stop a multiplex
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitAnywhereStateChange](https://docs.aws.amazon.com/medialive/latest/ug/about-emla.html)  **
  - **Description:** Grants permission to the node to submit state changes to the cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TransferInputDevice](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  **
  - **Description:** Grants permission to transfer an input device
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountConfiguration](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)  **
  - **Description:** Grants permission to update a customer's account configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChannel](https://docs.aws.amazon.com/medialive/latest/ug/editing-deleting-channel.html)  **
  - **Description:** Grants permission to update a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChannelClass](https://docs.aws.amazon.com/medialive/latest/ug/editing-deleting-channel.html)  **
  - **Description:** Grants permission to update the class of a channel
  - **Resource types (\*required):** [channel\*](#list_medialive-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChannelPlacementGroup](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to update a node
  - **Resource types (\*required):** [channel-placement-group\*](#list_medialive-resource-channel-placement-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateCloudWatchAlarmTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html)  **
  - **Description:** Grants permission to update a cloudwatch alarm template
  - **Resource types (\*required):** [cloudwatch-alarm-template\*](#list_medialive-resource-cloudwatch-alarm-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloudwatch-alarm-template-group\*](#list_medialive-resource-cloudwatch-alarm-template-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCloudWatchAlarmTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html)  **
  - **Description:** Grants permission to update a cloudwatch alarm template group
  - **Resource types (\*required):** [cloudwatch-alarm-template-group\*](#list_medialive-resource-cloudwatch-alarm-template-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCluster](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-create.html)  **
  - **Description:** Grants permission to update a cluster
  - **Resource types (\*required):** [cluster\*](#list_medialive-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateEventBridgeRuleTemplate](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html)  **
  - **Description:** Grants permission to update a eventbridge rule template
  - **Resource types (\*required):** [eventbridge-rule-template\*](#list_medialive-resource-eventbridge-rule-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventbridge-rule-template-group\*](#list_medialive-resource-eventbridge-rule-template-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventBridgeRuleTemplateGroup](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html)  **
  - **Description:** Grants permission to update a eventbridge rule template group
  - **Resource types (\*required):** [eventbridge-rule-template-group\*](#list_medialive-resource-eventbridge-rule-template-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInput](https://docs.aws.amazon.com/medialive/latest/ug/edit-input.html)  **
  - **Description:** Grants permission to update an input
  - **Resource types (\*required):** [input\*](#list_medialive-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInputDevice](https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html)  **
  - **Description:** Grants permission to update an input device
  - **Resource types (\*required):** [input-device\*](#list_medialive-resource-input-device)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateInputSecurityGroup](https://docs.aws.amazon.com/medialive/latest/ug/edit-input-security-group.html)  **
  - **Description:** Grants permission to update an input security group
  - **Resource types (\*required):** [input-security-group\*](#list_medialive-resource-input-security-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateMultiplex](https://docs.aws.amazon.com/medialive/latest/ug/edit-multiplex-program-channel.html)  **
  - **Description:** Grants permission to update a multiplex
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMultiplexProgram](https://docs.aws.amazon.com/medialive/latest/ug/edit-multiplex-program-channel.html)  **
  - **Description:** Grants permission to update a multiplex program
  - **Resource types (\*required):** [multiplex\*](#list_medialive-resource-multiplex)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetwork](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-identify-network-requirements.html)  **
  - **Description:** Grants permission to update the state of a node
  - **Resource types (\*required):** [network\*](#list_medialive-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateNode](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-nodes-create.html)  **
  - **Description:** Grants permission to update a node
  - **Resource types (\*required):** [node\*](#list_medialive-resource-node)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateNodeState](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to update the state of a node
  - **Resource types (\*required):** [node\*](#list_medialive-resource-node)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateReservation](https://docs.aws.amazon.com/medialive/latest/ug/reservations.html)  **
  - **Description:** Grants permission to update a reservation
  - **Resource types (\*required):** [reservation\*](#list_medialive-resource-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSdiSource](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  **
  - **Description:** Grants permission to update the state of a sdi source
  - **Resource types (\*required):** [sdi-source\*](#list_medialive-resource-sdi-source)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medialive-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medialive-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaLive
<a name="list_medialive-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/medialive/latest/ug/container-channel.html)  | arn:${Partition}:medialive:${Region}:${Account}:channel:${ChannelId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [channel-placement-group](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  | arn:${Partition}:medialive:${Region}:${Account}:channelPlacementGroup:${ClusterId}/${ChannelPlacementGroupId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [cloudwatch-alarm-template](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html)  | arn:${Partition}:medialive:${Region}:${Account}:cloudwatch-alarm-template:${CloudWatchAlarmTemplateId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [cloudwatch-alarm-template-group](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html)  | arn:${Partition}:medialive:${Region}:${Account}:cloudwatch-alarm-template-group:${CloudWatchAlarmTemplateGroupId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  | arn:${Partition}:medialive:${Region}:${Account}:cluster:${ClusterId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [eventbridge-rule-template](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html)  | arn:${Partition}:medialive:${Region}:${Account}:eventbridge-rule-template:${EventBridgeRuleTemplateId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [eventbridge-rule-template-group](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html)  | arn:${Partition}:medialive:${Region}:${Account}:eventbridge-rule-template-group:${EventBridgeRuleTemplateGroupId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [input](https://docs.aws.amazon.com/medialive/latest/ug/creating-input.html)  | arn:${Partition}:medialive:${Region}:${Account}:input:${InputId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [input-device](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html)  | arn:${Partition}:medialive:${Region}:${Account}:inputDevice:${DeviceId} |   | 
|  [input-security-group](https://docs.aws.amazon.com/medialive/latest/ug/working-with-input-security-groups.html)  | arn:${Partition}:medialive:${Region}:${Account}:inputSecurityGroup:${InputSecurityGroupId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [multiplex](https://docs.aws.amazon.com/medialive/latest/ug/eml-multiplex.html)  | arn:${Partition}:medialive:${Region}:${Account}:multiplex:${MultiplexId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [network](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  | arn:${Partition}:medialive:${Region}:${Account}:network:${NetworkId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [node](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  | arn:${Partition}:medialive:${Region}:${Account}:node:${ClusterId}/${NodeId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [offering](https://docs.aws.amazon.com/medialive/latest/ug/input-output-reservations.html)  | arn:${Partition}:medialive:${Region}:${Account}:offering:${OfferingId} |   | 
|  [reservation](https://docs.aws.amazon.com/medialive/latest/ug/reservations.html)  | arn:${Partition}:medialive:${Region}:${Account}:reservation:${ReservationId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [sdi-source](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)  | arn:${Partition}:medialive:${Region}:${Account}:sdiSource:${SdiSourceId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 
|  [signal-map](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html)  | arn:${Partition}:medialive:${Region}:${Account}:signal-map:${SignalMapId} | [aws:ResourceTag/${TagKey}](#list_medialive-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental MediaLive
<a name="list_medialive-policy-keys"></a>

AWS Elemental MediaLive defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/medialive/latest/ugtagging.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/medialive/latest/ugtagging.html)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/medialive/latest/ugtagging.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 