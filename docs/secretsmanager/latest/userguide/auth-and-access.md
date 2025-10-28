# Authentication and access control for AWS Secrets Manager

Secrets Manager uses [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") to secure access to secrets. IAM provides authentication and
access control. _Authentication_ verifies the identity of individuals'
requests. Secrets Manager uses a sign-in process with passwords, access keys, and multi-factor
authentication (MFA) tokens to verify the identity of the users. See [Signing in to AWS](../../../IAM/latest/UserGuide/console.md "../../../IAM/latest/UserGuide/console.md"). _Access
control_ ensures that only approved individuals can perform operations on AWS
resources such as secrets. Secrets Manager uses policies to define who has access to which resources, and
which actions the identity can take on those resources. See [Policies and permissions in
IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md").

###### Topics

- [Permissions reference for AWS Secrets Manager](#reference_iam-permissions "#reference_iam-permissions")
- [Secrets Manager administrator permissions](#auth-and-access_admin "#auth-and-access_admin")
- [Permissions to access secrets](#auth-and-access_secrets "#auth-and-access_secrets")
- [Permissions for Lambda rotation functions](#auth-and-access_rotate "#auth-and-access_rotate")
- [Permissions for encryption keys](#auth-and-access_encrypt "#auth-and-access_encrypt")
- [Permissions for replication](#auth-and-access_replication "#auth-and-access_replication")
- [Identity-based policies](auth-and-access_iam-policies.md "auth-and-access_iam-policies.md")
- [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md")
- [Control access to secrets using attribute-based access control (ABAC)](auth-and-access-abac.md "auth-and-access-abac.md")
- [AWS managed policy for AWS Secrets Manager](reference_available-policies.md "reference_available-policies.md")
- [Determine who has permissions to
  your AWS Secrets Manager secrets](determine-acccess_examine-iam-policies.md "determine-acccess_examine-iam-policies.md")
- [Access AWS Secrets Manager secrets from a different
  account](auth-and-access_examples_cross.md "auth-and-access_examples_cross.md")
- [Access secrets from an on-premises
  environment](auth-and-access-on-prem.md "auth-and-access-on-prem.md")

## Permissions reference for AWS Secrets Manager

The permissions reference for Secrets Manager is available at [Actions, resources, and condition keys for AWS Secrets Manager](../../../service-authorization/latest/reference/list_awssecretsmanager.md "../../../service-authorization/latest/reference/list_awssecretsmanager.md") in the _Service Authorization Reference_.

## Secrets Manager administrator permissions

To grant Secrets Manager administrator permissions, follow the instructions at [Adding and removing
IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md"), and attach the following policies:

- [SecretsManagerReadWrite](reference_available-policies.md#security-iam-awsmanpol-SecretsManagerReadWrite "reference_available-policies.md#security-iam-awsmanpol-SecretsManagerReadWrite")
- [IAMFullAccess](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies")

We recommend you do not grant administrator permissions to end users. While this allows
your users to create and manage their secrets, the permission required to enable rotation
(IAMFullAccess) grants significant permissions that are not appropriate
for end users.

## Permissions to access secrets

By using IAM permission policies, you control which users or services have access to
your secrets. A _permissions policy_ describes who can perform which
actions on which resources. You can:

- [Identity-based policies](auth-and-access_iam-policies.md "auth-and-access_iam-policies.md")
- [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md")

## Permissions for Lambda rotation functions

Secrets Manager uses AWS Lambda functions to [rotate secrets](rotating-secrets.md "rotating-secrets.md"). The
Lambda function must have access to the secret as well as the database or service that the
secret contains credentials for. See [Permissions for
rotation](rotating-secrets-required-permissions-function.md "rotating-secrets-required-permissions-function.md").

## Permissions for encryption keys

Secrets Manager uses AWS Key Management Service (AWS KMS) keys to [encrypt secrets](security-encryption.md "security-encryption.md"). The
AWS managed key `aws/secretsmanager` automatically has the correct permissions.
If you use a different KMS key, Secrets Manager needs permissions to that key. See [Permissions for the KMS key](security-encryption.md#security-encryption-authz "security-encryption.md#security-encryption-authz").

## Permissions for replication

By using IAM permission policies, you control which users or services can replicate your
secrets to other Regions. See [Prevent AWS Secrets Manager replication](replicate-secrets-permissions.md "replicate-secrets-permissions.md").
