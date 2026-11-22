

# Supported policy types

You can use X.509 certificate condition keys in the following policy types:
+ **IAM identity-based policies** – Attach to the users, groups, or roles that request certificates. Supports `Allow` and `Deny` statements.
+ **Service control policies (SCPs) and resource control policies (RCPs)** – Apply guardrails across the accounts in an organization in AWS Organizations. Use `Deny` statements.
+ **VPC endpoint policies** – Restrict the certificates that can be requested through an interface VPC endpoint for AWS Private CA. Supports `Allow` and `Deny` statements.
+ **Resource-based policies** – Control cross-account issuance from a shared CA. AWS Private CA resource-based policies are managed through AWS Resource Access Manager (RAM) and support only `Allow` statements. To restrict the certificates that a cross-account principal can request, add conditions to the `Allow` statement for `acm-pca:IssueCertificate`, for example in a RAM customer managed permission. For more information, see [Customer managed permissions in RAM](pca-cmp.md) and [Resource-based policies](pca-rbp.md).

Most of the examples in this topic use `Deny` statements. Because a resource-based policy can't contain a `Deny` statement, use those examples in identity-based policies, SCPs, RCPs, or VPC endpoint policies.