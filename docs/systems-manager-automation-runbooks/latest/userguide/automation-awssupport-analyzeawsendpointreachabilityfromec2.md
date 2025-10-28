# `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2`

**Description**

The `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2` runbook analyzes
connectivity from an Amazon Elastic Compute Cloud (Amazon EC2) instance or elastic network interface to an
AWS service endpoint. IPv6 is not supported. The runbook uses the value that you specify
for the `ServiceEndpoint` parameter to analyze connectivity to an endpoint. If an
AWS PrivateLink endpoint can't be found in your VPC, the runbook uses a public IP address for
the service in the current AWS Region. This automation uses Reachability Analyzer from Amazon Virtual Private Cloud. For
more information, see [What is
Reachability Analyzer?](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md"), in _Reachability Analyzer_.

This automation checks the following:

- Checks whether your virtual private cloud (VPC) is configured to use the Amazon
  provided DNS server.
- Checks whether an AWS PrivateLink endpoint exists in the VPC for the AWS service
  that you specify. If an endpoint is found, the automation verifies that the
  `privateDns` attribute is turned on.
- Checks if the AWS PrivateLink endpoint is using the default endpoint policy.

**Considerations**

- You are charged per analysis run between a source and destination. For more
  information, see [Amazon VPC
  Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").
- During the automation, a network insights path and network insights analysis are
  created. If the automation completes successfully, the runbook deletes these
  resources . If the cleanup step fails, the network insights path is not deleted by
  the runbook and you will need to delete it manually. If you don't delete the network
  insights path manually, it continues to count towards the quota for your
  AWS account. For more information about quotas for Reachability Analyzer, see [Quotas for Reachability Analyzer](../../../vpc/latest/reachability/reachability-analyzer-limits.md "../../../vpc/latest/reachability/reachability-analyzer-limits.md") in _Reachability Analyzer_.
- Operating system-level configurations such as the use of a proxy, local DNS
  resolver, or hosts file can affect connectivity even if the Reachability Analyzer returns
  `PASS`.
- Review the evaluation of all checks performed by the Reachability Analyzer. If any of the checks
  return with a status of `FAIL`, that might affect connectivity even if
  the overall reachability check returns a status of `PASS`.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2 "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2")

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

- Source

Type: String

Description: (Required) The ID of the Amazon EC2 instance or the network interface from
which you want to analyze reachability.

- ServiceEndpoint

Type: String

Description: (Required) The hostname of the service endpoint that you want to
analyze reachability to.

- RetainVpcReachabilityAnalysis

Type: String

Default: false

Description: (Optional) Determines whether the network insight path and related
analysis created are retained. By default, the resources used for analyze
reachability are deleted after successful analysis. If you choose to retain the
analysis, the runbook does not delete the analysis and you can visualize it in the
Amazon VPC console. A console link is available in the automation output.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:CreateNetworkInsightsPath`
- `ec2:DeleteNetworkInsightsAnalysis`
- `ec2:DeleteNetworkInsightsPath`
- `ec2:DescribeAvailabilityZones`
- `ec2:DescribeCustomerGateways`
- `ec2:DescribeDhcpOptions`
- `ec2:DescribeInstances`
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
- `ec2:DescribeTransitGatewayPeeringAttachments`
- `ec2:DescribeTransitGatewayConnects`
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
- `ec2:StartNetworkInsightsAnalysis`
- `elasticloadbalancing:DescribeListeners`
- `elasticloadbalancing:DescribeLoadBalancerAttributes`
- `elasticloadbalancing:DescribeLoadBalancers`
- `elasticloadbalancing:DescribeRules`
- `elasticloadbalancing:DescribeTags`
- `elasticloadbalancing:DescribeTargetGroups`
- `elasticloadbalancing:DescribeTargetHealth`
- `tiros:CreateQuery`
- `tiros:GetQueryAnswer`
- `tiros:GetQueryExplanation`

**Document Steps**

1. `aws:executeScript`: Validates the service endpoint by attempting to
   resolve the hostname.
2. `aws:executeScript`: Gathers details about the VPC and subnet.
3. `aws:executeScript`: Evaluates the DNS configuration of the VPC.
4. `aws:executeScript`: Evaluates the VPC endpoint checks.
5. `aws:executeScript`: Locates an internet gateway to connect to the
   public service endpoint.
6. `aws:executeScript`: Determines the destination to be used for
   reachability analysis.
7. `aws:executeScript`: Analyzes the reachability from source to the
   endpoint using Reachability Analyzer and cleans up the resources if the analysis is successful.
8. `aws:executeScript`: Generates a reachability evaluation report.
9. `aws:executeScript`: Generates the output in JSON.

**Outputs**

- `generateReport.EvalReport` - The results of the checks performed by
  the automation in text format.
- `generateJsonOutput.Output` - A minimal version of the results in JSON
  format.
