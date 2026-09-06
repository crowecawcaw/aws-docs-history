

# Actions, resources, and condition keys for Amazon CodeCatalyst
<a name="list_codecatalyst"></a>

Amazon CodeCatalyst (service prefix: `codecatalyst`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codecatalyst/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codecatalyst/codecatalyst.json) for this service.

**Topics**
+ [Actions defined by Amazon CodeCatalyst](#list_codecatalyst-actions-as-permissions)
+ [Permission-only actions for Amazon CodeCatalyst](#list_codecatalyst-permission-only-actions)
+ [Resource types defined by Amazon CodeCatalyst](#list_codecatalyst-resources-for-iam-policies)
+ [Condition keys for Amazon CodeCatalyst](#list_codecatalyst-policy-keys)

## Actions defined by Amazon CodeCatalyst
<a name="list_codecatalyst-actions-as-permissions"></a>

Amazon CodeCatalyst has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for Amazon CodeCatalyst
<a name="list_codecatalyst-permission-only-actions"></a>

The following actions are defined by Amazon CodeCatalyst but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AcceptConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to accept a request to connect this account to an Amazon CodeCatalyst space
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecatalyst-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Access level:** Write

- **   [AssociateIamRoleToConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to associate an IAM role to a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateIdentityCenterApplicationToSpace](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to associate an IAM Identity Center application with an Amazon CodeCatalyst space
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateIdentityToIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to associate an identity with an IAM Identity Center application for an Amazon CodeCatalyst space
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateIdentitiesToIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to associate multiple identities with an IAM Identity Center application for an Amazon CodeCatalyst space
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateIdentitiesFromIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to disassociate multiple identities from an IAM Identity Center application for an Amazon CodeCatalyst space
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to create an IAM Identity Center application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecatalyst-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSpace](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to create an Amazon CodeCatalyst space
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecatalyst-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSpaceAdminRoleAssignment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to create an administrator role assignment for a given Amazon CodeCatalyst space and IAM Identity Center application
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to delete an IAM Identity Center application
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateIamRoleFromConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to disassociate an IAM role from a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateIdentityCenterApplicationFromSpace](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to disassociate an IAM Identity Center application from an Amazon CodeCatalyst space
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateIdentityFromIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to disassociate an identity from an IAM Identity Center application for an Amazon CodeCatalyst space
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBillingAuthorization](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to describe the billing authorization for a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to get a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to get information about an IAM Identity Center application
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPendingConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to get a pending request to connect this account to an Amazon CodeCatalyst space
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnections](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to list connections that are not pending
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIamRolesForConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to list IAM roles associated with a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdentityCenterApplications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to view a list of all IAM Identity Center applications in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIdentityCenterApplicationsForSpace](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to view a list of IAM Identity Center applications by Amazon CodeCatalyst space
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSpacesForIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to view a list of Amazon CodeCatalyst spaces by IAM Identity Center application
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to list tags for an Amazon CodeCatalyst resource
  - **Resource types (\*required):** [connections](#list_codecatalyst-resource-connections) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [identity-center-applications](#list_codecatalyst-resource-identity-center-applications) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutBillingAuthorization](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to create or update the billing authorization for a connection
  - **Resource types (\*required):** [connections\*](#list_codecatalyst-resource-connections)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectConnection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to reject a request to connect this account to an Amazon CodeCatalyst space
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SynchronizeIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to synchronize an IAM Identity Center application with the backing identity store
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to tag an Amazon CodeCatalyst resource
  - **Resource types (\*required):** [connections](#list_codecatalyst-resource-connections) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecatalyst-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Resource types (\*required):** [identity-center-applications](#list_codecatalyst-resource-identity-center-applications) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecatalyst-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-connections)  **
  - **Description:** Grants permission to untag an Amazon CodeCatalyst resource
  - **Resource types (\*required):** [connections](#list_codecatalyst-resource-connections) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Resource types (\*required):** [identity-center-applications](#list_codecatalyst-resource-identity-center-applications) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecatalyst-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateIdentityCenterApplication](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html#permissions-reference-applications)  **
  - **Description:** Grants permission to update an IAM Identity Center application
  - **Resource types (\*required):** [identity-center-applications\*](#list_codecatalyst-resource-identity-center-applications)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon CodeCatalyst
<a name="list_codecatalyst-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [connections](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#)  | arn:${Partition}:codecatalyst:${Region}:${Account}:/connections/${ConnectionId} | [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_) | 
|  [identity-center-applications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#)  | arn:${Partition}:codecatalyst:${Region}:${Account}:/identity-center-applications/${IdentityCenterApplicationId} | [aws:ResourceTag/${TagKey}](#list_codecatalyst-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#)  | arn:${Partition}:codecatalyst:::space/${SpaceId}/project/${ProjectId} |   | 
|  [space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#)  | arn:${Partition}:codecatalyst:::space/${SpaceId} |   | 

## Condition keys for Amazon CodeCatalyst
<a name="list_codecatalyst-policy-keys"></a>

Amazon CodeCatalyst defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 