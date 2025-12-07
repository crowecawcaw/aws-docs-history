# Values that you specify when you create or edit inbound endpoints

When you create or edit an inbound endpoint, you specify the following values:

**Outpost ID**
If you are creating the endpoint for a VPC Resolver on an AWS Outposts VPC, this is the AWS Outposts ID.

**Endpoint name**
A friendly name that lets you easily find an inbound endpoint on the dashboard.

**Endpoint category**
Choose either **Default** or **Delegation**. When the category is **Default**, the
resolver on your network forwards the DNS requests to the IP address of the inbound endpoint. When the category is
**Delegation**, the authority for a domain is delegated to the VPC Resolver.

**VPC in the _region-name_ Region**
All inbound DNS queries from your network pass through this VPC on the way to VPC Resolver.

**Security group for this endpoint**
The ID of one or more security groups that you want to use to control access to this VPC. The
security group that you specify must include one or more inbound rules.
Inbound rules must allow TCP and UDP access on port 53.
If you are using the DoH protocol, you will also have to allow port 443 in security group.You can't change
this value after you create the endpoint.

Some security group rules will cause your connection to be tracked and the overall maximum queries per second per IP address for an inbound endpoint can be as low as 1500.
To avoid connection tracking caused by a security group, see [Untracked connections](../../../AWSEC2/latest/UserGuide/security-group-connection-tracking.md#untracked-connections "../../../AWSEC2/latest/UserGuide/security-group-connection-tracking.md#untracked-connections").

###### Note

In order to add multiple security groups, use the AWS CLI command `create-resolver-endpoint`.
For more information, see [create-resolver-endpoint](../../../cli/latest/reference/route53resolver/create-resolver-endpoint.md "../../../cli/latest/reference/route53resolver/create-resolver-endpoint.md")

For more information, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
in the _Amazon VPC User Guide_.

**Endpoint type**
The endpoint type can be either IPv4, IPv6, or dual-stack IP addresses. For a dual-stack
endpoint, the endpoint will have both IPv4 and IPv6 address that your
DNS resolver on your network can forward DNS query to.

###### Note

For security reasons, we are denying direct IPv6 traffic access from the public internet for all dual-stack and IPv6 IP addresses.

**IP addresses**
The IP addresses that you want DNS resolvers on your network to forward DNS queries to. We
require you to specify a minimum of two IP addresses for redundancy. If
you created a delegation inbound endpoint, use these IP addresses as the
glue NS records for the subdomain for which you want to delegate the
authority to VPC Resolver. Note the following:

**Multiple Availability Zones**
We recommend that you specify IP addresses in at least two Availability Zones. You can optionally specify
additional IP addresses in those or other Availability Zones.

**IP addresses and Amazon VPC elastic network interfaces**
For each combination of Availability Zone, Subnet, and IP address that you specify, VPC Resolver
creates an Amazon VPC elastic network interface. For the current
maximum number of DNS queries per second per IP address in
an endpoint, see [Quotas on Route 53 VPC Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver"). For
information about pricing for each elastic network
interface, see "Amazon Route 53" on the [Amazon Route 53 pricing
page](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

###### Note

Resolver endpoint has a private IP address. These IP addresses will not change through the
course of an endpoint's life.

For each IP address, specify the following values. Each IP address must be in an Availability Zone in the VPC
that you specified in **VPC in the _region-name_ Region**.

**Availability Zone**
The Availability Zone that you want DNS queries to pass through on the way to your VPC.
The Availability Zone that you specify must be configured with a subnet.

**Subnet**
The subnet that contains the IP addresses you want assigned to your Resolver endpoint ENIs.
These are the addresses you will send DNS queries to. The
subnet must have an available IP address.

The subnet IP address must match the **Endpoint type**.

**IP address**

The IP address that you want to assign to the inbound
endpoints.

Choose whether you want VPC Resolver to choose an IP address for
you from among the available IP addresses in the specified
subnet, or you want to specify the IP address
yourself.

If you choose to specify the IP address yourself, enter
either an IPv4 or IPv6 address, or both.

**Protocols**
Endpoint protocol determines how data is transmitted to the inbound endpoint. Choose a
protocol, or protocols, depending on the level of security
needed.

- **Do53:** (Default) The data is relayed using the Route 53 VPC Resolver
  without additional encryption. While the data cannot be read by
  external parties, it can be viewed within the AWS networks.
  This is the only protocol currently available for the
  **Delegation** inbound endpoint
  category.
- **DoH:** The data is transmitted over an encrypted HTTPS session.
  DoH adds an added level of security where data can't be
  decrypted by unauthorized users, and can't be read by anyone
  except the intended recipient.
- **DoH-FIPS:** The data is transmitted over an encrypted HTTPS
  session that is compliant with the FIPS 140-2 cryptographic
  standard. Supported for inbound endpoints only. For more
  information, see [FIPS PUB
  140-2](https://doi.org/10.6028/NIST.FIPS.140-2 "https://doi.org/10.6028/NIST.FIPS.140-2").

###### Note

For DoH/DoH-FIPS inbound endpoints, there is a known issue with incorrect source IP being published in the VPC Resolver query logging.

For an inbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 and DoH-FIPS in combination.
- Do53 alone.
- DoH alone.
- DoH-FIPS alone.
- None, which is treated as Do53.

###### Important

You can't change the protocol of an inbound endpoint directly from only Do53 to only DoH, or DoH-FIPS.
This is to prevent a sudden disruption to incoming traffic that
relies on Do53. To change the protocol from Do53 to DoH, or DoH-FIPS, you must
first enable both Do53 and DoH, or Do53 and DoH-FIPS, to make sure that all incoming traffic
has transferred to using the DoH protocol, or DoH-FIPS, and then remove the
Do53.

**Tags**
Specify one or more keys and the corresponding values. For example, you might specify
**Cost center** for **Key** and specify **456** for **Value**.
