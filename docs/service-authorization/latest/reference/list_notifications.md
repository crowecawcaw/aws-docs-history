

# Actions, resources, and condition keys for AWS User Notifications
<a name="list_notifications"></a>

AWS User Notifications (service prefix: `notifications`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/notifications/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/notifications/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/notifications/notifications.json) for this service.

**Topics**
+ [API operations defined by AWS User Notifications](#list_notifications-operations)
+ [Actions defined by AWS User Notifications](#list_notifications-actions-as-permissions)
+ [Permission-only actions for AWS User Notifications](#list_notifications-permission-only-actions)
+ [Resource types defined by AWS User Notifications](#list_notifications-resources-for-iam-policies)
+ [Condition keys for AWS User Notifications](#list_notifications-policy-keys)

## API operations defined by AWS User Notifications
<a name="list_notifications-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_notifications-actions-as-permissions).




- **   AssociateChannel  **
  - **IAM action:**  [notifications:AssociateChannel](#list_notifications-action-AssociateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateManagedNotificationAccountContact  **
  - **IAM action:**  [notifications:AssociateManagedNotificationAccountContact](#list_notifications-action-AssociateManagedNotificationAccountContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateManagedNotificationAdditionalChannel  **
  - **IAM action:**  [notifications:AssociateManagedNotificationAdditionalChannel](#list_notifications-action-AssociateManagedNotificationAdditionalChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateOrganizationalUnit  **
  - **IAM action:**  [notifications:AssociateOrganizationalUnit](#list_notifications-action-AssociateOrganizationalUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEventRule  **
  - **IAM action:**  [notifications:CreateEventRule](#list_notifications-action-CreateEventRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNotificationConfiguration  **
  - **IAM action:**  [notifications:CreateNotificationConfiguration](#list_notifications-action-CreateNotificationConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [notifications:TagResource](#list_notifications-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteEventRule  **
  - **IAM action:**  [notifications:DeleteEventRule](#list_notifications-action-DeleteEventRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotificationConfiguration  **
  - **IAM action:**  [notifications:DeleteNotificationConfiguration](#list_notifications-action-DeleteNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterNotificationHub  **
  - **IAM action:**  [notifications:DeregisterNotificationHub](#list_notifications-action-DeregisterNotificationHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableNotificationsAccessForOrganization  **
  - **IAM action:**  [notifications:DisableNotificationsAccessForOrganization](#list_notifications-action-DisableNotificationsAccessForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisassociateChannel  **
  - **IAM action:**  [notifications:DisassociateChannel](#list_notifications-action-DisassociateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateManagedNotificationAccountContact  **
  - **IAM action:**  [notifications:DisassociateManagedNotificationAccountContact](#list_notifications-action-DisassociateManagedNotificationAccountContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateManagedNotificationAdditionalChannel  **
  - **IAM action:**  [notifications:DisassociateManagedNotificationAdditionalChannel](#list_notifications-action-DisassociateManagedNotificationAdditionalChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateOrganizationalUnit  **
  - **IAM action:**  [notifications:DisassociateOrganizationalUnit](#list_notifications-action-DisassociateOrganizationalUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableNotificationsAccessForOrganization  **
  - **IAM action:**  [notifications:EnableNotificationsAccessForOrganization](#list_notifications-action-EnableNotificationsAccessForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   GetEventRule  **
  - **IAM action:**  [notifications:GetEventRule](#list_notifications-action-GetEventRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedNotificationChildEvent  **
  - **IAM action:**  [notifications:GetManagedNotificationChildEvent](#list_notifications-action-GetManagedNotificationChildEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedNotificationConfiguration  **
  - **IAM action:**  [notifications:GetManagedNotificationConfiguration](#list_notifications-action-GetManagedNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedNotificationEvent  **
  - **IAM action:**  [notifications:GetManagedNotificationEvent](#list_notifications-action-GetManagedNotificationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotificationConfiguration  **
  - **IAM action:**  [notifications:GetNotificationConfiguration](#list_notifications-action-GetNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotificationEvent  **
  - **IAM action:**  [notifications:GetNotificationEvent](#list_notifications-action-GetNotificationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotificationsAccessForOrganization  **
  - **IAM action:**  [notifications:GetNotificationsAccessForOrganization](#list_notifications-action-GetNotificationsAccessForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannels  **
  - **IAM action:**  [notifications:ListChannels](#list_notifications-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventRules  **
  - **IAM action:**  [notifications:ListEventRules](#list_notifications-action-ListEventRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedNotificationChannelAssociations  **
  - **IAM action:**  [notifications:ListManagedNotificationChannelAssociations](#list_notifications-action-ListManagedNotificationChannelAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedNotificationChildEvents  **
  - **IAM action:**  [notifications:ListManagedNotificationChildEvents](#list_notifications-action-ListManagedNotificationChildEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedNotificationConfigurations  **
  - **IAM action:**  [notifications:ListManagedNotificationConfigurations](#list_notifications-action-ListManagedNotificationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedNotificationEvents  **
  - **IAM action:**  [notifications:ListManagedNotificationEvents](#list_notifications-action-ListManagedNotificationEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemberAccounts  **
  - **IAM action:**  [notifications:ListMemberAccounts](#list_notifications-action-ListMemberAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotificationConfigurations  **
  - **IAM action:**  [notifications:ListNotificationConfigurations](#list_notifications-action-ListNotificationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotificationEvents  **
  - **IAM action:**  [notifications:ListNotificationEvents](#list_notifications-action-ListNotificationEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotificationHubs  **
  - **IAM action:**  [notifications:ListNotificationHubs](#list_notifications-action-ListNotificationHubs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationalUnits  **
  - **IAM action:**  [notifications:ListOrganizationalUnits](#list_notifications-action-ListOrganizationalUnits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [notifications:ListTagsForResource](#list_notifications-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterNotificationHub  **
  - **IAM action:**  [notifications:RegisterNotificationHub](#list_notifications-action-RegisterNotificationHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [notifications:TagResource](#list_notifications-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [notifications:UntagResource](#list_notifications-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEventRule  **
  - **IAM action:**  [notifications:UpdateEventRule](#list_notifications-action-UpdateEventRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotificationConfiguration  **
  - **IAM action:**  [notifications:UpdateNotificationConfiguration](#list_notifications-action-UpdateNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS User Notifications
<a name="list_notifications-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateChannel.html)  **
  - **Description:** Grants permission to associate a new Channel with a particular NotificationConfiguration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateManagedNotificationAccountContact](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateManagedNotificationAccountContact.html)  **
  - **Description:** Grants permission to associate an Account contact to a particular Managed Notification Configuration
  - **Resource types (\*required):** [ManagedNotificationConfiguration\*](#list_notifications-resource-ManagedNotificationConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateManagedNotificationAdditionalChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateManagedNotificationAdditionalChannel.html)  **
  - **Description:** Grants permission to associate a Channel to a particular Managed Notification Configuration
  - **Resource types (\*required):** [ManagedNotificationConfiguration\*](#list_notifications-resource-ManagedNotificationConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateOrganizationalUnit](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateOrganizationalUnit.html)  **
  - **Description:** Grants permission to associate an Organizational Unit to a particular Notification Configuration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_CreateEventRule.html)  **
  - **Description:** Grants permission to create a new EventRule, associating it with a NotificationConfiguration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_CreateNotificationConfiguration.html)  **
  - **Description:** Grants permission to create a NotificationConfiguration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_notifications-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_notifications-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeleteEventRule.html)  **
  - **Description:** Grants permission to delete an EventRule
  - **Resource types (\*required):** [EventRule\*](#list_notifications-resource-EventRule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeleteNotificationConfiguration.html)  **
  - **Description:** Grants permission to delete a NotificationConfiguration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterNotificationHub](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeregisterNotificationHub.html)  **
  - **Description:** Grants permission to deregister a NotificationHub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableNotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisableNotificationsAccessForOrganization.html)  **
  - **Description:** Grants permission to disable Service Trust for AWS User Notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DisassociateChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateChannel.html)  **
  - **Description:** Grants permission to remove a Channel from a NotificationConfiguration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateManagedNotificationAccountContact](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateManagedNotificationAccountContact.html)  **
  - **Description:** Grants permission to remove an Account contact from a Managed Notification Configuration
  - **Resource types (\*required):** [ManagedNotificationConfiguration\*](#list_notifications-resource-ManagedNotificationConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateManagedNotificationAdditionalChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateManagedNotificationAdditionalChannel.html)  **
  - **Description:** Grants permission to remove a Channel from a Managed Notification Configuration
  - **Resource types (\*required):** [ManagedNotificationConfiguration\*](#list_notifications-resource-ManagedNotificationConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateOrganizationalUnit](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateOrganizationalUnit.html)  **
  - **Description:** Grants permission to disassociate an Organizational Unit to a particular Notification Configuration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableNotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_EnableNotificationsAccessForOrganization.html)  **
  - **Description:** Grants permission to enable Service Trust for AWS User Notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetEventRule.html)  **
  - **Description:** Grants permission to get an EventRule
  - **Resource types (\*required):** [EventRule\*](#list_notifications-resource-EventRule)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedNotificationChildEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationChildEvent.html)  **
  - **Description:** Grants permission to get a Managed Notification Child Event
  - **Resource types (\*required):** [ManagedNotificationChildEvent\*](#list_notifications-resource-ManagedNotificationChildEvent)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationConfiguration.html)  **
  - **Description:** Grants permission to get a Managed Notification Configuration
  - **Resource types (\*required):** [ManagedNotificationConfiguration\*](#list_notifications-resource-ManagedNotificationConfiguration)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedNotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationEvent.html)  **
  - **Description:** Grants permission to get a Managed NotificationEvent
  - **Resource types (\*required):** [ManagedNotificationEvent\*](#list_notifications-resource-ManagedNotificationEvent)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationConfiguration.html)  **
  - **Description:** Grants permission to get a NotificationConfiguration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationEvent.html)  **
  - **Description:** Grants permission to get a NotificationEvent
  - **Resource types (\*required):** [NotificationEvent\*](#list_notifications-resource-NotificationEvent)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationsAccessForOrganization.html)  **
  - **Description:** Grants permission to read Service Trust for AWS User Notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListChannels](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListChannels.html)  **
  - **Description:** Grants permission to list Channels by NotificationConfiguration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEventRules](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListEventRules.html)  **
  - **Description:** Grants permission to list EventRules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedNotificationChannelAssociations](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationChannelAssociations.html)  **
  - **Description:** Grants permission to list Account contacts and Channels associated with a Managed Notification Configuration
  - **Resource types (\*required):** [ManagedNotificationConfiguration\*](#list_notifications-resource-ManagedNotificationConfiguration)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedNotificationChildEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationChildEvents.html)  **
  - **Description:** Grants permission to list Managed Notification Child Events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedNotificationConfigurations](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationConfigurations.html)  **
  - **Description:** Grants permission to list Managed Notification Configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedNotificationEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationEvents.html)  **
  - **Description:** Grants permission to list Managed Notification Events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMemberAccounts](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListMemberAccounts.html)  **
  - **Description:** Grants permission to list Member Accounts for a Notification Configuration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNotificationConfigurations](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationConfigurations.html)  **
  - **Description:** Grants permission to list NotificationConfigurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotificationEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationEvents.html)  **
  - **Description:** Grants permission to list NotificationEvents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotificationHubs](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationHubs.html)  **
  - **Description:** Grants permission to list NotificationHubs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationalUnits](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListOrganizationalUnits.html)  **
  - **Description:** Grants permission to list Organizational Units for a Notification Configuration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RegisterNotificationHub](https://docs.aws.amazon.com/notifications/latest/APIReference/API_RegisterNotificationHub.html)  **
  - **Description:** Grants permission to register a NotificationHub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_notifications-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_notifications-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateEventRule.html)  **
  - **Description:** Grants permission to update an EventRule
  - **Resource types (\*required):** [EventRule\*](#list_notifications-resource-EventRule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateNotificationConfiguration.html)  **
  - **Description:** Grants permission to update a NotificationConfiguration
  - **Resource types (\*required):** [NotificationConfiguration\*](#list_notifications-resource-NotificationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS User Notifications
<a name="list_notifications-permission-only-actions"></a>

The following actions are defined by AWS User Notifications but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetFeatureOptInStatus](https://docs.aws.amazon.com/notifications/latest/userguide/managing-notification-features.html)  | Grants permission to read the opt-in status of an AWS User Notification Service feature |  |   | Read | 
|   [PutFeatureOptInStatus](https://docs.aws.amazon.com/notifications/latest/userguide/managing-notification-features.html)  | Grants permission to update the opt-in status of an AWS User Notification Service feature |  |   | Write | 

## Resource types defined by AWS User Notifications
<a name="list_notifications-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [EventRule](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications::${Account}:configuration/${NotificationConfigurationId}/rule/${EventRuleId} |   | 
|  [ManagedNotificationChildEvent](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications::${Account}:managed-notification-configuration/category/${Category}/sub-category/${Subcategory}/event/${NotificationEventId}/child-event/${NotificationChildEventId} |   | 
|  [ManagedNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications::${Account}:managed-notification-configuration/category/${Category}/sub-category/${Subcategory} |   | 
|  [ManagedNotificationEvent](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications::${Account}:managed-notification-configuration/category/${Category}/sub-category/${Subcategory}/event/${NotificationEventId} |   | 
|  [NotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications::${Account}:configuration/${NotificationConfigurationId} | [aws:ResourceTag/${TagKey}](#list_notifications-aws_ResourceTag___TagKey_) | 
|  [NotificationEvent](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications:${Region}:${Account}:configuration/${NotificationConfigurationId}/event/${NotificationEventId} |   | 

## Condition keys for AWS User Notifications
<a name="list_notifications-policy-keys"></a>

AWS User Notifications defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 