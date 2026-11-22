

# ADVSEC01-BP03 Restrict DSP outbound traffic to authorized SSPs only

 DSPs transmit bid responses containing pricing signals, audience segment data, and creative selection decisions to SSP endpoints. If outbound traffic isn't restricted to authorized destinations, this data can leak to unauthorized parties and expose competitive intelligence. 

 **Desired outcome:** 
+  You have restricted all egress from your DSP bidding infrastructure to a defined list of authorized SSP endpoints. 
+  Your egress controls dynamically update as SSP partner endpoints change without requiring manual security group edits. 
+  You can detect and alert on outbound connection attempts to unauthorized destinations. 

 **Common anti-patterns:** 
+  Allowing unrestricted outbound internet access from bidding instances and relying only on application-level routing to direct responses to the correct SSP. 
+  Maintaining a static egress allowlist that doesn't account for SSPs using dynamic IP ranges or CDN-based endpoints. 
+  Failing to encrypt bid responses in transit, which exposes pricing and audience data to network-level observers. 

 **Benefits of establishing this best practice:** 
+  Reduces the risk of accidental data disclosure of bid pricing, audience segments, or proprietary algorithms to unapproved endpoints. 
+  Creates a defense-in-depth layer that catches application-level routing errors before data leaves the network boundary. 
+  Provides an auditable egress log for compliance with data handling agreements between DSP and SSP partners. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Egress control in programmatic advertising requires more than static IP allowlisting. SSPs frequently operate behind CDN infrastructure with rotating IP ranges, use DNS-based load balancing across regions, and might change endpoints during scaling events. Configure egress rules to allow legitimate partner traffic while restricting unauthorized outbound access to bid response data. 

 Three egress architectures can restrict bid response delivery, each with different trade-offs. 

1.  Security group-based egress (static IP allowlists) is simplest and adds zero latency, but breaks when partners rotate infrastructure. It works for stable, long-term partnerships with dedicated IP ranges and fails for most modern SSP relationships. 

1.  Domain-based egress through stateful firewalls (FQDN allowlists) accommodates dynamic infrastructure by resolving partner domains at connection time. It adds a DNS dependency, higher cost, and more operational complexity. 

1.  Proxy-based egress provides full request and response logging and content inspection, but adds latency and creates a single point of failure. 

 When a partner rotates IPs and your allowlist blocks their traffic, bid responses fail with no error returned to your bidding engine. The block appears as declining win rates that resemble normal marketplace dynamics unless you monitor egress block rates per destination. Overly broad FQDN patterns like \*.partner-cdn.com expose bid response data. A threat actor who controls a subdomain receives your pricing signals and audience segments. 

 The partner registry is the source of truth for egress policy and must be owned by a single team with clear SLAs. When partnerships activate, propagate registry changes to firewall rules within hours. When partnerships terminate, remove the corresponding rules to prevent data leakage to former partners. Edge cases help you determine success by asking questions such as: 
+  What happens when a partner's DNS returns NXDOMAIN during a provider migration? 
+  What happens when two partners share CDN infrastructure and terminating one would block the other? 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure VPC security groups for bid response egress:** Restrict outbound traffic from bidding instances to the minimum required ports (typically HTTPS/443) and known SSP IP ranges. Block all other outbound traffic by default. 

1.  **Deploy AWS Network Firewall with domain-based egress rules:** Create rule groups using domain list targets for each authorized SSP partner. Use FQDN-based rules rather than IP-based where SSP infrastructure uses dynamic IPs or CDN-fronted endpoints. 

1.  **Implement automated partner registry synchronization:** Build a partner endpoint registry (DynamoDB table or AWS Systems Manager Parameter Store) that stores authorized SSP FQDNs and IP ranges. Use an EventBridge-triggered Lambda function to update Network Firewall rule groups when the registry changes. 

1.  **Enable flow log monitoring for unauthorized egress:** Configure VPC Flow Logs to capture all egress traffic. Use CloudWatch Logs Insights or Amazon Athena queries to detect outbound connection attempts to non-allowlisted destinations. Create alarms for any successful connections to unauthorized endpoints. 

1.  **Enforce TLS for all outbound bid responses:** Configure bidding applications to require TLS 1.2\+ for all outbound connections. When SSP partners require mTLS for inbound bid response receipt, issue client certificates from AWS Private CA using a template that sets the TLS Client Authentication extended key usage (such as EndEntityClientAuthCertificate), and manage renewal and export through AWS Certificate Manager. ACM public certificates carry only the server-authentication EKU and can't serve as mTLS client identities. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs](advsec01-bp02.md) 
+  [ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS](advsec02-bp01.md) 

 **Related documents:** 
+  [AWS Network Firewall domain list filtering](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html) 
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 

 **Related services:** 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [AWS Network Firewall](https://aws.amazon.com/network-firewall/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/features/) 