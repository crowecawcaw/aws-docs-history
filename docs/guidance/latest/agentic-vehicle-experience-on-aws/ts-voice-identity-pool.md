

# iOS voice session fails with "Token is not from a supported provider of this identity pool"
<a name="ts-voice-identity-pool"></a>

 **Symptom.** iOS voice session startup fails with `NotAuthorizedException: Token is not from a supported provider of this identity pool`. The error is returned by the Amazon Cognito Identity service during `GetCredentialsForIdentity`. The user authenticated successfully against the Cognito user pool and holds a valid ID token; the failure is at the identity-pool credential exchange step. Web chat and any non-voice path are unaffected.

 **Root cause.** The Amazon Cognito Identity pool used for voice credential vending is configured to trust a specific Cognito user pool as its identity provider. If the iOS app authenticates against a different user pool — for example, a CMS-federated pool introduced to consolidate authentication — and that pool is not listed in the identity pool’s `CognitoIdentityProviders`, the `GetCredentialsForIdentity` call is rejected regardless of the token’s validity. The identity pool and the user pool must have a matching trust relationship; it is not sufficient for the token to be valid in its own pool.

 **Resolution.** 

1. Identify all Cognito user pools against which mobile voice clients may authenticate. For each pool, confirm whether its user pool ID and app client ID are listed as trusted providers on the voice identity pool.

1. Add any missing user pool as an additional `UserPoolAuthenticationProvider` on the identity pool, with `ServerSideTokenCheck` set to `true`. Both the user pool ID and the app client ID used by the mobile client must match the provider entry exactly.

1. Codify the trust relationship in infrastructure-as-code so that it is not lost on the next stack redeploy. If the identity pool is managed by CDK, add each additional pool as a provider entry in the construct and thread the pool ID and client ID through the stack properties. An out-of-band CLI fix that is not reflected in the CDK definition will be overwritten on the next `cdk deploy`.

1. After updating the identity pool, test the fix with the iOS client using the exact authentication flow the app uses (same user pool, same client ID, same token grant). A Python or CLI credential exchange against a different pool is not an adequate substitute.

1. If multiple deployment stages share the same identity pool infrastructure pattern, apply the same provider-list correction to each stage independently. The set of trusted providers is per-identity-pool, not per-region or per-account.