

# Controlling access with IAM policies

IAM provides multiple policy types to control access to the outbound identity federation feature. You can use [identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) to control which IAM principals can request tokens and enforce specific token properties such as audience, lifetimes, signing algorithms, subject selection, and Scope values. [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) enable you to enforce organization-wide restrictions on token generation across all accounts in your AWS Organizations. [Resource Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (RCPs) control access at the resource level. You can also use [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) to restrict which principals can access the AWS STS `GetWebIdentityToken` API through your VPC endpoints, adding network-level controls to your security posture. This section explains how to implement fine-grained access controls using these policy types and condition keys.

The permissions required to call `GetWebIdentityToken` depend on the properties included in the request:
+ Every token request requires `sts:GetWebIdentityToken`. Grant this permission through an identity-based policy attached to an IAM user or role.
+ A request that includes tags also requires `sts:TagGetWebIdentityToken`.
+ A request that includes Scope also requires `sts:SetWebIdentityTokenScope`. This permission does not replace `sts:GetWebIdentityToken`. A request that omits Scope does not require `sts:SetWebIdentityTokenScope`.

Selecting a `SubjectMode` does not require a separate action permission. To restrict which mode a principal can select, apply the `sts:SubjectMode` condition key to the policy statement that allows `sts:GetWebIdentityToken`.
+ Use the [sts:IdentityTokenAudience](reference_policies_iam-condition-keys.md#ck_identitytokenaudience) condition key to limit which external services can receive tokens.
+ Use the [sts:DurationSeconds](reference_policies_iam-condition-keys.md#ck_durationseconds) condition key to enforce maximum token lifetimes.
+ Use the [sts:SigningAlgorithm](reference_policies_iam-condition-keys.md#ck_signingalgorithm) condition key to require specific cryptographic algorithms.
+ Use the `sts:SubjectMode` condition key to restrict which identity AWS STS places in `sub`. `AWSIdentity` selects the ARN of the requesting IAM principal. `OriginIdentity` selects the TIP Subject carried by the calling session. For the shared context model and trusted identity sources, see [trusted identity propagation (TIP)](id_roles_providers_tip.md). When the request omits `SubjectMode`, AWS STS uses `AWSIdentity` as the effective mode and evaluates the `sts:SubjectMode` condition key with the value `AWSIdentity`.
+ Use the multivalued `sts:IdentityTokenScope` condition key to restrict the individual values supplied in Scope. AWS STS represents each distinct space-delimited Scope value as a separate condition-key value. Use a multivalued condition operator when the policy must evaluate multiple requested values.
+ Use the [aws:RequestTag](reference_policies_condition-keys.md#condition-keys-requesttag) condition key compare the tag key-value pair that was passed in the request with the tag pair that you specify in the policy.
+ Use the [aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys) condition key to compare the tag keys in a request with the keys that you specify in the policy.

Refer to [IAM and AWS STS](reference_policies_iam-condition-keys.md) condition keys to learn more about the condition keys available in IAM policies.

This sample identity policy combines multiple condition keys:

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowTokenGenerationWithRestrictions",
            "Effect": "Allow",
            "Action": "sts:GetWebIdentityToken",
            "Resource": "*",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "sts:IdentityTokenAudience": [
                        "https://api1.example.com",
                        "https://api2.example.com"
                    ]
                },
                "Null": {
                    "sts:IdentityTokenAudience": "false"
                },
                "NumericLessThanEquals": {
                    "sts:DurationSeconds": 300
                },
                "StringEquals": {
                    "sts:SigningAlgorithm": "ES384"
                }
            }
        }
    ]
}
```

`ForAllValues:StringEquals` requires every audience in the request to match an approved value. A request that includes an additional unapproved audience does not match this Allow statement. Because `ForAllValues:StringEquals` is also true when the key is absent, include a `Null` condition set to `false` to require `sts:IdentityTokenAudience` to be present and nonempty. For more information, see [Set operators for multivalued context keys](reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys).

## Control the subject identity
<a name="outbound-policy-subject-identity"></a>

`sts:SubjectMode` is a single-valued condition key. Use it in a policy condition to control which identity a caller can select for the standard `sub` claim:
+ `AWSIdentity` selects the ARN of the IAM principal that requested the token.
+ `OriginIdentity` selects the TIP Subject carried by the calling session.

The following policy allows `GetWebIdentityToken` only when the request selects `OriginIdentity` and the audience matches the external service. When the request omits `SubjectMode`, AWS STS uses `AWSIdentity` as the effective mode. Therefore, a request that omits `SubjectMode` does not match this Allow statement.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowTokenWithOriginIdentityForExternalService",
            "Effect": "Allow",
            "Action": "sts:GetWebIdentityToken",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sts:SubjectMode": "OriginIdentity"
                },
                "ForAllValues:StringEquals": {
                    "sts:IdentityTokenAudience": "https://api.example.com"
                }
            }
        }
    ]
}
```

