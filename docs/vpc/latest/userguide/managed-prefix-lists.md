# Consolidate and manage network CIDR blocks with managed prefix lists

A managed prefix list is a set of one or more CIDR blocks. You can use prefix lists to make it
easier to configure and maintain your security groups and route tables. You can create a
prefix list from the IP addresses that you frequently use, and reference them as a set in
security group rules and routes instead of referencing them individually. For example, you
can consolidate security group rules with different CIDR blocks but the same port and protocol
into a single rule that uses a prefix list. If you scale your network and need to allow traffic
from another CIDR block, you can update the relevant prefix list and all security groups that
use the prefix list are updated. You can also use managed prefix lists with other AWS accounts using Resource Access Manager (RAM).

There are two types of prefix lists:

- **Customer-managed prefix lists** — Sets of
  IP address ranges that you define and manage. You can share your prefix list
  with other AWS accounts, enabling those accounts to reference the prefix list in
  their own resources.
- **AWS-managed prefix lists** — Sets of IP
  address ranges for AWS services. You cannot create, modify, share, or delete an
  AWS-managed prefix list.

###### Contents

- [Prefix lists concepts and rules](#managed-prefix-lists-concepts "#managed-prefix-lists-concepts")
- [Identity and access management for prefix lists](#managed-prefix-lists-iam "#managed-prefix-lists-iam")
- [Customer-managed prefix lists](working-with-managed-prefix-lists.md "working-with-managed-prefix-lists.md")
- [AWS-managed prefix lists](working-with-aws-managed-prefix-lists.md "working-with-aws-managed-prefix-lists.md")
- [Optimize AWS infrastructure management with prefix lists](managed-prefix-lists-referencing.md "managed-prefix-lists-referencing.md")

## Prefix lists concepts and rules

A prefix list consists of _entries_. Each entry consists of a CIDR
block and, optionally, a description for the CIDR block.

###### Customer-managed prefix lists

The following rules apply to customer-managed prefix lists:

- A prefix list supports a single type of IP addressing only (IPv4 or IPv6). You
  cannot combine IPv4 and IPv6 CIDR blocks in a single prefix list.
- A prefix list applies only to the Region where you created it.
- When you create a prefix list, you must specify the maximum number of entries
  that the prefix list can support.
- When you reference a prefix list in a resource, the maximum number of entries for
  the prefix lists counts against the quota for the number of entries for the resource.
  For example, if you create a prefix list with 20 maximum entries and you reference
  that prefix list in a security group rule, this counts as 20 security group rules.
- When you reference a prefix list in a route table, route priority rules apply.
  For more information, see [Route priority for prefix
  lists](route-tables-priority.md#route-priority-managed-prefix-list "route-tables-priority.md#route-priority-managed-prefix-list").
- You can modify a prefix list. When you add or remove entries, we create a new version of
  the prefix list. Resources that reference the prefix always use the current (latest)
  version. You can restore the entries from a previous version of the prefix list, which
  also creates a new version.
- There are quotas related to prefix lists. For more information, see [Customer-managed prefix lists](amazon-vpc-limits.md#vpc-quotas-managed-prefix-lists "amazon-vpc-limits.md#vpc-quotas-managed-prefix-lists").
- Customer-managed prefix lists are available in all commercial [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") (including GovCloud (US) and China Regions).

###### AWS-managed prefix lists

The following rules apply to AWS-managed prefix lists:

- You cannot create, modify, share, or delete an AWS-managed prefix list.
- Different AWS-managed prefix lists have a different weight when you use them. For more information, see [AWS-managed prefix list weight](working-with-aws-managed-prefix-lists.md#aws-managed-prefix-list-weights "working-with-aws-managed-prefix-lists.md#aws-managed-prefix-list-weights").
- You cannot view the version number of an AWS-managed prefix list.

## Identity and access management for prefix lists

By default, users do not have permission to create, view, modify, or delete prefix lists. You can create an IAM policy and attach it to a role that allows users to work with prefix lists.

To see a list of Amazon VPC actions and the resources and condition keys that you can use
in an IAM policy, see [Actions,
resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md") in the _Service Authorization Reference_.

The following example policy allows users to view and work with prefix list
`pl-123456abcde123456` only. Users cannot create or delete prefix
lists.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:GetManagedPrefixListAssociations",
 "ec2:GetManagedPrefixListEntries",
 "ec2:ModifyManagedPrefixList",
 "ec2:RestoreManagedPrefixListVersion"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`123456789012`:prefix-list/`pl-123456abcde123456`"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeManagedPrefixLists",
 "Resource": "*"
 }
 ]
}`

```

For more information about working with IAM in Amazon VPC, see [Identity and access management for Amazon VPC](security-iam.md "security-iam.md").
