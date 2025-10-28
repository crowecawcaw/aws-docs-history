# Ensure internetwork traffic privacy in Amazon VPC

Amazon Virtual Private Cloud provides features that you can use to increase and monitor the security for your
virtual private cloud (VPC):

- **Security groups**: Security groups allow specific
  inbound and outbound traffic at the resource level (such as an EC2 instance). When you
  launch an instance, you can associate it with one or more security groups. Each instance in
  your VPC could belong to a different set of security groups. If you don't specify a security
  group when you launch an instance, the instance is automatically associated with the default
  security group for its VPC. For more information, see [Security groups](vpc-security-groups.md "vpc-security-groups.md").
- **Network access control lists (ACL)**: Network ACLs allow
  or deny specific inbound and outbound traffic at the subnet level. For more information, see
  [Control subnet traffic with network access control lists](vpc-network-acls.md "vpc-network-acls.md").
- **Flow logs**: Flow logs capture information about the IP
  traffic going to and from network interfaces in your VPC. You can create a flow log for a
  VPC, subnet, or individual network interface. Flow log data is published to CloudWatch Logs or Amazon S3,
  and it can help you diagnose overly restrictive or overly permissive security group and
  network ACL rules. For more information, see [Logging IP traffic using VPC Flow Logs](flow-logs.md "flow-logs.md").
- **Traffic mirroring**: You can copy network traffic from an
  elastic network interface of an Amazon EC2 instance. You can then send the traffic to
  out-of-band security and monitoring appliances. For more information, see the [Traffic Mirroring Guide](../mirroring.md "../mirroring.md").
