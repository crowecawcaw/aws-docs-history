

# Actions, resources, and condition keys for AWS Signin
<a name="list_signin"></a>

AWS Signin (service prefix: `signin`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/signin/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/signin/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/signin/signin.json) for this service.

**Topics**
+ [API operations defined by AWS Signin](#list_signin-operations)
+ [Actions defined by AWS Signin](#list_signin-actions-as-permissions)
+ [Permission-only actions for AWS Signin](#list_signin-permission-only-actions)
+ [Resource types defined by AWS Signin](#list_signin-resources-for-iam-policies)
+ [Condition keys for AWS Signin](#list_signin-policy-keys)

## API operations defined by AWS Signin
<a name="list_signin-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_signin-actions-as-permissions).




- **   CreateOAuth2Token  **
  - **IAM action:**  [signin:CreateOAuth2Token](#list_signin-action-CreateOAuth2Token) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateOAuth2TokenWithIAM  **
  - **IAM action:**  [signin:CreateOAuth2Token](#list_signin-action-CreateOAuth2Token) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DeleteConsoleAuthorizationConfiguration  **
  - **IAM action:**  [signin:DeleteConsoleAuthorizationConfiguration](#list_signin-action-DeleteConsoleAuthorizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePermissionStatement  **
  - **IAM action:**  [signin:DeleteResourcePermissionStatement](#list_signin-action-DeleteResourcePermissionStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetConsoleAuthorizationConfiguration  **
  - **IAM action:**  [signin:GetConsoleAuthorizationConfiguration](#list_signin-action-GetConsoleAuthorizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [signin:GetResourcePolicy](#list_signin-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   IntrospectOAuth2TokenWithIAM  **
  - **IAM action:**  [signin:IntrospectOAuth2Token](#list_signin-action-IntrospectOAuth2Token) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResourcePermissionStatements  **
  - **IAM action:**  [signin:ListResourcePermissionStatements](#list_signin-action-ListResourcePermissionStatements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutConsoleAuthorizationConfiguration  **
  - **IAM action:**  [signin:PutConsoleAuthorizationConfiguration](#list_signin-action-PutConsoleAuthorizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePermissionStatement  **
  - **IAM action:**  [signin:PutResourcePermissionStatement](#list_signin-action-PutResourcePermissionStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeOAuth2TokenWithIAM  **
  - **IAM action:**  [signin:RevokeOAuth2Token](#list_signin-action-RevokeOAuth2Token) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Signin
<a name="list_signin-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [Authenticate](https://docs.aws.amazon.com/signin/latest/APIReference/API_Authenticate.html)  **
  - **Description:** Grants permission to authenticate to the AWS Management Console
  - **Resource types (\*required):** [console\*](#list_signin-resource-console)
  - **Condition keys:** [signin:PrincipalArn](#list_signin-signin_PrincipalArn)
  - **Access level:** Read

- **   [AuthorizeOAuth2Access](https://docs.aws.amazon.com/signin/latest/APIReference/API_AuthorizeOAuth2Access.html)  **
  - **Description:** Grants permission to authenticate through a browser and obtain an OAuth 2.0 authorization code for credential exchange
  - **Resource types (\*required):** [console\*](#list_signin-resource-console) / **Condition keys:**  
  - **Resource types (\*required):** [oauth2-public-client-localhost\*](#list_signin-resource-oauth2-public-client-localhost) / **Condition keys:** [signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Resource types (\*required):** [oauth2-public-client-remote\*](#list_signin-resource-oauth2-public-client-remote) / **Condition keys:** [signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Resource types (\*required):** [oauth2-resource-service-principal\*](#list_signin-resource-oauth2-resource-service-principal) / **Condition keys:** [signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Access level:** Read

- **   [CreateOAuth2PublicClient](https://docs.aws.amazon.com/signin/latest/APIReference/API_CreateOAuth2PublicClient.html)  **
  - **Description:** Grants permission to dynamically register an OAuth 2.0 public client for use with AWS Sign-In
  - **Resource types (\*required):** [oauth2-public-client-registration\*](#list_signin-resource-oauth2-public-client-registration)
  - **Condition keys:** [signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Access level:** Write

- **   [CreateOAuth2Token](https://docs.aws.amazon.com/signin/latest/APIReference/API_CreateOAuth2Token.html)  **
  - **Description:** Grants permission to exchange an authorization code for OAuth 2.0 access token and refresh token that can be used to access AWS services from developer tools and applications
  - **Resource types (\*required):** [console\*](#list_signin-resource-console) / **Condition keys:**  
  - **Resource types (\*required):** [oauth2-public-client-localhost\*](#list_signin-resource-oauth2-public-client-localhost) / **Condition keys:** [signin:OAuthClientAuthentication](#list_signin-signin_OAuthClientAuthentication)<br />[signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthGrantType](#list_signin-signin_OAuthGrantType)<br />[signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Resource types (\*required):** [oauth2-public-client-remote\*](#list_signin-resource-oauth2-public-client-remote) / **Condition keys:** [signin:OAuthClientAuthentication](#list_signin-signin_OAuthClientAuthentication)<br />[signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthGrantType](#list_signin-signin_OAuthGrantType)<br />[signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Resource types (\*required):** [oauth2-resource-service-principal\*](#list_signin-resource-oauth2-resource-service-principal) / **Condition keys:** [signin:OAuthClientAuthentication](#list_signin-signin_OAuthClientAuthentication)<br />[signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthGrantType](#list_signin-signin_OAuthGrantType)<br />[signin:OAuthRedirectUri](#list_signin-signin_OAuthRedirectUri)
  - **Access level:** Read

- **   [CreateTrustedIdentityPropagationApplicationForConsole](https://docs.aws.amazon.com/signin/latest/APIReference/API_CreateTrustedIdentityPropagationApplicationForConsole.html)  **
  - **Description:** Grants permission to create an Identity Center application that represents the AWS Management Console on an Identity Center organization instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConsoleAuthorizationConfiguration](https://docs.aws.amazon.com/signin/latest/APIReference/API_DeleteConsoleAuthorizationConfiguration.html)  **
  - **Description:** Grants permission to disable console authorization configuration for an AWS account or organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePermissionStatement](https://docs.aws.amazon.com/signin/latest/APIReference/API_DeleteResourcePermissionStatement.html)  **
  - **Description:** Grants permission to remove a permission statement from the account's SignIn Resource Based Policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetConsoleAuthorizationConfiguration](https://docs.aws.amazon.com/signin/latest/APIReference/API_GetConsoleAuthorizationConfiguration.html)  **
  - **Description:** Grants permission to retrieve console authorization configuration for an AWS account or organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/signin/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve SignIn Resource Based Policy document that is attached with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [IntrospectOAuth2Token](https://docs.aws.amazon.com/signin/latest/APIReference/API_IntrospectOAuth2Token.html)  **
  - **Description:** Grants permission to inspect the metadata and active state of an OAuth 2.0 access token or refresh token
  - **Resource types (\*required):** [oauth2-public-client-localhost\*](#list_signin-resource-oauth2-public-client-localhost) / **Condition keys:** [signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthTokenType](#list_signin-signin_OAuthTokenType)
  - **Resource types (\*required):** [oauth2-public-client-remote\*](#list_signin-resource-oauth2-public-client-remote) / **Condition keys:** [signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthTokenType](#list_signin-signin_OAuthTokenType)
  - **Resource types (\*required):** [oauth2-resource-service-principal\*](#list_signin-resource-oauth2-resource-service-principal) / **Condition keys:** [signin:OAuthClientId](#list_signin-signin_OAuthClientId)<br />[signin:OAuthTokenType](#list_signin-signin_OAuthTokenType)
  - **Access level:** Read

- **   [ListResourcePermissionStatements](https://docs.aws.amazon.com/signin/latest/APIReference/API_ListResourcePermissionStatements.html)  **
  - **Description:** Grants permission to list the SignIn Resource Based Policy statements in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTrustedIdentityPropagationApplicationsForConsole](https://docs.aws.amazon.com/signin/latest/APIReference/API_ListTrustedIdentityPropagationApplicationsForConsole.html)  **
  - **Description:** Grants permission to list all Identity Center applications that represent the AWS Management Console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutConsoleAuthorizationConfiguration](https://docs.aws.amazon.com/signin/latest/APIReference/API_PutConsoleAuthorizationConfiguration.html)  **
  - **Description:** Grants permission to enable console authorization configuration for an AWS account or organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourcePermissionStatement](https://docs.aws.amazon.com/signin/latest/APIReference/API_PutResourcePermissionStatement.html)  **
  - **Description:** Grants permission to create a permission statement in the account's SignIn resource-based policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RevokeOAuth2Token](https://docs.aws.amazon.com/signin/latest/APIReference/API_RevokeOAuth2Token.html)  **
  - **Description:** Grants permission to revoke an OAuth 2.0 refresh token and its associated refresh tokens
  - **Resource types (\*required):** [oauth2-public-client-localhost\*](#list_signin-resource-oauth2-public-client-localhost) / **Condition keys:** [signin:OAuthTokenType](#list_signin-signin_OAuthTokenType)
  - **Resource types (\*required):** [oauth2-public-client-remote\*](#list_signin-resource-oauth2-public-client-remote) / **Condition keys:** [signin:OAuthTokenType](#list_signin-signin_OAuthTokenType)
  - **Resource types (\*required):** [oauth2-resource-service-principal\*](#list_signin-resource-oauth2-resource-service-principal) / **Condition keys:** [signin:OAuthTokenType](#list_signin-signin_OAuthTokenType)
  - **Access level:** Write



## Permission-only actions for AWS Signin
<a name="list_signin-permission-only-actions"></a>

The following actions are defined by AWS Signin but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateAccount](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/console-private-access.html)  **
  - **Description:** Grants permission to create an AWS account through the AWS Management Console sign-up flow
  - **Resource types (\*required):** [console\*](#list_signin-resource-console)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Signin
<a name="list_signin-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [console](https://docs.aws.amazon.com/signin/latest/APIReference)  | arn:${Partition}:signin:::console/${ConsoleName} |   | 
|  [oauth2-public-client-localhost](https://docs.aws.amazon.com/signin/latest/APIReference)  | arn:${Partition}:signin:${Region}:${Account}:oauth2/public-client/localhost |   | 
|  [oauth2-public-client-registration](https://docs.aws.amazon.com/signin/latest/APIReference)  | arn:${Partition}:signin:${Region}::external-client/dcr/\* |   | 
|  [oauth2-public-client-remote](https://docs.aws.amazon.com/signin/latest/APIReference)  | arn:${Partition}:signin:${Region}:${Account}:oauth2/public-client/remote |   | 
|  [oauth2-resource-service-principal](https://docs.aws.amazon.com/signin/latest/APIReference)  | arn:${Partition}:signin:${Region}:${Account}:service-principal/${ServicePrincipalName} |   | 

## Condition keys for AWS Signin
<a name="list_signin-policy-keys"></a>

AWS Signin defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [signin:OAuthClientAuthentication](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html)  | Filters access by the client authentication method used in the OAuth token request | String | 
|   [signin:OAuthClientId](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html)  | Filters access by the OAuth client ID used in the authorization or token request | String | 
|   [signin:OAuthGrantType](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html)  | Filters access by the OAuth grant type used in the token request | String | 
|   [signin:OAuthRedirectUri](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html)  | Filters access by the redirect URI specified in the OAuth authorization request | String | 
|   [signin:OAuthTokenType](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html)  | Filters access by the type of OAuth token being operated on | String | 
|   [signin:PrincipalArn](https://docs.aws.amazon.com/signin/latest/userguide/reference-signin-condition-keys.html)  | Filters access by the principal ARN during pre-authentication console sign-in | ARN | 