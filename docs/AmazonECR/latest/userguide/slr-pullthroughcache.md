# Amazon ECR service-linked role for pull through

cache

Amazon ECR uses a service-linked role named
**AWSServiceRoleForECRPullThroughCache** which gives permission for
Amazon ECR to perform actions on your behalf to complete pull through cache actions. For more
information about pull through cache, see [Templates to control repositories created
during a pull through cache or replication action](repository-creation-templates.md "repository-creation-templates.md").

## Service-linked role permissions

for Amazon ECR

The **AWSServiceRoleForECRPullThroughCache** service-linked role
trusts the following service to assume the role.

- `pullthroughcache.ecr.amazonaws.com`

**Permissions details**

The `AWSECRPullThroughCache_ServiceRolePolicy` permissions policy is
attached to the service-linked role. This managed policy grants Amazon ECR
permission to perform the following actions. For more information, see [AWSECRPullThroughCache_ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy").

- `ecr` – Allows the Amazon ECR service to pull and push
  images to a private repository.
- `secretsmanager:GetSecretValue` – Allows the Amazon ECR
  service to retrieve the encrypted contents of an AWS Secrets Manager secret. This is
  required when using a pull through cache rule to cache images from an
  upstream registry that requires authentication in your private registry.
  This permission applies only to secrets with the
  `ecr-pullthroughcache/` name prefix.

The `AWSECRPullThroughCache_ServiceRolePolicy` policy contains the
following JSON.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ECR",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:InitiateLayerUpload",
 "ecr:UploadLayerPart",
 "ecr:CompleteLayerUpload",
 "ecr:PutImage",
 "ecr:BatchGetImage",
 "ecr:BatchImportUpstreamImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetImageCopyStatus"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SecretsManager",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:ecr-pullthroughcache/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (for example a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Amazon ECR

You don't need to manually create the Amazon ECR service-linked role for pull
through cache. When you create a pull through cache rule for your private registry
in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECR creates the
service-linked role for you.

If you delete this service-linked role and need to create it again, you can use
the same process to recreate the role in your account. When you create a pull
through cache rule for your private registry, Amazon ECR creates the
service-linked role for you again if it doesn't already exist.

## Editing a service-linked role for

Amazon ECR

Amazon ECR doesn't allow manually editing the
**AWSServiceRoleForECRPullThroughCache** service-linked role.
After the service-linked role is created, you can't change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the service-linked role for

Amazon ECR

If you no longer need to use a feature or service that requires a service-linked
role, we recommend that you delete that role. That way, you don’t have an unused
entity that isn't actively monitored or maintained. However, you must delete the
pull through cache rules for your registry in every Region before you can manually
delete the service-linked role.

###### Note

If you try to delete resources while the Amazon ECR service is still using
the role, your delete action might fail. If that happens, wait for a few minutes
and try again.

###### To delete Amazon ECR resources used by the

**AWSServiceRoleForECRPullThroughCache** service-linked
role

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region where your pull through cache
   rules are created.
3. In the navigation pane, choose **Private
   registry**.
4. On the **Private registry** page, on the **Pull
   through cache configuration** section, choose
   **Edit**.
5. For each pull through cache rule you have created, select the rule and
   then choose **Delete rule**.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
**AWSServiceRoleForECRPullThroughCache** service-linked role.
For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
