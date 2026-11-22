

# SEC01-BP03 Stay up to date with security threats and recommendations

 Monitor trusted threat intelligence to keep pace with new vulnerabilities and attack techniques. Where possible, adopt services that fold new intelligence in automatically so detection improves without constant manual effort. 

 **Desired outcome:** 
+  You have a repeatable mechanism that keeps you informed of relevant new threats and recommendations. 
+  You use automation to detect potential vulnerabilities and exposures as new threats emerge. 
+  You take timely mitigating action against identified threats. 
+  You adopt services that update their threat intelligence automatically, which reduces manual tracking. 

 **Common anti-patterns:** 
+  No reliable, repeatable mechanism exists to stay informed of current threat intelligence. 
+  Teams maintain a manual inventory of technology and dependencies that requires human review for each new vulnerability. 
+  No mechanism updates workloads and dependencies to versions that carry known threat mitigations. 
+  Alerts from central threat detection are not routed to the teams that own the affected workloads. 

 **Benefits of establishing this best practice:** 
+  Missing an important shift in the tactics of unauthorized users becomes far less likely. 
+  Automated scanning and remediation mitigate risks faster and more predictably than manual review. 
+  Vulnerability response time and cost stay controlled as the portfolio grows. 
+  Shared intelligence across teams accelerates response to emerging threats. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A few public sources cover most of what you need for threat intelligence: 
+  The [MITRE ATT&CK](https://attack.mitre.org/) knowledge base documents known attack tactics, techniques, and procedures. 
+  The [Common Vulnerabilities and Exposures](https://www.cve.org/) list tracks specific flaws in the products you depend on. 
+  The [OWASP Top 10](https://owasp.org/projects/top-ten) captures the most critical risks to web applications. 
+  For AWS specifically, the [Threat Technique Catalog for AWS](https://aws-samples.github.io/threat-technique-catalog-for-aws/) records techniques the AWS Customer Incident Response Team sees during security events. 
+  AWS also announces updates on the AWS Security Blog. 

 Manually tracking every source does not scale as your portfolio grows. Managed controls incorporate new intelligence for you, at the cost of some flexibility over detection rules. Self-managed tooling provides full control but requires continuous maintenance. For most teams, that trade-off is worthwhile for commodity detection so your specialists can focus on threats specific to your workload. 

 AWS operates a global honeypot system called [MadPot](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime). Tens of thousands of sensors emulate hundreds of services and plausible customer environments, absorbing more than 100 million connection attempts each day. AWS classifies those interactions against known CVEs and attacker techniques, then analyzes them alongside AWS network telemetry. Tools such as [Sonaris](https://aws.amazon.com/blogs/security/how-aws-uses-active-defense-to-help-protect-customers-from-security-threats/) apply statistical and machine learning models to hundreds of billions of events per minute. They automatically restrict scanning and enumeration they can attribute to unauthorized activity with high confidence. The resulting threat intelligence helps protect AWS customers through the AWS network perimeter and powers services such as GuardDuty, AWS Shield, and AWS WAF managed rules. 

 Under the shared responsibility model, keeping software current is largely your responsibility. Unpatched dependencies are one of the most common paths to unauthorized access. A fleet management and patching strategy closes that gap systematically (for automation details, see the [Well-Architected Operational Excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html)). In larger organizations, a central team often operates threat detection across accounts. To shorten response time, integrate with those central mechanisms so intelligence and alerts reach the teams that own each workload. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Subscribe to threat intelligence sources:** Subscribe to the threat intelligence publications relevant to your business and industry, and to [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/) for notifications about CVEs and recommended remediation. 

1.  **Adopt services that update their intelligence automatically:** Use services such as [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html), whose Extended Threat Detection is enabled by default and correlates events over time to identify multi-stage attack sequences, and [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html), which rescans your workloads as new CVEs are published. 

1.  **Apply managed protections to internet-facing applications:** Use the managed rule groups in [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html) and [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html), which update automatically as new threats emerge. 

1.  **Automate fleet management and patching:** Deploy a fleet management and patching strategy that aligns with the Operational Excellence pillar, so dependencies move to versions with known mitigations without manual tracking. 

1.  **Integrate with central threat detection:** Connect to your organization's centralized threat detection mechanisms to share intelligence, receive alerts, and accelerate response to emerging threats. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP06 Identify threats and prioritize mitigations using a threat model](sec01-bp06.md) 
+  [SEC01-BP07 Evaluate and implement new security services and features regularly](sec01-bp07.md) 
+  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md) 
+  [FND05-BP07 Implement threat detection mechanisms](fnd05-bp07.md) 
+  [FND05-BP10 Prepare forensic capabilities](fnd05-bp10.md) 