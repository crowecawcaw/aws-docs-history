

# SMSEC05-BP03 Use a web application firewall to monitor and control content access
<a name="smsec05-bp03"></a>

Implement web application firewall to protect content origins and content delivery network (CDN) distributions from common exploits like SQL Injection or Cross Site Scripting (XSS), filter malicious traffic, and create custom rules while maintaining full logging and monitoring.

**Desired outcome:**
+ Help secure and control access to applications and interfaces from exploits or malicious attacks
+ Rate limiting and bot protection for content access points
+ Granular traffic filtering based on IP addresses, headers and request patterns

**Common anti-patterns:**
+ Organizations deploy streaming applications behind Amazon CloudFront without enabling AWS WAF, leaving content APIs vulnerable to SQL injection, cross-site scripting, and automated scraping by bots.
+ Teams configure AWS WAF rules without rate limiting, allowing automated tools to enumerate content catalogs or perform attacks against video authentication endpoints at high volume.
+ Organizations deploy only default managed rule groups without creating custom rules for streaming-specific threats such as manifest file scraping, segment URL enumeration, or token replay attacks.
+ Teams enable AWS WAF in count-only mode during initial deployment but never transition to blocking mode, leaving known attack patterns unmitigated indefinitely.
+ Organizations fail to configure AWS WAF logging, making forensic analysis of blocked requests impossible and stopping teams from tuning rules based on actual attack patterns targeting their streaming infrastructure.

**Benefits of establishing this best practice:**
+ AWS WAF rules filter malicious requests before they reach content origins, protecting against Open Worldwide Application Security Project (OWASP) Top 10 vulnerabilities and streaming-specific attack patterns like manifest scraping.
+ Rate limiting and bot detection rules block automated tools from scraping content catalogs, enumerating segment URLs, or performing credential stuffing against viewer authentication endpoints.
+ Custom AWS WAF rules enable IP-based blocking, geographic restrictions, and header-based filtering that enforce content licensing requirements at the request level.
+ Full AWS WAF logging provides detailed records of blocked and allowed requests, enabling security teams to identify emerging attack patterns and tune protection rules.
+ AWS WAF rules can be updated in real-time to respond to active threats during live events without requiring changes to origin infrastructure or application code.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

If you are using AWS Application Load Balancers or Amazon CloudFront, you can also use AWS WAF to validate requests originating from known IP addresses. You can use AWS WAF to get started with managed rule for common protections and create rules to filter web traffic based on conditions that include IP addresses, HTTP headers and body, or custom URIs.

### Implementation steps
<a name="implementation-steps"></a>

1. **Create an AWS WAF protection pack:** [Create a protection pack in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/setup-iap-console.html).

1. **Apply to application resources:** Apply the pack to your application resources.

1. **Deploy managed rule groups:** Deploy AWS WAF with managed rule groups.

1. **Create custom rules:** Create custom rules for streaming-specific protection such as rate limiting and geoblocking.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC05-BP01 Use DDoS protection service to maintain content availability](smsec05-bp01.html)
+ [SMSEC05-BP02 Restrict content origin access to only allow known entities](smsec05-bp02.html)

**Related documents**
+ [Setting Up AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/setup-iap-console.html)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS Web Application Firewall](https://aws.amazon.com/waf/)