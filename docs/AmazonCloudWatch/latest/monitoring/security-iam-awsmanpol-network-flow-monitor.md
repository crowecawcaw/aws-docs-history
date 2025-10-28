# AWS managed policies for Network Flow Monitor

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: CloudWatchNetworkFlowMonitorServiceRolePolicy

You can't attach `CloudWatchNetworkFlowMonitorServiceRolePolicy` to your IAM entities. This policy is attached
to a service-linked role named **AWSServiceRoleForNetworkFlowMonitor**, which publishes
network telemetry aggregation results, collected by Network Flow Monitor agents, to CloudWatch. It also allows the service to use AWS Organizations
to get information for multi-account scenarios.

To view the permissions for this policy, see [CloudWatchNetworkFlowMonitorServiceRolePolicy](../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

For more information, see [Service-linked roles for Network Flow Monitor](using-service-linked-roles-network-flow-monitor.md "using-service-linked-roles-network-flow-monitor.md").

## AWS managed policy: CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy

You can't attach `CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy` to your IAM entities. This policy is attached
to a service-linked role named **AWSServiceRoleForNetworkFlowMonitor_Topology**. Using these permissions, as
well as internal meta data information gathering (for performance efficiencies), this service-linked role gathers meta data about resource
network configurations, such as describing route tables and gateways, for resources that this service monitors network traffic for. This meta data
enables Network Flow Monitor to generate topology snapshots of the resources. When there is network degradation, Network Flow Monitor uses the topologies to
provide insights into the location of issues in the network and to help determine attribution for issues.

To view the permissions for this policy, see [CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy](../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

For more information, see [Service-linked roles for Network Flow Monitor](using-service-linked-roles-network-flow-monitor.md "using-service-linked-roles-network-flow-monitor.md").

## AWS managed policy: CloudWatchNetworkFlowMonitorAgentPublishPolicy

You can use this policy in IAM roles that are attached to Amazon EC2 and Amazon EKS instance resources to send telemetry reports (metrics) to
a Network Flow Monitor endpoint.

To view the permissions for this policy, see [CloudWatchNetworkFlowMonitorAgentPublishPolicy](../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.md "../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.md") in the _AWS Managed Policy Reference_.

## Updates to the Network Flow Monitor service-linked roles

For updates to the AWS managed policies for the Network Flow Monitor service-linked roles,
see the [AWS managed policies updates table](managed-policies-cloudwatch.md#security-iam-awsmanpol-updates "managed-policies-cloudwatch.md#security-iam-awsmanpol-updates") for CloudWatch.
You can also subscribe to automatic RSS alerts on the CloudWatch [Document history page](DocumentHistory.md "DocumentHistory.md").
