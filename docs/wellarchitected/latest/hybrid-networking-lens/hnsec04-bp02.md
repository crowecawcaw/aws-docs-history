# HNSEC04-BP02 Implement routing controls for network

segments

Implementing routing controls for network segments involves
strategically managing traffic flow between different parts of your
network infrastructure. This includes setting up route tables to
direct traffic based on security policies. These controls should
enforce the principle of least privilege, ensuring network
components can only communicate with authorized segments.

**Desired outcome:** Enable
centralized, flexible, and secure traffic routing between cloud and
on-premises networks.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Provides centralized control of network paths
- Allows for segmentation and isolation using null routes
- Prevents unauthorized or misrouted hybrid traffic

## Implementation guidance

- Design route tables to segment environments and block
  unnecessary paths.
- Use null routes to block specific destinations when needed.
- Periodically review and simulate route changes before
  deployment.

## Resources

- [Transit
  gateway route tables in AWS Transit Gateway](../../../vpc/latest/tgw/tgw-route-tables.md "../../../vpc/latest/tgw/tgw-route-tables.md")
- [Core
  network policy versions in AWS Cloud WAN](../../../network-manager/latest/cloudwan/cloudwan-create-policy-version.md "../../../network-manager/latest/cloudwan/cloudwan-create-policy-version.md")
