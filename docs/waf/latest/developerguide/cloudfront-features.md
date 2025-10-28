**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using AWS WAF with Amazon CloudFront

Learn how to use AWS WAF with Amazon CloudFront features.

When you create a protection pack (web ACL), you can specify one or more CloudFront distributions that you want AWS WAF
to inspect. CloudFront supports two types of distributions: standard distributions that protect individual tenants,
and multi-tenant distributions that protect multiple tenants through a single, shared configuration template.
AWS WAF inspects web requests for both distribution types based on
the rules you define in your protection packs (web ACLs), with different implementation patterns for each type.

###### Topics

- [How AWS WAF works with different distribution types](#cloudfront-features-distribution-types "#cloudfront-features-distribution-types")
- [Common use cases for protecting CloudFront distributions with AWS WAF](cloudfront-waf-use-cases.md "cloudfront-waf-use-cases.md")

## How AWS WAF works with different distribution types

### Distribution types

AWS WAF provides web application firewall capabilities for both standard and multi-tenant distribution CloudFront distributions.

#### Standard distributions

For standard distributions, AWS WAF adds protection using a single protection pack (web ACL) for each distribution.
You can enable this protection by associating an existing protection pack (web ACL) with a CloudFront distribution or by using one-click protection in the CloudFront console.
This lets you manage the security controls for each of your distributions independently, since any changes to a protection pack (web ACL) will only affect
the distribution associated with it.

This straightforward method of protecting CloudFront distributions is optimal for providing individual domains with specific protections from a single protection pack (web ACL).

##### Standard distribution considerations

- Changes to a protection pack (web ACL) affect only its associated distribution
- Each distribution requires independent protection pack (web ACL) configuration
- Rules and rule groups are managed separately for each distribution

#### Multi-tenant distributions

For multi-tenant distributions, AWS WAF adds protection across multiple domains using a single protection pack (web ACL).
Domains that are managed by multi-tenant distributions are known as distribution tenants.
You can only enable AWS WAF protection for multi-tenant distributions in the CloudFront console, either during or after the multi-tenant distribution creation process. However, changes to a protection pack (web ACL) are still managed through the AWS WAF console or API.

Multi-tenant distributions offer the flexibility to enable AWS WAF protections at two levels:

- **Multi-tenant distribution level** – Associated protection packs (web ACLs) provide baseline security controls that apply to all applications
  sharing that distribution
- **Distribution tenant level** – Individual tenants within a multi-tenant distribution can have their own protection packs (web ACLs) to implement additional security controls or override multi-tenant distribution settings

These two tiers make multi-tenant distributions optimal for sharing AWS WAF protections across multiple domains without losing the ability to customize security for an individual distribution.

#### Multi-tenant distribution considerations

- Individual distribution tenants inherit changes made to protection packs (web ACLs) that are associated with related multi-tenant distributions
- The protection packs (web ACLs) associated with specific distribution tenants can override settings
  configured at the multi-tenant protection pack (web ACL) level
- Managed rule groups can be implemented at both distribution and distribution tenant levels
- Application identifiers can be located in logs to track security events by distribution

### AWS WAF features by distribution type

| Compare protection pack (web ACL) implementations | AWS WAF Feature                                | Standard distributions                                                                                                    | Multi-tenant distributions |
| ------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| Associating protection packs (web ACLs)           | One protection pack (web ACL) per distribution | You can share protection packs (web ACLs) across tenants, with optional tenant-specific protection packs (web ACLs)       |
| Rule management                                   | Rules affect a single distribution             | Multi-tenant distribution rules affect all associated tenants; distribution tenant-specific rules affect only that tenant |
| Managed rule groups                               | Applied to individual distributions            | Can be applied at multi-tenant distribution level for all tenants or at tenant level for specific applications            |
| Logging                                           | Standard AWS WAF logs                          | Logs include tenant identifiers for security event attribution                                                            |
