

# Networking Flexible Cost Allocation limitations

To use Networking Flexible Cost Allocation (FCA), you need to be aware of the following limitations. For the traffic that each resource type allocates, see [Allocate EC2 instance data transfer](networking-flex-cost-allocation-ec2.md), [Allocate NAT gateway costs](networking-flex-cost-allocation-natgw.md), and [Allocate VPC peering data transfer](networking-flex-cost-allocation-pcx.md).

General
+ FCA isn't available in every Region. For the Regions where FCA is available, see [Regional availability](networking-flexible-cost-allocation.md#networking-flex-cost-allocation-availability).
+ FCA applies only to traffic within a single Region. Traffic between Regions isn't allocated, including traffic over a cross-Region VPC peering connection.
+ You can create policies for NAT gateways, Amazon EC2 instances, and VPC peering connections. Other networking resources aren't supported yet.
+ Allocation applies to traffic that is metered after an association takes effect. It isn't applied to earlier traffic.
+ Associations use only the latest version of a policy. If you create versions in quick succession, an intermediate version might never take effect. For more information, see [Updating a policy](networking-flex-cost-allocation-work-with.md#networking-flex-cost-allocation-update).
+ You can specify up to 100 CIDR ranges in a policy, and you can specify source ranges or destination ranges, but not both.
+ You can create up to 100 policies per Region per account.
+ A resource can be associated with only one policy at a time.
+ A policy can be associated with up to 100 resources, accounts, VPCs, and subnets in total. You can specify up to 20 of them in one request.
+ You can associate only resources that your account owns. You can't associate a VPC or subnet that another account shares with you. For an account scope, you can specify only your own account.

NAT gateways
+ If an AWS Network Firewall endpoint or a Gateway Load Balancer endpoint sits between the traffic source and the NAT gateway, FCA doesn't itemize the NAT gateway usage for that traffic to the originating resource. It bills the usage as usual to the account that owns the NAT gateway.
+ Private NAT gateways aren't supported yet. FCA doesn't allocate the costs of a private NAT gateway.
+ If a network ACL on the NAT gateway's subnet drops outbound traffic that the source security group allowed, FCA still counts that traffic toward allocated usage and NAT gateway charges. To avoid paying for denied traffic, block it at the source using security group rules instead.

Accounts and organizations
+ Only the management account or a standalone account can turn on the **Networking flexible cost allocation** preference. Creating a policy for an account doesn't turn on the preference. The allocated line items appear in the report of the account that owns the shared resource and in the management account's report.