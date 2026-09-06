

# Actions, resources, and condition keys for AWS User Notifications Contacts
<a name="list_notificationscontacts"></a>

AWS User Notifications Contacts (service prefix: `notifications-contacts`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/notifications/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/notifications-contacts/notifications-contacts.json) for this service.

**Topics**
+ [API operations defined by AWS User Notifications Contacts](#list_notificationscontacts-operations)
+ [Actions defined by AWS User Notifications Contacts](#list_notificationscontacts-actions-as-permissions)
+ [Resource types defined by AWS User Notifications Contacts](#list_notificationscontacts-resources-for-iam-policies)
+ [Condition keys for AWS User Notifications Contacts](#list_notificationscontacts-policy-keys)

## API operations defined by AWS User Notifications Contacts
<a name="list_notificationscontacts-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_notificationscontacts-actions-as-permissions).




- **   ActivateEmailContact  **
  - **IAM action:**  [notifications-contacts:ActivateEmailContact](#list_notificationscontacts-action-ActivateEmailContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEmailContact  **
  - **IAM action:**  [notifications-contacts:CreateEmailContact](#list_notificationscontacts-action-CreateEmailContact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [notifications-contacts:TagResource](#list_notificationscontacts-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteEmailContact  **
  - **IAM action:**  [notifications-contacts:DeleteEmailContact](#list_notificationscontacts-action-DeleteEmailContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetEmailContact  **
  - **IAM action:**  [notifications-contacts:GetEmailContact](#list_notificationscontacts-action-GetEmailContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEmailContacts  **
  - **IAM action:**  [notifications-contacts:ListEmailContacts](#list_notificationscontacts-action-ListEmailContacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [notifications-contacts:ListTagsForResource](#list_notificationscontacts-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendActivationCode  **
  - **IAM action:**  [notifications-contacts:SendActivationCode](#list_notificationscontacts-action-SendActivationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [notifications-contacts:TagResource](#list_notificationscontacts-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [notifications-contacts:UntagResource](#list_notificationscontacts-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS User Notifications Contacts
<a name="list_notificationscontacts-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateEmailContact](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to activate the email contact associated with the given ARN if the provided code is valid
  - **Resource types (\*required):** [EmailContactResource\*](#list_notificationscontacts-resource-EmailContactResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEmailContact](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to create an email contact
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_notificationscontacts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_notificationscontacts-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteEmailContact](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to delete an email contact associated with the given ARN
  - **Resource types (\*required):** [EmailContactResource\*](#list_notificationscontacts-resource-EmailContactResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEmailContact](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to get an email contact associated with the given ARN
  - **Resource types (\*required):** [EmailContactResource\*](#list_notificationscontacts-resource-EmailContactResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEmailContacts](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to list email contacts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to get tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SendActivationCode](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to send an activation link to the email associated with the given ARN
  - **Resource types (\*required):** [EmailContactResource\*](#list_notificationscontacts-resource-EmailContactResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [EmailContactResource\*](#list_notificationscontacts-resource-EmailContactResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_notificationscontacts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_notificationscontacts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [EmailContactResource\*](#list_notificationscontacts-resource-EmailContactResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_notificationscontacts-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS User Notifications Contacts
<a name="list_notificationscontacts-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [EmailContactResource](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html)  | arn:${Partition}:notifications-contacts::${Account}:emailcontact/${EmailContactId} | [aws:ResourceTag/${TagKey}](#list_notificationscontacts-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS User Notifications Contacts
<a name="list_notificationscontacts-policy-keys"></a>

AWS User Notifications Contacts defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 