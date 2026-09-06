

# Dynamic routing in your VPC using VPC Route Server
<a name="dynamic-routing-route-server"></a>

Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads.

Route server supports the following route table types:
+ VPC route tables not associated with subnets
+ Subnet route tables
+ Internet gateway route tables

Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use [Transit Gateway Connect](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html).

**Quotas**

For quotas associated with Amazon VPC Route Server, see [Route server quotas](amazon-vpc-limits.md#vpc-limits-route-servers).

**Pricing**

For information about costs associated with Amazon VPC Route Server, see the [VPC Route Server](https://aws.amazon.com/vpc/pricing/) tab on the Amazon VPC pricing page.

**Topics**
+ [Terminology](route-server-terms.md)
+ [How Amazon VPC Route Server works](route-server-how-it-works.md)
+ [Route server peer logging](route-server-peer-logging.md)
+ [Get started tutorial](route-server-tutorial.md)