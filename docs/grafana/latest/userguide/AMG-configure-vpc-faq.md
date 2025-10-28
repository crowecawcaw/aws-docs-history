# Troubleshoot using VPC with

Amazon Managed Grafana

Answers to common questions regarding using Amazon Virtual Private Cloud (Amazon VPC) with
Amazon Managed Grafana.

## When do I need to configure a

VPC in Amazon Managed Grafana?

You need to configure a VPC in Amazon Managed Grafana if you are trying to connect to a
data source that is only available in a private VPC (that is not publicly
accessible).

For data sources that are publicly available, or have a public-facing
endpoint, you do not need to configure a VPC.

If you connect to Amazon CloudWatch, Amazon Managed Service for Prometheus, or AWS X-Ray, you do not need to
configure a VPC. These data source are connected to Amazon Managed Grafana via AWS PrivateLink
by default.

## Why are my existing data

sources failing to connect after I configured a VPC with my Amazon Managed Grafana
workspace?

Your existing data sources are likely accessible through the public network
and your Amazon VPC configuration does not allow access to the public network. After
configuring the VPC connection in your Amazon Managed Grafana workspace, all traffic must
flow through that VPC. This includes private data sources hosted within that
VPC, data sources in another VPC, AWS Managed Services that are not available
in the VPC, and internet-facing data sources.

To resolve this issue, you must connect the other data sources to the VPC that
you have configured:

- For internet-facing data sources, connect the VPC to the internet. You
  can, for example, [Connect to the internet or
  other networks using NAT devices](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md") (from the
  _Amazon Virtual Private Cloud User Guide_).
- For data sources in other VPCs, create a peering between the two VPCs.
  For more information, see [Connect VPCs using VPC
  peering](../../../vpc/latest/userguide/vpc-peering.md "../../../vpc/latest/userguide/vpc-peering.md") (from the _Amazon Virtual Private Cloud User
  Guide_).