This policy authorizes the subject mode, but it does not create or attach TIP context. The credentials used to call AWS STS must meet the [`OriginIdentity` requirements](id_roles_providers_outbound_getting_started.md#outbound-federation-prerequisites). Otherwise, a request that selects `OriginIdentity` fails even when the IAM policy allows that mode. For the resulting claim behavior, see [Understanding token claims](id_roles_providers_outbound_token_claims.md).

## Control Scope values
<a name="outbound-policy-scope-values"></a>

Scope is an optional request value that represents what the caller requests from the external service. AWS STS copies an accepted Scope value into the token, but does not interpret it or grant permissions based on it. The external service determines what each value means and whether the identity in `sub` can use it.

When a request includes Scope, AWS STS performs an additional authorization check for `sts:SetWebIdentityTokenScope`. This is not a separate API operation. The principal needs both `sts:GetWebIdentityToken` and `sts:SetWebIdentityTokenScope`. A request that omits Scope does not require or invoke the `sts:SetWebIdentityTokenScope` authorization check.

Scope can be specified only when `SubjectMode` is `OriginIdentity` and the request specifies exactly one audience. IAM permissions cannot make a request that violates these requirements valid.

Although Scope is one space-delimited request string, AWS STS represents each distinct Scope value separately in the multivalued `sts:IdentityTokenScope` condition key. Scope values are case-sensitive when you use case-sensitive string operators. Use a multivalued condition operator to evaluate them.

The following policy allows a token request with `SubjectMode` set to `OriginIdentity` for one audience and restricts Scope to the `read` and `write` values. `ForAllValues:StringEquals` requires every requested Scope value to match an allowed value.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowTokenWithOriginIdentityForExternalService",
            "Effect": "Allow",
            "Action": "sts:GetWebIdentityToken",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sts:SubjectMode": "OriginIdentity"
                },
                "ForAllValues:StringEquals": {
                    "sts:IdentityTokenAudience": "https://api.example.com"
                }
            }
        },
        {
            "Sid": "AllowApprovedScopeValues",
            "Effect": "Allow",
            "Action": "sts:SetWebIdentityTokenScope",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sts:SubjectMode": "OriginIdentity"
                },
                "ForAllValues:StringEquals": {
                    "sts:IdentityTokenScope": [
                        "read",
                        "write"
                    ]
                }
            }
        }
    ]
}
```

The `AllowApprovedScopeValues` statement matches Scope values such as `read` and `write read`. It does not match `read delete` because `delete` is not in the allowed set. If the request includes tags, add the existing `sts:TagGetWebIdentityToken` permission as appropriate.

The permissions on this page control the outbound `GetWebIdentityToken` request; they do not attach TIP context to the calling session. To control TIP context attachment, including use of `sts:SetContext`, see [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md).

## Best practices
<a name="outbound-best-practices"></a>

Follow these recommendations to securely federate your AWS identities to external services.
+ **Use short token lifetimes:** Request tokens with the shortest lifetime that meets your operational needs.
+ **Grant least-privilege permissions:** Grant `sts:GetWebIdentityToken` only to IAM principals that require it. Grant `sts:TagGetWebIdentityToken` and `sts:SetWebIdentityTokenScope` only when callers need the corresponding optional request properties.
+ **Restrict token properties:** Use IAM condition keys to limit signing algorithms, audiences, token lifetimes, permitted `SubjectMode` values, and Scope values. When you permit Scope, use `sts:IdentityTokenScope` to restrict every requested value.
+ **Preserve default subject compatibility:** If an external service expects `sub` to contain an IAM principal ARN, omit `SubjectMode` or restrict it to `AWSIdentity`.
+ **Validate tokens and claims in external services:** Validate the token signature and relevant claims, including issuer (`iss`), subject (`sub`), audience (`aud`), expiration (`exp`), and the AWS identity and session-context claims your authorization model uses. If the token includes `scope`, independently determine what each value permits. When `SubjectMode` is `OriginIdentity`, validate `sub` together with `iss` and either `origin_identity.issuer` or `origin_identity.federated_provider_arn`. In this mode, `principal_id` under the `https://sts.amazonaws.com/` namespace identifies the IAM principal that requested the token. Validate `principal_id` when your authorization model also depends on that principal.
+ **Plan for SAML signing-key rotation:** For a TIP session established through SAML federation, `origin_identity.issuer` changes when the identity provider rotates its signing certificate. Update approved issuer values before rotation, or use `origin_identity.federated_provider_arn` when the external service needs a stable identifier for the configured SAML provider.