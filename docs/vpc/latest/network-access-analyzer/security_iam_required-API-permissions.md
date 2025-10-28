# Required API permissions for

Network Access Analyzer

Network Access Analyzer relies on data from other AWS services. It uses permissions from the following
services:

- Amazon EC2
- Elastic Load Balancing
- AWS Network Firewall
- AWS Resource Groups
- AWS Resource Groups Tagging API
- AWS Tiros
  To view the permissions for this policy, see [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](../../../aws-managed-policy/latest/reference/AmazonVPCNetworkAccessAnalyzerFullAccessPolicy.md "../../../aws-managed-policy/latest/reference/AmazonVPCNetworkAccessAnalyzerFullAccessPolicy.md") in the _AWS Managed Policy Reference_.

## Additional information

###### Network Access Analyzer API calls

The following permissions are required to call the Network Access Analyzer APIs. Users need these
permissions to create and start analyzing Network Access Scopes, or to view and delete
existing paths and analyses in your account. You must grant users permission to call the
Network Access Analyzer API actions that they need.

- `ec2:CreateNetworkInsightsAccessScope`
- `ec2:DeleteNetworkInsightsAccessScope`
- `ec2:DeleteNetworkInsightsAccessScopeAnalysis`
- `ec2:DescribeNetworkInsightsAccessScopeAnalyses`
- `ec2:DescribeNetworkInsightsAccessScopes`
- `ec2:GetNetworkInsightsAccessScopeAnalysisFindings`
- `ec2:GetNetworkInsightsAccessScopeContent`
- `ec2:StartNetworkInsightsAccessScopeAnalysis`

###### Describe API calls for networking-related resources

Network Access Analyzer uses describe calls while gathering information about your resources from Amazon VPC,
Amazon EC2, Elastic Load Balancing, and AWS Network Firewall (for example, subnets, network interfaces, and security
groups). To access Network Access Analyzer, users must also have these API permissions.

If you specify a resource group in a resource statement, Network Access Analyzer uses
`resource-groups:ListResourceGroups` while gathering information about your
network configuration. This action requires the following permissions:
`cloudformation:DescribeStacks`
`cloudformation:ListStackResources`, and `tag:GetResources`.

###### Tagging-related API calls

To tag or untag Network Access Analyzer resources, users need the following Amazon EC2 API permissions. To
allow users to work with tags, you must grant them permission to use the specific tagging
actions that they need.

- `ec2:CreateTags`
- `ec2:DeleteTags`

###### Tiros API calls

If you monitor API calls, you might see calls to Tiros APIs.
Tiros is a service that is only accessible by AWS services and that
surfaces network findings to Network Access Analyzer. Calls to the Tiros endpoint are
required for Network Access Analyzer to function. To access Network Access Analyzer, users must also have the same API
permissions.
