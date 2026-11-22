

# Troubleshoot Amazon Cognito

This chapter provides solutions to common problems you might encounter while working with Amazon Cognito. Amazon Cognito implementations can face various challenges across authentication flows, user pool configurations, and identity federation setups. Whether you're developing a new application or maintaining an existing one, this troubleshooting guide helps you identify and resolve common issues quickly.

To use this page, find your error message or symptom in the following index and choose the linked section. Each entry describes the problem, its likely causes, and a solution. The entries are grouped by the area of Amazon Cognito where the problem occurs, such as sign-in, tokens, or federation.


| Error message or symptom | Section | 
| --- | --- | 
| Invalid refresh token during token refresh | [`Invalid refresh token` error](#troubleshoot_invalid_refresh_token) | 
| NotAuthorizedException: Incorrect username or password. | [`Incorrect username or password.`](#troubleshoot_incorrect_username_password) | 
| InvalidParameterException: auth flow not enabled for this client | [`USER_PASSWORD_AUTH flow not enabled for this client`](#troubleshoot_auth_flow_not_enabled) | 
| UserNotConfirmedException: User is not confirmed. | [`User is not confirmed.`](#troubleshoot_user_not_confirmed) | 
| NEW\_PASSWORD\_REQUIRED challenge for a new user | [`NEW_PASSWORD_REQUIRED` challenge and `FORCE_CHANGE_PASSWORD` status](#troubleshoot_new_password_required) | 
| InvalidParameterException: Invalid attributes given, {{attribute\_name}} is missing | [`NEW_PASSWORD_REQUIRED` challenge and `FORCE_CHANGE_PASSWORD` status](#troubleshoot_new_password_required) | 
| NotAuthorizedException: Invalid session for the user, session can only be used once. | [`NEW_PASSWORD_REQUIRED` challenge and `FORCE_CHANGE_PASSWORD` status](#troubleshoot_new_password_required) | 
| NotAuthorizedException: Invalid session for the user, session is expired. | [`NEW_PASSWORD_REQUIRED` challenge and `FORCE_CHANGE_PASSWORD` status](#troubleshoot_new_password_required) | 
| LimitExceededException: Attempt limit exceeded, please try after some time. | [`Attempt limit exceeded, please try after some time.`](#troubleshoot_attempt_limit_exceeded) | 
| NotAuthorizedException: SECRET\_HASH was not received | [`Client {{client-id}} is configured with secret but SECRET_HASH was not received`](#troubleshoot_secret_hash_missing) | 
| NotAuthorizedException: Unable to verify secret hash | [`Unable to verify secret hash for client {{client-id}}`](#troubleshoot_secret_hash_mismatch) | 
| InvalidParameterException: not configured for secret but secret hash was received | [`App client {{client-id}} is not configured for secret but secret hash was received`](#troubleshoot_secret_hash_not_configured) | 
| redirect\_mismatch at the authorization endpoint | [`redirect_mismatch` at the authorization endpoint](#troubleshoot_oauth_redirect_mismatch) | 
| invalid\_grant at the token endpoint | [`invalid_grant` at the token endpoint](#troubleshoot_oauth_invalid_grant) | 
| invalid\_request with Proof Key for Code Exchange (PKCE) at the token endpoint | [`invalid_request` with PKCE at the token endpoint](#troubleshoot_oauth_invalid_request_pkce) | 
| invalid\_client or unauthorized\_client at the token endpoint | [`invalid_client` and `unauthorized_client` at the token endpoint](#troubleshoot_oauth_invalid_client) | 
| CORS error calling the token endpoint from a browser | [CORS error calling the token endpoint from a browser](#troubleshoot_oauth_cors) | 
| JWT signature or claim validation fails | [JWT signature or claim validation fails](#troubleshoot_jwt_validation) | 
| NotAuthorizedException: Access Token does not have required scopes | [`Access Token does not have required scopes`](#troubleshoot_token_missing_scopes) | 
| 401 Unauthorized from an API Gateway user pool authorizer | [`401 Unauthorized` from an API Gateway user pool authorizer](#troubleshoot_apigw_401) | 
| Managed login users can't select an MFA factor | [Managed login users can't select an MFA factor](#troubleshoot_mfa_factor_selection) | 
| Passwordless and passkey users can't use MFA | [Passwordless and passkey users can't use MFA](#troubleshoot_passwordless_mfa) | 
| Password reset code not received by email or SMS | [Not able to receive password reset code through email or SMS](#troubleshoot_password_reset_delivery) | 
| Could not reset password for the account | [Password reset fails with unverified recovery attributes: `Could not reset password for the account, please contact support or try again`](#troubleshoot_password_reset_unverified_recovery) | 
| LimitExceededException: Exceeded daily email limit | [`Exceeded daily email limit for the operation or the account. If a higher limit is required, please configure your user pool to use your own Amazon SES configuration for sending email.`](#troubleshoot_daily_email_limit) | 
| UsernameExistsException or AliasExistsException | [`UsernameExistsException` and `AliasExistsException`](#troubleshoot_username_exists) | 
| CodeMismatchException or ExpiredCodeException | [`Invalid verification code provided, please try again.` and `Invalid code provided, please request a code again.`](#troubleshoot_code_mismatch) | 
| InvalidParameterException: username cannot be of email format | [`Username cannot be of email format, since user pool is configured for email alias.`](#troubleshoot_username_email_format) | 
| InvalidParameterException: attribute cannot be updated | [`Invalid user attributes: {{attribute}}: Attribute cannot be updated.`](#troubleshoot_immutable_attribute) | 
| InvalidParameterException: Invalid phone number format. | [`Invalid phone number format.`](#troubleshoot_invalid_phone_format) | 
| Amazon Cognito console chooses a default configuration | [The Amazon Cognito console chooses a default configuration for a new user pool](#troubleshoot_console_default_config) | 
| InvalidLambdaResponseException or UnexpectedLambdaException | [`InvalidLambdaResponseException` and `UnexpectedLambdaException`](#troubleshoot_lambda_timeout_response) | 
| Lambda trigger invocation failed due to error AccessDeniedException. | [`{{trigger name}} invocation failed due to error AccessDeniedException.`](#troubleshoot_lambda_access_denied) | 
| Migrate user trigger errors | [Migrate user trigger errors](#troubleshoot_lambda_user_migration) | 
| Invalid user attributes: Required attribute (SAML) | [`Invalid user attributes: Required attribute`](#troubleshoot_saml_required_attribute) | 
| SAML Response signature is invalid | [`Invalid SAML response received: SAML Response signature is invalid`](#troubleshoot_saml_signature_invalid) | 
| Audience restriction or Application with identifier not found | [`Audience restriction` or `Application with identifier not found`](#troubleshoot_saml_audience_restriction) | 
| An error was encountered with the requested page (SAML ACS URL) | [`An error was encountered with the requested page`](#troubleshoot_saml_acs_url) | 
| Invalid relayState from identity provider | [`Invalid relayState from identity provider`](#troubleshoot_saml_relay_state) | 
| Social or OIDC federation: attributes required: [email] | [`attributes required: [email]` for social and OIDC providers](#troubleshoot_social_oidc_attributes) | 
| Token is not from a supported provider of this identity pool. | [`Token is not from a supported provider of this identity pool.`](#troubleshoot_idp_unsupported_provider) | 
| Invalid identity pool configuration. Check assigned IAM roles for this pool. | [`Invalid identity pool configuration. Check assigned IAM roles for this pool.`](#troubleshoot_idp_invalid_config) | 
| Unauthenticated access is not supported for this identity pool. | [`Unauthenticated access is not supported for this identity pool.`](#troubleshoot_idp_unauth_not_supported) | 
| Custom domain is not a valid subdomain | [`Custom domain is not a valid subdomain`](#troubleshoot_custom_domain_subdomain) | 
| Domain already associated with another user pool | [`Domain already associated with another user pool`](#troubleshoot_domain_already_associated) | 
| One or more of the CNAMEs that you provided are already associated with a different resource | [`One or more of the CNAMEs that you provided are already associated with a different resource`](#troubleshoot_cname_already_associated) | 
| The specified SSL certificate doesn't exist | [`The specified SSL certificate doesn't exist`](#troubleshoot_ssl_certificate_not_exist) | 
| TooManyRequestsException and throttling | [`TooManyRequestsException` and throttling](#troubleshoot_too_many_requests) | 

## Sign-in and authentication
<a name="troubleshoot_signin_auth"></a>

The following errors occur during sign-in and token refresh with Amazon Cognito user pools.

### `Invalid refresh token` error
<a name="troubleshoot_invalid_refresh_token"></a>

You receive this error when you exchange a refresh token for new ID and access tokens with the `InitiateAuth` or `AdminInitiateAuth` API operation.

**Problem**  
The token refresh request fails with an `Invalid refresh token` error.

**Cause**  
+ The refresh request uses a different app client ID than the one that generated the refresh token.
+ Device tracking is enabled, but the user's device isn't confirmed, or the request doesn't include the device key.
+ Device tracking is enabled, but the initial authentication didn't use the `USER_SRP_AUTH` flow.

**Solution**  
Apply the following steps based on your user pool configuration and API usage:  
+ **Use a consistent app client ID:** When you call the `InitiateAuth` or `AdminInitiateAuth` API for token refresh, use the exact same app client ID that was used during the initial authentication that generated the refresh token.
+ **Confirm the device:** If you have [device tracking](amazon-cognito-user-pools-device-tracking.md) enabled on your user pool, but the user's device isn't confirmed, call the [ConfirmDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.html) API first. After the user confirms their device, you can exchange the refresh token.
+ **Include the device key in the refresh request:** If device tracking is enabled, include the unique device key as an `AuthParameter` when you use the `REFRESH_TOKEN_AUTH` flow:

  ```
  {
    "AuthFlow": "REFRESH_TOKEN_AUTH",
    "AuthParameters": {
      "REFRESH_TOKEN": "example_refresh_token",
      "SECRET_HASH": "example_secret_hash",
      "DEVICE_KEY": "example_device_key"
    }
  }
  ```

  Include `SECRET_HASH` only if your app client has a client secret.
+ **Use `USER_SRP_AUTH` for device tracking:** If you use device tracking, the initial authentication flow must be `USER_SRP_AUTH`.

For more information, see [Working with user devices in your user pool](amazon-cognito-user-pools-device-tracking.md).

### `Incorrect username or password.`
<a name="troubleshoot_incorrect_username_password"></a>

A sign-in request returns this error when Amazon Cognito can't authenticate the user with the credentials provided.

**Problem**  
The request returns `NotAuthorizedException` with the message `Incorrect username or password.`

**Cause**  
+ The password is wrong.
+ The user doesn't exist and the app client has **Prevent user existence errors** enabled. Amazon Cognito returns this same generic message so that it doesn't reveal whether the user exists. The legacy setting instead returns `UserNotFoundException` with `User does not exist.`
+ The request uses the wrong app client, or it's missing the `SECRET_HASH` for a client that has a client secret.
+ The user's status prevents password sign-in.

**Solution**  
+ Verify the password and confirm that the request uses the correct app client.
+ Confirm that the user exists and check the user's status with administrative tools.
+ Include a valid `SECRET_HASH` if the app client has a client secret.
We recommend that you keep **Prevent user existence errors** enabled. It protects your user pool against user enumeration. To investigate sign-in failures, use AWS CloudTrail and user pool sign-in activity instead of turning it off.

For more information, see [Managing error responses](cognito-user-pool-managing-errors.md).

### `USER_PASSWORD_AUTH flow not enabled for this client`
<a name="troubleshoot_auth_flow_not_enabled"></a>

An authentication request fails because the requested authentication flow isn't enabled on the app client.

**Problem**  
The request returns `InvalidParameterException`. The message varies by flow: `USER_PASSWORD_AUTH flow not enabled for this client` for the client-side password flow, `Auth flow not enabled for this client` for admin flows, or `USER_AUTH flow not enabled for this client` for choice-based authentication.

**Cause**  
The authentication flow in the request isn't in the app client's list of allowed authentication flows.

**Solution**  
Enable the matching flow on the app client: `ALLOW_USER_PASSWORD_AUTH` for `USER_PASSWORD_AUTH`, `ALLOW_ADMIN_USER_PASSWORD_AUTH` for admin password authentication, or `ALLOW_USER_AUTH` for choice-based authentication.  
Password-based flows send the user's password to Amazon Cognito instead of using Secure Remote Password (SRP). We recommend SRP or choice-based authentication where possible, and that you use `ADMIN_USER_PASSWORD_AUTH` only from server-side code.

For more information, see [Authentication with user pools](authentication.md).

### `User is not confirmed.`
<a name="troubleshoot_user_not_confirmed"></a>

A user who signed up but never confirmed their account can't sign in.

**Problem**  
A sign-in request returns `UserNotConfirmedException` with the message `User is not confirmed.`

**Cause**  
The user completed sign-up but never confirmed their account, so their status is `UNCONFIRMED`.

**Solution**  
+ Have the user confirm their account. Call `ResendConfirmationCode` to send a new code, then call `ConfirmSignUp` with that code.
+ An administrator can confirm the user directly with `AdminConfirmSignUp`.
+ A pre sign-up Lambda trigger can automatically confirm users.
Automatic confirmation skips email and phone number verification. We recommend that you auto-confirm users only for trusted or migration scenarios.

For more information, see [Pre sign-up Lambda trigger](user-pool-lambda-pre-sign-up.md).

### `NEW_PASSWORD_REQUIRED` challenge and `FORCE_CHANGE_PASSWORD` status
<a name="troubleshoot_new_password_required"></a>

A user that an administrator created with the `AdminCreateUser` API operation must set a new password the first time they sign in.

**Problem**  
During sign-in, Amazon Cognito returns a `NEW_PASSWORD_REQUIRED` challenge and the user can't complete authentication with only their user name and temporary password.

**Cause**  
The user has the `FORCE_CHANGE_PASSWORD` status because an administrator created them with a temporary password. Amazon Cognito requires a permanent password before it issues tokens.

**Solution**  
Respond to the challenge with the [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) API operation (or the `AdminRespondToAuthChallenge` variant). In your response:  
+ In `ChallengeResponses`, provide `NEW_PASSWORD` and `USERNAME`. Include `SECRET_HASH` if your app client has a client secret.
+ Include every attribute that the challenge lists in `requiredAttributes`, each as `userAttributes.{{attribute_name}}`. If one is missing or empty, the request returns `InvalidParameterException` with the message `Invalid attributes given, {{attribute_name}} is missing`.
+ You can only set attributes that are mutable and that the app client has write access to.
+ Include the `Session` value from the challenge response. The `Session` from the challenge can be used only once and expires. Reusing or sending an expired session returns `NotAuthorizedException` with `Invalid session for the user, session can only be used once.` or `Invalid session for the user, session is expired.` Start sign-in again to get a new session.

For more information, see [Authentication with user pools](authentication.md).

### `Attempt limit exceeded, please try after some time.`
<a name="troubleshoot_attempt_limit_exceeded"></a>

Amazon Cognito temporarily blocks further attempts after repeated failures for a user.

**Problem**  
A request returns `LimitExceededException` with the message `Attempt limit exceeded, please try after some time.`

**Cause**  
Repeated failed password or verification code attempts for the same user cause Amazon Cognito to temporarily block further attempts. This protection defends against brute-force attacks.

**Solution**  
Wait before you retry, and add exponential backoff to your client. Don't automatically resubmit failed credentials, because repeated attempts extend the block. Ask the user to try again later or to reset their password.

## App client secret (`SECRET_HASH`) errors
<a name="troubleshoot_secret_hash_required"></a>

App clients that have a client secret require a `SECRET_HASH` value in authentication API requests. The following errors occur when the secret hash is missing, incorrect, or sent to a client that has no secret.

Your application calculates the `SECRET_HASH` for the current user, app client, and client secret with the following method:

```
Base64 ( HMAC_SHA256 ( "Client Secret Key", "Username" + "Client Id" ) )
```

The `Username` must be the value sent in the request. For the `REFRESH_TOKEN_AUTH` flow, when the user name isn't a sign-in attribute, use the user's `sub`. To get the client secret, you can:

1. Open the Amazon Cognito console and navigate to your app client from the **App clients** menu. In the **App client information** section, locate **Client secret**. Choose **Show client secret** and your app client secret appears.

1. Generate a [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) request. The client secret is included in the response.

Client secrets are for confidential (server-side) clients only. Never put a client secret or the secret hash routine in a browser or mobile app.

### `Client {{client-id}} is configured with secret but SECRET_HASH was not received`
<a name="troubleshoot_secret_hash_missing"></a>

**Problem**  
An authentication API request returns `NotAuthorizedException` with a message such as `Client {{client-id}} is configured with secret but SECRET_HASH was not received`.

**Cause**  
The app client has a client secret, but the request didn't include a `SECRET_HASH`.

**Solution**  
Compute the secret hash with the formula in this section and include it in the request.

### `Unable to verify secret hash for client {{client-id}}`
<a name="troubleshoot_secret_hash_mismatch"></a>

**Problem**  
An authentication API request returns `NotAuthorizedException` with the message `Unable to verify secret hash for client {{client-id}}`.

**Cause**  
The `SECRET_HASH` value is wrong. The calculation used the wrong user name, client ID, or client secret, or the client secret was rotated or deleted.

**Solution**  
+ Recompute the secret hash with the exact user name sent in the request, the correct client ID, and the current client secret.
+ For the `REFRESH_TOKEN_AUTH` flow, when the user name isn't a sign-in attribute, use the user's `sub` as the user name in the calculation.
+ If the client secret was rotated or deleted, get the current secret and recalculate.

### `App client {{client-id}} is not configured for secret but secret hash was received`
<a name="troubleshoot_secret_hash_not_configured"></a>

**Problem**  
An authentication API request returns `InvalidParameterException` with the message `App client {{client-id}} is not configured for secret but secret hash was received`.

**Cause**  
The request sent a `SECRET_HASH` to an app client that doesn't have a client secret.

**Solution**  
Remove the `SECRET_HASH` parameter from requests to this app client.

For more information, see [Computing secret hash values](signing-up-users-in-your-app.md#cognito-user-pools-computing-secret-hash).

## OAuth 2.0 and managed login
<a name="troubleshoot_oauth_managed_login"></a>

The following errors come from the Amazon Cognito OAuth 2.0 endpoints that managed login uses.

### `redirect_mismatch` at the authorization endpoint
<a name="troubleshoot_oauth_redirect_mismatch"></a>

**Problem**  
The `/oauth2/authorize` endpoint returns an error with `redirect_mismatch`.

**Cause**  
The `redirect_uri` in the request doesn't exactly match a callback URL that is registered on the app client.

**Solution**  
Register the exact callback URL on the app client and send an identical `redirect_uri`. The URI must be absolute and must not include a fragment (`#`). It must use HTTPS, except that you can use `http://localhost` (and `127.0.0.1` and `[::1]`) for testing.

For more information, see [Authorize endpoint](authorization-endpoint.md) and [Application-specific settings with app clients](user-pool-settings-client-apps.md).

### `invalid_grant` at the token endpoint
<a name="troubleshoot_oauth_invalid_grant"></a>

**Problem**  
The `/oauth2/token` endpoint returns `invalid_grant` when it exchanges an authorization code or a refresh token.

**Cause**  
The authorization code was already redeemed or doesn't exist. Authorization codes are single-use and short-lived. The error also occurs when the refresh token was revoked.

**Solution**  
Exchange each authorization code only once, and guard against a double exchange, such as a component that runs twice or a page refresh that replays the callback. If a refresh token was revoked, have the user sign in again.

For more information, see [Token endpoint](token-endpoint.md).

### `invalid_request` with PKCE at the token endpoint
<a name="troubleshoot_oauth_invalid_request_pkce"></a>

**Problem**  
The `/oauth2/token` endpoint returns `invalid_request` when your app client uses Proof Key for Code Exchange (PKCE).

**Cause**  
The token request is missing the `code_verifier` (the `error_description` is `invalid_code_verifier`), or the `code_verifier` doesn't match the `code_challenge` that was sent to `/oauth2/authorize`.

**Solution**  
Send the original `code_verifier` that corresponds to the `code_challenge` from the authorize request, and keep it for the duration of the flow.

For more information, see [Token endpoint](token-endpoint.md).

### `invalid_client` and `unauthorized_client` at the token endpoint
<a name="troubleshoot_oauth_invalid_client"></a>

**Problem**  
The `/oauth2/token` endpoint returns `invalid_client` or `unauthorized_client`.

**Cause**  
+ `invalid_client` means client authentication failed. A client that has a secret must authenticate with an `Authorization: Basic` header or `client_secret_post`, or the client ID is unknown.
+ `unauthorized_client` means the grant type isn't enabled on the app client. It also occurs when the `redirect_uri` on the token request doesn't match the one used at `/oauth2/authorize` (the `error_description` is `invalid_redirect`).

**Solution**  
+ For confidential clients, send valid client credentials.
+ Enable the grant type on the app client.
+ Use the same `redirect_uri` in the authorize request and the token request.
Public clients don't have a secret. We recommend that public clients use the authorization code grant with PKCE.

For more information, see [Token endpoint](token-endpoint.md).

### CORS error calling the token endpoint from a browser
<a name="troubleshoot_oauth_cors"></a>

**Problem**  
Browser calls to the `/oauth2/token` endpoint fail with a cross-origin resource sharing (CORS) error.

**Cause**  
The token endpoint returns `Access-Control-Allow-Origin: *` and supports browser calls only for public clients that use the authorization code grant with PKCE. It doesn't support custom CORS origin policies, and confidential clients aren't meant to call it from a browser.

**Solution**  
For browser-based apps, use a public client with the authorization code grant and PKCE. For confidential clients, exchange the authorization code for tokens from server-side code.

For more information, see [Token endpoint](token-endpoint.md).

## Tokens and JWT validation
<a name="troubleshoot_tokens_jwt"></a>

The following issues occur when your application validates Amazon Cognito tokens or passes them to other services.

### JWT signature or claim validation fails
<a name="troubleshoot_jwt_validation"></a>

**Problem**  
Your application rejects a valid Amazon Cognito JSON Web Token (JWT), or accepts a token that it shouldn't.

**Cause**  
The token's signature, claims, or type weren't validated correctly.

**Solution**  
+ Verify the signature against the JSON Web Key Set (JWKS) for your user pool, at `https://cognito-idp.{{Region}}.amazonaws.com/{{userPoolId}}/.well-known/jwks.json`, and select the key whose `kid` matches the token header.
+ Check the `iss` claim, the `exp` claim, and the `token_use` claim (`id` for ID tokens, `access` for access tokens).
+ ID tokens carry `aud` equal to your app client ID. Access tokens carry `client_id`. An access token that is scoped to an API resource also carries `aud` with the resource.
+ We recommend the `aws-jwt-verify` library. Never trust an unverified JWT.

For more information, see [Verifying a JSON Web Token](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md).

### `Access Token does not have required scopes`
<a name="troubleshoot_token_missing_scopes"></a>

**Problem**  
A self-service user pool operation such as `GetUser`, `UpdateUserAttributes`, or `AssociateSoftwareToken` returns `NotAuthorizedException` with `Access Token does not have required scopes`.

**Cause**  
These operations require the `aws.cognito.signin.user.admin` scope, which is missing from the access token. Tokens from SDK authentication (`InitiateAuth`) include this scope. Tokens from managed login include it only if the app client allows the scope and the request asks for it. Client credentials tokens never include it.

**Solution**  
Use an access token that carries `aws.cognito.signin.user.admin`. Authenticate with the Amazon Cognito API, or request the scope in managed login and allow it on the app client. We recommend that you allow only the scopes each app client needs.

For more information, see [Scopes, M2M, and APIs with resource servers](cognito-user-pools-define-resource-servers.md).

### `401 Unauthorized` from an API Gateway user pool authorizer
<a name="troubleshoot_apigw_401"></a>

**Problem**  
Requests to an Amazon API Gateway API that uses a Amazon Cognito user pool authorizer return `401 Unauthorized`.

**Cause**  
+ You sent an ID token when the method has no OAuth scopes configured, or an access token when scopes are configured.
+ The token is expired.
+ The token came from a user pool that doesn't match the authorizer.
+ The token's format or header doesn't match the authorizer's identity source.

**Solution**  
Send the token type the method expects, make sure the token hasn't expired, confirm it was issued by the authorizer's user pool, and match the identity source header. For a detailed walkthrough, see [How do I troubleshoot HTTP 401 Unauthorized errors from an API Gateway API with a Amazon Cognito user pool authorizer?](https://repost.aws/knowledge-center/api-gateway-cognito-401-unauthorized) in the AWS Knowledge Center on the AWS re:Post website.

For more information, see [Understanding user pool JSON web tokens (JWTs)](amazon-cognito-user-pools-using-tokens-with-identity-providers.md).

## Multi-factor authentication (MFA)
<a name="troubleshoot_mfa"></a>

The following issues affect multi-factor authentication in user pools.

### Managed login users can't select an MFA factor
<a name="troubleshoot_mfa_factor_selection"></a>

**Problem**  
Users can't choose their preferred MFA method when signing in through managed login, or they aren't prompted for the MFA method you expect.

**Cause**  
Amazon Cognito follows specific logic to determine which MFA factors are available to users, based on user pool settings, user attributes, and account recovery configuration. For example, users can't use email MFA if email is configured as their primary account recovery method.

**Solution**  
To override the default MFA factor selection, you can use either of these approaches:  
+ For public applications, use [SetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.html) with a valid access token to let users set their own MFA preferences.
+ For administrator-managed applications, use [AdminSetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.html) with AWS credentials to configure user MFA preferences.
With both operations, you can enable or disable SMS, email, and TOTP MFA methods for individual users, and set one method as preferred.

For more information, see [Adding MFA to a user pool](user-pool-settings-mfa.md).

### Passwordless and passkey users can't use MFA
<a name="troubleshoot_passwordless_mfa"></a>

**Problem**  
Users who sign in with one-time password (OTP) authentication methods can't add or use multi-factor authentication.

**Cause**  
OTP sign-in flows don't support MFA.

**Solution**  
Passkey authentication with user verification can satisfy MFA requirements. Set `FactorConfiguration` to `MULTI_FACTOR_WITH_USER_VERIFICATION` in your user pool `WebAuthnConfiguration` to allow passkeys to count as multi-factor authentication.

For more information, see [Authentication with user pools](authentication.md).

## Email and SMS delivery
<a name="troubleshoot_email_sms"></a>

The following issues affect the email and SMS messages that Amazon Cognito sends, such as verification and account recovery codes.

### Not able to receive password reset code through email or SMS
<a name="troubleshoot_password_reset_delivery"></a>

**Problem**  
Users can't receive verification codes during the forgot password workflow through their email or SMS.

**Cause**  
Codes might not be delivered for several reasons, including unverified contact attributes, messaging service limits, sandbox restrictions, or MFA conflicts.

**Solution**  
Follow this checklist to troubleshoot the issue:  
+ Check the user's email spam and junk folders.
+ Confirm that the user exists in the user pool.
+ Verify that the user's status isn't `FORCE_CHANGE_PASSWORD`. If it is, an administrator created the user and Amazon Cognito prompts them to set a password when they sign in with their temporary password.
+ Check that the user has a verified email or phone number attribute.
+ Check your Amazon Simple Email Service (Amazon SES) message-sending quota.
+ For SMS, check your delivery configuration and limits:
  + Confirm that you have moved out of the SMS sandbox. In the sandbox, you can send messages only to verified destination phone numbers.
  + Check your monthly SMS spend limit.
  + Confirm that you have an origination identity, which some destinations require, such as US phone numbers.
  + Confirm the permissions for your SMS path. Amazon Cognito sends SMS messages through AWS End User Messaging SMS, which needs permission for `sms-voice:SendTextMessage`, or through the legacy Amazon SNS path, which needs permission for `sns:Publish`.
+ Check whether Amazon SES (if your user pool is configured to **Send email with Amazon SES**) has been moved out of sandbox. In the sandbox, addresses that Amazon SES hasn't verified can't receive messages.
+ If the user has an active MFA factor, check that they aren't trying to generate a message to the same factor. For example, users with email MFA active can't send password reset codes by email.

For more information, see [Email settings for Amazon Cognito user pools](user-pool-email.md) and [SMS message settings for Amazon Cognito user pools](user-pool-sms-settings.md).

### Password reset fails with unverified recovery attributes: `Could not reset password for the account, please contact support or try again`
<a name="troubleshoot_password_reset_unverified_recovery"></a>

**Problem**  
Users receive this error when they attempt to reset their password.

**Cause**  
The error occurs when the user's email or phone number attribute is unverified, or when their MFA settings prevent using the configured recovery method.

**Solution**  
Review your user pool's account recovery configuration and the affected user's verification status:  
+ **Verify recovery settings:** In your user pool, navigate to **Sign In** > **User Account Recovery**. Ensure **Self service account recovery** is enabled and review your **Recovery message delivery method** setting.
+ **Check user attribute verification:** Verify that the user has a verified email address or phone number that matches your recovery method configuration. In the console, go to the user's profile, select **User attributes** > **Edit**, and mark the appropriate attribute as verified.
+ **Resolve MFA conflicts:** Users whose preferred MFA method is email can't receive password-reset codes by email, and users with SMS MFA can't receive codes by SMS. Update your **Recovery message delivery method** to provide alternative options such as **SMS if available, otherwise email** or **Email if available, otherwise SMS**.
+ **Administrative verification:** Use the API operation [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html) to programmatically verify user attributes when console access isn't available.

For more information, see [Passwords, account recovery, and password policies](managing-users-passwords.md).

### `Exceeded daily email limit for the operation or the account. If a higher limit is required, please configure your user pool to use your own Amazon SES configuration for sending email.`
<a name="troubleshoot_daily_email_limit"></a>

**Problem**  
Email operations return `LimitExceededException` with the message `Exceeded daily email limit for the operation or the account. If a higher limit is required, please configure your user pool to use your own Amazon SES configuration for sending email.`

**Cause**  
Your user pool sends email with the default Amazon Cognito email configuration, which has a limited daily volume.

**Solution**  
Configure your user pool to send email through Amazon SES (the **Send email with Amazon SES**, or `DEVELOPER`, email-sending account) with a verified identity in a supported Region.

For more information, see [Email settings for Amazon Cognito user pools](user-pool-email.md) and [Quotas in Amazon Cognito](quotas.md).

## Sign-up, verification codes, and attributes
<a name="troubleshoot_signup_attributes"></a>

The following errors occur during sign-up, attribute verification, and attribute updates.

### `UsernameExistsException` and `AliasExistsException`
<a name="troubleshoot_username_exists"></a>

**Problem**  
Sign-up or administrative user creation fails because the user name or an alias is already in use. `SignUp` returns `UsernameExistsException` (`User already exists`, `An account with the given email already exists.`, or `An account with the given phone_number already exists.`). `AdminCreateUser` returns `User account already exists`. A request can also return `AliasExistsException`.

**Cause**  
The user name is already taken, or an email address or phone number that is configured as an alias is already associated with another user. With an alias, users can sign in with an email address or phone number in addition to their user name. A username attribute, by contrast, makes the email address or phone number the user name itself.

**Solution**  
+ Use a different user name.
+ If the alias is already taken, have the user sign in or recover the existing account instead of creating a new one.
`SignUp` returns `UsernameExistsException` for a user name that is already taken even when the app client has **Prevent user existence errors** enabled. We recommend verification-based aliases so that Amazon Cognito doesn't reveal whether an email address or phone number already exists.

For more information, see [Working with user attributes](user-pool-settings-attributes.md).

### `Invalid verification code provided, please try again.` and `Invalid code provided, please request a code again.`
<a name="troubleshoot_code_mismatch"></a>

**Problem**  
Confirmation or verification fails. `CodeMismatchException` returns `Invalid verification code provided, please try again.` and `ExpiredCodeException` returns `Invalid code provided, please request a code again.` The MFA variant is `Invalid code or auth state for the user.`

**Cause**  
The submitted code doesn't match the latest code that Amazon Cognito sent, or the code expired.

**Solution**  
Request a new code and use the most recent one. Codes have a limited validity period: sign-up confirmation and attribute verification codes are valid for 24 hours, forgot-password (account recovery) codes for 1 hour, and MFA codes for 3–15 minutes.

For more information, see [Quotas in Amazon Cognito](quotas.md).

### `Username cannot be of email format, since user pool is configured for email alias.`
<a name="troubleshoot_username_email_format"></a>

**Problem**  
`SignUp` returns `InvalidParameterException` with `Username cannot be of email format, since user pool is configured for email alias.` The phone number variant is `Username cannot be of phone number format, since user pool is configured for phone number alias.`

**Cause**  
Your user pool uses email (or phone number) as an alias attribute, so the user name can't itself be an email address (or phone number).

**Solution**  
Submit a user name that isn't an email address or phone number, such as a UUID, and pass the email address as an attribute. If you want users to sign in with an email address as the user name itself, create a new user pool with email as a username attribute. You can't change the username attributes after you create a user pool.

For more information, see [Working with user attributes](user-pool-settings-attributes.md).

### `Invalid user attributes: {{attribute}}: Attribute cannot be updated.`
<a name="troubleshoot_immutable_attribute"></a>

**Problem**  
An attribute update returns `InvalidParameterException` with `Invalid user attributes: {{attribute}}: Attribute cannot be updated.`

**Cause**  
The attribute is immutable. You set an attribute's mutability when you create the user pool, and you can't change it afterward.

**Solution**  
Write or map only mutable attributes. To list the immutable attributes in your user pool, run the following AWS CLI command:  

```bash
aws cognito-idp describe-user-pool --user-pool-id {{user-pool-id}} --query 'UserPool.SchemaAttributes[?Mutable==`false`].Name'
```

For more information, see [Standard attributes](user-pool-settings-attributes.md#how-to-edit-standard-attributes).

### `Invalid phone number format.`
<a name="troubleshoot_invalid_phone_format"></a>

**Problem**  
A request returns `InvalidParameterException` with `Invalid phone number format.`

**Cause**  
The phone number isn't in E.164 format.

**Solution**  
Format phone numbers as E.164: a plus sign, the country code, and the subscriber number, with no spaces or other separators. For example, `+12065550100`.

For more information, see [Working with user attributes](user-pool-settings-attributes.md).

### The Amazon Cognito console chooses a default configuration for a new user pool
<a name="troubleshoot_console_default_config"></a>

**Problem**  
When you set up a new user pool in the console, Amazon Cognito chooses several default settings for you. Some settings can't be changed after the user pool is created. You need to know which settings Amazon Cognito chose for you so that you can make informed choices.

**Cause**  
The new user pool setup in the Amazon Cognito console is designed for rapid testing and prototyping. The console presents you with only the most critical configuration choices, those that can't be changed after user pool creation. You can modify all other settings that Amazon Cognito configures automatically later.

**Solution**  
We recommend the following approach:  

1. Use the console to create test user pools while you refine your implementation.

1. After you've determined your production configuration, apply those settings to your test user pools.

1. Use [DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html) and [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) API operations to generate JSON templates of your tested configuration.

1. Use these templates with deployment tools like the AWS SDKs, CDK, REST API, or CloudFormation to create your production resources.

For more information, see [Create a new application in the Amazon Cognito console](getting-started-user-pools-application.md).

## Lambda triggers
<a name="troubleshoot_lambda_triggers"></a>

The following errors occur when Amazon Cognito invokes an AWS Lambda trigger in your user pool.

### `InvalidLambdaResponseException` and `UnexpectedLambdaException`
<a name="troubleshoot_lambda_timeout_response"></a>

**Problem**  
A Amazon Cognito Lambda trigger fails because the function didn't respond in time or returned output that Amazon Cognito couldn't use.

**Cause**  
Amazon Cognito must receive a response from a Lambda trigger within 5 seconds, and you can't change this limit. If the call can be retried, Amazon Cognito might retry it. A function that returns malformed or unrecognizable output causes `InvalidLambdaResponseException`. An invocation failure, such as a timeout, causes `UnexpectedLambdaException`.

**Solution**  
Return the event object with the response fields that the trigger expects. Keep trigger code fast, and offload slow work to an asynchronous process.

For more information, see [Things to know about Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md#important-lambda-considerations).

### `{{trigger name}} invocation failed due to error AccessDeniedException.`
<a name="troubleshoot_lambda_access_denied"></a>

**Problem**  
A trigger fails with `{{trigger name}} invocation failed due to error AccessDeniedException.`

**Cause**  
The function's resource-based policy doesn't allow the Amazon Cognito service principal to invoke it, or the function was deleted. This is common when you configure a trigger with the AWS CLI, an SDK, CloudFormation, or AWS CDK, because the console adds the invoke permission automatically but those paths don't.

**Solution**  
Add a resource-based policy permission that lets the Amazon Cognito service principal, `cognito-idp.amazonaws.com`, invoke the function. Scope the permission with the `aws:SourceArn` condition set to your user pool ARN and the `aws:SourceAccount` condition set to your account. If the function was deleted, point the trigger at an existing function.

For more information, see [Things to know about Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md#important-lambda-considerations).

### Migrate user trigger errors
<a name="troubleshoot_lambda_user_migration"></a>

**Problem**  
The migrate user Lambda trigger fails during sign-in or forgot-password migration. Errors include `Exception migrating user in app client {{client-id}}` (returned as `UserNotFoundException`), sometimes with a reason such as an invalid user name, a missing `email`, `phone_number`, or `preferred_username`, an invalid `messageAction`, or an invalid `deliveryMedium`. Another error is `Error during migration: invalid finalUserStatus`.

**Cause**  
The trigger isn't configured correctly, the app client doesn't allow the required flow, the function returned attributes that aren't in the pool schema, or `finalUserStatus` is invalid.

**Solution**  
+ Grant Amazon Cognito permission to invoke the function.
+ Allow `USER_PASSWORD_AUTH` or `ADMIN_USER_PASSWORD_AUTH` on the app client.
+ Set `finalUserStatus` to `CONFIRMED` to let users sign in with their existing password, or to `RESET_REQUIRED` to require a password reset. Any other value returns `Error during migration: invalid finalUserStatus`.
+ Return only attributes that exist in your pool schema, and prefix custom attributes with `custom:`.

For more information, see [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md).

## Federation
<a name="troubleshoot_federation"></a>

The following errors occur when users federate into Amazon Cognito through SAML 2.0, social, or OpenID Connect (OIDC) identity providers.

### Invalid SAML response errors in federation
<a name="troubleshoot_invalid_saml_response"></a>

Users receive various `Invalid SAML response` and similar errors when they attempt to federate into Amazon Cognito using SAML 2.0. These errors can occur because of attribute mapping issues, certificate problems, or configuration mismatches.

#### `Invalid user attributes: Required attribute`
<a name="troubleshoot_saml_required_attribute"></a>

**Problem**  
A user is missing a value for an attribute that is required in your user pool, or the IdP is attempting to remove or update an immutable attribute.

**Solution**  
+ Check the [required attributes](user-pool-settings-attributes.md#how-to-edit-standard-attributes) defined in your user pool configuration.
+ Using network capture tools in your browser, retrieve the SAML response. You might need to perform URL and base64 decoding. Verify the attribute is present in the SAML assertion.
+ Sign in to your identity provider and review the attributes that it sends to Amazon Cognito. Verify that the IdP is configured to send the required attribute using the correct name.
+ For immutable attributes, run the following AWS CLI command to identify them:

  ```bash
  aws cognito-idp describe-user-pool --user-pool-id {{user-pool-id}} --query 'UserPool.SchemaAttributes[?Mutable==`false`].Name'
  ```
+ In the SAML attribute mappings of your IdP, delete any mapping that targets an immutable Amazon Cognito attribute. Alternately, update the destination attribute to a different, mutable attribute.

#### `Invalid SAML response received: SAML Response signature is invalid`
<a name="troubleshoot_saml_signature_invalid"></a>

**Problem**  
Your IdP has updated its SAML signing certificate, causing a mismatch between the certificate in the SAML response and the metadata file stored in Amazon Cognito.

**Solution**  

1. Download the latest metadata file from your IdP.

1. In the Amazon Cognito console, navigate to the **Social and external providers** for your user pool, edit your SAML provider, and replace the existing metadata file with the newly downloaded file.

#### `Audience restriction` or `Application with identifier not found`
<a name="troubleshoot_saml_audience_restriction"></a>

**Problem**  
An incorrect Entity ID is configured in your IdP, or the assertion uses another user pool's Uniform Resource Name (URN).

**Solution**  

1. Get your Amazon Cognito user pool ID from the **Overview** section in the console.

1. In the management console for your IdP, update the entity ID in the SAML application for your user pool. Configure the entity ID to match the format `urn:amazon:cognito:sp:{{user-pool-id}}`. Replace {{user-pool-id}} with the user pool ID from the previous step.

#### `An error was encountered with the requested page`
<a name="troubleshoot_saml_acs_url"></a>

**Problem**  
The Assertion Consumer Service (ACS) URL registered with your IdP is incorrectly configured, or the IdP is not sending the SAML response using the required POST binding.

**Solution**  
+ In the management console for your IdP, update the application with the correct ACS URL format, ensuring it uses the `HTTP POST` binding.
+ **Default domain format:** `https://cognito-idp.{{Region}}.amazonaws.com/{{user-pool-id}}/saml2/idpresponse`
+ **Custom domain format:** `https://{{auth.example.com}}/saml2/idpresponse`

#### `Invalid relayState from identity provider`
<a name="troubleshoot_saml_relay_state"></a>

**Problem**  
The `RelayState` parameter is missing or invalid, or the URL is mismatched between the IdP and Amazon Cognito.

**Solution**  
+ **For [service provider initiated (SP-initiated)](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-saml-idp-authentication) flows:** Always start the authentication at your user pool `/oauth2/authorize` endpoint. SAML assertions that don't return `RelayState` parameters from the user's initial visit to Amazon Cognito are not valid SP-initiated requests.
+ **For [identity provider initiated (IdP-initiated)](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation) flows:** The IdP must include the `RelayState` parameter with the SAML assertion to the `/saml2/idpresponse` endpoint, using the required format: `redirect_uri=REDIRECT_URI&state=STATE`.

For more information, see [Using SAML identity providers with a user pool](cognito-user-pools-saml-idp.md).

### `attributes required: [email]` for social and OIDC providers
<a name="troubleshoot_social_oidc_attributes"></a>

**Problem**  
Federated sign-in with a social or OIDC identity provider fails with `attributes required: [email]` (or `username attribute mapping required`).

**Cause**  
A user pool attribute that is required isn't mapped from the IdP, or the IdP didn't return it.

**Solution**  
+ Request the scopes that return the attribute you need, such as `email`.
+ Map the required attributes from the IdP to your user pool, and map the IdP `email_verified` claim.
+ Remove a mapping only for an optional attribute that the IdP doesn't send. Don't unmap a required attribute to silence the error.

For more information, see [Mapping IdP attributes to profiles and tokens](cognito-user-pools-specifying-attribute-mapping.md) and [Setting up a social IdP](cognito-user-pools-social-idp.md).

## Identity pools
<a name="troubleshoot_identity_pools"></a>

The following errors occur when an identity pool exchanges tokens for temporary AWS credentials.

### `Token is not from a supported provider of this identity pool.`
<a name="troubleshoot_idp_unsupported_provider"></a>

**Problem**  
A `GetId` or `GetCredentialsForIdentity` request returns `NotAuthorizedException` with `Token is not from a supported provider of this identity pool.`

**Cause**  
The `Logins` map key or the token doesn't match a provider that is configured on the identity pool. For a user pool provider, the key is `cognito-idp.{{Region}}.amazonaws.com/{{userPoolId}}`, and the token's app client ID must be registered with that provider on the identity pool.

**Solution**  
Use a `Logins` key that matches a configured provider, and register the token's app client ID with that provider.

For more information, see [Identity pools external identity providers](external-identity-providers.md).

### `Invalid identity pool configuration. Check assigned IAM roles for this pool.`
<a name="troubleshoot_idp_invalid_config"></a>

**Problem**  
A `GetCredentialsForIdentity` request returns `InvalidIdentityPoolConfigurationException` with `Invalid identity pool configuration. Check assigned IAM roles for this pool.`

**Cause**  
The identity pool has no role assigned for the authentication type, or the role's trust policy doesn't allow the identity pool to assume it. The role's trust policy must allow the `sts:AssumeRoleWithWebIdentity` action for the `cognito-identity.amazonaws.com` principal, with the `cognito-identity.amazonaws.com:aud` condition set to your identity pool ID and the `cognito-identity.amazonaws.com:amr` condition set to `authenticated` or `unauthenticated`.

**Solution**  
Assign a role for the authentication type, and set the role's trust policy to allow the identity pool to assume it with the conditions described.

For more information, see [IAM roles](iam-roles.md).

### `Unauthenticated access is not supported for this identity pool.`
<a name="troubleshoot_idp_unauth_not_supported"></a>

**Problem**  
A request returns `NotAuthorizedException` with `Unauthenticated access is not supported for this identity pool.`

**Cause**  
The request didn't include any `Logins`, but the identity pool doesn't allow guest (unauthenticated) access.

**Solution**  
Either send a `Logins` map with a valid provider token, or turn on guest access and assign an unauthenticated role. If you turn on guest access, anyone on the internet can get temporary AWS credentials. Grant the unauthenticated role only the minimum permissions it needs.

For more information, see [Using role-based access control](role-based-access-control.md).

## Custom domain configuration errors
<a name="troubleshoot_custom_domain_errors"></a>

When you configure custom domain names in Amazon Cognito, you might receive error messages. Common errors include validation issues, certificate problems, or domain conflicts.

### `Custom domain is not a valid subdomain`
<a name="troubleshoot_custom_domain_subdomain"></a>

**Problem**  
Custom domain creation fails with `Custom domain is not a valid subdomain`.

**Cause**  
This error indicates an issue with DNS resolution for the parent domain. Amazon Cognito doesn't support top-level domains and requires the parent domain to have a DNS A record for validation.

**Solution**  
+ **Create an A record for the parent domain:** You must create an A record in your DNS configuration for the parent domain of your custom domain.
  + **Example:** If your custom domain is `auth.xyz.example.com`, the parent domain is `xyz.example.com`. If you want to configure `xyz.example.com` as a custom domain, the parent is `example.com`.
  + The parent domain must resolve to a valid IP address. If it doesn't point to a real IP address, you can point its A record to a placeholder IP address, as described on the custom domain setup page.
+ **(Optional) Verify DNS propagation:** To ensure your DNS provider has propagated the change, you can run a `dig` command.
  + If using `auth.xyz.example.com` as the custom domain: `dig A xyz.example.com +short`
  + If using `xyz.example.com` as the custom domain: `dig A example.com +short`
  + The command should return the IP address you configured. If it doesn't, wait until the change has fully propagated.
+ **Remove the parent domain A record:** After you successfully create the custom domain in Amazon Cognito, you can remove the A record you created for the parent domain if it was a placeholder.

For more information, see [Using your own domain for managed login](cognito-user-pools-add-custom-domain.md).

### `Domain already associated with another user pool`
<a name="troubleshoot_domain_already_associated"></a>

**Problem**  
Custom domain creation fails because the domain name is already in use. Custom domain names must be unique across all AWS accounts and Regions.

**Cause**  
The domain name is already associated with another user pool.

**Solution**  
+ To use the domain name for a new user pool, you must delete the custom domain from the user pool it's currently associated with.
+ **Wait after deletion:** It takes time for the custom domain to fully delete from the first user pool. Creating a new custom domain with the same name immediately after deletion might still result in this error. Wait a few minutes before trying again.

### `One or more of the CNAMEs that you provided are already associated with a different resource`
<a name="troubleshoot_cname_already_associated"></a>

**Problem**  
Custom domain creation fails with `One or more of the CNAMEs that you provided are already associated with a different resource`.

**Cause**  
When you create a custom domain, Amazon Cognito creates an AWS-managed Amazon CloudFront distribution. A domain name can only be used with one Amazon CloudFront distribution. This error occurs if the domain name is already in use as an alternate domain for another Amazon CloudFront distribution.

**Solution**  
+ **Option 1:** Use a different domain name for your Amazon Cognito custom domain.
+ **Option 2:** If you use the domain name for Amazon Cognito, don't use it with another Amazon CloudFront distribution.

### `The specified SSL certificate doesn't exist`
<a name="troubleshoot_ssl_certificate_not_exist"></a>

**Problem**  
Custom domain creation fails with `The specified SSL certificate doesn't exist`.

**Cause**  
Amazon Cognito uses Amazon CloudFront, which requires the AWS Certificate Manager (ACM) certificate to be in the `us-east-1` (N. Virginia) AWS Region, regardless of the user pool's Region.

**Solution**  
+ **Ensure certificate Region:** Confirm the ACM certificate is in the `us-east-1` Region.
+ **Check certificate validity:** Make sure the selected certificate isn't expired.
+ **Imported certificates:** If you imported the certificate into ACM, ensure:
  + It was issued by a public certificate authority.
  + It includes the correct certificate chain.
+ **AWS KMS policy check:** An explicit `deny` statement in an AWS Key Management Service (AWS KMS) policy for the IAM user or role creating the domain can cause this error. Specifically, check for explicit denials on `kms:DescribeKey`, `kms:CreateGrant`, or `kms:*` actions.

## Quotas and throttling
<a name="troubleshoot_quotas_throttling"></a>

### `TooManyRequestsException` and throttling
<a name="troubleshoot_too_many_requests"></a>

**Problem**  
Requests return `TooManyRequestsException`.

**Cause**  
Your request rate exceeded the quota for an operation category. `RespondToAuthChallenge` and `AdminRespondToAuthChallenge` have their own quota, which is three times the quota of the `UserAuthentication` category.

**Solution**  
Retry with exponential backoff and jitter, cache tokens instead of re-authenticating, and reduce redundant calls. If you need a higher limit, request a quota increase in Service Quotas.

For more information, see [Quotas in Amazon Cognito](quotas.md).

## Additional troubleshooting resources
<a name="troubleshoot_additional_resources"></a>

For additional troubleshooting guidance, you can also explore the following external resource:
+ [AWS Knowledge Center Amazon Cognito articles](https://repost.aws/tags/knowledge-center/TA4IvCeWI1TE66q4jEj4Z-7A/amazon-cognito) - Curated troubleshooting articles