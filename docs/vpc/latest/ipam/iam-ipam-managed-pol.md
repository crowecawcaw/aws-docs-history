# AWS managed policies for IPAM

If you are using IPAM with a single AWS account and you create an IPAM, the **AWSIPAMServiceRolePolicy** managed policy is automatically created in your IAM account and attached to the **AWSServiceRoleForIPAM** [service-linked role](iam-ipam-slr.md "iam-ipam-slr.md").

If you enable IPAM integration with AWS Organizations, the **AWSIPAMServiceRolePolicy** managed policy is automatically created in your IAM account and in each of your AWS Organizations member accounts, and the managed policy is attached to the **AWSServiceRoleForIPAM** service-linked role.

This managed policy enables IPAM to do the following:

- Monitor CIDRs associated with networking resources across all members of your AWS Organization.
- Store metrics related to IPAM in Amazon CloudWatch, such as the IP address space available in your IPAM
  pools and the number of resource CIDRs that comply with allocation rules.
- Modify and read managed prefix lists.
  The following example shows the details of the managed policy that's created.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IPAMDiscoveryDescribeActions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAddresses",
 "ec2:DescribeByoipCidrs",
 "ec2:DescribeIpv6Pools",
 "ec2:DescribeManagedPrefixLists",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribePublicIpv4Pools",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpnConnections",
 "ec2:GetIpamDiscoveredAccounts",
 "ec2:GetIpamDiscoveredPublicAddresses",
 "ec2:GetIpamDiscoveredResourceCidrs",
 "ec2:GetManagedPrefixListEntries",
 "ec2:ModifyManagedPrefixList",
 "globalaccelerator:ListAccelerators",
 "globalaccelerator:ListByoipCidrs",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListChildren",
 "organizations:ListParents",
 "organizations:DescribeOrganizationalUnit"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchMetricsPublishActions",
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/IPAM"
 }
 }
 }
 ]
}`

```

The first statement in the preceding example enables IPAM to monitor the CIDRs used by your single AWS account or by the members of your AWS Organization.

The second statement in the preceding example uses the
`cloudwatch:PutMetricData` condition key to allow IPAM to store IPAM
metrics in your `AWS/IPAM`
[Amazon CloudWatch namespace](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md"). These metrics are used by the AWS Management Console to display data about the allocations in your IPAM pools and scopes. For more information,
see [Monitor CIDR usage with the IPAM dashboard](monitor-cidr-usage-ipam.md "monitor-cidr-usage-ipam.md").

## Updates to the AWS managed policy

View details about updates to AWS managed policies for IPAM since this service began
tracking these changes.

| Change                        | Description                                                                                                                                                                                                                                                                                                                                                                                              | Date              |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| AWSIPAMServiceRolePolicy      | Actions added to the AWSIPAMServiceRolePolicy managed policy (ec2:ModifyManagedPrefixList, ec2:DescribeManagedPrefixLists, and ec2:GetManagedPrefixListEntries) to enable IPAM to modify and read managed prefix lists.                                                                                                                                                                                  | October 31, 2025  |
| AWSIPAMServiceRolePolicy      | Actions added to the AWSIPAMServiceRolePolicy managed policy (`organizations:ListChildren`,`organizations:ListParents`, and `organizations:DescribeOrganizationalUnit`) to enable IPAM to get the details of Organizational Units (OUs) in AWS Organizations so that customers can use IPAM at the OU level.                                                                                             | November 21, 2024 |
| AWSIPAMServiceRolePolicy      | Action added to the AWSIPAMServiceRolePolicy managed policy<br>(`ec2:GetIpamDiscoveredPublicAddresses`) to enable<br>IPAM to get public IP addresses during resource discovery.                                                                                                                                                                                                                          | November 13, 2023 |
| AWSIPAMServiceRolePolicy      | Actions added to the AWSIPAMServiceRolePolicy managed policy<br>(`ec2:DescribeAccountAttributes`,<br>`ec2:DescribeNetworkInterfaces`,<br>`ec2:DescribeSecurityGroups`,<br>`ec2:DescribeSecurityGroupRules`,<br>`ec2:DescribeVpnConnections`,<br>`globalaccelerator:ListAccelerators`, and<br>`globalaccelerator:ListByoipCidrs`) to enable IPAM to get<br>public IP addresses during resource discovery. | November 1, 2023  |
| AWSIPAMServiceRolePolicy      | Two actions added to<br>the AWSIPAMServiceRolePolicy managed policy (`ec2:GetIpamDiscoveredAccounts` and<br>`ec2:GetIpamDiscoveredResourceCidrs`) to enable IPAM to get<br>the AWS accounts and resource CIDRs being monitored during<br>resource discovery.                                                                                                                                             | January 25, 2023  |
| IPAM started tracking changes | IPAM started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                              | December 2, 2021  |
