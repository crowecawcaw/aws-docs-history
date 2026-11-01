

# Troubleshooting agent connectivity
<a name="runtime-monitoring-agent-connectivity-troubleshooting"></a>

GuardDuty connects the Runtime Monitoring security agent to GuardDuty over one of the two connectivity methods: an Amazon VPC endpoint, or a link-local address.

Link-local connectivity is not supported in all AWS Regions. In Regions where it is not supported, the agent connects through an Amazon VPC endpoint. Link-local connectivity is only supported for automated management; for manual management, you need to create an Amazon VPC endpoint.

## Determining VPC connectivity method
<a name="runtime-monitoring-link-local-which-method"></a>

To determine which method an Amazon VPC uses, check the route table associated with the subnet that your monitored resource runs in for a route with the target `GuardDuty`. In the Amazon VPC console, choose **Route tables**, select the route table associated with the subnet that your monitored resource runs in, and then choose the **Routes** tab.
+ If the route table has a route to `169.254.170.248/29` or `fd00:ec2:6d00::/64` with the target `GuardDuty`, the Amazon VPC has link-local connectivity, and a security agent of version `v1.17.3` or later uses it. If the Amazon VPC also has a `guardduty-data` Amazon VPC endpoint, security agent version `v1.17.3` or later prioritizes link-local connectivity. You can't delete or modify the GuardDuty-managed route.
+ If the Amazon VPC has an Amazon VPC endpoint for `com.amazonaws.{{us-east-1}}.guardduty-data` and the security agent doesn't use link-local connectivity, the security agent uses the endpoint method.

## Troubleshooting VPC endpoint connectivity
<a name="runtime-monitoring-vpc-endpoint-troubleshooting"></a>

To troubleshoot the endpoint method, see [Validating VPC endpoint configuration](validate-vpc-endpoint-config-runtime-monitoring.md).

## Troubleshooting link-local connectivity
<a name="runtime-monitoring-link-local-not-reporting"></a>

If a resource shows **Unhealthy** with an agent not reporting coverage issue and its Amazon VPC has link-local connectivity (see [Determining VPC connectivity method](#runtime-monitoring-link-local-which-method)), use the following table.


| Issue type | Issue message | Troubleshooting steps | 
| --- | --- | --- | 
| Agent not reporting | Amazon EKS: `Unsupported agent version found. Upgrade agent to version v1.17.3 or later.`<br />Amazon ECS on AWS Fargate: `Unsupported agent version '{{version}}' for task(s) in TaskDefinition - '{{family}}'. Upgrade agent to version v1.17.3 or later.` | Link-local connectivity requires security agent version `v1.17.3` or later for Amazon EC2 instances, Amazon ECS (including AWS Fargate), and Amazon EKS clusters. These messages appear for Amazon EKS and Amazon ECS on AWS Fargate agents earlier than the minimum version. For security agent version history, see [GuardDuty security agent release versions](runtime-monitoring-agent-release-history.md). | 
| Agent not reporting | Other agent not reporting messages | Check the network path to the link-local ranges. If you run host-level controls that inspect or filter the agent's traffic, or apply security group outbound rules on your hosts, allow the GuardDuty link-local ranges `169.254.170.248/29` (IPv4) and `fd00:ec2:6d00::/64` (IPv6). For more information, see [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md).<br />Confirm that the agent meets the minimum version. | 