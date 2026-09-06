

# Data retrieval APIs for AWS Signin
<a name="awssignin"></a>

AWS Signin provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="signin-Authenticate"></a>[Authenticate](https://docs.aws.amazon.com/signin/latest/APIReference/API_Authenticate.html) | Authenticate to the AWS Management Console | Read | 
| <a name="signin-AuthorizeOAuth2Access"></a>[AuthorizeOAuth2Access](https://docs.aws.amazon.com/signin/latest/APIReference/API_AuthorizeOAuth2Access.html) | Authenticate through a browser and obtain an OAuth 2.0 authorization code for credential exchange | Read | 
| <a name="signin-CreateOAuth2Token"></a>[CreateOAuth2Token](https://docs.aws.amazon.com/signin/latest/APIReference/API_CreateOAuth2Token.html) | Exchange an authorization code for OAuth 2.0 access token and refresh token that can be used to access AWS services from developer tools and applications | Read | 
| <a name="signin-GetConsoleAuthorizationConfiguration"></a>[GetConsoleAuthorizationConfiguration](https://docs.aws.amazon.com/signin/latest/APIReference/API_GetConsoleAuthorizationConfiguration.html) | Retrieve console authorization configuration for an AWS account or organization | Read | 
| <a name="signin-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/signin/latest/APIReference/API_GetResourcePolicy.html) | Retrieve SignIn Resource Based Policy document that is attached with your account | Read | 
| <a name="signin-IntrospectOAuth2Token"></a>[IntrospectOAuth2Token](https://docs.aws.amazon.com/signin/latest/APIReference/API_IntrospectOAuth2Token.html) | Inspect the metadata and active state of an OAuth 2.0 access token or refresh token | Read | 
| <a name="signin-ListResourcePermissionStatements"></a>[ListResourcePermissionStatements](https://docs.aws.amazon.com/signin/latest/APIReference/API_ListResourcePermissionStatements.html) | List the SignIn Resource Based Policy statements in your account | List | 
| <a name="signin-ListTrustedIdentityPropagationApplicationsForConsole"></a>[ListTrustedIdentityPropagationApplicationsForConsole](https://docs.aws.amazon.com/signin/latest/APIReference/API_ListTrustedIdentityPropagationApplicationsForConsole.html) | List all Identity Center applications that represent the AWS Management Console | List | 