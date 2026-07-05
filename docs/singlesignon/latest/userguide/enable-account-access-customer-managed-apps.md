# Enable AWS account access for customer managed applications

You can enable AWS account access for customer managed applications in IAM Identity Center by
configuring a [trusted token issuer](using-apps-with-trusted-token-issuer.md "using-apps-with-trusted-token-issuer.md"). A trusted token issuer is an OAuth 2.0 authorization
server that issues signed tokens on behalf of authenticated users. IAM Identity Center exchanges these
tokens for credentials that allow your application to programmatically access AWS accounts
and roles assigned to those users. Trusted token issuers can also be used for access to
AWS managed applications. For more information, see [Using applications with a trusted token issuer](using-apps-with-trusted-token-issuer.md "using-apps-with-trusted-token-issuer.md").

###### Note

You can enable this feature only for [organization instances](organization-instances-identity-center.md "organization-instances-identity-center.md") of
IAM Identity Center. Only management account administrators or delegated administrators can enable the
`sso:account:access` scope for a customer managed application. If you are
an application builder in a member account, contact your IAM Identity Center administrator to enable
this scope for your application.

## How it works

After an administrator enables the `sso:account:access` scope
for a customer managed application, the following workflow occurs:

1. A user signs in to your application through your external identity provider
   (IdP).
2. Your application receives a signed JWT token from the IdP.
3. Your application exchanges this token for an IAM Identity Center token by calling the
   `CreateTokenWithIAM` API with the JWT bearer grant type
   (`urn:ietf:params:oauth:grant-type:jwt-bearer`). This call
   requires Signature Version 4 (SigV4) authentication. For more information, see
   [CreateTokenWithIAM](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md") in the _IAM Identity Center OIDC API
   Reference_.
4. Your application uses the IAM Identity Center token to call [portal API operations](../PortalAPIReference/API_Operations.md "../PortalAPIReference/API_Operations.md") (`ListAccounts`,
   `ListAccountRoles`, `GetRoleCredentials`) to discover
   accounts and roles assigned to the user and retrieve temporary AWS credentials
   on their behalf.
5. The user accesses AWS resources through your application without any
   additional sign-in steps.

If you enabled the refresh token grant when you set up your application,
`CreateTokenWithIAM` also returns a refresh token alongside the access
token. Your application can use this refresh token to obtain new access tokens without
repeating the full JWT Bearer token exchange. To refresh an access token, call
`CreateTokenWithIAM` with the `refresh_token` grant
type.

## Prerequisites

Before you enable account access for a customer managed application, you need:

- A [customer managed application](customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md "customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md") configured in IAM Identity Center that supports JSON
  Web Tokens (JWTs). The application must have a backend server component that can
  securely store credentials. Browser-based applications, such as single page
  applications (SPAs), and other public clients are not supported for this
  feature.
- A [trusted token issuer](using-apps-with-trusted-token-issuer.md "using-apps-with-trusted-token-issuer.md") attached to your application.
- Access to the AWS Organizations management account or delegated administrator account
  for IAM Identity Center. Application builders in member accounts cannot enable this scope
  directly.

## Enable account access

###### To enable the `sso:account:access` scope for a customer managed application

1. Sign in to the AWS Management Console using your organization's management account or
   delegated administrator account.
2. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. In the navigation pane, choose **Applications**.
4. Choose the **Customer managed** tab.
5. Choose the name of the application you want to configure.
6. In the **AWS account access** section, turn on
   **Enable AWS account access**.

After you enable account access, the application can programmatically call Identity
portal API operations to list accounts and roles, and retrieve temporary AWS
credentials for roles that an authenticated user is authorized to access.

###### Important

When you enable the `sso:account:access` scope for an application, that
application can access all accounts and roles available for an authenticated user
through their permission set assignments. You cannot restrict the application to
specific accounts or roles. Ensure you understand this level of access before
enabling this feature.

## Programmatic access

You can use the `PutApplicationAccessScope` API to programmatically enable
the `sso:account:access` scope for a customer managed application. You must
call the API from your organization's management account or delegated administrator
account.

**AWS CLI**

```
aws sso-admin put-application-access-scope \
  --application-arn arn:aws:sso::`123456789012`:application/`ssoins-1234567890abcdef`/`apl-1234567890abcdef` \
  --scope "sso:account:access"
```

**API request:**

```
{
  "ApplicationArn": "arn:aws:sso::`123456789012`:application/`ssoins-1234567890abcdef`/`apl-1234567890abcdef`",
  "Scope": "sso:account:access"
}
```

To disable account access, use the `DeleteApplicationAccessScope` API with
the same application ARN and scope value.

For more information, see [PutApplicationAccessScope](../APIReference/API_PutApplicationAccessScope.md "../APIReference/API_PutApplicationAccessScope.md") and [DeleteApplicationAccessScope](../APIReference/API_DeleteApplicationAccessScope.md "../APIReference/API_DeleteApplicationAccessScope.md") in the _IAM Identity Center API
Reference_.

## Security best practices

- The `sso:account:access` scope grants the application access to
  all accounts and roles available to the authenticated user. You cannot restrict
  access to specific accounts or roles. Only enable this scope for applications
  that require this level of access.
- Keep IAM Identity Center access tokens and refresh tokens on your backend server. Never
  expose them to client-side code.
- Do not log tokens or credentials in application logs, error messages, or
  debugging output.
- Do not pass tokens in URL query parameters. Use the
  `x-amz-sso_bearer_token` header for access tokens.
- Use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to monitor API calls made by your applications.

## Related information

- [Customer managed applications](customermanagedapps.md "customermanagedapps.md")
- [Using applications with a trusted token issuer](using-apps-with-trusted-token-issuer.md "using-apps-with-trusted-token-issuer.md")
- [AWS access portal API Reference](../PortalAPIReference/API_Operations.md "../PortalAPIReference/API_Operations.md")
