**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF Classic

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

AWS WAF Classic is a web application firewall that lets you monitor the HTTP and HTTPS
requests that are forwarded to an Amazon API Gateway API, Amazon CloudFront or an Application Load Balancer. AWS WAF Classic
also lets you control access to your content. Based on conditions that you specify, such as
the IP addresses that requests originate from or the values of query strings, API Gateway, CloudFront or
an Application Load Balancer responds to requests either with the requested content or with an HTTP 403 status
code (Forbidden). You also can configure CloudFront to return a custom error page when a request
is blocked.

###### Topics

- [Setting up AWS WAF Classic](classic-setting-up-waf.md "classic-setting-up-waf.md")
- [How AWS WAF Classic works](classic-how-aws-waf-works.md "classic-how-aws-waf-works.md")
- [AWS WAF Classic pricing](classic-aws-waf-pricing.md "classic-aws-waf-pricing.md")
- [Getting started with AWS WAF Classic](classic-getting-started.md "classic-getting-started.md")
- [Creating and configuring a Web Access Control List (Web ACL)](classic-web-acl.md "classic-web-acl.md")
- [Working with AWS WAF Classic rule groups for use with AWS Firewall Manager](classic-working-with-rule-groups.md "classic-working-with-rule-groups.md")
- [Getting started with AWS Firewall Manager to enable AWS WAF Classic
  rules](classic-getting-started-fms.md "classic-getting-started-fms.md")
- [Tutorial: Creating an
  AWS Firewall Manager policy with hierarchical rules](hierarchical-rules.md "hierarchical-rules.md")
- [Logging Web ACL traffic information](classic-logging.md "classic-logging.md")
- [Listing IP addresses blocked by rate-based rules](classic-listing-managed-ips.md "classic-listing-managed-ips.md")
- [How AWS WAF Classic works with Amazon CloudFront features](classic-cloudfront-features.md "classic-cloudfront-features.md")
- [Security in AWS WAF Classic](classic-security.md "classic-security.md")
- [AWS WAF Classic quotas](classic-limits.md "classic-limits.md")
