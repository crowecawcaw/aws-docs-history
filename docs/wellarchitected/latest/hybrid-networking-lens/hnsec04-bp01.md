# HNSEC04-BP01 Control access to network resources

Comprehensive network access control applied across both on-premises
and cloud environments to create a unified security posture that
addresses the unique challenges of hybrid infrastructures while
maintaining compliance with regulatory requirements.

**Desired outcome:** Protect hybrid
network resources by controlling traffic from on-premises and cloud
environments.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Restrict network access to only approved sources
- Minimizes risk of unauthorized or malicious traffic
- Enables granular, instance-level security controls

## Implementation guidance

- Define least-privilege inbound and outbound rules matching
  only approved network prefixes.
- Regularly review and update rules for accuracy and compliance.

## Resources

- [Control
  traffic to your AWS resources using security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
- [Control
  subnet traffic with network access control lists](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md")
