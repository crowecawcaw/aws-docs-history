# Authorizing AWS KMS to synchronize multi-Region

keys

To support [multi-Region keys](multi-region-keys-auth.md "multi-region-keys-auth.md"), AWS KMS needs
permission to synchronize the [shared properties](multi-region-keys-overview.md#mrk-sync-properties "multi-region-keys-overview.md#mrk-sync-properties") of
a multi-Region primary key with its replica keys. To get these permissions, AWS KMS creates the
**AWSServiceRoleForKeyManagementServiceMultiRegionKeys** service-linked role in your AWS account. Users who create multi-Region keys
must have the `iam:CreateServiceLinkedRole` permission that allows them to create
service-linked roles.

You can view the [SynchronizeMultiRegionKey](ct-synchronize-multi-region-key.md "ct-synchronize-multi-region-key.md") CloudTrail event that
records AWS KMS synchronizing shared properties in your AWS CloudTrail logs.

To view details about updates to the **AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy** managed policy, see
[AWS KMS updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

###### Topics

- [About the service-linked role for multi-Region
  keys](#about-multi-region-slr "#about-multi-region-slr")
- [Create the service-linked role](#create-mrk-slr "#create-mrk-slr")
- [Edit the service-linked role description](#edit-mrk-slr "#edit-mrk-slr")
- [Delete the service-linked role](#delete-mrk-slr "#delete-mrk-slr")

## About the service-linked role for multi-Region

keys

A [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md")
is an IAM role that gives one AWS service permission to call other AWS services on
your behalf. It's designed to make it easier for you to use the features of multiple
integrated AWS services without having to create and maintain complex IAM
policies.

For multi-Region keys, AWS KMS creates the **AWSServiceRoleForKeyManagementServiceMultiRegionKeys** service-linked role with the
**AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy** managed
policy. This policy gives the role the `kms:SynchronizeMultiRegionKey`
permission, which allows it to synchronize the shared properties of multi-Region
keys.

Because the **AWSServiceRoleForKeyManagementServiceMultiRegionKeys** service-linked role trusts only
`mrk.kms.amazonaws.com`, only AWS KMS can assume this service-linked role. This
role is limited to the operations that AWS KMS needs to synchronize multi-Region shared
properties. It does not give AWS KMS any additional permissions. For example, AWS KMS does not
have permission to create, replicate, or delete any KMS keys.

For more information about how AWS services use service-linked roles, see [Using Service-Linked Roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in
the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "KMSSynchronizeMultiRegionKey",
 "Effect" : "Allow",
 "Action" : [
 "kms:SynchronizeMultiRegionKey"
 ],
 "Resource" : "*"
 }
 ]
}`

```

## Create the service-linked role

AWS KMS automatically creates the **AWSServiceRoleForKeyManagementServiceMultiRegionKeys** service-linked role in your AWS account when
you create a multi-Region key, if the role does not already exist. You cannot create or
re-create this service-linked role directly.

## Edit the service-linked role description

You cannot edit the role name or the policy statements in the **AWSServiceRoleForKeyManagementServiceMultiRegionKeys** service-linked
role, but you can edit the role description. For instructions, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete the service-linked role

AWS KMS does not delete the **AWSServiceRoleForKeyManagementServiceMultiRegionKeys** service-linked role from your AWS account and you
cannot delete it. However, AWS KMS does not assume the **AWSServiceRoleForKeyManagementServiceMultiRegionKeys** role or use any of its
permissions unless you have multi-Region keys in your AWS account and Region.
