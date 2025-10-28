**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Resource-level DDoS protection for Application Load Balancers

**Resource level DDoS protection** adds immediate defense to Application Load Balancers without
the pricing considerations of a AWS WAF managed rule group.
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
