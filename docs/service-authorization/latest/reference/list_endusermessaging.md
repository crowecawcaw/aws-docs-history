

# Actions, resources, and condition keys for AWS End User Messaging
<a name="list_endusermessaging"></a>

AWS End User Messaging (service prefix: `end-user-messaging`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/end-user-messaging/latest/userguide/what-is-service.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/IAM/end-user-messaging/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/end-user-messaging/end-user-messaging.json) for this service.

**Topics**
+ [Actions defined by AWS End User Messaging](#list_endusermessaging-actions-as-permissions)
+ [Resource types defined by AWS End User Messaging](#list_endusermessaging-resources-for-iam-policies)
+ [Condition keys for AWS End User Messaging](#list_endusermessaging-policy-keys)

## Actions defined by AWS End User Messaging
<a name="list_endusermessaging-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateBrandProfile.html)  **
  - **Description:** Grants permission to create a brand profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_endusermessaging-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBrandProfileAttributes](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateBrandProfileAttributes.html)  **
  - **Description:** Grants permission to create attributes for a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBrandProfileFromRegistration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateBrandProfileFromRegistration.html)  **
  - **Description:** Grants permission to create a new brand profile populated from an existing registration via Bedrock mapping
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_endusermessaging-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNotifyCodeConfiguration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateNotifyCodeConfiguration.html)  **
  - **Description:** Grants permission to create a notify code configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_endusermessaging-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistrationsFromBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateRegistrationsFromBrandProfile.html)  **
  - **Description:** Grants permission to create DRAFT registrations pre-filled from brand profile attributes via Bedrock mapping
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_DeleteBrandProfile.html)  **
  - **Description:** Grants permission to delete a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBrandProfileAttribute](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_DeleteBrandProfileAttribute.html)  **
  - **Description:** Grants permission to delete a brand profile attribute
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotifyCodeConfiguration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_DeleteNotifyCodeConfiguration.html)  **
  - **Description:** Grants permission to delete a notify code configuration
  - **Resource types (\*required):** [notify-code-configuration\*](#list_endusermessaging-resource-notify-code-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetBrandProfile.html)  **
  - **Description:** Grants permission to get a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBrandProfileAttribute](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetBrandProfileAttribute.html)  **
  - **Description:** Grants permission to get a brand profile attribute
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetJob.html)  **
  - **Description:** Grants permission to get the details of an asynchronous job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotifyCodeConfiguration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetNotifyCodeConfiguration.html)  **
  - **Description:** Grants permission to get a notify code configuration
  - **Resource types (\*required):** [notify-code-configuration\*](#list_endusermessaging-resource-notify-code-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBrandProfileAttributes](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListBrandProfileAttributes.html)  **
  - **Description:** Grants permission to list the attributes for a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBrandProfiles](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListBrandProfiles.html)  **
  - **Description:** Grants permission to list brand profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListJobs.html)  **
  - **Description:** Grants permission to list asynchronous jobs in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotifyCodeConfigurations](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListNotifyCodeConfigurations.html)  **
  - **Description:** Grants permission to list notify code configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegistrationsFromBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListRegistrationsFromBrandProfile.html)  **
  - **Description:** Grants permission to list the registrations created from a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [brand-profile](#list_endusermessaging-resource-brand-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notify-code-configuration](#list_endusermessaging-resource-notify-code-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SendNotifyCodeVerification](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_SendNotifyCodeVerification.html)  **
  - **Description:** Grants permission to send a notify code verification
  - **Resource types (\*required):** [notify-code-configuration](#list_endusermessaging-resource-notify-code-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [brand-profile](#list_endusermessaging-resource-brand-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_endusermessaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Resource types (\*required):** [notify-code-configuration](#list_endusermessaging-resource-notify-code-configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_endusermessaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [brand-profile](#list_endusermessaging-resource-brand-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Resource types (\*required):** [notify-code-configuration](#list_endusermessaging-resource-notify-code-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_endusermessaging-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateBrandProfile.html)  **
  - **Description:** Grants permission to update a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrandProfileAttribute](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateBrandProfileAttribute.html)  **
  - **Description:** Grants permission to update a brand profile attribute
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrandProfileFromRegistration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateBrandProfileFromRegistration.html)  **
  - **Description:** Grants permission to update a brand profile from a registration
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNotifyCodeConfiguration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateNotifyCodeConfiguration.html)  **
  - **Description:** Grants permission to update a notify code configuration
  - **Resource types (\*required):** [notify-code-configuration\*](#list_endusermessaging-resource-notify-code-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegistrationsFromBrandProfile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateRegistrationsFromBrandProfile.html)  **
  - **Description:** Grants permission to update registrations from a brand profile
  - **Resource types (\*required):** [brand-profile\*](#list_endusermessaging-resource-brand-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateNotifyCodeVerification](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ValidateNotifyCodeVerification.html)  **
  - **Description:** Grants permission to validate a notify code verification
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS End User Messaging
<a name="list_endusermessaging-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [brand-profile](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_BrandProfileInfo.html)  | arn:${Partition}:end-user-messaging:${Region}:${Account}:brand-profile/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_) | 
|  [notify-code-configuration](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_NotifyCodeConfiguration.html)  | arn:${Partition}:end-user-messaging:${Region}:${Account}:notify-code-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_endusermessaging-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS End User Messaging
<a name="list_endusermessaging-policy-keys"></a>

AWS End User Messaging defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 