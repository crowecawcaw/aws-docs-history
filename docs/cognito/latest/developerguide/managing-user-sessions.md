

# Managing user sessions
<a name="managing-user-sessions"></a>

With Amazon Cognito user pool session management, you can track, list, and revoke a user's active sessions across all of their devices and apps. You can also limit how many active sessions a user can hold. With session management, you can build sign-out and session-visibility experiences, respond to compromised accounts, and enforce active-device limits. Session management builds on the revocation methods in [Ending user sessions with token revocation](token-revocation.md) and tracks the lifecycle of the [Refresh tokens](amazon-cognito-user-pools-using-the-refresh-token.md) that your user pool issues.

Session tracking is an opt-in feature that you turn on at the user pool level. When session tracking is off, Amazon Cognito does not store server-side session records and token contents are unchanged.

## How session management works
<a name="managing-user-sessions-how-it-works"></a>

Amazon Cognito user pools have two types of sessions, and session management tracks both.
+ **Single sign-on (SSO) sessions**: A server-side session created when a user signs in through managed login. An SSO session lets the user access other app clients in the same user pool without re-authenticating. It is backed by a browser cookie and scoped to a single browser or device.
+ **Token sessions**: A session that represents an app's active authenticated session for a user. A token session tracks the lifecycle of a refresh token issued to a specific app client and is scoped to that app client.

### The session model
<a name="managing-user-sessions-session-model"></a>

Each SSO session and each set of tokens is a separate session with its own start time, last-active time, and lifecycle. When a user authenticates through an SSO session, the resulting token session carries a reference to the SSO session it came from. With this reference, you can understand the relationship between an SSO session and the token sessions beneath it, while each session is still tracked independently.

Each time a user authenticates, Amazon Cognito creates a new token session. Refreshing or rotating tokens does not create a new session. Instead, these actions extend the existing session, and the issued tokens keep the same session identifier.

### The sid claim
<a name="managing-user-sessions-sid-claim"></a>

When session tracking is enabled, Amazon Cognito adds a `sid` claim to the ID and access tokens it issues. The `sid` claim is the session identifier, and it stays the same across every refresh and rotation within the same session. `sid` follows the standard OpenID Connect session ID claim name.

If your user pool uses a pre token generation trigger that adds its own `sid` claim, Amazon Cognito doesn't change that claim, and session tracking doesn't operate for that user pool — it behaves as if session tracking is disabled, even when you enable it. To use session management, remove the `sid` claim from your trigger. For the claims a trigger can and can't modify, see [Claims and scopes reference](user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-excluded-claims).

### Session count limits
<a name="managing-user-sessions-count-limits"></a>

Amazon Cognito limits how many active sessions a user can hold. When a user reaches the limit, Amazon Cognito revokes the least recently used session.
+ **Token sessions**: You can configure the maximum number of active token sessions for each user at the user pool level. The default is 20 and the maximum is 100.
+ **SSO sessions**: Each user can hold up to 10 SSO sessions. This limit is fixed and you cannot configure it.

Machine-to-machine (client credentials) tokens do not use refresh tokens and are not tracked as sessions. They are excluded from session management.

## Enable session tracking
<a name="managing-user-sessions-enable"></a>

Session tracking is off by default. To use session management, you must opt in by enabling it at the user pool level.

### Tier requirement
<a name="managing-user-sessions-tier-requirement"></a>

Session tracking requires the user pool to be in the [Essentials or Plus feature plan](cognito-sign-in-feature-plans.md). If you try to enable session tracking on a pool in an ineligible tier, the operation returns `FeatureUnavailableInTierException`. If you downgrade a user pool with session tracking enabled to the Lite feature plan, Amazon Cognito returns an error. Disable session tracking before you downgrade.

### Configure pool-level settings
<a name="managing-user-sessions-pool-settings"></a>

Use the following operations to manage pool-level session settings.
+ `SetUserPoolSessionConfiguration`: Enables or disables session tracking (`UserSessionTracking`) and sets the pool-wide maximum active token sessions for each user (`TokenSession.MaxPerUser`).
+ `GetUserPoolSessionConfiguration`: Reads the current pool-level session configuration.

