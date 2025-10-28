# Block public access to VPCs and subnets

VPC Block Public Access (BPA) is a centralized security feature that enables you
to authoritatively prevent public internet access to VPC resources across an entire AWS
account, ensuring compliance with security requirements while providing
flexibility for specific exceptions and audit capabilities.

The VPC BPA feature has the following modes:

- **Bidirectional**: All traffic to and
  from internet gateways and egress-only internet gateways in this Region (except for
  excluded VPCs and subnets) is blocked.
- **Ingress-only**: All internet
  traffic to the VPCs in this Region (except for VPCs or subnets which are excluded)
  is blocked. Only traffic to and from NAT gateways and egress-only internet gateways
  is allowed because these gateways only allow outbound connections to be
  established.
  You can also create "exclusions" for this feature for traffic you don't want to
  block. An exclusion is a mode that can be applied to a single VPC or subnet that exempts it
  from the account's VPC BPA mode and will allow bidirectional or egress-only access.

Exclusions can have either of the following modes:

- **Bidirectional**: All internet
  traffic to and from the excluded VPCs and subnets is allowed.
- **Egress-only**: Outbound internet
  traffic from the excluded VPCs and subnets is allowed. Inbound internet traffic to
  the excluded VPCs and subnets is blocked. This only applies when VPC BPA is set to
  Bidirectional.

###### Contents

- [VPC BPA basics](security-vpc-bpa-basics.md "security-vpc-bpa-basics.md")
- [Assess impact of VPC BPA and
  monitor VPC BPA](security-vpc-bpa-assess-impact-main.md "security-vpc-bpa-assess-impact-main.md")
- [Advanced example](security-vpc-bpa-example.md "security-vpc-bpa-example.md")
