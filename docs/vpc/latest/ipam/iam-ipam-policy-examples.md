# Example policy

The example policy in this section contains all the relevant AWS Identity and Access Management (IAM) actions for full IPAM usage. Depending on how you are using IPAM, you may not need to include all of the IAM actions. For a full experience using the IPAM console, you may need to include additional
IAM actions for services such as AWS Organizations, AWS Resource Access Manager (AWS RAM), and Amazon CloudWatch.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AssociateIpamByoasn",
 "ec2:DeprovisionIpamByoasn",
 "ec2:DescribeIpamByoasn",
 "ec2:DisassociateIpamByoasn",
 "ec2:ProvisionIpamByoasn",
 "ec2:CreateIpam",
 "ec2:DescribeIpams",
 "ec2:ModifyIpam",
 "ec2:DeleteIpam",
 "ec2:CreateIpamScope",
 "ec2:DescribeIpamScopes",
 "ec2:ModifyIpamScope",
 "ec2:DeleteIpamScope",
 "ec2:CreateIpamPool",
 "ec2:DescribeIpamPools",
 "ec2:ModifyIpamPool",
 "ec2:DeleteIpamPool",
 "ec2:ProvisionIpamPoolCidr",
 "ec2:GetIpamPoolCidrs",
 "ec2:DeprovisionIpamPoolCidr",
 "ec2:AllocateIpamPoolCidr",
 "ec2:GetIpamPoolAllocations",
 "ec2:ReleaseIpamPoolAllocation",
 "ec2:CreateIpamResourceDiscovery",
 "ec2:DescribeIpamResourceDiscoveries",
 "ec2:ModifyIpamResourceDiscovery",
 "ec2:DeleteIpamResourceDiscovery",
 "ec2:AssociateIpamResourceDiscovery",
 "ec2:DescribeIpamResourceDiscoveryAssociations",
 "ec2:DisassociateIpamResourceDiscovery",
 "ec2:GetIpamResourceCidrs",
 "ec2:ModifyIpamResourceCidr",
 "ec2:GetIpamAddressHistory",
 "ec2:GetIpamDiscoveredResourceCidrs",
 "ec2:GetIpamDiscoveredAccounts",
 "ec2:GetIpamDiscoveredPublicAddresses"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/ipam.amazonaws.com/AWSServiceRoleForIPAM",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "ipam.amazonaws.com"
 }
 }
 }
 ]
}`

```
