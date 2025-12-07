# Controlling access with IAM policies

IAM provides multiple policy types to control access to the outbound identity federation feature. You can use [identity-based policies](access_policies_identity-vs-resource.md "access_policies_identity-vs-resource.md") to control which IAM principals can request tokens and enforce specific token properties such as audience, lifetimes, and signing algorithms. [Service Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCPs) enable you to enforce organization-wide restrictions on token generation across all accounts in your AWS Organizations. [Resource Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") (RCPs) control access at the resource level. You can also use [VPC endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") to restrict which principals can access the AWS STS `GetWebIdentityToken` API through your VPC endpoints, adding network-level controls to your security posture. This section explains how to implement fine-grained access controls using these policy types and condition keys.

To request identity tokens, an IAM principal must have the `sts:GetWebIdentityToken` permission. Grant this permission through identity policies attached to IAM users or roles. To allow Tags (key, value pairs) to be passed to the GetWebIdentityToken call, the IAM principal must have the `sts:TagGetWebIdentityToken` permission.

- Use the [sts:IdentityTokenAudience](reference_policies_iam-condition-keys.md#ck_identitytokenaudience "reference_policies_iam-condition-keys.md#ck_identitytokenaudience") condition key to limit which external services can receive tokens.
- Use the [sts:DurationSeconds](reference_policies_iam-condition-keys.md#ck_durationseconds "reference_policies_iam-condition-keys.md#ck_durationseconds") condition key to enforce maximum token lifetimes.
- Use the [sts:SigningAlgorithm](reference_policies_iam-condition-keys.md#ck_signingalgorithm "reference_policies_iam-condition-keys.md#ck_signingalgorithm") condition key to require specific cryptographic algorithms.
- Use the [aws:RequestTag](reference_policies_condition-keys.md#condition-keys-requesttag "reference_policies_condition-keys.md#condition-keys-requesttag") condition key compare the tag key-value pair that was passed in the request with the tag pair that you specify in the policy.
- Use the [aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys "reference_policies_condition-keys.md#condition-keys-tagkeys") condition key to compare the tag keys in a request with the keys that you specify in the policy.
  Refer to [IAM and AWS STS](reference_policies_iam-condition-keys.md "reference_policies_iam-condition-keys.md") condition keys to learn more about the condition keys available in IAM policies.

This sample identity policy combines multiple condition keys:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowTokenGenerationWithRestrictions",
            "Effect": "Allow",
            "Action": "sts:GetWebIdentityToken",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "sts:IdentityTokenAudience": [
                        "https://api1.example.com",
                        "https://api2.example.com"
                    ]
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

## Best practices

Follow these recommendations to securely federate your AWS identities to external services.

- **Use short token lifetimes:** Request tokens with the shortest lifetime that meets your operational needs.
- **Implement least privilege access and restrict token properties with IAM policies:** Grant the `sts:GetWebIdentityToken` permission only to IAM principals that require it. Use condition keys to specify signing algorithms, permitted token audiences, and maximum token lifetimes as you require.
- **Validate claims in external services:** For security, always validate relevant claims such as subject ("sub"), audience ("aud") etc. to ensure they match your expected values. Validate custom claims when possible to enable fine-grain authorization decisions in external services.