The following example request enables session tracking and sets the maximum number of token sessions for each user to 20:

```
{
    "UserPoolId": "us-east-1_aBcDeFgHi",
    "UserSessionTracking": "ENABLED",
    "TokenSession": {
        "MaxPerUser": 20
    }
}
```

### Configure per-client SSO session validity
<a name="managing-user-sessions-client-settings"></a>

Each app client can control how long it silently reuses an SSO session before it requires the user to authenticate again. Use the following operations to manage this setting.
+ `SetUserPoolClientSessionConfiguration`: Sets the per-client SSO session validity (`SSOSession.MaxValidityMinutes`).
+ `GetUserPoolClientSessionConfiguration`: Reads the current per-client session configuration.

`SSOSession.MaxValidityMinutes` accepts a value from 0 to 129,600 minutes (90 days), with a default of 60 minutes. This value has the following behavior:
+ A value greater than 0: This app client reuses the SSO session for up to the specified number of minutes after the user last authenticated through managed login, and issues new tokens without asking the user to sign in again. Silently reusing the session doesn't reset this period. When it ends, the user must sign in again to use this app client.
+ A value of 0: This app client never reuses the SSO session and always asks the user to sign in. Amazon Cognito still creates the SSO session, so other app clients in the same user pool can reuse it.

The validity that Amazon Cognito applies is the validity of the app client the user is currently signing in to, not the client that created the session.

The following example request sets the SSO session validity for an app client to 43,200 minutes (30 days):

```
{
    "UserPoolId": "us-east-1_aBcDeFgHi",
    "ClientId": "1example23456789",
    "SSOSession": {
        "MaxValidityMinutes": 43200
    }
}
```

### SSO session lifespan
<a name="managing-user-sessions-sso-lifespan"></a>

Every SSO session expires 90 days after the user's last fresh authentication, unless it is revoked earlier, regardless of the maximum validity configured on any app client. A fresh authentication resets the 90-day window, but silently reusing the session does not extend it. Within that window, each app client can reuse the session for up to its own configured maximum validity.

## List a user's sessions
<a name="managing-user-sessions-list"></a>

You can list all active sessions for a user, including both SSO and token sessions. Only active sessions are returned. Revoked and expired sessions are not included.
+ `ListUserSessions`: Lets a signed-in user list their own sessions. The caller authorizes the request with an access token.
+ `AdminListUserSessions`: Lets an administrator list a user's sessions. The caller authorizes the request with AWS Identity and Access Management (IAM) credentials.

Both operations return all of a user's sessions across every app client in the user pool, as a flat list in a single page of up to 125 sessions.

### Session fields
<a name="managing-user-sessions-fields"></a>

Each session in the response includes the following fields.


| Field | Applies to | Description | 
| --- | --- | --- | 
| SessionId | Both | A unique 28-character identifier. Token sessions use a tkn prefix and SSO sessions use an sso prefix. | 
| SessionType | Both | TOKEN or SSO. | 
| ClientId | Both | The app client the session belongs to. | 
| CreateDate | Both | When the session was created. | 
| LastActiveDate | Both | The time of the most recent activity. For token sessions, this is the most recent token refresh or rotation. For SSO sessions, this is the most recent authentication, token grant, or rotation. | 
| DeviceType | Both | The operating system and browser or app, derived from the user agent of the most recent activity. | 
| LastIPAddress | Both | The IP address of the most recent activity. | 
| LastLocation | Both | The city and country of the most recent activity, derived from the IP address. | 
| OriginSessionId | Token sessions only | The SSO session this token session came from. Null for sessions that did not come through an SSO session. | 
| IsCurrentSession | Both | Whether the session matches the access token in the request. Always false for AdminListUserSessions, which takes no access token. | 

## Revoke sessions
<a name="managing-user-sessions-revoke"></a>

You can revoke a specific session by its session ID.
+ `RevokeUserSession`: Lets a signed-in user revoke one of their own sessions. The caller authorizes the request with an access token.
+ `AdminRevokeUserSession`: Lets an administrator revoke a user's session. The caller authorizes the request with IAM credentials.

Both operations accept either a token session ID or an SSO session ID. Revoking a session revokes all of the tokens for that session and deletes the session record.

