

# SEC05-BP03 Implement inspection-based protection

 Inspect traffic between your network layers to confirm it matches expected patterns. Analyze flows, metadata, and behavior to detect and respond to events. Make protections stricter as traffic moves closer to sensitive data. 

 **Desired outcome:** 
+  You inspect and authorize traffic that crosses between your network layers. 
+  Your allow and deny decisions rest on explicit rules, current threat intelligence, and deviation from baseline behavior. 
+  Your protections tighten as traffic approaches your most sensitive data. 
+  You maintain a baseline view of normal traffic to compare against. 

 **Common anti-patterns:** 
+  Teams rely only on port and protocol rules and forgo intelligent inspection. 
+  Teams write firewall rules around specific current threat patterns that change over time. 
+  Teams inspect traffic only where it moves between private and public subnets or out to the internet. 
+  Teams operate without a baseline of normal traffic, so anomalies go unnoticed. 

 **Benefits of establishing this best practice:** 
+  Intelligent rules allow or deny traffic based on conditions within the traffic itself, not just ports and protocols. 
+  Managed rule sets from AWS and partners track new and evolving risks without constant manual research. 
+  Reduced rule maintenance lowers the chance of false positives and stale detection indicators. 
+  Consistent inspection across layers improves detection and response. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Port and protocol rules allow or deny traffic based on the path alone. Inspection also examines content and behavior, because unauthorized traffic reuses permitted ports and protocols to blend in. Write rules keyed to the data in the traffic and to deviation from a known baseline of normal traffic. Because threat signatures age quickly, use intelligence-driven managed rule sets. 

 Choose where to inspect. You can inspect per VPC, centralize inspection in a dedicated VPC, or use a hybrid model. In a hybrid model, east-west traffic flows through an inspection VPC and internet ingress is inspected per VPC. Centralizing reduces the number of places to manage but adds routing complexity and a potential chokepoint. Per-VPC inspection keeps flows local but multiplies the configuration you maintain. To perform deep packet inspection, the solution must terminate TLS, which increases visibility at the cost of processing overhead and key management. 

 Inspection divides into inline and out-of-band models. Inline solutions sit in the traffic path and can block in real time. [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) provides inline stateful and stateless filtering and supports [Suricata-compatible](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-ips.html) open source unauthorized access prevention rules. Third-party firewalls and unauthorized access prevention systems from [AWS Marketplace](https://aws.amazon.com/marketplace/search) can run inline behind a [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html). Out-of-band solutions analyze a copy of the traffic and add no latency to the path. [VPC traffic mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html) feeds such tools, though mirrored traffic counts toward interface bandwidth and incurs the same data transfer charges as the original. 

 Web-facing components need protection tuned to HTTP-based threats. A web application firewall inspects HTTP and HTTPS requests before they reach services such as Amazon API Gateway, Amazon CloudFront, AWS AppSync, or an Application Load Balancer. With [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html), you can combine [managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html) with your own rules or partner rule groups. Some web application firewalls require you to terminate TLS before inspection, so factor deep packet inspection into where you place the firewall. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose your inspection scope:** Decide whether broad rules through a centralized inspection VPC fit your workload or whether you need a more granular per-VPC approach. Base the choice on your routing model, the sensitivity of the data behind each layer, and how much configuration you can maintain. 

1.  **Deploy inline inspection:** For [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), create your rules, firewall policy, and firewall, then [route traffic to the firewall endpoint](https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html) to enable inspection. For a third-party appliance, deploy it across one or more Availability Zones behind a [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html), then create the load balancer, endpoint service, and endpoint, and configure routing. 

1.  **Deploy out-of-band inspection:** Turn on [VPC traffic mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html) on the interfaces whose inbound and outbound traffic you want to capture, and point the mirror sessions to the Network Load Balancer in front of your analysis appliance. Use Amazon EventBridge rules to invoke an AWS Lambda function that enables mirroring automatically when new resources are created. 

1.  **Protect inbound web traffic:** Configure an [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) web access control list (web ACL) with a default allow or deny action, using your own rules or AWS managed rule groups. Associate the web ACL with a resource such as an Application Load Balancer, an API Gateway REST API, or a CloudFront distribution to begin protecting web traffic. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC05-BP02 Control traffic flow within your network layers](sec05-bp02.md) 
+  [SEC05-BP04 Automate network protection](sec05-bp04.md) 
+  [SEC05-BP01 Create network layers](sec05-bp01.md) 

 **Related documents:** 
+  [What is traffic mirroring?](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html) 
+  [AWS Network Firewall example architectures with routing](https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html) 
+  [AWS Network Firewall best practices guide](https://aws.github.io/aws-security-services-best-practices/guides/network-firewall/) 
+  [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Level up your AWS Network Firewall rules for maximum protection (SEC231)](https://www.youtube.com/watch?v=iyT2TJrZhC8) 
+  [AWS re:Invent 2025 - Robust network security with perimeter protection and zero trust (NET326)](https://www.youtube.com/watch?v=kJ3tgbTWE4E) 
+  [AWS re:Inforce 2025 - AWS Network Firewall: Latest features and deployment options (NIS201-NEW)](https://www.youtube.com/watch?v=nauTd9uOtsU) 
+  [AWS re:Invent 2025 - Managing Bots vs Humans with CloudFront and AWS WAF (NET324)](https://www.youtube.com/watch?v=IiJz-NIA_Xg) 

 **Related tools:** 
+  [AWS Network Firewall](https://aws.amazon.com/network-firewall/) 
+  [Gateway Load Balancer](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [AWS Marketplace](https://aws.amazon.com/marketplace/search) 