# Service-linked role permissions for WorkSpaces Secure Browser

WorkSpaces Secure Browser uses the service-linked role named `AWSServiceRoleForAmazonWorkSpacesWeb` –
WorkSpaces Secure Browser uses this service-linked role to access Amazon EC2 resources of customer accounts for streaming instances and CloudWatch metrics.

The `AWSServiceRoleForAmazonWorkSpacesWeb` service-linked role trusts the following services to assume the
role:

- `workspaces-web.amazonaws.com`
  The role permissions policy named `AmazonWorkSpacesWebServiceRolePolicy` allows WorkSpaces Secure Browser to
  complete the following actions on the specified
  resources. For more
  information, see [AWS managed
  policy: AmazonWorkSpacesWebServiceRolePolicy](security-iam-awsmanpol-AmazonWorkSpacesWebServiceRolePolicy.md "security-iam-awsmanpol-AmazonWorkSpacesWebServiceRolePolicy.md").

- Action: `ec2:DescribeVpcs` on
  `all AWS resources`
- Action: `ec2:DescribeSubnets` on `all AWS resources`
- Action: `ec2:DescribeAvailabilityZones` on
  `all AWS resources`
- Action: `ec2:CreateNetworkInterface`
  with
  `aws:RequestTag/WorkSpacesWebManaged: true` on subnet and security group
  resources
- Action: `ec2:DescribeNetworkInterfaces` on
  `all AWS resources`
- Action: `ec2:DeleteNetworkInterface` on

network interfaces with `aws:ResourceTag/WorkSpacesWebManaged:
 true`

- Action: `ec2:DescribeSubnets` on `all AWS resources`
- Action: `ec2:AssociateAddress` on
  `all AWS resources`
- Action: `ec2:DisassociateAddress` on
  `all AWS resources`
- Action: `ec2:DescribeRouteTables` on
  `all AWS resources`
- Action: `ec2:DescribeSecurityGroups` on
  `all AWS resources`
- Action: `ec2:DescribeVpcEndpoints` on
  `all AWS resources`
- Action: `ec2:CreateTags` on `ec2:CreateNetworkInterface`
  Operation with `aws:TagKeys: ["WorkSpacesWebManaged"]`
- Action: `cloudwatch:PutMetricData` on
  `all AWS resources`
- Action: `kinesis:PutRecord` on Kinesis data streams with names that start
  with `amazon-workspaces-web-`
- Action: `kinesis:PutRecords` on Kinesis data streams with names that start
  with `amazon-workspaces-web-`
- Action: `kinesis:DescribeStreamSummary` on Kinesis data streams with names
  that start with `amazon-workspaces-web-`
  You must configure permissions to allow an IAM entity (such as a user, group, or role)
  to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.
