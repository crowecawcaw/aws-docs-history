# Creating inbound

endpoints

After you have created a Resolver on Outpost, you can add both inbound and outbound endpoints to
resolve DNS queries to and from your on-premises network.

###### To configure inbound endpoints for Resolver on Outpost

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and then
   navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is located.
4. Select the check box next to the Resolver that is in operational state and
   choose **View details**.
5. On the **Inbound endpoints** table, choose **Create
   inbound endpoint**.
6. On the **Create inbound endpoint** page, enter the applicable
   values. For more information, see [Values that you
   specify when you create or edit inbound endpoints on an Outpost](#resolver-forwarding-inbound-queries-values-outpost "#resolver-forwarding-inbound-queries-values-outpost").
7. Choose **Create endpoint**.

## Values that you

specify when you create or edit inbound endpoints on an Outpost

When you create or edit an inbound endpoint, you specify the following
values:

**Outpost ID**

If you are creating the endpoint for a Resolver on an AWS Outposts VPC,
this is the AWS Outposts ID.

**Endpoint name**

A friendly name that lets you easily find an inbound endpoint on the
dashboard.

**VPC in the _region-name_ Region**

All inbound DNS queries from your network pass through this VPC on the
way to Resolver.

**Security group for this endpoint**

The ID of one or more security groups that you want to use to control
access to this inbound endpoint. The security group that you specify
must include one or more inbound rules. Inbound rules must allow TCP and
UDP access on port 53. You can't change this value after you create the
endpoint.

For more information, see [Security groups for your
VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon VPC User Guide_.

**IP addresses**

The IP addresses that you want to assign to the inbound endpoints. We
require you to specify a minimum of two IP addresses for redundancy.
Note the following:

**IP addresses and Amazon VPC elastic network interfaces**

For each combination of Availability Zone, Subnet, and IP
address that you specify, Resolver creates an Amazon VPC elastic
network interface. For the current maximum number of DNS
queries per second per IP address in an endpoint, see [Quotas on Route 53 Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver"). For
information about pricing for each elastic network
interface, see Amazon Route 53 on the [Amazon Route 53 pricing
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
through on the way to your VPC. The Availability Zone that
you specify must be configured with a subnet.

**Subnet**

The subnet that contains the IP address that you want to
forward DNS queries to. The subnet must have an available IP
address.

Specify the subnet for an IPv4 address. IPv6 is not
supported.

**IP address**

The IP address that you want to forward DNS queries
to.

Choose whether you want Resolver to choose an IP address for
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
bill; you can use tags for other purposes as well. For more information
about using tags for cost allocation, see [Using cost allocation
tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