### Cascade to linked sessions
<a name="managing-user-sessions-cascade"></a>

Use the `RevokeAssociatedSessions` parameter to control whether revocation cascades to linked sessions. The parameter is interpreted relative to the type of session you revoke.


| Target session | `NONE` (default) | `LINKED` | 
| --- | --- | --- | 
| Token session | Revokes only the targeted token session. | Also revokes the parent SSO session the token session came through. The other token sessions under that SSO session are not revoked. | 
| SSO session | Revokes only the targeted SSO session. | Also revokes the token sessions that came through that SSO session. | 

`RevokeToken` also accepts the `RevokeAssociatedSessions` parameter. Because `RevokeToken` always targets a token session, the token session row applies: `LINKED` also revokes the parent SSO session that the token session came through.

### Choose between RevokeToken and RevokeUserSession
<a name="managing-user-sessions-revoke-choice"></a>

Both `RevokeToken` and `RevokeUserSession` revoke the tokens and delete the session record for a token session, so they produce the same result. The difference is how you identify the session and when you use each operation. For more information about `RevokeToken`, see [Ending user sessions with token revocation](token-revocation.md).
+ Use `RevokeToken` for normal app sign-out, when the app still holds the refresh token. `RevokeToken` also accepts the optional `RevokeAssociatedSessions` parameter to revoke the parent SSO session.
+ Use `RevokeUserSession` for remote management, when you identify the session by its session ID from `ListUserSessions`. For example, use `RevokeUserSession` to sign out a lost or stolen device, where the app no longer has access to the token.

### Global sign-out
<a name="managing-user-sessions-global-signout"></a>

When session tracking is enabled, `GlobalSignOut` and `AdminUserGlobalSignOut` also revoke all of the user's token sessions and SSO sessions, in addition to revoking the user's refresh tokens. This behavior is automatic and requires no new parameters. `AdminDisableUser` also revokes all of the user's token sessions when session tracking is enabled.

## Set active session limits
<a name="managing-user-sessions-concurrent-limits"></a>

You can cap how many active token sessions a user can hold by setting `TokenSession.MaxPerUser` with `SetUserPoolSessionConfiguration`. The cap applies across all app clients in the user pool.

When a user reaches the cap and signs in again, the sign-in succeeds and Amazon Cognito automatically revokes the least recently used token session to make room. This eviction behavior is `TERMINATE_LEAST_RECENTLY_USED`. Amazon Cognito does not deny the new sign-in.

If you lower the cap below a user's current number of sessions, Amazon Cognito doesn't evict any sessions right away, and token refresh or rotation doesn't evict them either. Instead, the user's next sign-in evicts the least recently used sessions until the user is within the new cap. For example, if a user has 5 sessions and you lower the cap to 2, the next sign-in leaves 2 sessions: the new session and the most recently used existing session.

## Multi-Region considerations
<a name="managing-user-sessions-multi-region"></a>

In a multi-Region user pool, Amazon Cognito enforces the token session cap per Region, and the count is eventually consistent across Regions. As a result, near-simultaneous sign-ins for the same user in different Regions can briefly push the total above the cap. Amazon Cognito reconciles the excess at the user's next authentication or token refresh by revoking the least recently active sessions until the user is back within the cap. Session revocation and session data propagate to all Regions.

## Using AWS CloudFormation
<a name="managing-user-sessions-cloudformation"></a>

AWS CloudFormation supports session configuration through two attachment resources.
+ `AWS::Cognito::UserPoolSessionConfigurationAttachment`: Backs the pool-level configuration. Create, Update, and Delete all map to `SetUserPoolSessionConfiguration`. Delete resets the pool to its default values (session tracking disabled, `MaxPerUser` 20).
+ `AWS::Cognito::UserPoolClientSessionConfigurationAttachment`: Backs the per-client configuration. Create, Update, and Delete all map to `SetUserPoolClientSessionConfiguration`. Delete resets the client to its default values (`SSOSession.MaxValidityMinutes` 60).

Because per-client settings require pool-level session tracking to be enabled when they are written, declare the client attachment with a `DependsOn` reference to the pool attachment.