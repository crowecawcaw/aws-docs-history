# VPC attachments in AWS Cloud WAN

When you attach a VPC to a core network edge in AWS Cloud WAN, you must specify one subnet from
each Availability Zone to be used by the core network edge to route traffic. Specifying one
subnet from an Availability Zone enables traffic to reach resources in every subnet in that
Availability Zone. For more information about limits to core network VPC attachments, see
[Transit
Gateway attachment to a VPC](../../../vpc/latest/tgw/tgw-vpc-attachments.md "../../../vpc/latest/tgw/tgw-vpc-attachments.md") in the _Transit Gateway User
Guide_.

###### Important

You cannot select a subnet from a Local Zone while creating a Cloud WAN VPC
attachment. Doing so will result in an error. For more information about Local Zones,
see the [_AWS Local Zones User Guide_](../../../local-zones/latest/ug/what-is-aws-local-zones.md "../../../local-zones/latest/ug/what-is-aws-local-zones.md").

## Appliance mode

If you plan to configure a stateful network appliance in your VPC, you can enable
appliance mode support for the VPC attachment in which the appliance is located when you
create an attachment. This ensures that Cloud WAN uses the same Availability Zone for
that VPC attachment for the lifetime of the flow of traffic between a source and
destination. It also allows Cloud WAN to send traffic to any Availability Zone in the
VPC as long as there is a subnet association in that zone. While appliance mode is only
supported on VPC attachments, the network flow can enter the core network from any other
Cloud WAN attachment type, including VPC, VPN, and Connect attachments. Cloud WAN
appliance mode also works for network flows that have sources and destinations across
different AWS Regions in your core network. Network flows can potentially be
rebalanced across different Availability Zones if you don't initially enable appliance
mode but later edit the attachment configuration to enable it. You can enable or disable
appliance mode using either the console or the command line or API.

Appliance mode in Cloud WAN optimizes traffic routing by considering the source and
destination Availability Zones when determining the path through an appliance mode VPC.
This approach enhances efficiency and reduces latency. The following are example
scenarios.

### Scenario 1: Intra-Availability Zone

Traffic Routing via Appliance VPC

When traffic flows from source Availability Zone us-east-1a to destination
Availability Zone us-east-1a, with Appliance Mode VPC attachments in both us-east-1a
and us-east-1b, Cloud WAN selects a network interface from us-east-1a within the
appliance VPC. This Availability Zone is maintained for the entire duration of the
traffic flow between source and destination.

### Scenario 2: Inter-Availability Zone

Traffic Routing via Appliance VPC

For traffic flowing from source Availability Zone us-east-1a to destination
Availability Zone us-east-1b, with Appliance Mode VPC attachments in both us-east-1a
and us-east-1b, Cloud WAN uses a flow hash algorithm to select either us-east-1a or
us-east-1b in the appliance VPC. The chosen Availability Zone is used consistently
for the lifetime of the flow.

### Scenario 3: Routing traffic

through an appliance VPC without Availability Zone data

When traffic originates from source Availability Zone us-east-1a to a
destination without Availability Zone information (e.g., internet-bound traffic),
with Appliance Mode VPC attachments in both us-east-1a and us-east-1b, Cloud WAN
selects a network interface from us-east-1a within the appliance VPC.

### Scenario 4: Routing traffic through

an appliance VPC in an Availability Zone distinct from either the source or
destination

When traffic flows from source Availability Zone us-east-1a to destination
Availability Zone us-east-1b, with Appliance Mode VPC attachments in different
Availability Zone example us-east-1c and us-east-1d, Cloud WAN uses a flow hash
algorithm to select either us-east-1c or us-east-1d in the appliance VPC. The chosen
Availability Zone is used consistently for the lifetime of the flow.

###### Note

- When you create a VPC attachment you can't create a core network VPC
  attachment that uses only IPv6 subnets. A core network VPC attachment must also
  support IPv4 addresses.
- Appliance mode is only supported for VPC attachments.

## DNS support

DNS support in Cloud WAN enables the resolution of public DNS host names to private
IP addresses when queried across VPCs attached to the same core network edge similar to
the DNS resolution capability available for transit gateways. This feature is enabled by
default in your core network and can be configured in your core network policy by
setting the `dns-support` parameter to either `true` or
`false`, with the setting applying to all core network edges in the core
network. You can view your DNS support configuration through the console in the core
network policy or by using the [`get-core-network`](../../../cli/latest/reference/networkmanager/get-core-network.md "../../../cli/latest/reference/networkmanager/get-core-network.md") command.

###### Note

DNS support only works between VPCs attached to the same core network edge
and does not function across different regions or between VPCs attached to
different core network edges.

## Security group referencing

You can configure security groups by specifying a list of rules that allow network
traffic based on criteria such as IP CIDRs, prefix lists, ports and security group
referencing. Security group referencing allows you to specify other security groups as
references, or matching criterion in inbound security rules to allow
instance-to-instance traffic. With this capability, you do not need to reconfigure
security rules as applications scale up or down or if their IP addresses change. Rules
with security group references also provide higher scale as a single rule can cover
thousands of instances and prevents you from over-running security group rule
limits.

Security group referencing is a regional feature for Cloud WAN, meaning VPCs must be
connected to the same core network edge for this feature to work. When you create a VPC
attachment, Cloud WAN automatically enables security group referencing for VPCs attached
to the same core network edge.

###### Note

Security group referencing is enabled by default at the attachment level but
disabled by default at the core network level.

With security group referencing support in Cloud WAN, you can:

- Reference security groups across VPCs connected to the same core network
  edge
- Simplify security group management for applications that span multiple VPCs
- Maintain security group references even as instances scale up or down
- Reduce the number of security group rules needed for cross-VPC communication

### Limitations

The following limitations apply to security group referencing in Cloud WAN:

- Security group referencing only works between VPCs attached to the same
  core network edge. It does not work across different regions or between VPCs
  attached to different core network edges.
- Security group referencing is not supported for VPC attachments in the
  use1-az3 Availability Zone .
- Security group referencing is not supported for AWS PrivateLink endpoints.
  We recommend using IP CIDR-based security rules as an alternative.
- Security group referencing works for Elastic File System (EFS) as long as
  an allow all egress security group rule is configured for the EFS interfaces
  in the VPC.
- Security group referencing support can be configured for both core network
  and VPC attachments and will only work if it has been enabled for both a
  core network and its VPC attachments.

###### Topics

- [Create a VPC attachment](cloudwan-vpc-attachment-add.md "cloudwan-vpc-attachment-add.md")
- [View or edit a VPC attachment](cloudwan-attachments-viewing-editing-vpc.md "cloudwan-attachments-viewing-editing-vpc.md")
