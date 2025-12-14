**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Resource-level DDoS protection for Application Load Balancers

**Resource level DDoS protection** adds immediate defense to Application Load Balancers without incurring charges of deploying AWS WAF managed rule groups.
This standard tier of Anti-DDoS protection uses AWS threat intelligence and traffic pattern analysis to protect Application Load Balancers.
To identify known malicous sources, Anti-DDoS protection performs on-host filtering of both direct client IP addresses and X-Forwarded-For (XFF) headers.
After a known malicious source is identified, protection is activated through one of two modes:

**Active under DDoS** is the default protective mode and is recommended for most use cases.

This mode:

- Activates protection automatically when detecting high load conditions or potential DDoS events
- Rate-limits traffic from known malicious sources only during attack conditions
- Minimizes impact on legitimate traffic during normal operations
- Uses Application Load Balancer health metrics and AWS WAF response data to determine when to engage protection
  **Always on** is an optional mode that is always active once enabled.

This mode:

- Maintains continuous protection against known malicious sources
- Rate-limits traffic from known malicious sources in real time
- Applies protection to both direct connections and requests with malicious IPs in XFF headers
- May have higher impact on legitimate traffic but provides maximum security

## Enable standard DDoS protection on an existing webACL

You can enable DDoS protection when you create a web ACL or update an existing web ACL associated with Application Load Balancer.

###### Note

If you have an existing web ACL that is associated with an Application Load Balancer, Anti-DDoS protection is
enabled by default with **Active under DDoS** mode.

###### To enable Anti-DDoS protection in the AWS WAF console

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. Choose **Web ACLs** in the navigation pane, and then open any web ACL that is associated with an Application Load Balancer.
3. Choose **Associated AWS resources**.
4. Under **Resource level DDoS protection**, choose **Edit**.
5. Select one of the following protection modes:
   - **Active under DDoS** (recommended) - Protection engages only during high load conditions
   - **Always on** - Always-on protection against known malicious sources

6. Choose **Save changes**.

###### Note

For information about creating a web ACL, see [Creating a protection pack (web ACL) in AWS WAF](web-acl-creating.md "web-acl-creating.md").

###### To optimize web ACL request costs for your Application Load Balancer

You must associate a web ACL with your Application Load Balancer to enable resource-level protection.
If your Application Load Balancer is associated with a web ACL that has no configuration, you will not incur charges from AWS WAF requests, however, AWS WAF will not provide sampled requests or report on the Application Load Balancer in CloudWatch metrics.
You can take the following actions to enable observability features for the Application Load Balancer:

- Use the `Block` action or `Allow` action with custom request headers in the `DefaultAction`. For information, see [Inserting custom request headers for non-blocking actions](customizing-the-incoming-request.md "customizing-the-incoming-request.md").
- Add any rules to the web ACL. For information, see [AWS WAF rules](waf-rules.md "waf-rules.md").
- Enable a logging destination. For information, see [Configuring logging for a protection pack (web ACL)](logging-management-configure.md "logging-management-configure.md").
- Associate the web ACL with an AWS Firewall Manager policy. For information, see [Creating an AWS Firewall Manager policy for
  AWS WAF](create-policy.md#creating-firewall-manager-policy-for-waf "create-policy.md#creating-firewall-manager-policy-for-waf").
  AWS WAF will not provide sampled requests or publish CloudWatch metrics without these configurations.
