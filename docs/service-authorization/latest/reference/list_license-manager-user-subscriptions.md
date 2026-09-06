

# Actions, resources, and condition keys for AWS License Manager User Subscriptions
<a name="list_license-manager-user-subscriptions"></a>

AWS License Manager User Subscriptions (service prefix: `license-manager-user-subscriptions`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/license-manager/latest/userguide/using-service-linked-roles.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/license-manager-user-subscriptions/license-manager-user-subscriptions.json) for this service.

**Topics**
+ [API operations defined by AWS License Manager User Subscriptions](#list_license-manager-user-subscriptions-operations)
+ [Actions defined by AWS License Manager User Subscriptions](#list_license-manager-user-subscriptions-actions-as-permissions)
+ [Resource types defined by AWS License Manager User Subscriptions](#list_license-manager-user-subscriptions-resources-for-iam-policies)
+ [Condition keys for AWS License Manager User Subscriptions](#list_license-manager-user-subscriptions-policy-keys)

## API operations defined by AWS License Manager User Subscriptions
<a name="list_license-manager-user-subscriptions-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_license-manager-user-subscriptions-actions-as-permissions).




- **   AssociateUser  **
  - **IAM action:**  [license-manager-user-subscriptions:AssociateUser](#list_license-manager-user-subscriptions-action-AssociateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager-user-subscriptions:TagResource](#list_license-manager-user-subscriptions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseServerEndpoint  **
  - **IAM action:**  [license-manager-user-subscriptions:CreateLicenseServerEndpoint](#list_license-manager-user-subscriptions-action-CreateLicenseServerEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager-user-subscriptions:TagResource](#list_license-manager-user-subscriptions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteLicenseServerEndpoint  **
  - **IAM action:**  [license-manager-user-subscriptions:DeleteLicenseServerEndpoint](#list_license-manager-user-subscriptions-action-DeleteLicenseServerEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterIdentityProvider  **
  - **IAM action:**  [license-manager-user-subscriptions:DeregisterIdentityProvider](#list_license-manager-user-subscriptions-action-DeregisterIdentityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateUser  **
  - **IAM action:**  [license-manager-user-subscriptions:DisassociateUser](#list_license-manager-user-subscriptions-action-DisassociateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListIdentityProviders  **
  - **IAM action:**  [license-manager-user-subscriptions:ListIdentityProviders](#list_license-manager-user-subscriptions-action-ListIdentityProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstances  **
  - **IAM action:**  [license-manager-user-subscriptions:ListInstances](#list_license-manager-user-subscriptions-action-ListInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseServerEndpoints  **
  - **IAM action:**  [license-manager-user-subscriptions:ListLicenseServerEndpoints](#list_license-manager-user-subscriptions-action-ListLicenseServerEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProductSubscriptions  **
  - **IAM action:**  [license-manager-user-subscriptions:ListProductSubscriptions](#list_license-manager-user-subscriptions-action-ListProductSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [license-manager-user-subscriptions:ListTagsForResource](#list_license-manager-user-subscriptions-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUserAssociations  **
  - **IAM action:**  [license-manager-user-subscriptions:ListUserAssociations](#list_license-manager-user-subscriptions-action-ListUserAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterIdentityProvider  **
  - **IAM action:**  [license-manager-user-subscriptions:RegisterIdentityProvider](#list_license-manager-user-subscriptions-action-RegisterIdentityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager-user-subscriptions:TagResource](#list_license-manager-user-subscriptions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartProductSubscription  **
  - **IAM action:**  [license-manager-user-subscriptions:StartProductSubscription](#list_license-manager-user-subscriptions-action-StartProductSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager-user-subscriptions:TagResource](#list_license-manager-user-subscriptions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StopProductSubscription  **
  - **IAM action:**  [license-manager-user-subscriptions:StopProductSubscription](#list_license-manager-user-subscriptions-action-StopProductSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [license-manager-user-subscriptions:TagResource](#list_license-manager-user-subscriptions-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [license-manager-user-subscriptions:UntagResource](#list_license-manager-user-subscriptions-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateIdentityProviderSettings  **
  - **IAM action:**  [license-manager-user-subscriptions:UpdateIdentityProviderSettings](#list_license-manager-user-subscriptions-action-UpdateIdentityProviderSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS License Manager User Subscriptions
<a name="list_license-manager-user-subscriptions-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateUser](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.html)  **
  - **Description:** Grants permission to associate a subscribed user to an instance launched with license manager user subscriptions products
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLicenseServerEndpoint](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_CreateLicenseServerEndpoint.html)  **
  - **Description:** Grants permission to create a license server endpoint for a given server type for a given Identity Provider
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLicenseServerEndpoint](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DeleteLicenseServerEndpoint.html)  **
  - **Description:** Grants permission to delete a license server endpoint for a given server type for a given Identity Provider
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-server-endpoint\*](#list_license-manager-user-subscriptions-resource-license-server-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterIdentityProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DeregisterIdentityProvider.html)  **
  - **Description:** Grants permission to deregister Microsoft Active Directory with license-manager-user-subscriptions for a product
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateUser](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DisassociateUser.html)  **
  - **Description:** Grants permission to disassociate a subscribed user from an instance launched with license manager user subscriptions products
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [instance-user\*](#list_license-manager-user-subscriptions-resource-instance-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListIdentityProviders](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListIdentityProviders.html)  **
  - **Description:** Grants permission to list all the identity providers on license manager user subscriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInstances](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListInstances.html)  **
  - **Description:** Grants permission to list all the instances launched with license manager user subscription products
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLicenseServerEndpoints](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListLicenseServerEndpoints.html)  **
  - **Description:** Grants permission to list license server endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProductSubscriptions](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListProductSubscriptions.html)  **
  - **Description:** Grants permission to lists all the product subscriptions for a product and identity provider
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a selected resource
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [instance-user\*](#list_license-manager-user-subscriptions-resource-instance-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-server-endpoint\*](#list_license-manager-user-subscriptions-resource-license-server-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [product-subscription\*](#list_license-manager-user-subscriptions-resource-product-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUserAssociations](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListUserAssociations.html)  **
  - **Description:** Grants permission to list all the users associated to an instance launched for a product
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RegisterIdentityProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_RegisterIdentityProvider.html)  **
  - **Description:** Grants permission to registers Microsoft Active Directory with license-manager-user-subscriptions for a product
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Access level:** Write

- **   [StartProductSubscription](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_StartProductSubscription.html)  **
  - **Description:** Grants permission to start product subscription for a user on a registered active directory for a product
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Access level:** Write

- **   [StopProductSubscription](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_StopProductSubscription.html)  **
  - **Description:** Grants permission to stop product subscription for a user on a registered active directory for a product
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [product-subscription\*](#list_license-manager-user-subscriptions-resource-product-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a selected resource
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Resource types (\*required):** [instance-user\*](#list_license-manager-user-subscriptions-resource-instance-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Resource types (\*required):** [license-server-endpoint\*](#list_license-manager-user-subscriptions-resource-license-server-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Resource types (\*required):** [product-subscription\*](#list_license-manager-user-subscriptions-resource-product-subscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-user-subscriptions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-user-subscriptions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a selected resource
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [instance-user\*](#list_license-manager-user-subscriptions-resource-instance-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-server-endpoint\*](#list_license-manager-user-subscriptions-resource-license-server-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [product-subscription\*](#list_license-manager-user-subscriptions-resource-product-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateIdentityProviderSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UpdateIdentityProviderSettings.html)  **
  - **Description:** Grants permission to update the identity provider configuration
  - **Resource types (\*required):** [identity-provider\*](#list_license-manager-user-subscriptions-resource-identity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS License Manager User Subscriptions
<a name="list_license-manager-user-subscriptions-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [identity-provider](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-provider.html)  | arn:${Partition}:license-manager-user-subscriptions:${Region}:${Account}:identity-provider/${IdentityProviderId} | [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_) | 
|  [instance-user](https://docs.aws.amazon.com/license-manager/latest/userguide/instance-user.html)  | arn:${Partition}:license-manager-user-subscriptions:${Region}:${Account}:instance-user/${InstanceUserId} | [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_) | 
|  [license-server-endpoint](https://docs.aws.amazon.com/license-manager/latest/userguide/license-server-endpoint.html)  | arn:${Partition}:license-manager-user-subscriptions:${Region}:${Account}:license-server-endpoint/${LicenseServerEndpointId} | [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_) | 
|  [product-subscription](https://docs.aws.amazon.com/license-manager/latest/userguide/product-subscription.html)  | arn:${Partition}:license-manager-user-subscriptions:${Region}:${Account}:product-subscription/${ProductSubscriptionId} | [aws:ResourceTag/${TagKey}](#list_license-manager-user-subscriptions-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS License Manager User Subscriptions
<a name="list_license-manager-user-subscriptions-policy-keys"></a>

AWS License Manager User Subscriptions defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by tag keys that are passed in the request | ArrayOfString | 