# HNSEC05-BP01 Use IPSec VPN over Internet

For hybrid network connectivity over the internet, IPSec VPN
services can be used to create encrypted tunnels between cloud and
on-premises environments.

**Desired outcome:** Ensure that all
data transmitted between AWS and on-premises networks over the
internet is encrypted and protected from unauthorized access.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Provides encryption for data in transit
- Reduces risk of data interception or tampering over public
  networks
- Supports compliance with security and privacy requirements
- Enables secure, flexible hybrid networking without dedicated
  links

## Implementation guidance

- Establish IPSec VPN tunnels between your cloud and on-premises
  network, such as using AWS Site-to-Site VPN.
- Configure VPN endpoints to enforce strong encryption and
  authentication.
- Monitor tunnel health and activity.
- Ensure only approved subnets and IP ranges are routable over
  the VPN.

## Resources

- [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- [Get
  started with AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/SetUpVPNConnections.md "../../../vpn/latest/s2svpn/SetUpVPNConnections.md")
