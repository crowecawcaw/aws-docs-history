# Performance Insights API and interface VPC endpoints (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
Amazon RDS Performance Insights. You can access Performance Insights as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or Direct Connect connection.
Instances in your VPC don't need public IP addresses to access Performance Insights.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for Performance Insights.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Performance Insights

Before you set up an interface endpoint for Performance Insights, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Performance Insights supports making calls to all of its API actions through the interface
endpoint.

By default, full access to Performance Insights is allowed through the interface endpoint. To control traffic to Performance Insights
through the interface endpoint, associate a security group with the endpoint network interfaces.

## Availability

Performance Insights API currently supports VPC endpoints in AWS Regions that support Performance Insights.
For information about Performance Insights availability,
see [Supported
Regions and DB engines for Performance Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md")
.

## Create an interface endpoint for Performance Insights

You can create an interface endpoint for Performance Insights using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Performance Insights using the following service name:

If you enable private DNS for the interface endpoint, you can make API requests to
Performance Insights using its default Regional DNS name. For example,
`pi.us-east-1.amazonaws.com`.

## Creating a VPC endpoint policy for

Performance Insights API

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Performance Insights through the interface endpoint.
To control the access allowed to Performance Insights from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Performance Insights actions

The following is an example of a custom endpoint policy. When you attach
this policy to your interface endpoint, it grants access to the listed Performance Insights
actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "rds:CreatePerformanceAnalysisReport",
            "rds:DeletePerformanceAnalysisReport",
            "rds:GetPerformanceAnalysisReport"
         ],
         "Resource":"*"
      }
   ]
}
```

###### Example: VPC endpoint policy that denies all access from a specified AWS account

The following VPC endpoint policy denies AWS account `123456789012` all access to
resources using the endpoint. The policy allows all actions from other accounts.

```
{
  "Statement": [
    {
      "Action": "*",
      "Effect": "Allow",
      "Resource": "*",
      "Principal": "*"
    },
    {
      "Action": "*",
      "Effect": "Deny",
      "Resource": "*",
      "Principal": { "AWS": [ "123456789012" ] }
     }
   ]
}
```

## IP addressing for Performance Insights

IP addresses enable resources in your VPC to communicate with each other, and with resources over the internet.
Performance Insights supports both IPv4 and IPv6 addressing protocols.
By default, Performance Insights and Amazon VPC use the IPv4 addressing protocol.
You can't turn off this behavior. When you create a VPC, make sure to specify an IPv4 CIDR block (a range of private IPv4 addresses).

You can optionally assign an IPv6 CIDR block to your VPC and subnets, and assign IPv6 addresses from that block to RDS resources in your subnet.
Support for the IPv6 protocol expands the number of supported IP addresses. By using the IPv6 protocol, you ensure that you have sufficient
available addresses for the future growth of the internet. New and existing RDS resources can use IPv4 and IPv6 addresses within your VPC.
Configuring, securing, and translating network traffic between the two protocols used in different parts of an application can cause operational overhead.
You can standardize on the IPv6 protocol for Amazon RDS resources to simplify your network configuration. For more information about service endpoints and quotas,
see [Amazon Relational Database Service endpoints and quotas](../../../general/latest/gr/rds-service.md "../../../general/latest/gr/rds-service.md").

For more information about Amazon RDS IP addressing, see
[Amazon RDS IP addressing](USER_VPC.md#USER_VPC.IP_addressing "USER_VPC.md#USER_VPC.IP_addressing").
