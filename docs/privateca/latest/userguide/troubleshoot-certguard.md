

# AccessDeniedException with X.509 certificate condition keys

When a policy that uses X.509 certificate condition keys denies a request, AWS Private CA returns an `AccessDeniedException`. The response doesn't say which condition key or value caused the denial. Use the following steps to find the cause.

1. Find the denied request in AWS CloudTrail. The error message might state whether an explicit `Deny` statement or the absence of an `Allow` statement caused the denial, and the type of policy involved. If it does, start with the policies of that type. Otherwise, check each type of policy that applies to the principal: identity-based policies, SCPs, RCPs, VPC endpoint policies, and the CA's resource-based policy.

1. Compare the certificate that you requested with each statement that refers to X.509 certificate condition keys. Work out the value of each key from the CSR, the certificate template, any API passthrough values, and the request parameters, as described in [Condition key reference](certguard-condition-keys.md#certguard-condition-key-reference).

1. Check for the following common causes:
   + A negated operator, such as `StringNotEquals`, on a key that the certificate doesn't have. These conditions are `true` for absent keys, so the `Deny` statement applies.
   + A case-sensitive comparison on `acm-pca:x509Subject/CN` or `acm-pca:x509SAN/Name/CN`. Use `ForAnyValue:StringEqualsIgnoreCase` or `ForAnyValue:StringNotEqualsIgnoreCase`.
   + A hostname in a condition written in uppercase or with a trailing dot. AWS Private CA lowercases hostnames and removes the trailing dot before evaluation.
   + A `ForAllValues` condition on `acm-pca:x509Ext/ExtendedKeyUsage` that lists purpose names but not their OIDs.
   + An hour-based validity limit that doesn't account for the default `notBefore`, which is 60 minutes before the issuance time.
   + A condition value that contains characters outside Latin-1. IAM can't match these values.
   + A statement that applies to requests made by ACM or a connector on your behalf. Scope the statement to the principals that it's meant for. For connector creation failures, see [Allow connector creation when you use X.509 certificate condition keys](pca-rbp.md#connector-permission-check-condition-keys).

1. Change the request or the policy, and try the request again. Test policy changes in a non-production account first.

If AWS Private CA returns a `MalformedCSRException` instead, for more information about resolving it, see [MalformedCSRException with X.509 certificate condition keys](troubleshoot-certguard-malformed-csr.md).