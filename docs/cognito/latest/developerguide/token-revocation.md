# Ending user sessions with token revocation

You can revoke refresh tokens and end user sessions with the following methods. When you
revoke a refresh token, all access tokens that were previously issued by that refresh token
become invalid. The other refresh tokens issued to the user are not affected.

**RevokeToken operation**

[RevokeToken](../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md") revokes all access tokens for a given refresh token, including
the initial access token from interactive sign-in. This operation doesn't affect any of
the user's other refresh tokens or the ID- and access-token children of those other
refresh tokens.

**Revocation endpoint**

The [revoke endpoint](revocation-endpoint.md "revocation-endpoint.md") revokes a given
refresh token and all ID and access tokens that the refresh token generated. This
endpoint also revokes the initial access token from interactive sign-in. Requests to
this endpoint don't affect any of the user's other refresh tokens or the ID- and
access-token children of those other refresh tokens.

**GlobalSignOut operation**

[GlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md") is a self-service operation that a user authorizes with their
access token. This operation revokes all of the requesting user's refresh, ID, and
access tokens.

**AdminUserGlobalSignOut operation**

[AdminUserGlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md") is a server-side operation that an administrator
authorizes with IAM credentials. This operation revokes all of the target user's
refresh, ID, and access tokens.

###### Things to know about revoking tokens

- Your request to revoke a refresh token must include the client ID that was used to
  obtain the token.
- User pool JWTs are self-contained with a signature and expiration time that was
  assigned when the token was created. Revoked tokens can't be used with any Amazon Cognito API
  calls that require a token. However, revoked tokens will still be valid if they are
  verified using any JWT library that verifies the signature and expiration of the
  token.
- When you create a new user pool client, token revocation is enabled by default.
- You can revoke refresh tokens only in app clients with token revocation enabled.
- After you enable token revocation, new claims are added in the Amazon Cognito JSON Web Tokens.
  The `origin_jti` and `jti` claims are added to access and ID tokens.
  These claims increase the size of the application client access and ID tokens.
- When you disable token revocation in an app client where it was previously enabled,
  revoked tokens don't become active again.
- When you [disable a user
  account](how-to-manage-user-accounts.md#manage-user-accounts-enable-disable "how-to-manage-user-accounts.md#manage-user-accounts-enable-disable") (which revokes refresh and access tokens), the revoked tokens don't
  become active if you enable the user account again.
- When you create a new user pool client using the AWS Management Console, the AWS CLI, or the AWS
  API, token revocation is enabled by default.

## Enable token revocation

Before you can revoke a token for an existing user pool client, you must enable token
revocation. You can enable token revocation for existing user pool clients using the AWS CLI
or the AWS API. To do this, call the `aws cognito-idp
 describe-user-pool-client` CLI command or the `DescribeUserPoolClient`
API operation to retrieve the current settings from your app client. Then call the `aws
 cognito-idp update-user-pool-client` CLI command or the
`UpdateUserPoolClient` API operation. Include the current settings from your
app client and set the `EnableTokenRevocation` parameter to
`true`.

To create or modify an app client with token revocation enabled with the Amazon Cognito API or
with an AWS SDK, include the following parameter in your [CreateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md") or [UpdateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md") API request.

```
"EnableTokenRevocation": `true`

```

To configure token revocation in the Amazon Cognito console, select an app client from the
**App clients** menu in your user pool. Select the
**Edit** button in **App client information** and enable
or disable token revocation under **Advanced configuration**.

## Revoke a token

You can revoke a refresh token using a [RevokeToken](../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md") API request, for example with the `aws cognito-idp
 revoke-token` CLI command. You can also revoke tokens using the [Revoke endpoint](revocation-endpoint.md "revocation-endpoint.md"). This endpoint is
available after you add a domain to your user pool. You can use the revocation endpoint on
either an Amazon Cognito hosted domain or your own custom domain.

The following is the body of an example `RevokeToken` API request.

```
{
   "ClientId": "`1example23456789`",
   "ClientSecret": "`abcdef123456789ghijklexample`",
   "Token": "`eyJjdHkiOiJKV1QiEXAMPLE`"
}
```

The following is an example cURL request to the `/oauth2/revoke` endpoint of
a user pool with a custom domain.

```
curl --location 'auth.mydomain.com/oauth2/revoke' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic `Base64Encode(client_id:client_secret)`' \
--data-urlencode 'token=`abcdef123456789ghijklexample`' \
--data-urlencode 'client_id=`1example23456789`'
```

The `RevokeToken` operation and the `/oauth2/revoke` endpoint
require no additional authorization unless your app client has a client secret.
