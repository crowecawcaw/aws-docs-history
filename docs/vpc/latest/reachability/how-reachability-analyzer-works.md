# How Reachability Analyzer works

Reachability Analyzer analyzes the path between a source and destination by building a model of the network
configuration, and then checking for reachability based on the configuration. It does not send
packets or analyze the data plane.

To use Reachability Analyzer, you specify the path for the traffic from a source to a destination. For
example, you could specify an internet gateway as the source, an EC2 instance as the
destination, 22 as the destination port, and TCP as the protocol. This would allow you to verify
that you can connect to the EC2 instance through the internet gateway using SSH.

If there are multiple reachable paths between a source and a destination, Reachability Analyzer identifies
and displays the shortest path. You can analyze the path again, specifying or excluding an
intermediate component, to find an alternative reachable path that traverses the intermediate
component.

If the path is not reachable, Reachability Analyzer displays information about the component or combination
of components that is blocking the path. There might be additional components blocking the
path.

###### Contents

- [Source and destination resources](#source-and-destination-resources "#source-and-destination-resources")
- [Intermediate components](#intermediate-components "#intermediate-components")
- [Path components](#path-components "#path-components")
- [Considerations](#considerations "#considerations")
- [Resource configuration](#resource-configuration "#resource-configuration")

## Source and destination resources

The source and destination resources must be in the same Region. The source and
destination resources must be in the same VPC or in VPCs that are connected through a VPC
peering connection or a transit gateway. The source and destination resources can belong to
different AWS accounts in the same organization from AWS Organizations.

Reachability Analyzer supports the following resource types as sources and destinations:

- EC2 instances
- Internet gateways
- Network interfaces
- Transit gateways
- Transit gateway attachments
- Virtual private gateways
- VPC endpoint services
- VPC endpoints
- VPC peering connections

In addition, Reachability Analyzer supports IP addresses as destinations.

## Intermediate components

Reachability Analyzer supports the following resource types as intermediate components. Specific
intermediate components can be included or excluded from analysis when you're creating a path
to analyse. See [Getting started with Reachability Analyzer](getting-started.md "getting-started.md") for more information.

- Load balancers
- NAT gateways
- AWS Network Firewall
- Transit gateways
- Transit gateway attachments
- VPC peering connections

## Path components

The following resource types can appear in reachable paths and in explanations when
a path is not reachable:

- EC2 instances
- Internet gateways
- Load balancers
- NAT gateways
- Network ACLs
- Network Firewall firewall
- Network interfaces
- Prefix lists
- Route tables
- Security groups
- Subnets
- Target groups
- Transit gateways
- Transit gateway attachments
- Transit gateway route tables
- Virtual private gateways
- VPC endpoint services
- VPC endpoints
- VPC gateway endpoints
- VPC peering connections
- VPCs
- VPN connections

## Considerations

Consider the following when working with Reachability Analyzer:

- Reachability Analyzer supports only resources with an IPv4 address. If a resource has both IPv4 and
  IPv6 addresses, Reachability Analyzer includes only the IPv4 addresses in its analysis.
- If you enable trusted access, the delegated administrator account can create and
  delete paths that traverse owner and participant subnets within your organization from
  AWS Organizations. This account can also start and delete path analyses. For more information,
  see [Cross-account analyses for Reachability Analyzer](multi-account.md "multi-account.md").
- Paths are not a shareable resource.
- Transit gateway Connect attachments are not supported. Reachability Analyzer analyzes connectivity only
  up to these attachments.
- With the TCP protocol, when a network path traverses a transit gateway route table,
  only forward traffic is analyzed.
- Paths through a Gateway Load Balancer endpoint do not include the Gateway Load Balancer or its targets. You should
  verify connectivity between the Gateway Load Balancer and its targets using a separate analysis.
- Reachability Analyzer does not consider the health of registered targets.
- Reachability Analyzer does not support Network Firewall rule groups that reference a resource group. In this
  case, the analysis fails.
- For a cross-account path through a Network Firewall firewall, the rule group must be created in the
  same delegated administrator account as the user running the analysis.
- Reachability Analyzer supports all stateful and stateless 5-tuple rules in Network Firewall. It doesn't support
  domain lists, Suricata rules, rule options, and tag-based resource groups. When Reachability Analyzer
  encounters an unsupported rule in Network Firewall, it provides an informational message in the path
  details.
- The packet header leaving the source and the packet header arriving at the destination
  can differ, due to intermediate components transforming the packets. For example, internet
  gateways and NAT gateways provide network address translation (NAT).
- Reachability Analyzer does not consider the advertised state of BYOIP address ranges. If a BYOIP
  address range is not advertised, resources that use these addresses might not be reachable
  from the internet.
- Reachability Analyzer does not report connectivity due to traffic mirroring.
- Reachability Analyzer automatically deletes an analysis 120 days after its creation date.
- Your account has quotas related to Reachability Analyzer. For more information, see [Quotas for Reachability Analyzer](reachability-analyzer-limits.md "reachability-analyzer-limits.md").

## Resource configuration

Use the following documentation to help you update the configuration of your network resources:

- [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md")
- [Firewalls (AWS Network Firewall)](../../../network-firewall/latest/developerguide/firewalls.md "../../../network-firewall/latest/developerguide/firewalls.md")
- [Internet gateways](../userguide/VPC_Internet_Gateway.md "../userguide/VPC_Internet_Gateway.md")
- Load balancers and target groups (ELB)
  - [Application Load Balancers](../../../elasticloadbalancing/latest/application.md "../../../elasticloadbalancing/latest/application.md")
  - [Classic Load Balancers](../../../elasticloadbalancing/latest/classic.md "../../../elasticloadbalancing/latest/classic.md")
  - [Gateway Load Balancers](../../../elasticloadbalancing/latest/gateway.md "../../../elasticloadbalancing/latest/gateway.md")
  - [Network Load Balancers](../../../elasticloadbalancing/latest/network.md "../../../elasticloadbalancing/latest/network.md")

- [Network ACLs](../userguide/vpc-network-acls.md "../userguide/vpc-network-acls.md")
- [Route tables](../userguide/VPC_Route_Tables.md "../userguide/VPC_Route_Tables.md")
- [Security groups for EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md")
- [Transit gateways](../tgw.md "../tgw.md")
- [VPC endpoint services (AWS PrivateLink)](../privatelink/concepts.md "../privatelink/concepts.md")
- [VPC peering configurations](../peering/peering-configurations.md "../peering/peering-configurations.md")
- [VPN connections](../userguide/vpn-connections.md "../userguide/vpn-connections.md")
