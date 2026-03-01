# AWS managed policies for Amazon ECR Public

Amazon ECR Public provides several managed policies that you can attach to users or Amazon EC2
instances. These policies allow for differing levels of control over Amazon ECR resources and API
operations. You can apply these policies directly or use them as starting points for
creating your own policies. For more information about each API operation that's mentioned
in these policies, see [Actions](../../../AmazonECRPublic/latest/APIReference/API_Operations.md "../../../AmazonECRPublic/latest/APIReference/API_Operations.md") in the
_Amazon ECR Public API Reference_.

###### Topics

- [AmazonElasticContainerRegistryPublicFullAccess](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess "#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess")
- [AmazonElasticContainerRegistryPublicPowerUser](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser "#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser")
- [AmazonElasticContainerRegistryPublicReadOnly](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly "#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly")
- [Amazon ECR Public updates to AWS managed policies](#public-security-iam-awsmanpol-updates "#public-security-iam-awsmanpol-updates")

## `AmazonElasticContainerRegistryPublicFullAccess`

You can attach the `AmazonElasticContainerRegistryPublicFullAccess` policy
to your IAM identities. This policy grants administrative access to Amazon ECR Public
resources and allows an IAM identity (such as a user, group, or role) to use all
Amazon ECR Public features.

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicFullAccess](../../../aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicFullAccess.md") in the _AWS Managed Policy
Reference_.

## `AmazonElasticContainerRegistryPublicPowerUser`

You can attach the `AmazonElasticContainerRegistryPublicPowerUser` policy
to your IAM identities. This policy grants power user access to Amazon ECR Public
resources, providing write access to public repositories without allowing deletion of
repositories or modification of policy documents.

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicPowerUser](../../../aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicPowerUser.md "../../../aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicPowerUser.md") in the _AWS Managed Policy
Reference_.

## `AmazonElasticContainerRegistryPublicReadOnly`

You can attach the `AmazonElasticContainerRegistryPublicReadOnly` policy
to your IAM identities. This policy grants read-only permissions to Amazon ECR Public
resources, including the ability to describe public registries, list and describe public
repositories, describe images, and pull images with the Docker CLI.

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicReadOnly](../../../aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicReadOnly.md "../../../aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicReadOnly.md") in the _AWS Managed Policy
Reference_.

## Amazon ECR Public updates to AWS managed policies

View details about updates to AWS managed policies for Amazon ECR Public since the time
that this service began tracking these changes. For automatic alerts about changes to
this page, subscribe to the RSS feed on the Amazon ECR Public Document history page.

| Change                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                   | Date             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Amazon ECR started tracking<br>changes                                                                                                                                                                                          | Amazon ECR started tracking changes for AWS managed policies.                                                                                                                                                                                                                                                                 | June 24, 2021    |
| [AmazonElasticContainerRegistryPublicReadOnly](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly "#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly") –<br>New policy       | Amazon ECR added a new policy that grants read-only permissions to<br>Amazon ECR Public. These permissions include the ability to describe<br>public registries, to list and describe public repositories, to<br>describe images within a public repository and to pull images from<br>Amazon ECR Public with the Docker CLI. | December 1, 2020 |
| [AmazonElasticContainerRegistryPublicPowerUser](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser "#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser") –<br>New policy    | Amazon ECR added a new policy that grants administrative permissions to<br>Amazon ECR Public that allow write access to public repositories.<br>However, these permissions don't allow users to delete public<br>repositories or change the policy documents that are applied to<br>them.                                     | December 1, 2020 |
| [AmazonElasticContainerRegistryPublicFullAccess](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess "#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess") –<br>New policy | Amazon ECR added a new policy that grants full access to Amazon ECR<br>Public.                                                                                                                                                                                                                                                | December 1, 2020 |
