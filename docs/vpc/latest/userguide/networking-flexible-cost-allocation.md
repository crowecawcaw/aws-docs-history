

# Networking Flexible Cost Allocation

Networking Flexible Cost Allocation (FCA) is a feature of Amazon Virtual Private Cloud (Amazon VPC). With it, you can attribute the data transfer and data processing charges of a shared networking resource to the resources, subnets, VPCs, accounts, or IP address ranges that generated the usage. For example, when several teams share a single NAT gateway, your bill shows one charge for the NAT gateway. With FCA, your AWS Cost and Usage Report also show how much of that charge each team's traffic accounts for.

FCA changes how usage is itemized in your reports. It doesn't change your bill, and it doesn't change how your traffic is routed or metered.

To start, you create a policy that specifies the cost to allocate and the level of detail to report. You then associate the policy with the resources that you want to allocate costs for. After you turn on the data in your [Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/), the itemized usage appears in your reports.

The following resources are supported:
+ **NAT gateway** – Allocate the data transfer and data processing charges of a NAT gateway.
+ **Amazon EC2 instance** – Allocate data transfer between an Amazon EC2 instance and a directly connected peer in the same VPC.
+ **VPC peering connection** – Allocate data transfer over a VPC peering connection in the same Region.

## When allocation takes effect
<a name="networking-flex-cost-allocation-effective-time"></a>

Allocation doesn't begin immediately. When you create an association, it has an expected effective time. This is the earliest time that the association can take effect. The expected effective time is the time that you create the association plus 60 minutes, rounded up to the next hour. For example, if you create an association at 2:01 PM, its expected effective time is 4:00 PM. The association takes effect after its expected effective time. If there is a significant delay in processing your changes, an association can take effect later. FCA doesn't apply allocation retroactively to earlier usage.

## Regional availability
<a name="networking-flex-cost-allocation-availability"></a>

FCA is available at no additional charge in all commercial AWS Regions except Middle East (Bahrain) and Middle East (UAE). It's also available in the China Regions. It isn't available in the AWS GovCloud (US) Regions.

## Pricing
<a name="networking-flex-cost-allocation-pricing"></a>

There is no additional charge for FCA. You continue to pay the standard charges for your NAT gateways, data transfer, and other resources. For more information about pricing, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).

**Topics**
+ [When allocation takes effect](#networking-flex-cost-allocation-effective-time)
+ [Regional availability](#networking-flex-cost-allocation-availability)
+ [Pricing](#networking-flex-cost-allocation-pricing)
+ [How it works](networking-flex-cost-allocation-basics.md)
+ [Set up and manage](networking-flex-cost-allocation-work-with.md)
+ [Policy examples](networking-flex-cost-allocation-iam-examples.md)
+ [Allocate EC2 instance data transfer](networking-flex-cost-allocation-ec2.md)
+ [Allocate NAT gateway costs](networking-flex-cost-allocation-natgw.md)
+ [Allocate VPC peering data transfer](networking-flex-cost-allocation-pcx.md)
+ [Manage within an AWS Organization](networking-flex-cost-allocation-orgs.md)
+ [Limitations](networking-flex-cost-allocation-limitations.md)
+ [Create resources with CloudFormation](networking-flex-cost-allocation-cfn.md)
+ [Understand the Cost and Usage Reports output](networking-flex-cost-allocation-cur.md)
+ [Troubleshoot](networking-flex-cost-allocation-troubleshoot.md)

Related resources
+ [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)
+ [NAT gateways](vpc-nat-gateway.md)
+ [VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
+ [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)