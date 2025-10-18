# Use AWS WAF protections

You can use [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf "https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf") to protect your CloudFront distributions and origin servers. AWS WAF is a web application
 firewall that helps secure your web applications and APIs by blocking requests before they reach
 your servers. For more information, see [Accelerate and protect your websites using CloudFront and AWS WAF](https://aws.amazon.com/blogs/networking-and-content-delivery/accelerate-and-protect-your-websites-using-amazon-cloudfront-and-aws-waf/ "https://aws.amazon.com/blogs/networking-and-content-delivery/accelerate-and-protect-your-websites-using-amazon-cloudfront-and-aws-waf/") and [Guidelines for Implementing AWS WAF](https://docs.aws.amazon.com/whitepapers/latest/guidelines-for-implementing-aws-waf/guidelines-for-implementing-aws-waf.html "https://docs.aws.amazon.com/whitepapers/latest/guidelines-for-implementing-aws-waf/guidelines-for-implementing-aws-waf.html").

To enable AWS WAF protections, you can:


* Use one-click protection in the CloudFront console. One-click protection creates an AWS WAF web
 access control list (web ACL), configures rules to protect your servers from common web threats,
 and attaches the web ACL to the CloudFront distribution for you. The topics in this section assume the
 use of one-click protections.
* Use a preconfigured web ACL (access control list) that you create in the AWS WAF console, or
 by using the AWS WAF APIs. For more information, see [Web access control lists (ACLs)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html "https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html") in the
 *AWS WAF Developer Guide* and [AssociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html "https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html") in the
 *AWS WAF API Reference*
You can enable AWS WAF when you:


* Create a distribution
* Use the **Security** dashboard to edit the security settings of an
 existing distribution
When you use one-click protection, CloudFront applies an AWS recommended set of protections
 that:


* Block IP addresses from potential threats based on Amazon internal threat
 intelligence.
* Protect against the most common vulnerabilities found in web applications as described in
 the [OWASP Top 10](https://owasp.org/www-project-top-ten/ "https://owasp.org/www-project-top-ten/").
* Defend against malicious actors discovering application vulnerabilities.
###### Important

You must enable AWS WAF if you want to view security metrics in the CloudFront
 **Security** dashboard. Without AWS WAF, enabled, you can only use the
 **Security** dashboard to enable AWS WAF or configure CloudFront geographic
 restrictions. For more information about the dashboard, see [Manage AWS WAF security protections in the CloudFront security dashboard](security-dashboard.md "security-dashboard.md"), later in this section.

###### Topics

* [Enable AWS WAF for distributions](WAF-one-click.md "WAF-one-click.md")
* [Manage AWS WAF security protections in the CloudFront security dashboard](security-dashboard.md "security-dashboard.md")
* [Set up rate limiting](WAF-one-click-rate-limiting.md "WAF-one-click-rate-limiting.md")
* [Disable AWS WAF security protections](disable-waf.md "disable-waf.md")
