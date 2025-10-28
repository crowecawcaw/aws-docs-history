# Prerequisites: IAM Role and Amazon S3 Access

Loading data from an Amazon Simple Storage Service (Amazon S3) bucket requires an AWS Identity and Access Management (IAM) role that has
access to the bucket. Amazon Neptune assumes this role to load the data.

###### Note

You can load encrypted data from Amazon S3 if it was encrypted using the Amazon S3
`SSE-S3` mode. In that case, Neptune is able to impersonate your
credentials and issue `s3:getObject` calls on your behalf.

You can also load encrypted data from Amazon S3 that was encrypted using the
`SSE-KMS` mode, as long as your IAM role includes the necessary
permissions to access AWS KMS. Without proper AWS KMS permissions, the bulk
load operation fails and returns a `LOAD_FAILED` response.

Neptune does not currently support loading Amazon S3 data encrypted using the
`SSE-C` mode.

The following sections show how to use a managed IAM policy to create an IAM
role for accessing Amazon S3 resources, and then attach the role to your Neptune cluster.

###### Topics

- [Creating an IAM role to allow
  Amazon Neptune to access Amazon S3 resources](bulk-load-tutorial-IAM-CreateRole.md "bulk-load-tutorial-IAM-CreateRole.md")
- [Adding the IAM Role to an
  Amazon Neptune Cluster](bulk-load-tutorial-IAM-add-role-cluster.md "bulk-load-tutorial-IAM-add-role-cluster.md")
- [Creating the Amazon S3 VPC Endpoint](bulk-load-tutorial-vpc.md "bulk-load-tutorial-vpc.md")
- [Chaining IAM roles in Amazon Neptune](bulk-load-tutorial-chain-roles.md "bulk-load-tutorial-chain-roles.md")

###### Note

These instructions require that you have access to the IAM console and permissions to
manage IAM roles and policies. For more information, see [Permissions for Working in the AWS Management Console](../../../IAM/latest/UserGuide/access_permissions-required.md#Credentials-Permissions-overview-console "../../../IAM/latest/UserGuide/access_permissions-required.md#Credentials-Permissions-overview-console") in the
_IAM User Guide_.

The Amazon Neptune console requires the user to have the following IAM permissions to
attach the role to the Neptune cluster:

```
iam:GetAccountSummary on resource: *
iam:ListAccountAliases on resource: *
iam:PassRole on resource: * with iam:PassedToService restricted to rds.amazonaws.com
```
