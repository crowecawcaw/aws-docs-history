# Required API permissions for

Reachability Analyzer

Reachability Analyzer relies on data from other AWS services. It uses permissions from the following
services:

- Amazon EC2
- Elastic Load Balancing
- AWS Network Firewall
- AWS Tiros
  To view the permissions for this policy, see [AmazonVPCReachabilityAnalyzerFullAccessPolicy](../../../aws-managed-policy/latest/reference/AmazonVPCReachabilityAnalyzerFullAccessPolicy.md "../../../aws-managed-policy/latest/reference/AmazonVPCReachabilityAnalyzerFullAccessPolicy.md") in the _AWS Managed Policy Reference_.

## Additional information

###### Reachability Analyzer API calls

The following permissions are required to call the Reachability Analyzer APIs. Users need these
permissions to create and start analyzing a specified path for reachability, or to view
and delete existing paths and analyses in your account. You must grant users permission to
call the Reachability Analyzer API actions they need.

- `ec2:CreateNetworkInsightsPath`
- `ec2:DeleteNetworkInsightsAnalysis`
- `ec2:DeleteNetworkInsightsPath`
- `ec2:DescribeNetworkInsightsAnalyses`
- `ec2:DescribeNetworkInsightsPaths`
- `ec2:EnableReachabilityAnalyzerOrganizationSharing`
- `ec2:StartNetworkInsightsAnalysis`

###### Describe API calls for networking-related resources

Reachability Analyzer uses describe API calls while gathering information about your resources from
Amazon VPC, Amazon EC2, and Elastic Load Balancing (for example, subnets, network interfaces, and security groups).
To access Reachability Analyzer, users must also have these API permissions.

###### Cross-account analysis

The following permissions are required to establish a trust relationship between Reachability Analyzer
and AWS Organizations.

- `cloudformation:ActivateOrganizationsAccess`
- `iam:CreateServiceLinkedRole`
- `iam:GetRole`
- `organizations:EnableAWSServiceAccess`
- `organizations:DescribeOrganization`
- `organizations:DisableAWSServiceAccess`
- `organizations:ListRoots`

After you establish a trust relationship, a user in the management account or a
delegated administrator account can run cross-account analyses using resources from
the member accounts. The user must have the following permissions to do so.

- `organizations:DescribeOrganization`
- `organizations:ListAWSServiceAccessForOrganization`
- `organizations:ListDelegatedServicesForAccount`
- `organizations:ListDelegatedAdministrators`
- `organizations:ListAccounts`

###### Tagging-related API calls

To tag or untag Reachability Analyzer resources, users need the following Amazon EC2 API permissions. To
allow users to work with tags, you must grant them permission to use the specific tagging
actions they need.

- `ec2:CreateTags`
- `ec2:DeleteTags`

###### Tiros API calls

If you monitor API calls, you might see calls to Tiros APIs.
Tiros is a service that is only accessible by AWS services and that
surfaces network reachability findings to Reachability Analyzer. Calls to the Tiros endpoint
are required for Reachability Analyzer to function. To access Reachability Analyzer, users must also have the same API
permissions.
