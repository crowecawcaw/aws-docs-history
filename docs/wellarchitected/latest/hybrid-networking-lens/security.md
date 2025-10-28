# Security

The security of your hybrid networking environment is crucial and
should span protection across your on-premises and cloud
environments. It is recommended to implement security controls for
traffic within your cloud environment, and particularly, traffic
flowing from the Internet and from your on-premises network to
AWS. The following services can help secure your hybrid networking
environment on AWS.

A **security group** (SG) acts as a
virtual firewall for your network interfaces in a VPC and allows
you to control inbound and outbound traffic including hybrid
traffic.

A **network access control list**
(ACL) is an optional layer of security for your VPC that acts as a
firewall for controlling traffic in and out of one or more
subnets. You might set up network ACLs with rules similar to your
security groups in order to add an additional layer of security to
your VPC.

**AWS Network Firewall** is a managed service that makes it
easy to deploy essential network protections such as URL and domain names, IP addresses, and
content-based traffic filtering to secure traffic traversing to and from your VPCs.

**AWS CloudTrail** is a service
that enables governance, compliance, operational auditing, and
risk auditing of your AWS account. With CloudTrail, you can log,
continuously monitor, and retain account activity related to
actions across your AWS infrastructure. CloudTrail provides event
history of your AWS account activity, including actions taken
through the AWS Management Console, AWS SDKs, command line tools,
and other AWS services. This event history simplifies security
analysis, resource change tracking, and troubleshooting. In
addition, you can use CloudTrail to detect unusual activity in
your AWS accounts. These capabilities also help simplify
operational analysis and troubleshooting.

**Amazon GuardDuty** is a threat
detection service that continuously monitors for malicious
activity and unauthorized behavior to protect your AWS accounts
and workloads. With the cloud, the collection and aggregation of
account and network activities is simplified, but it can be time
consuming for security teams to continuously analyze event log
data for potential threats. With GuardDuty, you now have an
intelligent and cost-effective option for continuous threat
detection in AWS. GuardDuty analyzes tens of billions of events
across multiple AWS data sources, such as AWS CloudTrail event
logs, Amazon VPC Flow Logs, and DNS logs.
