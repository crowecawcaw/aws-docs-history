

# Actions, resources, and condition keys for AWS Support Authorization
<a name="list_supportauthz"></a>

AWS Support Authorization (service prefix: `supportauthz`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awssupport/latest/user/support-authorization.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/supportauthz/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awssupport/latest/user/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/supportauthz/supportauthz.json) for this service.

**Topics**
+ [API operations defined by AWS Support Authorization](#list_supportauthz-operations)
+ [Actions defined by AWS Support Authorization](#list_supportauthz-actions-as-permissions)
+ [Permission-only actions for AWS Support Authorization](#list_supportauthz-permission-only-actions)
+ [Resource types defined by AWS Support Authorization](#list_supportauthz-resources-for-iam-policies)
+ [Condition keys for AWS Support Authorization](#list_supportauthz-policy-keys)

## API operations defined by AWS Support Authorization
<a name="list_supportauthz-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_supportauthz-actions-as-permissions).




- **   CreateSupportPermit  **
  - **IAM action:**  [supportauthz:CreateSupportPermit](#list_supportauthz-action-CreateSupportPermit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [supportauthz:TagResource](#list_supportauthz-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteSupportPermit  **
  - **IAM action:**  [supportauthz:DeleteSupportPermit](#list_supportauthz-action-DeleteSupportPermit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAction  **
  - **IAM action:**  [supportauthz:GetAction](#list_supportauthz-action-GetAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSupportPermit  **
  - **IAM action:**  [supportauthz:GetSupportPermit](#list_supportauthz-action-GetSupportPermit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActions  **
  - **IAM action:**  [supportauthz:ListActions](#list_supportauthz-action-ListActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSupportPermitRequests  **
  - **IAM action:**  [supportauthz:ListSupportPermitRequests](#list_supportauthz-action-ListSupportPermitRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSupportPermits  **
  - **IAM action:**  [supportauthz:ListSupportPermits](#list_supportauthz-action-ListSupportPermits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [supportauthz:ListTagsForResource](#list_supportauthz-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RejectSupportPermitRequest  **
  - **IAM action:**  [supportauthz:RejectSupportPermitRequest](#list_supportauthz-action-RejectSupportPermitRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [supportauthz:TagResource](#list_supportauthz-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [supportauthz:UntagResource](#list_supportauthz-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Support Authorization
<a name="list_supportauthz-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSupportPermit](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_CreateSupportPermit.html)  **
  - **Description:** Grants permission to create a support permit
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supportauthz-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_supportauthz-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSupportPermit](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_DeleteSupportPermit.html)  **
  - **Description:** Grants permission to delete a support permit
  - **Resource types (\*required):** [supportpermit\*](#list_supportauthz-resource-supportpermit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supportauthz-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAction](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_GetAction.html)  **
  - **Description:** Grants permission to retrieve details about a support action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSupportPermit](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_GetSupportPermit.html)  **
  - **Description:** Grants permission to retrieve a support permit
  - **Resource types (\*required):** [supportpermit\*](#list_supportauthz-resource-supportpermit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supportauthz-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListActions](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ListActions.html)  **
  - **Description:** Grants permission to list available support actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSupportPermitRequests](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ListSupportPermitRequests.html)  **
  - **Description:** Grants permission to list support permit requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSupportPermits](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ListSupportPermits.html)  **
  - **Description:** Grants permission to list support permits
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [supportpermit\*](#list_supportauthz-resource-supportpermit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supportauthz-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RejectSupportPermitRequest](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_RejectSupportPermitRequest.html)  **
  - **Description:** Grants permission to reject a support permit request
  - **Resource types (\*required):** [supportpermitrequest\*](#list_supportauthz-resource-supportpermitrequest)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [supportpermit\*](#list_supportauthz-resource-supportpermit)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supportauthz-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_supportauthz-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supportauthz-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [supportpermit\*](#list_supportauthz-resource-supportpermit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supportauthz-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supportauthz-aws_TagKeys)
  - **Access level:** Tagging, Write



## Permission-only actions for AWS Support Authorization
<a name="list_supportauthz-permission-only-actions"></a>

The following actions are defined by AWS Support Authorization but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [RegisterKey](https://docs.aws.amazon.com/awssupport/latest/user/support-authorization-getting-started.html)  | Grants permission to register a KMS key to use for a support permit |  |   | Write | 

## Resource types defined by AWS Support Authorization
<a name="list_supportauthz-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [supportpermit](https://docs.aws.amazon.com/awssupport/latest/user/support-authorization-permits.html)  | arn:${Partition}:supportauthz:${Region}:${Account}:supportpermit/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_supportauthz-aws_ResourceTag___TagKey_) | 
|  [supportpermitrequest](https://docs.aws.amazon.com/awssupport/latest/user/support-authorization-permit-requests.html)  | arn:${Partition}:supportauthz:${Region}:${Account}:supportpermitrequest/${ResourceId} |   | 

## Condition keys for AWS Support Authorization
<a name="list_supportauthz-policy-keys"></a>

AWS Support Authorization defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key-value pair in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key-value pair assigned to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request | ArrayOfString | 