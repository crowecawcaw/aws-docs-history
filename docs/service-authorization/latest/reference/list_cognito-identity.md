

# Actions, resources, and condition keys for Amazon Cognito Identity
<a name="list_cognito-identity"></a>

Amazon Cognito Identity (service prefix: `cognito-identity`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cognito/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cognito-identity/cognito-identity.json) for this service.

**Topics**
+ [API operations defined by Amazon Cognito Identity](#list_cognito-identity-operations)
+ [Actions defined by Amazon Cognito Identity](#list_cognito-identity-actions-as-permissions)
+ [Resource types defined by Amazon Cognito Identity](#list_cognito-identity-resources-for-iam-policies)
+ [Condition keys for Amazon Cognito Identity](#list_cognito-identity-policy-keys)

## API operations defined by Amazon Cognito Identity
<a name="list_cognito-identity-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cognito-identity-actions-as-permissions).




- **   CreateIdentityPool  **
  - **IAM action:**  [cognito-identity:CreateIdentityPool](#list_cognito-identity-action-CreateIdentityPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cognito-identity:TagResource](#list_cognito-identity-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteIdentities  **
  - **IAM action:**  [cognito-identity:DeleteIdentities](#list_cognito-identity-action-DeleteIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdentityPool  **
  - **IAM action:**  [cognito-identity:DeleteIdentityPool](#list_cognito-identity-action-DeleteIdentityPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeIdentity  **
  - **IAM action:**  [cognito-identity:DescribeIdentity](#list_cognito-identity-action-DescribeIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIdentityPool  **
  - **IAM action:**  [cognito-identity:DescribeIdentityPool](#list_cognito-identity-action-DescribeIdentityPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCredentialsForIdentity  **
  - **IAM action:**  [cognito-identity:GetCredentialsForIdentity](#list_cognito-identity-action-GetCredentialsForIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetId  **
  - **IAM action:**  [cognito-identity:GetId](#list_cognito-identity-action-GetId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetIdentityPoolRoles  **
  - **IAM action:**  [cognito-identity:GetIdentityPoolRoles](#list_cognito-identity-action-GetIdentityPoolRoles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpenIdToken  **
  - **IAM action:**  [cognito-identity:GetOpenIdToken](#list_cognito-identity-action-GetOpenIdToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpenIdTokenForDeveloperIdentity  **
  - **IAM action:**  [cognito-identity:GetOpenIdTokenForDeveloperIdentity](#list_cognito-identity-action-GetOpenIdTokenForDeveloperIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrincipalTagAttributeMap  **
  - **IAM action:**  [cognito-identity:GetPrincipalTagAttributeMap](#list_cognito-identity-action-GetPrincipalTagAttributeMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListIdentities  **
  - **IAM action:**  [cognito-identity:ListIdentities](#list_cognito-identity-action-ListIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityPools  **
  - **IAM action:**  [cognito-identity:ListIdentityPools](#list_cognito-identity-action-ListIdentityPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cognito-identity:ListTagsForResource](#list_cognito-identity-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   LookupDeveloperIdentity  **
  - **IAM action:**  [cognito-identity:LookupDeveloperIdentity](#list_cognito-identity-action-LookupDeveloperIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   MergeDeveloperIdentities  **
  - **IAM action:**  [cognito-identity:MergeDeveloperIdentities](#list_cognito-identity-action-MergeDeveloperIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityPoolRoles  **
  - **IAM action:**  [cognito-identity:SetIdentityPoolRoles](#list_cognito-identity-action-SetIdentityPoolRoles)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SetPrincipalTagAttributeMap  **
  - **IAM action:**  [cognito-identity:SetPrincipalTagAttributeMap](#list_cognito-identity-action-SetPrincipalTagAttributeMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [cognito-identity:TagResource](#list_cognito-identity-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UnlinkDeveloperIdentity  **
  - **IAM action:**  [cognito-identity:UnlinkDeveloperIdentity](#list_cognito-identity-action-UnlinkDeveloperIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnlinkIdentity  **
  - **IAM action:**  [cognito-identity:UnlinkIdentity](#list_cognito-identity-action-UnlinkIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [cognito-identity:UntagResource](#list_cognito-identity-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateIdentityPool  **
  - **IAM action:**  [cognito-identity:TagResource](#list_cognito-identity-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cognito-identity:UntagResource](#list_cognito-identity-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cognito-identity:UpdateIdentityPool](#list_cognito-identity-action-UpdateIdentityPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by Amazon Cognito Identity
<a name="list_cognito-identity-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_CreateIdentityPool.html)  **
  - **Description:** Grants permission to create a new identity pool
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cognito-identity-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cognito-identity-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DeleteIdentities.html)  **
  - **Description:** Grants permission to delete identities from an identity pool. You can specify a list of 1-60 identities that you want to delete
  - **Resource types (\*required):** 
  - **Condition keys:** [cognito-identity:IdentityPoolArn](#list_cognito-identity-cognito-identity_IdentityPoolArn)
  - **Access level:** Write

- **   [DeleteIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DeleteIdentityPool.html)  **
  - **Description:** Grants permission to delete a user pool. Once a pool is deleted, users will not be able to authenticate with the pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DescribeIdentity.html)  **
  - **Description:** Grants permission to return metadata related to the given identity, including when the identity was created and any associated linked logins
  - **Resource types (\*required):** 
  - **Condition keys:** [cognito-identity:IdentityPoolArn](#list_cognito-identity-cognito-identity_IdentityPoolArn)
  - **Access level:** Read

- **   [DescribeIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DescribeIdentityPool.html)  **
  - **Description:** Grants permission to get details about a particular identity pool, including the pool name, ID description, creation date, and current number of users
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCredentialsForIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html)  **
  - **Description:** Grants permission to return credentials for the provided identity ID
  - **Resource types (\*required):** 
  - **Condition keys:** [cognito-identity-auth:AccountId](#list_cognito-identity-cognito-identity-auth_AccountId)<br />[cognito-identity-auth:IdentityPoolArn](#list_cognito-identity-cognito-identity-auth_IdentityPoolArn)<br />[cognito-identity-unauth:AccountId](#list_cognito-identity-cognito-identity-unauth_AccountId)<br />[cognito-identity-unauth:IdentityPoolArn](#list_cognito-identity-cognito-identity-unauth_IdentityPoolArn)
  - **Access level:** Read

- **   [GetId](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetId.html)  **
  - **Description:** Grants permission to generate (or retrieve) a Cognito ID. Supplying multiple logins will create an implicit linked account
  - **Resource types (\*required):** 
  - **Condition keys:** [cognito-identity-auth:AccountId](#list_cognito-identity-cognito-identity-auth_AccountId)<br />[cognito-identity-auth:IdentityPoolArn](#list_cognito-identity-cognito-identity-auth_IdentityPoolArn)<br />[cognito-identity-unauth:AccountId](#list_cognito-identity-cognito-identity-unauth_AccountId)<br />[cognito-identity-unauth:IdentityPoolArn](#list_cognito-identity-cognito-identity-unauth_IdentityPoolArn)
  - **Access level:** Write

- **   [GetIdentityPoolAnalytics](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolAnalytics.html)  **
  - **Description:** Grants permission to get analytics data about the total current identity count for all identity pool identity provider (IdPs)
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityPoolDailyAnalytics](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolDailyAnalytics.html)  **
  - **Description:** Grants permission to get analytics data about the number of new identities and total identities for all identity pool identity providers (IdPs)
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolRoles.html)  **
  - **Description:** Grants permission to get the roles for an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityProviderDailyAnalytics](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityProviderDailyAnalytics.html)  **
  - **Description:** Grants permission to get analytics data about the number of new identities and total identities for one identity pool identity provider (IdPs)
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOpenIdToken](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdToken.html)  **
  - **Description:** Grants permission to get an OpenID token, using a known Cognito ID
  - **Resource types (\*required):** 
  - **Condition keys:** [cognito-identity-auth:AccountId](#list_cognito-identity-cognito-identity-auth_AccountId)<br />[cognito-identity-auth:IdentityPoolArn](#list_cognito-identity-cognito-identity-auth_IdentityPoolArn)<br />[cognito-identity-unauth:AccountId](#list_cognito-identity-cognito-identity-unauth_AccountId)<br />[cognito-identity-unauth:IdentityPoolArn](#list_cognito-identity-cognito-identity-unauth_IdentityPoolArn)
  - **Access level:** Read

- **   [GetOpenIdTokenForDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.html)  **
  - **Description:** Grants permission to register (or retrieve) a Cognito IdentityId and an OpenID Connect token for a user authenticated by your backend authentication process
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPrincipalTagAttributeMap](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetPrincipalTagAttributeMap.html)  **
  - **Description:** Grants permission to get the principal tags for an identity pool and provider
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListIdentities.html)  **
  - **Description:** Grants permission to list the identities in an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdentityPools](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListIdentityPools.html)  **
  - **Description:** Grants permission to list all of the Cognito identity pools registered for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags that are assigned to an Amazon Cognito identity pool
  - **Resource types (\*required):** [identitypool](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [LookupDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_LookupDeveloperIdentity.html)  **
  - **Description:** Grants permission to retrieve the IdentityId associated with a DeveloperUserIdentifier or the list of DeveloperUserIdentifiers associated with an IdentityId for an existing identity
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [MergeDeveloperIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_MergeDeveloperIdentities.html)  **
  - **Description:** Grants permission to merge two users having different IdentityIds, existing in the same identity pool, and identified by the same developer provider
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_SetIdentityPoolRoles.html)  **
  - **Description:** Grants permission to set the roles for an identity pool. These roles are used when making calls to GetCredentialsForIdentity action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetPrincipalTagAttributeMap](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_SetPrincipalTagAttributeMap.html)  **
  - **Description:** Grants permission to set the principal tags for an identity pool and provider. These tags are used when making calls to GetOpenIdToken action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign a set of tags to an Amazon Cognito identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cognito-identity-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cognito-identity-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnlinkDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnlinkDeveloperIdentity.html)  **
  - **Description:** Grants permission to unlink a DeveloperUserIdentifier from an existing identity
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UnlinkIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnlinkIdentity.html)  **
  - **Description:** Grants permission to unlink a federated identity from an existing account
  - **Resource types (\*required):** 
  - **Condition keys:** [cognito-identity-auth:AccountId](#list_cognito-identity-cognito-identity-auth_AccountId)<br />[cognito-identity-auth:IdentityPoolArn](#list_cognito-identity-cognito-identity-auth_IdentityPoolArn)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from an Amazon Cognito identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cognito-identity-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UpdateIdentityPool.html)  **
  - **Description:** Grants permission to update an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-identity-resource-identitypool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Cognito Identity
<a name="list_cognito-identity-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [identitypool](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)  | arn:${Partition}:cognito-identity:${Region}:${Account}:identitypool/${IdentityPoolId} | [aws:ResourceTag/${TagKey}](#list_cognito-identity-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Cognito Identity
<a name="list_cognito-identity-policy-keys"></a>

Amazon Cognito Identity defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a key that is present in the request | ArrayOfString | 
|   [cognito-identity-auth:AccountId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-auth-account-id)  | Filters access by the owning AWS account ID for identity pool authenticated users. Applies to unauthenticated (public) API operations | String | 
|   [cognito-identity-auth:IdentityPoolArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-auth-identity-pool-arn)  | Filters access by the identity pool ID for a given authenticated-user identity ID. Applies to unauthenticated (public) API operations | ARN | 
|   [cognito-identity-unauth:AccountId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-unauth-account-id)  | Filters access by the owning AWS account ID of an identity pool for identity pool guest users. Applies to unauthenticated (public) API operations | String | 
|   [cognito-identity-unauth:IdentityPoolArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-unauth-identity-pool-arn)  | Filters access by the identity pool ID for a given guest-user identity ID. Applies to unauthenticated (public) API operations | ARN | 
|   [cognito-identity:IdentityPoolArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-identity-pool-arn)  | Filters access by the identity pool ID for a given identity ID for DeleteIdentities and DescribeIdentity | ARN | 