

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Using AWS WAF with Amazon CloudFront
<a name="cloudfront-features"></a>

Learn how to use AWS WAF with Amazon CloudFront features.

When you create a protection pack (web ACL), you can specify one or more CloudFront distributions that you want AWS WAF to inspect. CloudFront supports two types of distributions: standard distributions that protect individual tenants, and multi-tenant distributions that protect multiple tenants through a single, shared configuration template. AWS WAF inspects web requests for both distribution types based on the rules you define in your protection packs (web ACLs), with different implementation patterns for each type.

**Topics**
+ [How AWS WAF works with different distribution types](#cloudfront-features-distribution-types)
+ [Using AWS WAF with CloudFront Flat-Rate Pricing Plans](#waf-cf-pricing-plans)
+ [AI traffic monetization with CloudFront](#cloudfront-features-ai-traffic-monetization)
+ [Common use cases for protecting CloudFront distributions with AWS WAF](cloudfront-waf-use-cases.md)

## How AWS WAF works with different distribution types
<a name="cloudfront-features-distribution-types"></a>

### Distribution types
<a name="distribution-types-overview"></a>

AWS WAF provides web application firewall capabilities for both standard and multi-tenant distribution CloudFront distributions.

#### Standard distributions
<a name="standard-distribution-overview"></a>

For standard distributions, AWS WAF adds protection using a single protection pack (web ACL) for each distribution. You can enable this protection by associating an existing protection pack (web ACL) with a CloudFront distribution or by using one-click protection in the CloudFront console. This lets you manage the security controls for each of your distributions independently, since any changes to a protection pack (web ACL) will only affect the distribution associated with it.

This straightforward method of protecting CloudFront distributions is optimal for providing individual domains with specific protections from a single protection pack (web ACL).

##### Standard distribution considerations
<a name="standard-waf-considerations"></a>
+ Changes to a protection pack (web ACL) affect only its associated distribution
+ Each distribution requires independent protection pack (web ACL) configuration
+ Rules and rule groups are managed separately for each distribution

#### Multi-tenant distributions
<a name="tenant-distribution-overview"></a>

For multi-tenant distributions, AWS WAF adds protection across multiple domains using a single protection pack (web ACL). Domains that are managed by multi-tenant distributions are known as distribution tenants. You can only enable AWS WAF protection for multi-tenant distributions in the CloudFront console, either during or after the multi-tenant distribution creation process. However, changes to a protection pack (web ACL) are still managed through the AWS WAF console or API. 

Multi-tenant distributions offer the flexibility to enable AWS WAF protections at two levels:
+ **Multi-tenant distribution level** – Associated protection packs (web ACLs) provide baseline security controls that apply to all applications sharing that distribution
+ **Distribution tenant level** – Individual tenants within a multi-tenant distribution can have their own protection packs (web ACLs) to implement additional security controls or override multi-tenant distribution settings

These two tiers make multi-tenant distributions optimal for sharing AWS WAF protections across multiple domains without losing the ability to customize security for an individual distribution. 

#### Multi-tenant distribution considerations
<a name="tenant-waf-considerations"></a>
+ Individual distribution tenants inherit changes made to protection packs (web ACLs) that are associated with related multi-tenant distributions
+ The protection packs (web ACLs) associated with specific distribution tenants can override settings configured at the multi-tenant protection pack (web ACL) level
+ Managed rule groups can be implemented at both distribution and distribution tenant levels
+ Application identifiers can be located in logs to track security events by distribution

### AWS WAF features by distribution type
<a name="distribution-types-comparison"></a>


**Compare protection pack (web ACL) implementations**  

| AWS WAF Feature | Standard distributions | Multi-tenant distributions | 
| --- | --- | --- | 
| Associating protection packs (web ACLs) | One protection pack (web ACL) per distribution | You can share protection packs (web ACLs) across tenants, with optional tenant-specific protection packs (web ACLs) | 
| Rule management | Rules affect a single distribution | Multi-tenant distribution rules affect all associated tenants; distribution tenant-specific rules affect only that tenant | 
| Managed rule groups | Applied to individual distributions | Can be applied at multi-tenant distribution level for all tenants or at tenant level for specific applications | 
| Logging | Standard AWS WAF logs | Logs include tenant identifiers for security event attribution | 

## Using AWS WAF with CloudFront Flat-Rate Pricing Plans
<a name="waf-cf-pricing-plans"></a>

CloudFront flat-rate pricing plans combine the Amazon CloudFront global content delivery network (CDN) with multiple AWS services and features into a monthly price with no overage charges, regardless of traffic spikes or attacks.

Flat-rate pricing plans include the following AWS services and features for a simple monthly price:
+ CloudFront CDN
+ AWS WAF and DDoS protection
+ Bot management and analytics
+ Amazon Route 53 DNS
+ Amazon CloudWatch Logs ingestion
+ TLS certificate
+ Serverless edge compute
+ Amazon S3 storage credits each month

Plans are available in Free, Pro, Business, and Premium tiers to match your application's needs. Plans do not need an annual commitment to get the best available rates. Start with the Free plan and upgrade to access more capabilities and larger usage allowances.

For more information and a complete list of plans and features, see [CloudFront flat-rate pricing plans](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html) in the *Amazon CloudFront Developer Guide*.

**Important**  
A valid AWS WAF protection pack (web ACL) must remain associated with your CloudFront distribution when using any pricing plan. You cannot remove the protection pack (web ACL) association unless you switch back to pay-as-you-go pricing.  
While a AWS WAF web ACL must remain associated with your distribution, you maintain full control over your security configuration. You can customize your protection by adjusting which rules are enabled or disabled in your web ACL, and modify rule settings to match your security requirements. For information about managing web ACL rules, see [AWS WAF Rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html).

## AI traffic monetization with CloudFront
<a name="cloudfront-features-ai-traffic-monetization"></a>

AI traffic monetization is available exclusively for AWS WAF web ACL resources associated with Amazon CloudFront distributions. Payment verification and settlement occur at CloudFront edge locations, minimizing latency for agents worldwide.

### Considerations when using AI Traffic Monetization with CloudFront Functions and Lambda@Edge
<a name="cloudfront-features-monetization-edge-functions"></a>

When you use CloudFront Functions or Lambda@Edge with distributions that have Monetize rules in AWS WAF, note the following behavior for AWS WAF-generated responses.

**AWS WAF-generated responses (402 Payment Required Challenge)**  
Viewer-response function (CloudFront Functions and Lambda@Edge) does not run on AWS WAF-generated 402 response. You cannot use these functions to customize the Payment Required Challenge. You also cannot add headers to it or modify it. If you need to add custom headers to 402 responses (for example, CORS or analytics headers), use a Response Headers Policy instead. Response Headers Policies apply to AWS WAF-generated responses.

For more information about CloudFront Functions and response header policies, see the following:
+ Viewer-response functions don't run on HTTP status codes 400 and higher. For more information about edge function restrictions, see [HTTP status codes](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-function-restrictions-all.html#function-restrictions-status-codes).
+ For more information about response header policies, see [Understanding response headers policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html).

**Paid responses (200 after settlement)**  
After a successful payment settlement, the origin response passes through the normal CloudFront response pipeline, including viewer-response function. A viewer-response function can modify the response that the agent receives after paying. For example, it can change the status code or remove headers.