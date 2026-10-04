

# Authentication levels with ACR and AMR claims
<a name="cognito-user-pools-step-up-authentication"></a>

Amazon Cognito can record how strongly a user authenticated and which methods they used. You provide a target authentication level as an input when a user signs in, and Amazon Cognito reports the level that the user reached and the methods that they completed as claims in the tokens that it issues. These claims apply to any sign-in, including a user's initial sign-in.

You request an authentication level with the `acr_values` parameter on the managed login authorize and login endpoints, or with the equivalent `TARGET_ACR_VALUES` parameter in the `USER_AUTH` API flow. Both accept an ordered list of target authentication levels. You can add the optional `max_age` parameter (`MAX_AGE` in the API) to require that the user authenticated within a recent time window. In response to these inputs, Amazon Cognito adds two claims to the tokens that it issues:
+ The `acr` claim is a string that indicates the authentication level that the user satisfied, for example `urn:cognito:loa:3`.
+ The `amr` claim is an array of strings that indicates the authentication methods that the user completed, for example `["pwd", "otp", "mfa"]`.

The `acr` and `amr` claims follow the definitions in the OpenID Connect Core specification. Amazon Cognito uses its own ACR level URIs. You can translate the Amazon Cognito levels to whatever standard your application requires.

Step-up authentication is a common use case for these claims. In step-up authentication, your application requires a user to authenticate with a stronger method before they perform a sensitive operation. To decide whether to prompt, your application compares the `acr` level and the `auth_time` claim in the user's ID token against the level and freshness that the operation requires, and requests step-up only when they aren't already met. When step-up is needed, redirect the user to the managed login authorize or login endpoint with `acr_values`, or call the `USER_AUTH` API flow with `TARGET_ACR_VALUES`. For an example, see the [Step-up authentication](cognito-scenarios.md#scenario-step-up-authentication) scenario.

You can request ACR and AMR from any Amazon Cognito sign-in entry point. The mechanics for each entry point are documented with that entry point.
+ SDK and API sign-in — Request a target level in the `USER_AUTH` flow with the `TARGET_ACR_VALUES` and `MAX_AGE` parameters. For the parameters and step-up behavior, see [Step-up authentication with the USER\_AUTH flow](authentication-flows-selection-sdk.md#cognito-user-pools-step-up-user-auth).
+ Managed login and hosted UI — Pass the `acr_values` and `max_age` parameters on the authorize and login endpoints. For details, see the [authorize endpoint](authorization-endpoint.md#authorization-endpoint-step-up) and [login endpoint](login-endpoint.md#login-endpoint-step-up).
+ Federated sign-in — Amazon Cognito derives the ACR and AMR values of a federated user from the identity provider (IdP) response and maps them with the `AcrMapping` field. For OIDC identity providers, see [Step-up authentication for federated users](cognito-user-pools-oidc-idp.md#cognito-user-pools-step-up-federation).

Requesting step-up authentication requires the Essentials or Plus feature plan. For more information, see [Feature plan requirements](#cognito-user-pools-step-up-authentication-tiers).

**Topics**
+ [Authentication levels and methods](#cognito-user-pools-step-up-authentication-concepts)
+ [Configuring ACR level names](#cognito-user-pools-step-up-acr-configuration)
+ [Feature plan requirements](#cognito-user-pools-step-up-authentication-tiers)
+ [Your responsibilities for step-up authentication](#cognito-user-pools-step-up-responsibilities)

## Authentication levels and methods
<a name="cognito-user-pools-step-up-authentication-concepts"></a>

Amazon Cognito evaluates the authentication factors that a user completes and expresses the result as an authentication level in the `acr` claim and a list of authentication methods in the `amr` claim.

### ACR authentication levels
<a name="cognito-user-pools-step-up-acr-levels"></a>

Amazon Cognito defines four fixed authentication levels. The authentication factor combinations that satisfy each level are fixed and you can't change them. You can customize only the URI name of each level for your user pool. For more information, see [Configuring ACR level names](#cognito-user-pools-step-up-acr-configuration).

Amazon Cognito assigns the highest authentication level that the user's completed factors fully satisfy.


**ACR levels and satisfying factor combinations**  

| ACR level | Default ACR value | Satisfying factor combinations | 
| --- | --- | --- | 
| 1 | urn:cognito:loa:1 | Password only | 
| 2 | urn:cognito:loa:2 | A single one-time password delivered by SMS or email. Level 2 doesn't include passkeys | 
| 3 | urn:cognito:loa:3 | A passkey (platform or roaming) on its own; or a password with an SMS one-time code; or a password with an email one-time code | 
| 4 | urn:cognito:loa:4 | A password with a time-based one-time password (TOTP) from an authenticator app | 

Level 1 represents password-only authentication. Federation doesn't satisfy a level through this table. Instead, Amazon Cognito derives the authentication level of a federated user from the response of the identity provider (IdP). For more information, see [Step-up authentication for federated users](cognito-user-pools-oidc-idp.md#cognito-user-pools-step-up-federation).

### AMR values
<a name="cognito-user-pools-step-up-amr-values"></a>

The `amr` claim is a list of strings. Each authentication factor that the user completes adds its value to the list. Amazon Cognito can add the following values.


**AMR values**  

| Authentication method | AMR value | Notes | 
| --- | --- | --- | 
| Password | pwd | Password-family sign-in, including Secure Remote Password (SRP) | 
| TOTP from an authenticator app | otp | A time-based one-time password from an app such as an authenticator app | 
| SMS one-time code | sms | A one-time code delivered by SMS | 
| Email one-time code | email\_otp | A one-time code delivered by email | 
| Passkey with a platform authenticator | swk | A software-bound key, for example a passkey secured by a device biometric | 
| Passkey with a roaming authenticator | hwk | A hardware-bound key, for example a security key | 
| Multi-factor combination | mfa | Added when the user completes two or more distinct factors | 
| Federated sign-in | fed | A default placeholder that Amazon Cognito adds when a user federates through an IdP that doesn't support ACR and AMR, or returns no values that Amazon Cognito recognizes | 

### ACR and AMR token claims
<a name="cognito-user-pools-step-up-token-claims"></a>

Amazon Cognito adds the `acr` and `amr` claims to access tokens and ID tokens. Your application inspects the `acr` and `amr` claims in the access token or ID token to evaluate the authentication level. When a user refreshes their tokens, Amazon Cognito preserves the same `acr` and `amr` values on the new access and ID tokens, so the user isn't asked to step up again after every refresh. For more information about token contents, see [Using the ID token](amazon-cognito-user-pools-using-the-id-token.md) and [Using the access token](amazon-cognito-user-pools-using-the-access-token.md).

The following example shows an ID token after a user authenticates with a password and a TOTP.

```
{
  "sub": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_ExAmPlE",
  "aud": "abc123def456",
  "exp": 1759348800,
  "iat": 1759345200,
  "auth_time": 1759345200,
  "token_use": "id",
  "acr": "urn:cognito:loa:4",
  "amr": ["pwd", "otp", "mfa"],
  "email": "user@example.com",
  "cognito:username": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
}
```

When a user refreshes their tokens, Amazon Cognito sets the same `acr` and `amr` values on the new access and ID tokens. The values carry over without modification. This behavior provides a smoother experience because users aren't asked to step up again after every refresh.

Refreshing a token doesn't reset the `auth_time` claim. If you want to force a user to authenticate again after a period of time, use the `max_age` parameter, which compares the current time to `auth_time` regardless of how many times the user refreshed their tokens.

When a user completes step-up authentication, Amazon Cognito issues new access, ID, and refresh tokens with the updated `acr` and `amr` claims and a fresh validity period.

## Configuring ACR level names
<a name="cognito-user-pools-step-up-acr-configuration"></a>

You can customize the URI name of each authentication level for your user pool with the `AcrConfiguration` field. Configure this field when you create or update a user pool with the [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) or [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) operation. The factor combinations that satisfy each level stay fixed. You customize only the names.

Configuring custom ACR level names with the `AcrConfiguration` field requires the Essentials or Plus feature plan. For more information, see [Feature plan requirements](#cognito-user-pools-step-up-authentication-tiers).

The `AcrConfiguration` field is a map with the keys `Level1` through `Level4`. Each value is an object with a single `AcrValue` string. You can override only the levels that you want to customize. The following example request customizes the names of levels 2 and 3.

```
{
  "AcrConfiguration": {
    "Level2": { "AcrValue": "urn:my-standard:loa:2" },
    "Level3": { "AcrValue": "urn:my-standard:loa:3" }
  }
}
```

The response always returns the effective configuration, with the default names merged in for any levels that you didn't customize.

```
{
  "AcrConfiguration": {
    "Level1": { "AcrValue": "urn:cognito:loa:1" },
    "Level2": { "AcrValue": "urn:my-standard:loa:2" },
    "Level3": { "AcrValue": "urn:my-standard:loa:3" },
    "Level4": { "AcrValue": "urn:cognito:loa:4" }
  }
}
```

The following validation rules apply to each `AcrValue`.
+ Each `AcrValue` must be unique across all four levels. This includes the default names that fill in for levels that you don't customize. A value that collides with the default for an uncustomized level is rejected.
+ Each `AcrValue` is a string of 1 to 64 characters.
+ Each `AcrValue` can't contain spaces, double quotation marks, or backslashes.

If you change your ACR level names, a user might later present an access token whose `acr` value no longer matches any configured level. Amazon Cognito doesn't respect the stale value and treats it as an unrecognized level, but this isn't an error. Amazon Cognito still honors the token's `amr` values and prompts only for factors that aren't already listed in the `amr` claim, without crediting any particular level.

## Feature plan requirements
<a name="cognito-user-pools-step-up-authentication-tiers"></a>

The following capabilities require the Essentials or Plus feature plan.
+ Requesting step-up authentication. This applies to the `TARGET_ACR_VALUES` parameter on `InitiateAuth` and the `acr_values` parameter on managed login.
+ Configuring custom ACR level names with the `AcrConfiguration` field on `CreateUserPool` or `UpdateUserPool`.

The behavior when you request step-up authentication on an insufficient feature plan depends on the entry point.
+ The `InitiateAuth` API returns a `FeatureUnavailableInTierException`.
+ The managed login authorize endpoint silently ignores `acr_values` and proceeds with normal authentication, without an error.

For more information about feature plans, see [User pool feature plans](cognito-sign-in-feature-plans.md).

## Your responsibilities for step-up authentication
<a name="cognito-user-pools-step-up-responsibilities"></a>

Amazon Cognito issues tokens with the authentication level that the user achieved. Your application is responsible for the following.
+ Check the user's current ID token before you redirect. Evaluate `auth_time` against your `max_age`, and the ID token's `acr` level against the level that the operation requires, with the tokens that your application already holds. Redirect the user to Amazon Cognito for step-up only if the required level or freshness isn't already met.
+ Set the correct `TARGET_ACR_VALUES` or `acr_values`, and the correct `MAX_AGE` or `max_age`. Amazon Cognito acts only on what you provide. It doesn't infer the level or freshness that you intend. If you request the wrong level or omit the parameters, Amazon Cognito doesn't step the user up as you intended.
+ Validate the `acr` claim in your application. After Amazon Cognito returns tokens, your application must verify that the `acr` claim matches the level that the operation requires before it grants access. Amazon Cognito issues the token with the achieved level. Enforcing that an operation requires a given level is the responsibility of your application.
+ Translate Amazon Cognito levels to other standards outside the token. Amazon Cognito computes the `acr` and `amr` claims from the authentication flow. You can't customize, override, add to, or suppress these claims with a pre token generation Lambda trigger or any other Lambda trigger. If you need to translate the Amazon Cognito levels to another standard, such as NIST or eIDAS, do so in your application layer.