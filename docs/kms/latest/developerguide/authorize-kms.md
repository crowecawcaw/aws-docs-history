# Authorizing AWS KMS to manage AWS CloudHSM and Amazon EC2 resources

To support your AWS CloudHSM key stores, AWS KMS needs permission to get information about your
AWS CloudHSM clusters. It also needs permission to create the network infrastructure that connects
your AWS CloudHSM key store to its AWS CloudHSM cluster. To get these permissions, AWS KMS creates the
**AWSServiceRoleForKeyManagementServiceCustomKeyStores** service-linked role in your AWS account. Users who create AWS CloudHSM key stores
must have the `iam:CreateServiceLinkedRole` permission that allows them to create
service-linked roles.

To view details about updates to the **AWSKeyManagementServiceCustomKeyStoresServiceRolePolicy** managed policy, see
[AWS KMS updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

###### Topics

- [About the AWS KMS service-linked role](#about-key-store-slr "#about-key-store-slr")
- [Create the service-linked role](#create-key-store-slr "#create-key-store-slr")
- [Edit the service-linked role description](#edit-key-store-slr "#edit-key-store-slr")
- [Delete the service-linked role](#delete-key-store-slr "#delete-key-store-slr")

## About the AWS KMS service-linked role

A [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md")
is an IAM role that gives one AWS service permission to call other AWS services on
your behalf. It's designed to make it easier for you to use the features of multiple
integrated AWS services without having to create and maintain complex IAM policies. For
more information, see [Using service-linked roles for
AWS KMS](using-service-linked-roles.md "using-service-linked-roles.md").

For AWS CloudHSM key stores, AWS KMS creates the **AWSServiceRoleForKeyManagementServiceCustomKeyStores** service-linked role with the
**AWSKeyManagementServiceCustomKeyStoresServiceRolePolicy** managed
policy. This policy grants the role the following permissions:

- [cloudhsm:Describe\*](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md")
  – detects changes in the AWS CloudHSM cluster that is attached to your custom key
  store.
- [ec2:CreateSecurityGroup](../../../AWSEC2/latest/APIReference/API_CreateSecurityGroup.md "../../../AWSEC2/latest/APIReference/API_CreateSecurityGroup.md") – used when you [connect an AWS CloudHSM key store](connect-keystore.md "connect-keystore.md") to create the security
  group that enables network traffic flow between AWS KMS and your AWS CloudHSM cluster.
- [ec2:AuthorizeSecurityGroupIngress](../../../AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.md "../../../AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.md") – used when you [connect an AWS CloudHSM key store](connect-keystore.md "connect-keystore.md") to allow network access
  from AWS KMS into the VPC that contains your AWS CloudHSM cluster.
- [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md") – used when you [connect an AWS CloudHSM key store](connect-keystore.md "connect-keystore.md") to create the network
  interface used for communication between AWS KMS and the AWS CloudHSM cluster.
- [ec2:RevokeSecurityGroupEgress](../../../AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.md "../../../AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.md") – used when you [connect an AWS CloudHSM key store](connect-keystore.md "connect-keystore.md") to remove all outbound
  rules from the security group that AWS KMS created.
- [ec2:DeleteSecurityGroup](../../../AWSEC2/latest/APIReference/API_DeleteSecurityGroup.md "../../../AWSEC2/latest/APIReference/API_DeleteSecurityGroup.md") – used when you [disconnect an AWS CloudHSM key store](disconnect-keystore.md "disconnect-keystore.md") to delete security
  groups that were created when you connected the AWS CloudHSM key store.
- [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md") – used to monitor changes in the security
  group that AWS KMS created in the VPC that contains your AWS CloudHSM cluster so that AWS KMS can
  provide clear error messages in case of failures.
- [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md") –
  used to monitor changes in the VPC that contains your AWS CloudHSM cluster so that AWS KMS can
  provide clear error messages in case of failures.
- [ec2:DescribeNetworkAcls](../../../AWSEC2/latest/APIReference/API_DescribeNetworkAcls.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkAcls.md") – used to monitor changes in the network ACLs
  for the VPC that contains your AWS CloudHSM cluster so that AWS KMS can provide clear error
  messages in case of failures.
- [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md") – used to monitor changes in the network
  interfaces that AWS KMS created in the VPC that contains your AWS CloudHSM cluster so that AWS KMS
  can provide clear error messages in case of failures.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudhsm:Describe*",
 "ec2:CreateNetworkInterface",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateSecurityGroup",
 "ec2:DescribeSecurityGroups",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:DeleteSecurityGroup",
 "ec2:DescribeVpcs",
 "ec2:DescribeNetworkAcls",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": "*"
 }
 ]
}`

```

Because the **AWSServiceRoleForKeyManagementServiceCustomKeyStores**
service-linked role trusts only `cks.kms.amazonaws.com`, only AWS KMS can assume
this service-linked role. This role is limited to the operations that AWS KMS needs to view
your AWS CloudHSM clusters and to connect an AWS CloudHSM key store to its associated AWS CloudHSM cluster. It
does not give AWS KMS any additional permissions. For example, AWS KMS does not have permission
to create, manage, or delete your AWS CloudHSM clusters, HSMs, or backups.

**Regions**

Like the AWS CloudHSM key stores feature, the **AWSServiceRoleForKeyManagementServiceCustomKeyStores** role is supported in all
AWS Regions where AWS KMS and AWS CloudHSM are available. For a list of AWS Regions that each service supports, see [AWS Key Management Service Endpoints and Quotas](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") and [AWS CloudHSM endpoints and quotas](../../../general/latest/gr/cloudhsm.md "../../../general/latest/gr/cloudhsm.md") in the _Amazon Web Services General Reference_.

For more information about how AWS services use service-linked roles, see [Using service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in
the IAM User Guide.

## Create the service-linked role

AWS KMS automatically creates the **AWSServiceRoleForKeyManagementServiceCustomKeyStores** service-linked role in your AWS account
when you create an AWS CloudHSM key store, if the role does not already exist. You cannot create or
re-create this service-linked role directly.

## Edit the service-linked role description

You cannot edit the role name or the policy statements in the **AWSServiceRoleForKeyManagementServiceCustomKeyStores**
service-linked role, but you can edit role description. For instructions, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete the service-linked role

AWS KMS does not delete the **AWSServiceRoleForKeyManagementServiceCustomKeyStores** service-linked role from your AWS account
even if you have [deleted all of your AWS CloudHSM key
stores](delete-keystore.md "delete-keystore.md"). Although there is currently no procedure for deleting the **AWSServiceRoleForKeyManagementServiceCustomKeyStores**
service-linked role, AWS KMS does not assume this role or use its permissions unless you have
active AWS CloudHSM key stores.
