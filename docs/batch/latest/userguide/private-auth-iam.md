# Required IAM permissions for private registry authentication

The execution role is required to use this feature. This allows the container agent to pull the container image.
For more information, see [AWS Batch IAM execution role](execution-IAM-role.md "execution-IAM-role.md").

To provide access to the secrets that you create, add the following permissions as an inline policy to the
execution role. For more information, see [Adding and Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

- `secretsmanager:GetSecretValue`
- `kms:Decrypt`—Required only if your key uses a custom KMS key and not the default key.
  The Amazon Resource Name (ARN) for your custom key must be added as a resource.
  The following is an example inline policy that adds the permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret_name`",
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key_id`"
 ]
 }
 ]
}`

```
