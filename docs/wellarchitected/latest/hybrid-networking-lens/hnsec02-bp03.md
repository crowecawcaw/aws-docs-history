# HNSEC02-BP03 Implement least privilege access for hybrid

network management

To implement least privilege, hybrid connectivity resources
management should be granted only to teams responsible for hybrid
connectivity. The teams should own circuits, dedicated connections,
and VPNs even though other teams depend on these shared networking
resources.

**Desired outcome:** Ensure that
hybrid connectivity resources are securely managed, access is
restricted to authorized personnel, and operational risk is
minimized by centralizing ownership and management.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enforces least privilege and separation of duties
- Reduces risk of misconfiguration or unauthorized changes
- Improve governance and compliance
- Enables consistent operational practices and incident response
- Ensures accountability for networking and security controls

## Implementation guidance

- Assign responsibility for managing hybrid connectivity
  resources, such as Direct Connect, VPN, Transit Gateway, to a
  dedicated networking and security team.
- Restrict permissions so only approved networking and security
  personnel can create, modify, or delete connectivity
  resources.
- Separate development and operational responsibilities to
  prevent developers from modifying shared networking
  infrastructure.
- Establish standard operating procedures and change management
  workflows for connectivity changes.
- Audit access and configuration change regularly. For example,
  you can achieve this using AWS CloudTrail.

## Resources

- [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")
- [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- [AWS Transit Gateway for Amazon VPC](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md")
- [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
