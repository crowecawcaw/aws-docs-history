Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing Amazon Redshift admin passwords

using AWS Secrets Manager

Amazon Redshift can integrate with AWS Secrets Manager to generate and manage your admin credentials
inside an encrypted secret. With AWS Secrets Manager, you can replace your admin passwords with an API
call to programmatically retrieve the secret when it’s needed. Using secrets instead of
hard-coded credentials reduces the risk of those credentials being exposed or compromised.
For more information about AWS Secrets Manager, see the [_AWS Secrets Manager User Guide_](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

You can specify that Amazon Redshift manages your admin password using AWS Secrets Manager when you perform
one of the following operations:

- Create a provisioned cluster or serverless namespace
- Edit, update, or modify the admin credentials of a provisioned cluster or
  serverless namespace
- Restore a cluster or serverless namespace from a snapshot
  When you specify that Amazon Redshift manages the admin password in AWS Secrets Manager, Amazon Redshift generates
  the password and stores it in Secrets Manager. You can access the secret directly in AWS Secrets Manager to
  retrieve the credentials for the admin user. Optionally, you can specify a customer managed
  key to encrypt the secret if you need to access the secret from another AWS account. You
  can also use the KMS key that AWS Secrets Manager provides.

Amazon Redshift manages the settings for the secret and rotates the secret every 30 days by
default. You can manually rotate the secret at any time. If you delete a provisioned cluster
or serverless namespace that manages a secret in AWS Secrets Manager, the secret and its associated
metadata are also deleted.

To connect to a cluster or serverless namespace with secret-managed credentials, you can
retrieve the secret from AWS Secrets Manager using the Secrets Manager console or the
`GetSecretValue` Secrets Manager API call. For more information, see [Retrieve secrets from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") and [Connect to a SQL
database with credentials in an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/retrieving-secrets_jdbc.md "../../../secretsmanager/latest/userguide/retrieving-secrets_jdbc.md") in the
_AWS Secrets Manager User Guide_.

## Permissions required

for AWS Secrets Manager integration

Users must have the required permissions to perform operations related to AWS Secrets Manager
integration. Create IAM policies that grant permissions to perform specific API
operations on the specified resources they need. Then attach those policies to the IAM
permission sets or roles that require those permissions. For more information, see [Identity and access management in
Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

The user who specifies that Amazon Redshift manages the admin password in AWS Secrets Manager must have
permissions to perform the following operations:

- `secretsmanager:CreateSecret`
- `secretsmanager:RotateSecret`
- `secretsmanager:DescribeSecret`
- `secretsmanager:UpdateSecret`
- `secretsmanager:DeleteSecret`
- `secretsmanager:GetRandomPassword`
- `secretsmanager:TagResource`

If the user wants to pass a KMS key in the `MasterPasswordSecretKmsKeyId`
parameter for provisioned clusters, or the `AdminPasswordSecretKmsKeyId`
parameter for serverless namespaces, they require the following permissions in addition
to the permissions listed above.

- `kms:Decrypt`
- `kms:GenerateDataKey`
- `kms:CreateGrant`
- `kms:RetireGrant`

## Admin

password secret rotation

By default, Amazon Redshift automatically rotates your secret every 30 days to ensure your
credentials don’t stay the same for prolonged periods. When Amazon Redshift rotates an admin
password secret, AWS Secrets Manager updates the existing secret to contain a new admin password.
Amazon Redshift changes the admin password for the cluster to match the password in the updated
secret.

You can rotate a secret immediately instead of waiting for a scheduled rotation by
using AWS Secrets Manager. For more information on rotating secrets, see [Rotate AWS Secrets Manager
secrets](../../../secretsmanager/latest/userguide/retrieving-secrets_jdbc.md "../../../secretsmanager/latest/userguide/retrieving-secrets_jdbc.md") in the _AWS Secrets Manager User Guide_.

## Considerations

using AWS Secrets Manager with Amazon Redshift

When using AWS Secrets Manager to manage your provisioned cluster or serverless namespace’s
admin credentials, consider the following:

- When you pause a cluster whose admin credentials are managed by AWS Secrets Manager,
  your cluster's secret won't be deleted and you'll continue to be billed for the
  secret. Secrets are only deleted when you delete the cluster.
- If your cluster is paused when Amazon Redshift attempts to rotate its attached
  secret, the rotation will fail. In this case, Amazon Redshift stops auto-rotation and
  won’t try to rotate it again, even after you resume the cluster. You must
  restart the auto-rotation schedule using the
  `secretsmanager:RotateSecret` API call to continue having
  AWS Secrets Manager automatically rotate your secret.
- If your serverless namespace doesn’t have a workgroup associated when
  Amazon Redshift attempts to rotate its attached secret, the rotation will fail and
  won’t try to rotate it again, even after you attach a workgroup. You must
  restart the auto-rotation schedule using the
  `secretsmanager:RotateSecret` API call to continue having
  AWS Secrets Manager automatically rotate your secret.
