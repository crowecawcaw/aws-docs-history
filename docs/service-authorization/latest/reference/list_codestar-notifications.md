

# Actions, resources, and condition keys for AWS CodeStar Notifications
<a name="list_codestar-notifications"></a>

AWS CodeStar Notifications (service prefix: `codestar-notifications`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codestar-notifications/codestar-notifications.json) for this service.

**Topics**
+ [API operations defined by AWS CodeStar Notifications](#list_codestar-notifications-operations)
+ [Actions defined by AWS CodeStar Notifications](#list_codestar-notifications-actions-as-permissions)
+ [Resource types defined by AWS CodeStar Notifications](#list_codestar-notifications-resources-for-iam-policies)
+ [Condition keys for AWS CodeStar Notifications](#list_codestar-notifications-policy-keys)

## API operations defined by AWS CodeStar Notifications
<a name="list_codestar-notifications-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codestar-notifications-actions-as-permissions).




- **   CreateNotificationRule  **
  - **IAM action:**  [codestar-notifications:CreateNotificationRule](#list_codestar-notifications-action-CreateNotificationRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-notifications:TagResource](#list_codestar-notifications-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteNotificationRule  **
  - **IAM action:**  [codestar-notifications:DeleteNotificationRule](#list_codestar-notifications-action-DeleteNotificationRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTarget  **
  - **IAM action:**  [codestar-notifications:DeleteTarget](#list_codestar-notifications-action-DeleteTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeNotificationRule  **
  - **IAM action:**  [codestar-notifications:DescribeNotificationRule](#list_codestar-notifications-action-DescribeNotificationRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEventTypes  **
  - **IAM action:**  [codestar-notifications:ListEventTypes](#list_codestar-notifications-action-ListEventTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotificationRules  **
  - **IAM action:**  [codestar-notifications:ListNotificationRules](#list_codestar-notifications-action-ListNotificationRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codestar-notifications:ListTagsForResource](#list_codestar-notifications-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargets  **
  - **IAM action:**  [codestar-notifications:ListTargets](#list_codestar-notifications-action-ListTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   Subscribe  **
  - **IAM action:**  [codestar-notifications:Subscribe](#list_codestar-notifications-action-Subscribe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [codestar-notifications:TagResource](#list_codestar-notifications-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   Unsubscribe  **
  - **IAM action:**  [codestar-notifications:Unsubscribe](#list_codestar-notifications-action-Unsubscribe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [codestar-notifications:UntagResource](#list_codestar-notifications-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateNotificationRule  **
  - **IAM action:**  [codestar-notifications:UpdateNotificationRule](#list_codestar-notifications-action-UpdateNotificationRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS CodeStar Notifications
<a name="list_codestar-notifications-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_CreateNotificationRule.html)  **
  - **Description:** Grants permission to create a notification rule for a resource
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)<br />[codestar-notifications:NotificationsForResource](#list_codestar-notifications-codestar-notifications_NotificationsForResource)
  - **Access level:** Write

- **   [DeleteNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DeleteNotificationRule.html)  **
  - **Description:** Grants permission to delete a notification rule for a resource
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)<br />[codestar-notifications:NotificationsForResource](#list_codestar-notifications-codestar-notifications_NotificationsForResource)
  - **Access level:** Write

- **   [DeleteTarget](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DeleteTarget.html)  **
  - **Description:** Grants permission to delete a target for a notification rule
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DescribeNotificationRule.html)  **
  - **Description:** Grants permission to get information about a notification rule
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)<br />[codestar-notifications:NotificationsForResource](#list_codestar-notifications-codestar-notifications_NotificationsForResource)
  - **Access level:** Read

- **   [ListEventTypes](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListEventTypes.html)  **
  - **Description:** Grants permission to list notifications event types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotificationRules](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListNotificationRules.html)  **
  - **Description:** Grants permission to list notification rules in an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags attached to a notification rule resource ARN
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)
  - **Access level:** List

- **   [ListTargets](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTargets.html)  **
  - **Description:** Grants permission to list the notification rule targets for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)
  - **Access level:** List

- **   [Subscribe](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Subscribe.html)  **
  - **Description:** Grants permission to create an association between a notification rule and an Amazon SNS topic
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)<br />[codestar-notifications:NotificationsForResource](#list_codestar-notifications-codestar-notifications_NotificationsForResource)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to attach resource tags to a notification rule resource ARN
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [Unsubscribe](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Unsubscribe.html)  **
  - **Description:** Grants permission to remove an association between a notification rule and an Amazon SNS topic
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)<br />[codestar-notifications:NotificationsForResource](#list_codestar-notifications-codestar-notifications_NotificationsForResource)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate resource tags from a notification rule resource ARN
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_UpdateNotificationRule.html)  **
  - **Description:** Grants permission to change a notification rule for a resource
  - **Resource types (\*required):** [notificationrule\*](#list_codestar-notifications-resource-notificationrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-notifications-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-notifications-aws_TagKeys)<br />[codestar-notifications:NotificationsForResource](#list_codestar-notifications-codestar-notifications_NotificationsForResource)
  - **Access level:** Write



## Resource types defined by AWS CodeStar Notifications
<a name="list_codestar-notifications-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [notificationrule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/security_iam_service-with-iam.html)  | arn:${Partition}:codestar-notifications:${Region}:${Account}:notificationrule/${NotificationRuleId} | [aws:ResourceTag/${TagKey}](#list_codestar-notifications-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CodeStar Notifications
<a name="list_codestar-notifications-policy-keys"></a>

AWS CodeStar Notifications defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 
|   [codestar-notifications:NotificationsForResource](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/security_iam_id-based-policy-examples.html)  | Filters access based on the ARN of the resource for which notifications are configured | ARN | 