- For AWS Managed Services that are not accessible in your VPC, such
  as CloudWatch, X-Ray, or Amazon Managed Service for Prometheus, you might need to create an interface VPC
  endpoint for that service in your VPC. For more information, see [Access
  an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
  _AWS PrivateLink Guide_.

## Can I use a VPC

with dedicated tenancy?

No, [VPCs configured](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") with `Tenancy` set to
`Dedicated` are not supported.

## Can I connect

both AWS Managed Services (such as Amazon Managed Service for Prometheus, CloudWatch, or X-Ray) and private
data sources (including Amazon Redshift) to the same Amazon Managed Grafana workspace?

Yes. You must configure connectivity to the AWS Managed Services in the same
VPC as your private data sources (for example, using an [interface VPC
endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") or a [NAT Gateway](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md")), and configure
your Amazon Managed Grafana workspace to connect to the same VPC.

## Why do I get a `502 Bad Gateway

Error` when I am trying to connect to a data source after I
configured the VPC in my Amazon Managed Grafana workspace?

The following are the three most common reasons why your data source
connection returns a `502` error.

- **Security group error** — The
  security groups selected during VPC configuration in Amazon Managed Grafana must
  allow connectivity to the data source via inbound and outbound
  rules.

To resolve this issues, make sure that the rules in both the data
source security group and the Amazon Managed Grafana security group allow this
connectivity.

- **User permission error** — The
  assigned workspace user does not have the right permissions to query the
  data source.

To resolve this issue, confirm that the user has the required IAM
permissions to edit the workspace, and the correct data source policy to
access and query the data from the hosting service. Permissions are
available in the AWS Identity and Access Management (IAM) console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

- **Incorrect connection details provided**
  — The Amazon Managed Grafana workspace is unable to connect to your data
  source due to incorrect connection details provided.

To resolve this issue, please confirm the information in the data
source connection, including the data source authentication and endpoint
URL, and retry the connection.

## Can I connect to multiple VPCs from the

same Amazon Managed Grafana workspace?

You can only configure a single VPC for a Amazon Managed Grafana workspace. To access data
sources in a different VPC, or across regions, see the next question.

## How do I connect to data

sources in a different VPC? How do I connect to data sources from a VPC
that's in a different AWS Region or AWS account?

You can use [VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") or
[AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") to
connect the cross-region or cross-account VPCs, then connect the VPC that is in
the same AWS account and Region as your Amazon Managed Grafana workspace. Amazon Managed Grafana
connects to the outside data sources as any other connection within the
VPC.

###### Note

If VPC peering isn't an option for you, share your use case with your
Account Manager, or send email to [aws-grafana-feedback@amazon.com](mailto:aws-grafana-feedback@amazon.com "mailto:aws-grafana-feedback@amazon.com").

## When my Amazon Managed Grafana workspace

is connected to a VPC will I still be able to connect to other public data
sources?

Yes. You can connect data sources from both your VPC and public data sources
to a single Amazon Managed Grafana workspace at the same time. For public data sources, you
must configure VPC connectivity via a [NAT Gateway](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md"), or other [VPC
connection](../../../vpc/latest/userguide/extend-intro.md "../../../vpc/latest/userguide/extend-intro.md"). Requests to public data sources traverse your VPC,
giving you additional visibility and control over those requests.

## What should I do if I'm unable to update

an Amazon Managed Grafana workspace due to insufficient IP addresses?

You might encounter the following error when modifying your Amazon Managed Grafana workspace
configuration: **`All subnets in the VPC configuration must have at
 least 15 available IP addresses`**.

You will receive this error if one or more subnets connected to your
workspace do not meet the minimum IP requirements. A minimum of 15 available IP
addresses must be in each subnet connected to your workspace. When the number of
available IP addresses for a subnet falls below 15, you might experience the
following issues:

- Inability to make configuration changes to your workspace until you
  free up additional IP addresses or attach subnets with additional IP
  addresses
- Your workspace will not be able to receive security updates or
  patches
- In rare scenarios, you could experience a complete availability loss
  for the workspace, resulting in non-functioning alerts and inaccessible
  dashboards

###### Mitigate IP exhaustion

1. If a subnet has less than 15 available IP addresses, release IP
   addresses associated with instances or delete unused network interfaces
   to free up IP capacity.
2. If you are unable to free up IP addresses in the existing subnet, then
   you must replace the subnet with one that has at least 15 available IP
   addresses. We recommend using dedicated subnets for Amazon Managed Grafana.

###### Replace a subnet

1. Open the [Amazon Managed Grafana
   console](https://console.aws.amazon.com/grafana "https://console.aws.amazon.com/grafana").
2. In the left navigation pane, choose **All
   workspaces**, then select the name of your
   workspace.
3. In the **Network access control** tab, next to
   **Outbound VPC connection**, choose
   **Edit**.
4. Under **Mappings**, select the Availability Zone
   which contains the subnet with insufficient IP addresses.
5. In the dropdown, deselect the subnet with insufficient IP addresses
   and select a subnet with at least 15 available IP addresses. If
   necessary, create a new subnet in your VPC. For more information, see
   [Create a
   subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the _Amazon VPC User Guide_.
6. Choose **Save changes** to complete the setup.

## Before configuring a VPC

connection my Grafana alerts were successfully being sent to downstream
services, such as PagerDuty and Slack. After configuring VPC, why are my
Grafana alerts not being delivered to these notification
destinations?

After you configure a VPC connection for an Amazon Managed Grafana workspace, all traffic
to data sources in the workspace flows through the configured VPC. Make sure
that the VPC has a route to reach these alert notification services. For
example, alert notification destinations hosted by third parties might require
connectivity to the Internet. Much like data sources, configure an Internet or
AWS Transit Gateway, or other VPC connection to the external destination.

## Can I edit my VPC manually? Why does

modifying my security group or subnet cause my Amazon Managed Grafana workspace to become
unavailable?

The Amazon Managed Grafana VPC connection uses the security groups and subnets to control
the traffic allowed between the VPC and your Amazon Managed Grafana workspace. When the
security group or subnet is modified or deleted from outside the Amazon Managed Grafana
console (such as with the VPC console), the VPC connection in your Amazon Managed Grafana
workspace stops protecting your workspace security, and the workspace becomes
unreachable. To fix this issue, update the security groups configured for your
Amazon Managed Grafana workspace in the Amazon Managed Grafana console. When viewing your workspace,
select **Outbound VPC connection** on the **Network
access control** tab to modify the subnets or security groups
associated with the VPC connection.
