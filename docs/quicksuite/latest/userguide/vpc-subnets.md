# Subnets

A _subnet_ is a range of IP addresses in your VPC.
You need to provide at least two subnets to create a VPC connection. Each subnet must
belong a different availability zone. You can attach AWS resources, such as Amazon EC2
instances and Amazon RDS DB instances, to subnets. You can create subnets to group instances
together according to your security and operational needs.

For Amazon Quick Suite to connect to your database, the network needs to route traffic to
the data sources that you want to reach from one of the subnets used by the Amazon Quick Suite
network interface. Amazon Quick Suite determines which subnet to route traffic through on the
backend. If the availability zone that the subnet is attached to experiences an outage,
Amazon Quick Suite reroutes the traffic to one of the other subnets that are configured in the
VPC connection. If the data sources are on different subnets, make sure that there is a
route from the Amazon Quick Suite network interface to your database instance. By default,
each subnet in a VPC is associated with one main route table and can reach the other
subnets. For more information, see [VPC and Subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md")
and [Network ACLs](../../../vpc/latest/userguide/vpc-connection-network-acls.md "../../../vpc/latest/userguide/vpc-connection-network-acls.md") in the _Amazon VPC User Guide._

If you use Amazon RDS, DB instances are associated with a subnet group that you can view
either in the Amazon RDS console ([https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/")) or in the VPC console. For troubleshooting
connectivity to Amazon RDS, see the AWS Support article [How can I troubleshoot connectivity to an Amazon RDS instance that uses a public or
private subnet of a VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/rds-connectivity-instance-subnet-vpc/ "https://aws.amazon.com/premiumsupport/knowledge-center/rds-connectivity-instance-subnet-vpc/")
