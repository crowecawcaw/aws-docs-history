# Values that you specify when you create or edit

outbound endpoints

When you create or edit an outbound endpoint, you specify the following values:

**Outpost ID**
If you are creating the endpoint for a Resolver on an AWS Outposts VPC, this is the AWS Outposts ID.

**Endpoint name**
A friendly name that lets you easily find an outbound endpoint on the dashboard.

**VPC in the _region-name_ Region**
All outbound DNS queries will flow through this VPC on the way to your network.

**Security group for this endpoint**

The ID of one or more security groups that you want to use to control access to this VPC.
The security group that you specify must include one or more outbound rules. Outbound rules must allow TCP and UDP access
on the port that you're using for DNS queries on your network.
You can't change this value after you create an endpoint.

Some security group rules will cause your connection to be tracked and potentially impact the maximum queries per second from outbound endpoint to your target name server.
To avoid connection tracking caused by a security group, see [Untracked connections](../../../AWSEC2/latest/UserGuide/security-group-connection-tracking.md#untracked-connections "../../../AWSEC2/latest/UserGuide/security-group-connection-tracking.md#untracked-connections").

For more information, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
in the _Amazon VPC User Guide_.

**Endpoint type**
The endpoint type can be either IPv4, IPv6, or dual-stack IP addresses. For a dual-stack
endpoint, the endpoint will have both IPv4 and IPv6 address that your
DNS resolver on your network can forward DNS query to.

###### Note

For security reasons, we are denying direct IPv6 traffic access to the public internet for all dual-stack and IPv6 IP addresses.

**IP addresses**
The IP addresses in your VPC that you want Resolver to forward DNS queries to on the way to resolvers
on your network. These are not the IP addresses of the DNS resolvers on your network; you specify resolver
IP addresses when you create the rules that you associate with one or more VPCs. We require you to specify
a minimum of two IP addresses for redundancy.

###### Note

Resolver endpoint has a private IP address. These IP addresses will not change through the
course of an endpoint's life.

Note the following:

**Multiple Availability Zones**
We recommend that you specify IP addresses in at least two Availability Zones. You can optionally specify
additional IP addresses in those or other Availability Zones.

**IP addresses and Amazon VPC elastic network interfaces**
For each combination of Availability Zone, Subnet, and IP address that you specify, Resolver creates an
Amazon VPC elastic network interface. For the current maximum number of DNS queries per second per IP address
in an endpoint, see [Quotas on Route 53 Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver").
For information about pricing for each elastic network interface, see "Amazon Route 53" on the
[Amazon Route 53 pricing page](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

**Order of IP addresses**
You can specify IP addresses in any order. When forwarding DNS queries, Resolver doesn't choose IP addresses based on the order
that the IP addresses are listed in.

For each IP address, specify the following values. Each IP address must be in an Availability Zone in the VPC
that you specified in **VPC in the _region-name_ Region**.

**Availability Zone**
The Availability Zone that you want DNS queries to pass through on the way to your network.
The Availability Zone that you specify must be configured with a subnet.

**Subnet**
The subnet that contains the IP address that you want DNS queries to originate from on the way
to your network. The subnet must have an available IP address.

The subnet IP address must match the **Endpoint type**.

**IP address**
The IP address that you want DNS queries to originate from on the way to your network.

Choose whether you want Resolver to choose an IP address for you from among the available IP addresses
in the specified subnet, or you want to specify the IP address yourself.

If you choose to specify the IP address yourself, enter an IPv4 or IPv6 address, or
both.

**Protocols**
Endpoint protocol determines how data is transmitted from the outbound endpoint. Choose a
protocol, or protocols, depending on the level of security
needed.

- **Do53:** (Default) The data is relayed using the Route 53 Resolver
  without additional encryption. While the data cannot be read by
  external parties, it can be viewed within the AWS
  networks.
- **DoH:** The data is transmitted over an encrypted HTTPS session.
  DoH adds an added level of security where data can't be
  decrypted by unauthorized users, and can't be read by anyone
  except the intended recipient.

For an outbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 alone.
- DoH alone.
- None, which is treated as Do53.

**Tags**
Specify one or more keys and the corresponding values. For example, you might specify
**Cost center** for **Key** and specify **456** for **Value**.
