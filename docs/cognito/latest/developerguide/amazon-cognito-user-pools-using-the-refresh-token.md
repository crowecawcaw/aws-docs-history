# Refresh tokens

You can use the refresh token to retrieve new ID and access tokens. By default, the
refresh token expires 30 days after your application user signs into your user pool. When you
create an application for your user pool, you can set the application's refresh token
expiration to any value between 60 minutes and 10 years.

## Getting

new access and identity tokens with a refresh token

Amazon Cognito issues refresh tokens in response to successful authentication with the managed
login authorization-code flow and with API operations or SDK methods. The refresh token
returns new ID and access tokens, and optionally a new refresh token. You can use refresh
tokens in the following ways.

**GetTokensFromRefreshToken**

The [GetTokensFromRefreshToken](../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md") API operation issues new ID and access tokens
from a valid refresh token. You also get a new refresh token if you've enabled refresh
token rotation.

**InitiateAuth and AdminitiateAuth**

The [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") or [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API operations include the `REFRESH_TOKEN_AUTH`
authentication flow. In this flow, you pass a refresh token and get new ID and access
tokens. You can't authenticate with `REFRESH_TOKEN_AUTH` in app clients
with [refresh token rotation](#using-the-refresh-token-rotation "#using-the-refresh-token-rotation")
enabled.

**OAuth token endpoint**

The [token endpoint](token-endpoint.md "token-endpoint.md") in user pools with a
[domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md") has a
`refresh_token` grant type that issues new ID, access, and optionally
(with [refresh token rotation](#using-the-refresh-token-rotation "#using-the-refresh-token-rotation"))
refresh tokens from a valid refresh token.

## Refresh token rotation

You can optionally configure refresh token rotation in your app client. With refresh
token rotation, your client can invalidate the original refresh token and issue a new
refresh token with each token refresh. When this setting is enabled, each successful request
in all forms of token refresh return a new ID, access, _and_ refresh token. When this setting is disabled, token-refresh requests
return new access and ID tokens only and the original refresh token remains valid. The new
refresh token is valid for the remaining duration of the original refresh token. You can
configure [app clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md") to rotate
refresh tokens or to carry over the original refresh token. To allow for retries for a brief
duration, you can also configure a grace period for the original refresh token of up to 60
seconds.

###### Things to know about refresh token rotation

- After you enable refresh token rotation, new claims are added in JSON web tokens
  from your user pool. The `origin_jti` and `jti` claims are added
  to access and ID tokens. These claims increase the size of the JWTs.
- Refresh token rotation isn't compatible with the authentication flow
  `REFRESH_TOKEN_AUTH`. To implement refresh token rotation, you must disable
  this authentication flow in your app client and design your application to submit
  token-refresh requests with the [GetTokensFromRefreshToken](../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md") API operation or the equivalent SDK method.
- With refresh token rotation inactive, you can complete token-refresh requests with
  either `GetTokensFromRefreshToken` or `REFRESH_TOKEN_AUTH`.
- When [device
  remembering](amazon-cognito-user-pools-device-tracking.md "amazon-cognito-user-pools-device-tracking.md") is active in your user pool, you must provide the device key in
  `GetTokensFromRefreshToken` requests. If your user doesn't have a
  confirmed-device key that your application submits in the initial authentication
  request, Amazon Cognito issues a new one. To refresh tokens in this configuration, you must
  provide a device key, whether you specified one in `AuthParameters` or
  received a new one in the authentication response.
- You can pass `ClientMetadata` to the pre token generation Lambda trigger
  in your `GetTokensFromRefreshToken` request. This data, which gets passed to
  the input event for your trigger, delivers additional context that you can use in the
  custom logic of your Lambda function.

As a security best practice, enable refresh token rotation on your app clients.

Enable refresh token rotation (console)
The following procedure turns refresh token rotation on or off for your app
client. This procedure requires an existing app client. To learn more about creating
an app client, see [Application-specific settings with app
clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md").

###### To enable refresh token rotation

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Navigate to the **App clients** menu and select an existing
   app client.
5. Select **Edit** from the **App client
   information** section of the page.
6. Under **Advanced security configurations**, locate the
   **Enable refresh token rotation** option.
7. To enable rotation, select the checkbox. To disable rotation, deselect the
   checkbox.
8. Under **Refresh token rotation grace period**, enter a number
   of seconds, up to 60, that you want to set as the delay before the rotated-out
   refresh token is revoked.

Enable refresh token rotation (API)
Configure refresh token rotation in a [CreateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md") or [UpdateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md") API request. The following partial request body turns
on refresh token rotation and sets the grace period to ten seconds.

```
"RefreshTokenRotation" : {
   "Feature" : "ENABLED,
   "RetryGracePeriodSeconds" : 10
}
```

## API and SDK token refresh

There are two ways to use the refresh token to get new ID and access tokens with the
user pools API, depending on whether refresh token rotation is active. In app clients with
refresh token rotation active, use the [GetTokensFromRefreshToken](../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md") API operation. In app clients without refresh token
rotation, use the `REFRESH_TOKEN_AUTH` flow of the [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") or [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API operations.

###### Note

Users can authenticate with user pools in [managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md") or in custom
applications that you build with AWS SDKs and Amazon Cognito API operations. The
`REFRESH_TOKEN_AUTH` flow and `GetTokensFromRefreshToken` can both
complete token refresh for managed login users. Token refresh in custom applications
doesn't affect managed login sessions. These sessions are set in a browser cookie and are
valid for one hour. The `GetTokensFromRefreshToken` response issues new ID,
access, and optionally refresh tokens, but doesn't renew the managed login session
cookie.

`REFRESH_TOKEN_AUTH` isn't available in app clients with refresh token
rotation enabled.

GetTokensFromRefreshToken
[GetTokensFromRefreshToken](../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md") returns new ID, access and refresh tokens from a
request that you authorize with a refresh token. The following is an example request
body for `GetTokensFromRefreshToken`. You can submit client metadata to
Lambda triggers in requests to this operation.

```
{
    "RefreshToken": "`eyJjd123abcEXAMPLE`",
    "ClientId": "`1example23456789`",
    "ClientSecret": "`myappclientsecret123abc`",
    "ClientMetadata": {
      "`MyMetadataKey`" : "`MyMetadataValue`"
   },
}
```

AdminInitiateAuth/InitiateAuth
To use the refresh token when refresh token rotation is inactive, use the [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") or [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API operations. Pass
`REFRESH_TOKEN_AUTH` for the `AuthFlow` parameter. In the
`AuthParameters` property of `AuthFlow`, pass your user's
refresh token as the value of `"REFRESH_TOKEN"`. Amazon Cognito returns new ID and
access tokens after your API request passes all challenges.

The following is an example request body for a token refresh with the
`InitiateAuth` or `AdminInitiateAuth` API.

```
{
    "AuthFlow": "REFRESH_TOKEN_AUTH",
    "ClientId": "`1example23456789`",
    "UserPoolId": "`us-west-2_EXAMPLE`",
    "AuthParameters": {
        "REFRESH_TOKEN": "`eyJjd123abcEXAMPLE`",
        "SECRET_HASH": "`kT5acwCVrbD6JexhW3EQwnRSe6fLuPTRkEQ50athqv8=`"
    }
}
```

## OAuth token refresh

You can also submit refresh tokens to the [Token endpoint](token-endpoint.md "token-endpoint.md") in a user pool where you have configured a domain. In the
request body, include a `grant_type` value of `refresh_token` and a
`refresh_token` value of your user's refresh token.

Requests to the token endpoint are available in app clients with refresh token rotation
active and those where it's inactive. When refresh token rotation is active, the token
endpoint returns a new refresh token.

The following is an example request with a refresh token.

```
POST /oauth2/token HTTP/1.1
Host: `auth.example.com`
Content-Type: application/x-www-form-urlencoded
Authorization: Basic `ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw`
Content-Length: **

client_id=`1example23456789`&grant_type=refresh_token&refresh_token=`eyJjd123abcEXAMPLE`
```

## Revoking

refresh tokens

You can revoke refresh tokens that belong to a user. For more information about revoking
tokens, see [Ending user sessions with token revocation](token-revocation.md "token-revocation.md").

###### Note

Revoking the refresh token will revoke all ID and access tokens that Amazon Cognito issued from
refresh requests with that token.

To sign users out from all current signed-in session, revoke all of their tokens with
[GlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md") or [AdminUserGlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md") API requests. After the user is signed out, the following
effects happen.

- The user's refresh token can't get new tokens for the user.
- The user's access token can't make token-authorized API requests.
- The user must re-authenticate to get new tokens. Because managed login session
  cookies don't expire automatically, your user can re-authenticate with a session cookie,
  with no additional prompt for credentials. After you sign out your managed login users,
  redirect them to the [Logout endpoint](logout-endpoint.md "logout-endpoint.md"),
  where Amazon Cognito clears their session cookie.

With refresh tokens, you can persist users' sessions in your app for a long time. Over
time, your users might want to deauthorize some applications where they have stayed signed
in with their refresh tokens. To sign your user out from a single session, revoke their
refresh token. When your user wants to sign themself out from all authenticated sessions,
generate a [GlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md") API request . Your app can present your user with a choice like
**Sign out from all devices**. `GlobalSignOut` accepts a
user's valid–unaltered, unexpired, not-revoked–access token. Because this API
is token-authorized, one user can't use it to initiate sign-out for another user.

You can, however, generate an [AdminUserGlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md") API request that you authorize with your AWS credentials
to sign out any user from all of their devices. The administrator application must call this
API operation with AWS developer credentials and pass the user pool ID and the user's
username as parameters. The `AdminUserGlobalSignOut` API can sign out any user in
the user pool.

For more information about requests that you can authorize with either AWS credentials
or a user's access token, see [List of API operations grouped by authorization
model](authentication-flows-public-server-side.md#user-pool-apis-auth-unauth "authentication-flows-public-server-side.md#user-pool-apis-auth-unauth").
