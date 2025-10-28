# `AWSSupport-TroubleshootSessionManager`

**Description**

The `AWSSupport-TroubleshootSessionManager` runbook helps you
troubleshoot common issues that prevent you from connecting to managed Amazon Elastic Compute Cloud
(Amazon EC2) instances using Session Manager. Session Manager is a tool in AWS Systems Manager. This runbook checks the
following:

- Checks whether the instance is running and reporting as managed by
  Systems Manager.
- Runs the `AWSSupport-TroubleshootManagedInstance` runbook if
  the instance is not reporting as managed by Systems Manager.
- Checks the version of the SSM Agent installed on the instance.
- Checks whether an instance profile containing a recommended AWS Identity and Access Management
  (IAM) policy for Session Manager is attached to the Amazon EC2 instance.
- Collects SSM Agent logs from the instance.
- Analyzes your Session Manager preferences.
- Runs the `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2`
  runbook to analyze the instance's connectivity to the endpoints for Session Manager,
  AWS Key Management Service (AWS KMS), Amazon Simple Storage Service (Amazon S3) and Amazon CloudWatch Logs (CloudWatch Logs).

**Considerations**

- Hybrid managed nodes are not supported.
- This runbook only checks whether a recommended managed IAM policy is
  attached to the instance profile. It does not analyze IAM or AWS KMS
  permissions contained in your instance profile.

###### Important

The `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2` runbook
uses [VPC Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to analyze the network connectivity
between a source and a service endpoint. You are charged per analysis run
between a source and destination. For more details, see [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSessionManager "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSessionManager")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- InstanceId

Type: String

Description: (Required) The ID of the Amazon EC2 instance that you are unable
to connect to using Session Manager.

- SessionPreferenceDocument

Type: String

Default: SSM-SessionManagerRunShell

Description: (Optional) The name of your session preferences document. If
you don't specify a custom session preferences document when starting
sessions, use the default value.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:CreateNetworkInsightsPath`
- `ec2:DeleteNetworkInsightsAnalysis`
- `ec2:DeleteNetworkInsightsPath`
- `ec2:StartNetworkInsightsAnalysis`
- `tiros:CreateQuery`
- `ec2:DescribeAvailabilityZones`
- `ec2:DescribeCustomerGateways`
- `ec2:DescribeDhcpOptions`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeInternetGateways`
- `ec2:DescribeManagedPrefixLists`
- `ec2:DescribeNatGateways`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeNetworkInsightsAnalyses`
- `ec2:DescribeNetworkInsightsPaths`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribePrefixLists`
- `ec2:DescribeRegions`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:DescribeTransitGatewayAttachments`
- `ec2:DescribeTransitGatewayConnects`
- `ec2:DescribeTransitGatewayPeeringAttachments`
- `ec2:DescribeTransitGatewayRouteTables`
- `ec2:DescribeTransitGateways`
- `ec2:DescribeTransitGatewayVpcAttachments`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeVpcEndpoints`
- `ec2:DescribeVpcEndpointServiceConfigurations`
- `ec2:DescribeVpcPeeringConnections`
- `ec2:DescribeVpcs`
- `ec2:DescribeVpnConnections`
- `ec2:DescribeVpnGateways`
- `ec2:GetManagedPrefixListEntries`
- `ec2:GetTransitGatewayRouteTablePropagations`
- `ec2:SearchTransitGatewayRoutes`
- `elasticloadbalancing:DescribeListeners`
- `elasticloadbalancing:DescribeLoadBalancerAttributes`
- `elasticloadbalancing:DescribeLoadBalancers`
- `elasticloadbalancing:DescribeRules`
- `elasticloadbalancing:DescribeTags`
- `elasticloadbalancing:DescribeTargetGroups`
- `elasticloadbalancing:DescribeTargetHealth`
- `iam:GetInstanceProfile`
- `iam:ListAttachedRolePolicies`
- `iam:ListRoles`
- `iam:PassRole`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:DescribeInstanceInformation`
- `ssm:GetAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListCommands`
- `ssm:ListCommandInvocations`
- `ssm:SendCommand`
- `ssm:StartAutomationExecution`
- `tiros:GetQueryAnswer`
- `tiros:GetQueryExplanation`

**Document Steps**

1. `aws:waitForAwsResourceProperty`: Waits up to 6 minutes for
   your target instance to pass status checks.
2. `aws:executeScript`: Parses the session preference
   document.
3. `aws:executeAwsApi`: Gets the ARN of the instance profile
   attached to your instance.
4. `aws:executeAwsApi`: Checks whether your instance is reporting
   as managed by Systems Manager.
5. `aws:branch`: Branches based on whether your instance is
   reporting as managed by Systems Manager.
6. `aws:executeScript`: Checks whether the SSM Agent installed on
   your instance supports Session Manager.
7. `aws:branch`: Branches based on the platform of your instance
   to collect `ssm-cli` logs.
8. `aws:runCommand`: Collects logs output from
   `ssm-cli` from a Linux or macOS
   instance.
9. `aws:runCommand`: Collects logs output from
   `ssm-cli` from a Windows instance.
10. `aws:executeScript`: Parses the `ssm-cli`
    logs.
11. `aws:executeScript`: Checks whether a recommended IAM policy
    is attached to the instance profile.
12. `aws:branch`: Determines whether to evaluate
    `ssmmessages` endpoint connectivity based on
    `ssm-cli` logs.
13. `aws:executeAutomation`: Evaluates whether the instance can
    connect to an `ssmmessages` endpoint.
14. `aws:branch`: Determines whether to evaluate Amazon S3 endpoint
    connectivity based on `ssm-cli` logs and your session
    preferences.
15. `aws:executeAutomation`: Evaluates whether the instance can
    connect to an Amazon S3 endpoint.
16. `aws:branch`: Determines whether to evaluate AWS KMS endpoint
    connectivity based on `ssm-cli` logs and your session
    preferences.
17. `aws:executeAutomation`: Evaluates whether the instance can
    connect to an AWS KMS endpoint.
18. `aws:branch`: Determines whether to evaluate CloudWatch Logs endpoint
    connectivity based on `ssm-cli` logs and your session
    preferences.
19. `aws:executeAutomation`: Evaluates whether the instance can
    connect to an CloudWatch Logs endpoint.
20. `aws:executeAutomation`: Runs the
    `AWSSupport-TroubleshootManagedInstance` runbook.
21. `aws:executeScript`: Compiles the output of the previous steps
    and outputs a report.

**Ouputs**

- `generateReport.EvalReport` - The results of the checks
  performed by the runbook in plain text.
