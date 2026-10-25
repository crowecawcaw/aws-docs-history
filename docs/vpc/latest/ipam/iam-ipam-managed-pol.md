

# AWS managed policies for IPAM
<a name="iam-ipam-managed-pol"></a>

If you are using IPAM with a single AWS account and you create an IPAM, the **AWSIPAMServiceRolePolicy** managed policy is automatically created in your IAM account and attached to the **AWSServiceRoleForIPAM** [service-linked role](iam-ipam-slr.md).

If you enable IPAM integration with AWS Organizations, the **AWSIPAMServiceRolePolicy** managed policy is automatically created in your IAM account and in each of your AWS Organizations member accounts, and the managed policy is attached to the **AWSServiceRoleForIPAM** service-linked role.

This managed policy enables IPAM to do the following:
+ Monitor CIDRs associated with networking resources across all members of your AWS Organization, including public IP addresses used by Global Accelerator and CloudFront, and DNS records in Route 53 hosted zones that resolve to those IP addresses (statement `IPAMDiscoveryDescribeActions`). 
+ Store metrics related to IPAM in Amazon CloudWatch, such as the IP address space available in your IPAM pools and the number of resource CIDRs that comply with allocation rules (statement `CloudWatchMetricsPublishActions`). The `cloudwatch:PutMetricData` condition key restricts this to your `AWS/IPAM` [Amazon CloudWatch namespace](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html). These metrics are used by the AWS Management Console to display data about the allocations in your IPAM pools and scopes. For more information, see [Monitor CIDR usage with the IPAM dashboard](monitor-cidr-usage-ipam.md).
+ Allocate CIDRs from your IPAM pools when enforcing IPAM policy allocation rules (statement `IPAMAllocationPolicyActions`). For more information, see [Define public IPv4 allocation strategy with IPAM policies](define-public-ipv4-allocation-strategy-with-ipam-policies.md).
+ Modify and read managed prefix lists (statements `PrefixListResolverWriteActions` and `PrefixListResolverReadActions`). For more information, see [Automate prefix list updates with IPAM](automate-prefix-list-updates.md).
+ Create, associate, and delete the DHCP option sets that IPAM manages for IPAM policy DHCP rules (statement `IPAMDhcpOptionSetManagementActions`). IPAM does not modify or delete DHCP option sets that you create.

To view the current JSON policy document, version history, and ARN for this policy, see [AWSIPAMServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSIPAMServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Updates to the AWS managed policy
<a name="iam-ipam-managed-pol-updates"></a>

View details about updates to AWS managed policies for IPAM since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| AWSIPAMServiceRolePolicy | Actions added to the AWSIPAMServiceRolePolicy managed policy (ec2:DescribeDhcpOptions, ec2:CreateDhcpOptions, ec2:AssociateDhcpOptions, and ec2:DeleteDhcpOptions) to let IPAM create, associate, and delete the DHCP option sets that it manages for IPAM policy DHCP rules. | October 15, 2026 | 
| AWSIPAMServiceRolePolicy | Actions added to the AWSIPAMServiceRolePolicy managed policy (route53:ListHostedZones, route53:GetHostedZone, route53:ListResourceRecordSets, and route53:ListTagsForResource) to let IPAM read DNS records in Route 53 hosted zones during resource discovery. | October 15, 2026 | 
| AWSIPAMServiceRolePolicy | Action added to the AWSIPAMServiceRolePolicy managed policy (ec2:GetIpamDiscoveredRoutes) to let IPAM get routes during resource discovery for BGP route protection monitoring. | September 9, 2026 | 
| AWSIPAMServiceRolePolicy | Actions added to the AWSIPAMServiceRolePolicy managed policy (ec2:ModifyManagedPrefixList, ec2:DescribeManagedPrefixLists, and ec2:GetManagedPrefixListEntries) to enable IPAM to modify and read managed prefix lists. | October 31, 2025 | 
| AWSIPAMServiceRolePolicy | Actions added to the AWSIPAMServiceRolePolicy managed policy (cloudfront:ListAnycastIpLists, cloudfront:ListDistributionsByAnycastIpListId, and cloudfront:ListTagsForResource) to let IPAM discover BYOIP CIDRs used by CloudFront anycast IP lists. | October 23, 2025 | 
| AWSIPAMServiceRolePolicy | Action added to the AWSIPAMServiceRolePolicy managed policy (ec2:AllocateIpamPoolCidr) to let IPAM allocate CIDRs from IPAM pools when enforcing IPAM policy allocation rules. | October 23, 2025 | 
| AWSIPAMServiceRolePolicy | Actions added to the AWSIPAMServiceRolePolicy managed policy (`organizations:ListChildren`,`organizations:ListParents`, and `organizations:DescribeOrganizationalUnit`) to enable IPAM to get the details of Organizational Units (OUs) in AWS Organizations so that customers can use IPAM at the OU level.  | November 21, 2024 | 
| AWSIPAMServiceRolePolicy | Action added to the AWSIPAMServiceRolePolicy managed policy (`ec2:GetIpamDiscoveredPublicAddresses`) to enable IPAM to get public IP addresses during resource discovery. | November 13, 2023 | 
| AWSIPAMServiceRolePolicy | Actions added to the AWSIPAMServiceRolePolicy managed policy (ec2:DescribeAccountAttributes, ec2:DescribeNetworkInterfaces, ec2:DescribeSecurityGroups, ec2:DescribeSecurityGroupRules, ec2:DescribeVpnConnections, globalaccelerator:ListAccelerators, and globalaccelerator:ListByoipCidrs) to enable IPAM to get public IP addresses during resource discovery. | November 1, 2023 | 
| AWSIPAMServiceRolePolicy | Two actions added to the AWSIPAMServiceRolePolicy managed policy (`ec2:GetIpamDiscoveredAccounts` and `ec2:GetIpamDiscoveredResourceCidrs`) to enable IPAM to get the AWS accounts and resource CIDRs being monitored during resource discovery. | January 25, 2023 | 
| IPAM started tracking changes | IPAM started tracking changes for its AWS managed policies. | December 2, 2021 | 