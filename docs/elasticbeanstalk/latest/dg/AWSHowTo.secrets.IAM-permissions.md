# Required IAM permissions for Elastic Beanstalk to access secrets and parameters

You must grant the necessary permissions to your environment’s EC2 instances to fetch the secrets and parameters for AWS Secrets Manager and AWS Systems Manager Parameter
Store. Permissions are provided to the EC2 instances via an EC2 [instance profile role.](iam-instanceprofile.md "iam-instanceprofile.md")

The following sections list the specific permissions that you need to add to an EC2 instance profile, depending on which service you use. Follow the
steps provided in [Update the permissions policy for a
role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _IAM User Guide_ to add these permissions.

###### IAM permissions for the ECS managed Docker platform

The ECS managed Docker platform requires additional IAM permissions to the ones provided in this topic. For more information about all of the
required permissions for your ECS managed Docker platform environment to support Elastic Beanstalk environment variables integration with secrets, see [Execution Role ARN format](create_deploy_docker_v2config.md#create_deploy_docker_v2config_executionRoleArn_format "create_deploy_docker_v2config.md#create_deploy_docker_v2config_executionRoleArn_format").

###### Topics

- [Required IAM permissions for Secrets Manager](#AWSHowTo.secrets.IAM-permissions.secrets-manager "#AWSHowTo.secrets.IAM-permissions.secrets-manager")
- [Required IAM permissions Systems Manager Parameter Store](#AWSHowTo.secrets.IAM-permissions.ssm-paramter-store "#AWSHowTo.secrets.IAM-permissions.ssm-paramter-store")

## Required IAM permissions for Secrets Manager

The following permissions grant access to fetch encrypted secrets from the AWS Secrets Manager store:

- secretsmanager:GetSecretValue
- kms:Decrypt

The permission to decrypt an AWS KMS key is only required if your secret uses a customer managed key instead of the default key. The addition of
your custom key ARN adds the permission to decrypt the customer managed key.

###### Example policy with Secrets Manager and KMS key permissions

JSON

```
`{
 "Version": "`2012-10-17`",
 "Statement": [
 {
 "Effect": "`Allow`",
 "Action": [
 "`secretsmanager:GetSecretValue`",
 "`kms:Decrypt`"
 ],
 "Resource": [
 "`arn:aws:secretsmanager:us-east-1:`111122223333`:secret:my-secret`",
 "`arn:aws:kms:us-east-1:`111122223333`:key/my-key`"
 ]
 }
 ]
}`

```

## Required IAM permissions Systems Manager Parameter Store

The following permissions grant access to fetch encrypted parameters from the AWS Systems Manager Parameter Store:

- ssm:GetParameter
- kms:Decrypt

The permission to decrypt an AWS KMS key is only required for `SecureString` parameter types that uses a customer managed key
instead of a default key. The addition of your custom key ARN adds the permission to decrypt the customer managed key. The regular parameter types that
aren't encrypted, `String` and `StringList`, don’t need an AWS KMS key.

###### Example policy with Systems Manager and AWS KMS key permissions

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "`Allow`",
 "Action": [
 "`ssm:GetParameter`",
 "`kms:Decrypt`"
 ],
 "Resource": [
 "`arn:aws:ssm:us-east-1:`111122223333`:parameter/my-parameter`",
 "`arn:aws:kms:us-east-1:`111122223333`:key/my-key`"
 ]
 }
 ]
}`

```
