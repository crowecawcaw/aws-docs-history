# Creating outbound

endpoints

After you have opted in and configured a VPC Resolver, you can also add both inbound and
outbound endpoints to resolve DNS queries to your on-premises network.

###### Note

When you configure outbound endpoints, VPC Resolver caches DNS responses so that queries
can still be resolved if your Outpost becomes disconnected from the Region.
Maintaining this cache might increase DNS requests to your on-premises
resolvers.

###### To configure outbound endpoints for Resolver on Outpost

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and then
   navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is located.
4. Select the checkmark next to the VPC Resolver that is in operational state and
   choose **View details**.
5. On the **Outbound endpoints** table, choose **Create
   outbound endpoint**.
6. On the **Create outbound endpoint** page, enter the
   applicable values. For more information, see [Values that you specify when you create or edit outbound endpoints in an
   AWS Outposts](#resolver-forwarding-outbound-queries-endpoint-values-outpost "#resolver-forwarding-outbound-queries-endpoint-values-outpost").
7. Choose **Create endpoint**.

## Values that you specify when you create or edit outbound endpoints in an

AWS Outposts

When you create or edit an outbound endpoint, you specify the following
values:

**Outpost ID**

If you are creating the endpoint for a VPC Resolver on an AWS Outposts VPC,
this is the AWS Outposts ID.

**Endpoint name**

A friendly name that lets you easily find an outbound endpoint on the
dashboard.

**VPC in the _region-name_ Region**

All outbound DNS queries from your VPC pass through this VPC on the
way to your network.

**Security group for this endpoint**

The ID of one or more security groups that you want to use to control
access to this VPC. The security group that you specify must include one
or more outbound rules. Outbound rules must allow TCP and UDP access on
the port that you're using for DNS queries on your network. You can't
change this value after you create the endpoint.

For more information, see [Security groups for your
VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon VPC User Guide_.

**IP addresses**

The IP addresses that you want to assign to the outbound endpoints. We
require you to specify a minimum of two IP addresses for redundancy.
Note the following:

**IP addresses and Amazon VPC elastic network interfaces**

For each combination of Availability Zone, Subnet, and IP
address that you specify, VPC Resolver creates an Amazon VPC elastic
network interface. For the current maximum number of DNS
queries per second per IP address in an endpoint, see [Quotas on Route 53 VPC Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver"). For
information about pricing for each elastic network
interface, see "Amazon Route 53" on the [Amazon Route 53 pricing
page](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

###### Note

Resolver endpoint has a private IP address. These IP addresses will
not change through the course of an endpoint's life.

For each IP address, specify the following values. Each IP address
must be in an Availability Zone in the VPC that you specified in
**VPC in the _region-name_
Region**.

**Availability Zone**

The Availability Zone that you want DNS queries to pass
through on the way from your VPC. The Availability Zone that
you specify must be configured with a subnet.

**Subnet**

The subnet that contains the IP address that you want to
forward DNS queries from. The subnet must have an available
IP address.

Specify the subnet for an IPv4 address. IPv6 is not
supported.

**IP address**

The IP address that you want to assign to the outbound
endpoints.

Choose whether you want VPC Resolver to choose an IP address for
you from among the available IP addresses in the specified
subnet, or you want to specify the IP address
yourself.

If you choose to specify the IP address yourself, enter an
IPv4 address. IPv6 is not supported.

**Tags**

Specify one or more keys and the corresponding values. For example,
you might specify **Cost center** for
**Key** and specify **456** for
**Value**.

These are the tags that AWS Billing and Cost Management provides for organizing your AWS
bill; you can use also tags for other purposes. For more information
about using tags for cost allocation, see [Using cost allocation
tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

## Creating forwarding rules for

outbound endpoints

You can also create forwarding rules for outbound endpoints. For more information,
see [To create forwarding rules and
associate the rules with one or more VPCs](resolver-forwarding-outbound-queries-configuring.md#resolver-forwarding-outbound-queries-configuring-create-rule-procedure "resolver-forwarding-outbound-queries-configuring.md#resolver-forwarding-outbound-queries-configuring-create-rule-procedure")
