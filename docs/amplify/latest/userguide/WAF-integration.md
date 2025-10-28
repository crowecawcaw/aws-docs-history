# Firewall support for Amplify hosted sites

Firewall support for Amplify hosted sites enables you to protect your web applications with a direct
integration with AWS WAF. AWS WAF allows you to configure a set of rules, called a web access control
list (web ACL), that allow, block, or monitor (count) web requests based on customizable web
security rules and conditions that you define. When you integrate your Amplify app with AWS WAF,
you gain more control and visibility into the HTTP traffic accepted by your app. To learn more
about AWS WAF, see [How AWS WAF Works](../../../waf/latest/developerguide/how-aws-waf-works.md "../../../waf/latest/developerguide/how-aws-waf-works.md") in the
_AWS WAF Developer Guide_.

Firewall support is available in all AWS Regions in which Amplify
Hosting operates. This integration
falls under an AWS WAF global resource, similar to CloudFront. Web ACLs can be attached to multiple
Amplify Hosting apps, but they must reside in the same Region.

You can use AWS WAF to protect your Amplify app from common web exploits, such as SQL
injection and cross-site scripting. These could affect your app's availability and performance,
compromise security, or consume excessive resources. For example, you can create rules to allow or
block requests from specified IP address ranges, requests from CIDR blocks, requests that
originate from a specific country or region, or requests that contain unexpected SQL code or
scripting.

You can also create rules that match a specified string or a regular expression pattern in
HTTP headers, method, query string, URI, and the request body (limited to the first 8 KB).
Additionally, you can create rules to block events from specific user agents, bots, and content
scrapers. For example, you can use rate-based rules to specify the number of web requests that are
allowed by each client IP in a trailing, continuously updated, 5-minute period.

To learn more about the types of rules that are supported and additional AWS WAF features, see
the [AWS WAF
Developer Guide](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md") and the [AWS WAF API Reference](../../../waf/latest/APIReference/API_Types_AWS_WAFV2.md "../../../waf/latest/APIReference/API_Types_AWS_WAFV2.md").

###### Important

Security is a shared responsibility between AWS and you. AWS WAF isn't the solution to all
internet security issues and you must configure it to meet your security and compliance
objectives. To help you understand how to apply the shared responsibility model when using AWS WAF,
see [Security in your
use of the AWS WAF service](../../../waf/latest/developerguide/security.md "../../../waf/latest/developerguide/security.md").

###### Topics

- [Enabling AWS WAF for an Amplify application in the AWS Management Console](getting-started-using-waf.md "getting-started-using-waf.md")
- [Disassociate a web ACL from an Amplify application](disassociate-web-acl.md "disassociate-web-acl.md")
- [Enabling AWS WAF for an Amplify application using the AWS CDK](amplify-waf-CDK.md "amplify-waf-CDK.md")
- [How Amplify integrates with AWS WAF](amplify-waf-configuration.md "amplify-waf-configuration.md")
- [Firewall pricing for Amplify applications](waf-pricing.md "waf-pricing.md")
