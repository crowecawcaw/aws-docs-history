# DSSEC03-BP02 Verify network security posture through automated

analysis

Automated network analysis tools provide mathematical proof of
network configurations. This enables you to verify adherence to data
residency and privacy requirements.

**Desired outcome:** Maintain data
sovereignty through continuous automated verification of network
paths and boundaries.

**Common anti-patterns:**

- Relying solely on manual network configuration reviews without
  automated verification of actual connectivity paths.
- Assuming network boundaries are correctly configured without
  testing reachability scenarios.
- Not validating that network configurations block data
  exfiltration or unauthorized cross-border data flows.

**Benefits of establishing this best
practice:**

- Provides mathematical proof of network security configurations
  and their effectiveness in blocking unauthorized access.
- Supports proactive identification of network misconfigurations
  before they are exploited.
- Automates complex network analysis that is typically
  time-intensive and error-prone if performed manually.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement network analysis using
[AWS VPC Network Access Analyzer](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md") and
[VPC
Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to mathematically verify (using
automated reasoning to analyze possible network paths) network
configurations and identify potential security gaps. Start by
defining network access scopes that align with your data residency
requirements, and data export controls. Then establish continuous
monitoring for network configuration changes.

Key AWS services include:

- VPC Network Access Analyzer for identifying unintended network
  access patterns, and demonstrating regulatory adherence.
- VPC Reachability Analyzer for verifying connectivity between
  specific resources.
- Amazon Inspector for automated network reachability
  assessments of EC2 instances.

Common usage approaches include:

- Creating network access scopes to specify the desired
  connectivity between AWS resources.
- Establishing reachability tests.
- Integrating network analysis into CI/CD pipelines for
  infrastructure changes.

### Implementation steps

1. Use VPC Network Access Analyzer to validate if traffic
   between a source and destination is blocked as you intended.
   To do this:
   - Create Network Access Scopes that specify prohibited
     network paths.
   - Define MatchPaths for network connections that violate
     compliance requirements (for example, cross-border data
     flows).
   - Configure ExcludePaths for legitimate exceptions to
     security policies.

2. Use VPC Reachability Analyzer to verify intended
   connectivity between resources. Reachability Analyzer
   analyzes the path between a source and destination by
   building a model of the network configuration. It does not
   send packets during analysis.
   - VPC Reachability Analyzer is especially useful when you
     are designing your network. For example, it assists you
     to understand the route that a connection would take if
     it were allowed to reach the destination. You can use
     this information to make sure data is encrypted in
     transit, or apply additional traffic filtering
     conditions.
   - You can also include specific intermediate components in
     the analysis. For example, you can analyze the path
     between a source and destination through a specific
     transit gateway. This makes it particularly valuable for
     security audits, policy enforcement, and compliance
     verification.

Automated network analysis provides mathematical verification of
network security configurations, assisting you to maintain data
sovereignty and block unauthorized access. VPC Network Access
Analyzer and VPC Reachability Analyzer enable you to
continuously verify that network paths align with your security
requirements and compliance obligations.

## Resources

**Related best practices:**

- [SEC05-BP04
  Automate network protection](../security-pillar/sec_network_auto_protect.md "../security-pillar/sec_network_auto_protect.md")
- [SEC05-BP02
  Control traffic flow within your network layers](../security-pillar/sec_network_protection_layered.md "../security-pillar/sec_network_protection_layered.md")

**Related examples:**

- Example
  [network
  access scopes](../../../vpc/latest/network-access-analyzer/example-scopes.md "../../../vpc/latest/network-access-analyzer/example-scopes.md") in Network Access Analyzer.
- Reachability analyzer
  [source
  and destination resources](../../../vpc/latest/reachability/how-reachability-analyzer-works.md#source-and-destination-resources "../../../vpc/latest/reachability/how-reachability-analyzer-works.md#source-and-destination-resources") list.

**Related documents:**

- [VPC
  Network Access Analyzer User Guide](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md")
- [VPC
  Reachability Analyzer User Guide](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md")
- [Amazon Inspector Network Reachability Documentation](../../../inspector/v1/userguide/inspector_network-reachability.md "../../../inspector/v1/userguide/inspector_network-reachability.md")
- [AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md")
- [Network
  Security on AWS Whitepaper](../../../whitepapers/latest/aws-security-best-practices/network-security.md "../../../whitepapers/latest/aws-security-best-practices/network-security.md")
- [Automated
  Reasoning for Network Security](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/")
- [Network
  Monitoring and Analysis Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/ "https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/")
- [An
  unexpected discovery](https://aws.amazon.com/blogs/security/an-unexpected-discovery-automated-reasoning-often-makes-systems-more-efficient-and-easier-to-maintain/ "https://aws.amazon.com/blogs/security/an-unexpected-discovery-automated-reasoning-often-makes-systems-more-efficient-and-easier-to-maintain/")

**Related videos:**

- [AWS re:Inforce 2022 - Validate effective network access controls
  on AWS (NIS202)](https://www.youtube.com/watch?v=aN2P2zeQek0&t=288s "https://www.youtube.com/watch?v=aN2P2zeQek0&t=288s")

**Related services:**

- [VPC
  Network Access Analyzer](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md")
- [VPC
  Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md")
- [Amazon Inspector](../../../inspector/v1/userguide/inspector_network-reachability.md "../../../inspector/v1/userguide/inspector_network-reachability.md")
- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
