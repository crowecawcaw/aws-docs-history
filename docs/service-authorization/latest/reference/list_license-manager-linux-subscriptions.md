

# Actions, resources, and condition keys for AWS License Manager Linux Subscriptions Manager
<a name="list_license-manager-linux-subscriptions"></a>

AWS License Manager Linux Subscriptions Manager (service prefix: `license-manager-linux-subscriptions`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/license-manager/latest/userguide/using-service-linked-roles.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/license-manager-linux-subscriptions/license-manager-linux-subscriptions.json) for this service.

**Topics**
+ [API operations defined by AWS License Manager Linux Subscriptions Manager](#list_license-manager-linux-subscriptions-operations)
+ [Actions defined by AWS License Manager Linux Subscriptions Manager](#list_license-manager-linux-subscriptions-actions-as-permissions)
+ [Resource types defined by AWS License Manager Linux Subscriptions Manager](#list_license-manager-linux-subscriptions-resources-for-iam-policies)
+ [Condition keys for AWS License Manager Linux Subscriptions Manager](#list_license-manager-linux-subscriptions-policy-keys)

## API operations defined by AWS License Manager Linux Subscriptions Manager
<a name="list_license-manager-linux-subscriptions-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_license-manager-linux-subscriptions-actions-as-permissions).




- **   DeregisterSubscriptionProvider  **
  - **IAM action:**  [license-manager-linux-subscriptions:DeregisterSubscriptionProvider](#list_license-manager-linux-subscriptions-action-DeregisterSubscriptionProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetRegisteredSubscriptionProvider  **
  - **IAM action:**  [license-manager-linux-subscriptions:GetRegisteredSubscriptionProvider](#list_license-manager-linux-subscriptions-action-GetRegisteredSubscriptionProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceSettings  **
  - **IAM action:**  [license-manager-linux-subscriptions:GetServiceSettings](#list_license-manager-linux-subscriptions-action-GetServiceSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLinuxSubscriptionInstances  **
  - **IAM action:**  [license-manager-linux-subscriptions:ListLinuxSubscriptionInstances](#list_license-manager-linux-subscriptions-action-ListLinuxSubscriptionInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLinuxSubscriptions  **
  - **IAM action:**  [license-manager-linux-subscriptions:ListLinuxSubscriptions](#list_license-manager-linux-subscriptions-action-ListLinuxSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRegisteredSubscriptionProviders  **
  - **IAM action:**  [license-manager-linux-subscriptions:ListRegisteredSubscriptionProviders](#list_license-manager-linux-subscriptions-action-ListRegisteredSubscriptionProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [license-manager-linux-subscriptions:ListTagsForResource](#list_license-manager-linux-subscriptions-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterSubscriptionProvider  **
  - **IAM action:**  [license-manager-linux-subscriptions:RegisterSubscriptionProvider](#list_license-manager-linux-subscriptions-action-RegisterSubscriptionProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager-linux-subscriptions:TagResource](#list_license-manager-linux-subscriptions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [license-manager-linux-subscriptions:TagResource](#list_license-manager-linux-subscriptions-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [license-manager-linux-subscriptions:UntagResource](#list_license-manager-linux-subscriptions-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateServiceSettings  **
  - **IAM action:**  [license-manager-linux-subscriptions:UpdateServiceSettings](#list_license-manager-linux-subscriptions-action-UpdateServiceSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS License Manager Linux Subscriptions Manager
<a name="list_license-manager-linux-subscriptions-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DeregisterSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_DeregisterSubscriptionProvider.html)  **
  - **Description:** Grants permission to permanently delete a subscription provider in AWS License Manager
  - **Resource types (\*required):** [subscription-provider\*](#list_license-manager-linux-subscriptions-resource-subscription-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetRegisteredSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_GetRegisteredSubscriptionProvider.html)  **
  - **Description:** Grants permission to get a subscription provider in AWS License Manager
  - **Resource types (\*required):** [subscription-provider\*](#list_license-manager-linux-subscriptions-resource-subscription-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceSettings](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_GetServiceSettings.html)  **
  - **Description:** Grants permission to get the service settings for Linux subscriptions in AWS License Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLinuxSubscriptionInstances](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListLinuxSubscriptionInstances.html)  **
  - **Description:** Grants permission to list all instances with Linux subscriptions in AWS License Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLinuxSubscriptions](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListLinuxSubscriptions.html)  **
  - **Description:** Grants permission to list all Linux subscriptions in AWS License Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRegisteredSubscriptionProviders](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListRegisteredSubscriptionProviders.html)  **
  - **Description:** Grants permission to list subscription providers in AWS License Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a selected resource
  - **Resource types (\*required):** [subscription-provider\*](#list_license-manager-linux-subscriptions-resource-subscription-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RegisterSubscriptionProvider](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_RegisterSubscriptionProvider.html)  **
  - **Description:** Grants permission to create a new subscription provider in AWS License Manager
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-linux-subscriptions-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a selected resource
  - **Resource types (\*required):** [subscription-provider\*](#list_license-manager-linux-subscriptions-resource-subscription-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-linux-subscriptions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a selected resource
  - **Resource types (\*required):** [subscription-provider\*](#list_license-manager-linux-subscriptions-resource-subscription-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-linux-subscriptions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateServiceSettings](https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_UpdateServiceSettings.html)  **
  - **Description:** Grants permission to update the service settings for Linux subscriptions in AWS License Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS License Manager Linux Subscriptions Manager
<a name="list_license-manager-linux-subscriptions-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [subscription-provider](https://docs.aws.amazon.com/license-manager/latest/userguide/subscription-providers.html)  | arn:${Partition}:license-manager-linux-subscriptions:${Region}:${Account}:subscription-provider/${SubscriptionProviderId} | [aws:ResourceTag/${TagKey}](#list_license-manager-linux-subscriptions-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS License Manager Linux Subscriptions Manager
<a name="list_license-manager-linux-subscriptions-policy-keys"></a>

AWS License Manager Linux Subscriptions Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](identity-access-management.html)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by tag keys that are passed in the request | ArrayOfString | 