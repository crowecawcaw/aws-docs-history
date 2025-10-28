# Security best practices for your VPC

The following best practices are general guidelines and don’t represent a complete security
solution. Because these best practices might not be appropriate or sufficient for your
environment, treat them as helpful considerations rather than prescriptions.

- When you add subnets to your VPC to host your application, create them in multiple
  Availability Zones. An Availability Zone is one or more discrete data centers with
  redundant power, networking, and connectivity in an AWS Region. Using multiple
  Availability Zones makes your production applications highly available, fault tolerant,
  and scalable.
- Use security groups to control traffic to EC2 instances in your subnets. For more
  information, see [Security groups](vpc-security-groups.md "vpc-security-groups.md").
- Use network ACLs to control inbound and outbound traffic at the subnet level. For more
  information, see [Control subnet traffic with network access control lists](vpc-network-acls.md "vpc-network-acls.md").
- Manage access to AWS resources in your VPC using AWS Identity and Access Management (IAM) identity
  federation, users, and roles. For more information, see [Identity and access management for Amazon VPC](security-iam.md "security-iam.md").
- Use VPC Flow Logs to monitor the IP traffic going to and from a VPC, subnet, or network
  interface. For more information, see [VPC Flow Logs](flow-logs.md "flow-logs.md").
- Use Network Access Analyzer to identify unintended network access to resources in our VPCs. For more
  information, see the [Network Access Analyzer Guide](../network-access-analyzer.md "../network-access-analyzer.md").
- Use AWS Network Firewall to monitor and protect your VPC by filtering inbound and outbound traffic.
  For more information, see the [AWS Network Firewall Guide](../../../network-firewall/latest/developerguide.md "../../../network-firewall/latest/developerguide.md").
- Use Amazon GuardDuty to detect potential threats to your accounts, containers, workloads, and
  data within your AWS environment. The foundational threat detection includes monitoring
  the VPC flow logs associated with your Amazon EC2 instances. For more information, see [VPC Flow Logs](../../../guardduty/latest/ug/guardduty_data-sources.md#guardduty_vpc "../../../guardduty/latest/ug/guardduty_data-sources.md#guardduty_vpc") in the _Amazon GuardDuty User Guide_.
  For answers to frequently asked questions related to VPC security, see _Security and
  Filtering_ in the [Amazon VPC FAQs](https://aws.amazon.com/vpc/faqs/ "https://aws.amazon.com/vpc/faqs/").
