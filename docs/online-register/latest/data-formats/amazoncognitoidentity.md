

# Data retrieval APIs for Amazon Cognito Identity
<a name="amazoncognitoidentity"></a>

Amazon Cognito Identity provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cognito-identity-DescribeIdentity"></a>[DescribeIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DescribeIdentity.html) | Return metadata related to the given identity, including when the identity was created and any associated linked logins | Read | 
| <a name="cognito-identity-DescribeIdentityPool"></a>[DescribeIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DescribeIdentityPool.html) | Get details about a particular identity pool, including the pool name, ID description, creation date, and current number of users | Read | 
| <a name="cognito-identity-GetCredentialsForIdentity"></a>[GetCredentialsForIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html) | Return credentials for the provided identity ID | Read | 
| <a name="cognito-identity-GetIdentityPoolAnalytics"></a>[GetIdentityPoolAnalytics](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolAnalytics.html) | Get analytics data about the total current identity count for all identity pool identity provider (IdPs) | Read | 
| <a name="cognito-identity-GetIdentityPoolDailyAnalytics"></a>[GetIdentityPoolDailyAnalytics](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolDailyAnalytics.html) | Get analytics data about the number of new identities and total identities for all identity pool identity providers (IdPs) | Read | 
| <a name="cognito-identity-GetIdentityPoolRoles"></a>[GetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolRoles.html) | Get the roles for an identity pool | Read | 
| <a name="cognito-identity-GetIdentityProviderDailyAnalytics"></a>[GetIdentityProviderDailyAnalytics](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityProviderDailyAnalytics.html) | Get analytics data about the number of new identities and total identities for one identity pool identity provider (IdPs) | Read | 
| <a name="cognito-identity-GetOpenIdToken"></a>[GetOpenIdToken](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdToken.html) | Get an OpenID token, using a known Cognito ID | Read | 
| <a name="cognito-identity-GetOpenIdTokenForDeveloperIdentity"></a>[GetOpenIdTokenForDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.html) | Register (or retrieve) a Cognito IdentityId and an OpenID Connect token for a user authenticated by your backend authentication process | Read | 
| <a name="cognito-identity-GetPrincipalTagAttributeMap"></a>[GetPrincipalTagAttributeMap](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetPrincipalTagAttributeMap.html) | Get the principal tags for an identity pool and provider | Read | 
| <a name="cognito-identity-ListIdentities"></a>[ListIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListIdentities.html) | List the identities in an identity pool | List | 
| <a name="cognito-identity-ListIdentityPools"></a>[ListIdentityPools](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListIdentityPools.html) | List all of the Cognito identity pools registered for your account | List | 
| <a name="cognito-identity-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListTagsForResource.html) | List the tags that are assigned to an Amazon Cognito identity pool | Read | 
| <a name="cognito-identity-LookupDeveloperIdentity"></a>[LookupDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_LookupDeveloperIdentity.html) | Retrieve the IdentityId associated with a DeveloperUserIdentifier or the list of DeveloperUserIdentifiers associated with an IdentityId for an existing identity | Read | 