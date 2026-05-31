# Password management with Amazon DocumentDB and AWS Secrets Manager

Amazon DocumentDB integrates with Secrets Manager to manage primary user passwords for your clusters.

###### Topics

- [Limitations for Secrets Manager integration with Amazon DocumentDB](#asm-limitations "#asm-limitations")
- [Overview of managing primary user passwords with AWS Secrets Manager](#asm-overview "#asm-overview")
- [Enforcing Amazon DocumentDB management of the primary user password in AWS Secrets Manager](#asm-enforce "#asm-enforce")
- [Managing the primary user password for a cluster with Secrets Manager](#asm-managing-pw "#asm-managing-pw")

## Limitations for Secrets Manager integration with Amazon DocumentDB

Managing primary user passwords with Secrets Manager isn't supported for the following features:

- Clusters that are part of an Amazon DocumentDB global database
- Amazon DocumentDB cross-Region read replicas

## Overview of managing primary user passwords with AWS Secrets Manager

With AWS Secrets Manager, you can replace hard-coded credentials in your code, including database passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
For more information about Secrets Manager, see [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

When you store database secrets in Secrets Manager, your AWS account incurs charges. For information about pricing, see [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/").

You can specify that Amazon DocumentDB manages the primary user password in Secrets Manager for an Amazon DocumentDB cluster when you perform one of the following operations:

- Create the cluster
- Modify the cluster

When you specify that Amazon DocumentDB manages the primary user password in Secrets Manager, Amazon DocumentDB generates the password and stores it in Secrets Manager.
You can interact directly with the secret to retrieve the credentials for the primary user.
You can also specify a customer managed key to encrypt the secret, or use the KMS key that is provided by Secrets Manager.

Amazon DocumentDB manages the settings for the secret and rotates the secret every seven days by default.
You can modify some of the settings, such as the rotation schedule.
If you delete a cluster that manages a secret in Secrets Manager, the secret and its associated metadata are also deleted.

To connect to a cluster with the credentials in a secret, you can retrieve the secret from Secrets Manager.
For more information, see [Get secrets from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") and
[Connect to a SQL database using JDBC with credentials in an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/retrieving-secrets_jdbc.md "../../../secretsmanager/latest/userguide/retrieving-secrets_jdbc.md") in the _AWS Secrets Manager User Guide_.

## Enforcing Amazon DocumentDB management of the primary user password in AWS Secrets Manager

You can use IAM condition keys to enforce Amazon DocumentDB management of the primary user password in AWS Secrets Manager.
The following policy doesn't allow users to create or restore instances or clusters unless the primary user password is managed by Amazon DocumentDB in Secrets Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "rds:CreateDBCluster"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "rds:ManageMasterUserPassword": false
 }
 }
 }
 ]
}`

```

## Managing the primary user password for a cluster with Secrets Manager

You can configure Amazon DocumentDB management of the primary user password in Secrets Manager when you perform the following actions:

- [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md")
- [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md")

You can use the Amazon DocumentDB console or the AWS CLI to perform these actions.
