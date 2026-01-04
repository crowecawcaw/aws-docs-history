# TELCOOPS02-BP02 Adopt a multi-account strategy to isolate

different telecommunication workload

Implement a strategic multi-account architecture that effectively separates and isolates
telecommunications workloads while maintaining necessary interconnectivity and operational
efficiency. This approach creates logical boundaries between different environments, services,
and data classifications to enhance security and operational stability. The strategy should
balance the benefits of isolation with the need for seamless integration and management across
the telecommunications landscape.

**Desired outcome:**

- Secure workload isolation.
- Optimized resource management.
- Clear account boundaries.
- Efficient cross-account connectivity.
- Standardized account governance.
- Scalable account structure.

**Common anti-patterns:**

- Single account for each workload.
- No account categorization.
- Excessive account fragmentation.
- Missing connectivity strategy.
- Inconsistent security controls.
- Ad-hoc account creation.
- Poor resource sharing controls.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Design a multi-account architecture that addresses telecommunications-specific isolation
requirements.

Categorize workloads based on:

- Regulatory data sovereignty (separate accounts per country where laws mandate subscriber data remain within borders like EU GDPR, cybersecurity laws, and data localization regulations).
- Subscriber data sensitivity (isolated accounts for CPNI and PII processing with enhanced security controls versus anonymized network telemetry).
- Network function security domains (dedicated accounts for control plane functions like AMF or SMF requiring high security, user plane UPF functions optimized for throughput, and signaling functions requiring Diameter or SIP/SS7 firewall protection).

This categorization enables mapping
telecommunications regulatory and operational requirements to appropriate account boundaries
while maintaining cloud infrastructure efficiency.

Implement a hierarchical Organizational Unit (OU) structure reflecting your telecommunications architecture:

- RAN OU for edge-deployed radio functions
- 5G core OU with separated control and user plane accounts
- IMS OU for multimedia subsystem functions
- BSS OU for billing (PCI DSS compliance) and CRM (PII protection)
- OSS OU for network management and assurance
- Regional compliance OUs for per-country data sovereignty

Apply service control
policies enforcing regulatory requirements (deny cross-region replication from EU accounts for
GDPR, mandatory encryption for billing accounts). Establish standardized connectivity using
centralized transit and private connectivity services with separate paths for control plane
signaling versus user plane data traffic. Deploy centralized logging, monitoring, and security
tooling in dedicated Security OU accounts to maintain visibility and unified governance across
telco workloads.

### Implementation steps

- Deploy AWS Control Tower for automated account setup and use AWS Organizations for hierarchical
  account structure and policy management.
- Implement AWS IAM Identity Center for centralized access management and AWS Security Hub CSPM for
  multi-account security monitoring.
- Configure AWS Transit Gateway for centralized network connectivity and AWS Network Firewall for
  consistent security controls.
- Use AWS Resource Access Manager for cross-account resource sharing and AWS Systems Manager
  for centralized operations management.
- Deploy AWS CloudFormation StackSets for multi-account resource deployment and AWS Organizations for
  policy-based governance.

## Resources

**Key AWS services:**

- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
- [AWS Resource Access Manager](https://aws.amazon.com/ram/ "https://aws.amazon.com/ram/")
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/")
