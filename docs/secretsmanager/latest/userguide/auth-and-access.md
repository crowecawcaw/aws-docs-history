

# Authentication and access control for AWS Secrets Manager
<a name="auth-and-access"></a>

Secrets Manager uses [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) to secure access to secrets. IAM provides authentication and access control. *Authentication* verifies the identity of individuals' requests. Secrets Manager uses a sign-in process with passwords, access keys, and multi-factor authentication (MFA) tokens to verify the identity of the users. See [Signing in to AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/console.html). *Access control* ensures that only approved individuals can perform operations on AWS resources such as secrets. Secrets Manager uses policies to define who has access to which resources, and which actions the identity can take on those resources. See [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

**Topics**
+ [Permissions reference for AWS Secrets Manager](#reference_iam-permissions)
+ [Secrets Manager administrator permissions](#auth-and-access_admin)
+ [Permissions to access secrets](#auth-and-access_secrets)
+ [Permissions for Lambda rotation functions](#auth-and-access_rotate)
+ [Permissions for encryption keys](#auth-and-access_encrypt)
+ [Permissions for replication](#auth-and-access_replication)
+ [Identity-based policies](auth-and-access_iam-policies.md)
+ [Resource-based policies](auth-and-access_resource-policies.md)
+ [Control access to secrets using attribute-based access control (ABAC)](auth-and-access-abac.md)
+ [AWS managed policy for AWS Secrets Manager](reference_available-policies.md)
+ [Determine who has permissions to your AWS Secrets Manager secrets](determine-acccess_examine-iam-policies.md)
+ [Access AWS Secrets Manager secrets from a different account](auth-and-access_examples_cross.md)
+ [Access secrets from an on-premises environment](auth-and-access-on-prem.md)

## Permissions reference for AWS Secrets Manager
<a name="reference_iam-permissions"></a>

The permissions reference for Secrets Manager is available at [Actions, resources, and condition keys for AWS Secrets Manager](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecretsmanager.html) in the *Service Authorization Reference*.

## Secrets Manager administrator permissions
<a name="auth-and-access_admin"></a>

To grant Secrets Manager administrator permissions, follow the instructions at [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html), and attach the following policies:
+ [SecretsManagerReadWrite](reference_available-policies.md#security-iam-awsmanpol-SecretsManagerReadWrite)
+ [IAMFullAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies)

We recommend you do not grant administrator permissions to end users. While this allows your users to create and manage their secrets, the permission required to enable rotation (IAMFullAccess) grants significant permissions that are not appropriate for end users.

## Permissions to access secrets
<a name="auth-and-access_secrets"></a>

By using IAM permission policies, you control which users or services have access to your secrets. A *permissions policy* describes who can perform which actions on which resources. You can: 
+ [Identity-based policies](auth-and-access_iam-policies.md)
+ [Resource-based policies](auth-and-access_resource-policies.md)

## Permissions for Lambda rotation functions
<a name="auth-and-access_rotate"></a>

Secrets Manager uses AWS Lambda functions to [rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html). The Lambda function must have access to the secret as well as the database or service that the secret contains credentials for. See [Permissions for rotation](rotating-secrets-required-permissions-function.md).

## Permissions for encryption keys
<a name="auth-and-access_encrypt"></a>

Secrets Manager uses AWS Key Management Service (AWS KMS) keys to [encrypt secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html). The AWS managed key `aws/secretsmanager` automatically has the correct permissions. If you use a different KMS key, Secrets Manager needs permissions to that key. See [Permissions for the KMS key](security-encryption.md#security-encryption-authz). 

## Permissions for replication
<a name="auth-and-access_replication"></a>

By using IAM permission policies, you control which users or services can replicate your secrets to other Regions. See [Prevent AWS Secrets Manager replication](replicate-secrets-permissions.md).