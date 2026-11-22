

# Identity and access management for Performance Monitor

Performance Monitor uses AWS Identity and Access Management (IAM) policies and a service-linked role to control access. You can use IAM to do the following:
+ Control which users can create, edit, or delete monitors.
+ Control which users can view network path data.
+ Control which users can modify the monitoring scope.

## AWS managed policies
<a name="CloudWatch-PerformanceMonitor-iam-managed-policies"></a>

For information about the AWS managed policies for CloudWatch Network Monitoring, see [AWS managed policies for Network Flow Monitor](security-iam-awsmanpol-network-flow-monitor.md).

## Service-linked roles
<a name="CloudWatch-PerformanceMonitor-iam-slr"></a>

Performance Monitor uses the Network Flow Monitor service-linked role, `AWSServiceRoleForNetworkFlowMonitor`. This role is created automatically when you initialize Performance Monitor. The role grants the following permissions:
+ Amazon EC2 read-only access, to list VPCs, subnets, and instances for topology mapping
+ CloudWatch metrics publishing, to emit performance metrics
+ AWS Organizations read access, for multi-account configurations

You can't modify or delete the service-linked role while a scope exists. To delete the role, you must first delete your scope. For more information, see [Service-linked roles for Network Flow Monitor](using-service-linked-roles-network-flow-monitor.md).