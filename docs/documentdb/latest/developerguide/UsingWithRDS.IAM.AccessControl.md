# Managing access permissions to your Amazon DocumentDB resources

Every AWS resource is owned by an AWS account, and permissions to create or access the resources are governed by permissions policies.
An account administrator can attach permissions policies to IAM identities (that is, users, groups, and roles), and some services (such as AWS Lambda) also support attaching permissions policies to resources.

###### Note

An _account administrator_ (or administrator user) is a user with administrator permissions. For more information, see [IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

###### Topics

- [Amazon DocumentDB Resources and operations](#CreatingIAMPolicies-RDS "#CreatingIAMPolicies-RDS")
- [Understanding resource ownership](#UsingWithRDS.IAM.AccessControl.ResourceOwner "#UsingWithRDS.IAM.AccessControl.ResourceOwner")
- [Managing access to resources](#UsingWithRDS.IAM.AccessControl.ManagingAccess "#UsingWithRDS.IAM.AccessControl.ManagingAccess")
- [Specifying policy elements: actions, effects, resources, and principals](#SpecifyingIAMPolicyActions-RDS "#SpecifyingIAMPolicyActions-RDS")
- [Specifying conditions in a policy](#SpecifyingIAMPolicyConditions-RDS "#SpecifyingIAMPolicyConditions-RDS")

## Amazon DocumentDB Resources and operations

In Amazon DocumentDB, the primary resource is a _cluster_. Amazon DocumentDB supports other resources that can be used with the primary resource such as _instances_, _parameter groups_, and _event subscriptions_. These resources are referred to as _subresources_.

These resources and subresources have unique Amazon Resource Names (ARNs) associated with them, as shown in the following table.

| **Resource Type**       | **ARN Format**                                                                |
| ----------------------- | ----------------------------------------------------------------------------- |
| Cluster                 | `arn:aws:rds:`region`:`account-id`:cluster:`db-cluster-name``                 |
| Cluster parameter group | `arn:aws:rds:`region`:`account-id`:cluster-pg:`cluster-parameter-group-name`` |
| Cluster snapshot        | `arn:aws:rds:`region`:`account-id`:cluster-snapshot:`cluster-snapshot-name``  |
| Instance                | `arn:aws:rds:`region`:`account-id`:db:`db-instance-name``                     |
| Security group          | `arn:aws:rds:`region`:`account-id`:secgrp:`security-group-name``              |
| Subnet group            | `arn:aws:rds:`region`:`account-id`:subgrp:`subnet-group-name``                |

Amazon DocumentDB provides a set of operations to work with the Amazon DocumentDB resources. For a list of available operations, see [Actions](API_Operations.md "API_Operations.md").

## Understanding resource ownership

A _resource owner_ is the AWS account that created a resource. That is, the resource owner is the AWS account of the _principal entity_ (the root account, an IAM user, or an IAM role) that authenticates the request that creates the resource. The following examples illustrate how this works:

- If you use the root account credentials of your AWS account to create an Amazon DocumentDB resource, such as an instance, your AWS account is the owner of the Amazon DocumentDB resource.
- If you create an IAM user in your AWS account and grant permissions to create Amazon DocumentDB resources to that user, the user can create Amazon DocumentDB resources. However, your AWS account, to which the user belongs, owns the Amazon DocumentDB resources.
- If you create an IAM role in your AWS account with permissions to create Amazon DocumentDB resources, anyone who can assume the role can create Amazon DocumentDB resources. Your AWS account, to which the role belongs, owns the Amazon DocumentDB resources.

## Managing access to resources

A _permissions policy_ describes who has access to what. The following section explains the available options for creating permissions policies.

###### Note

This section discusses using IAM in the context of Amazon DocumentDB. It doesn't provide detailed information about the IAM service. For complete IAM documentation, see [What Is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the _IAM User Guide_. For information about IAM policy syntax and descriptions, see [AWSIAM Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

Policies that are attached to an IAM identity are referred to as _identity-based_ policies (IAM policies). Policies that are attached to a resource are referred to as _resource-based_ policies. Amazon DocumentDB supports only identity-based policies (IAM policies).

###### Topics

- [Identity-based policies (IAM policies)](#UsingWithRDS.IAM.AccessControl.ManagingAccess.IdentityBased "#UsingWithRDS.IAM.AccessControl.ManagingAccess.IdentityBased")
- [Resource-based policies](#UsingWithRDS.IAM.AccessControl.ManagingAccess.ResourceBased "#UsingWithRDS.IAM.AccessControl.ManagingAccess.ResourceBased")

### Identity-based policies (IAM policies)

You can attach policies to IAM identities. For example, you can do the following:

- **Attach a permissions policy to a user or a group in your account** – An account administrator can use a permissions policy that is associated with a particular user to grant permissions for that user to create an Amazon DocumentDB resource, such
  as an instance.
- **Attach a permissions policy to a role (grant cross-account permissions)** – You can attach an identity-based permissions policy to an IAM role to grant cross-account permissions.
  For example, an administrator can create a role to grant cross-account permissions to another AWS account or an AWS service as follows:
  1.  Account A administrator creates an IAM role and attaches a permissions policy to the role that grants permissions on resources in Account A.
  2.  Account A administrator attaches a trust policy to the role identifying Account B as the principal who can assume the role.
  3.  Account B administrator can then delegate permissions to assume the role to any users in Account B. Doing this allows the users in Account B to create or access resources in Account A. The principal in the trust policy can also be an AWS service principal if you want to grant permissions to an AWS service to assume the role.
      For more information about using IAM to delegate permissions, see [Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _IAM User Guide_.

The following is an example policy that allows the user with the ID `123456789012` to create instances for your AWS account. The new instance must use an option group and a parameter group that starts with `default`, and it must use the `default`
subnet group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateDBInstanceOnly",
 "Effect": "Allow",
 "Action": [
 "rds:CreateDBInstance"
 ],
 "Resource": [
 "arn:aws:rds:*:123456789012:db:test*",
 "arn:aws:rds:*:123456789012:pg:cluster-pg:default*",
 "arn:aws:rds:*:123456789012:subgrp:default"
 ]
 }
 ]
}`

```

For more information about using identity-based policies with Amazon DocumentDB, see [Using identity-based policies (IAM policies) for Amazon DocumentDB](UsingWithRDS.IAM.AccessControl.md "UsingWithRDS.IAM.AccessControl.md"). For more information about users, groups, roles, and permissions, see [Identities (Users, Groups, and Roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

### Resource-based policies

Other services, such as Amazon Simple Storage Service (Amazon S3), also support resource-based permissions policies. For example, you can attach a policy to an Amazon S3 bucket to manage access permissions to that bucket. Amazon DocumentDB doesn't support resource-based policies.

## Specifying policy elements: actions, effects, resources, and principals

For each Amazon DocumentDB resource (see [Amazon DocumentDB Resources and operations](#CreatingIAMPolicies-RDS "#CreatingIAMPolicies-RDS")), the service defines a set of API operations. For more information, see [Actions](../../../redshift/latest/APIReference/API_Operations.md "../../../redshift/latest/APIReference/API_Operations.md"). To grant permissions for these API operations, Amazon DocumentDB defines a set of actions that you can specify in a policy. Performing an API operation can require permissions for more than one action.

The following are the basic policy elements:

- **Resource** – In a policy, you use an Amazon Resource Name (ARN) to identify the resource to which the
  policy applies.
- **Action** – You use action keywords to identify resource operations that you want to allow or deny. For example, the `rds:DescribeDBInstances` permission allows the user to perform the `DescribeDBInstances` operation.
- **Effect** – You specify the effect when the user requests the specific action—this can be either allow or deny. If you don't explicitly grant access to (allow) a resource, access is implicitly denied. You can also explicitly deny access to a resource, which you might do to make sure that a user cannot access it, even if a different policy grants access.
- **Principal** – In identity-based policies (IAM policies), the user that the policy is attached to is the implicit principal. For resource-based policies, you specify the user, account, service, or other entity that you want to receive permissions (applies to resource-based policies only). Amazon DocumentDB doesn't support resource-based policies.

To learn more about IAM policy syntax and descriptions, see [AWS IAM Policy
Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

For a table showing all of the Amazon DocumentDB API actions and the resources that they apply to, see [Amazon DocumentDB API permissions: actions, resources, and conditions reference](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md").

## Specifying conditions in a policy

When you grant permissions, you can use the IAM policy language to specify the conditions when a policy should take effect. For example, you might want a policy to be applied only after a specific date. For more information about specifying conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition") in the _IAM User Guide_.

To express conditions, you use predefined condition keys. Amazon DocumentDB has no service-specific context keys that can be used in an IAM policy. For a list of global condition context keys that are available to all services, see [Available Keys for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.
