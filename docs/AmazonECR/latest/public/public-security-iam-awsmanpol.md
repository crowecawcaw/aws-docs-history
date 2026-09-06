

# AWS managed policies for Amazon ECR Public
<a name="public-security-iam-awsmanpol"></a>

Amazon ECR Public provides several managed policies that you can attach to users or Amazon EC2 instances. These policies allow for differing levels of control over Amazon ECR resources and API operations. You can apply these policies directly or use them as starting points for creating your own policies. For more information about each API operation that's mentioned in these policies, see [Actions](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Operations.html) in the *Amazon ECR Public API Reference*.

**Topics**
+ [`AmazonElasticContainerRegistryPublicFullAccess`](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess)
+ [`AmazonElasticContainerRegistryPublicPowerUser`](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser)
+ [`AmazonElasticContainerRegistryPublicReadOnly`](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly)
+ [Amazon ECR Public updates to AWS managed policies](#public-security-iam-awsmanpol-updates)

## `AmazonElasticContainerRegistryPublicFullAccess`
<a name="public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess"></a>

You can attach the `AmazonElasticContainerRegistryPublicFullAccess` policy to your IAM identities. This policy grants administrative access to Amazon ECR Public resources and allows an IAM identity (such as a user, group, or role) to use all Amazon ECR Public features.

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicFullAccess.html) in the *AWS Managed Policy Reference*.

## `AmazonElasticContainerRegistryPublicPowerUser`
<a name="public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser"></a>

You can attach the `AmazonElasticContainerRegistryPublicPowerUser` policy to your IAM identities. This policy grants power user access to Amazon ECR Public resources, providing write access to public repositories without allowing deletion of repositories or modification of policy documents.

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicPowerUser](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicPowerUser.html) in the *AWS Managed Policy Reference*.

## `AmazonElasticContainerRegistryPublicReadOnly`
<a name="public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly"></a>

You can attach the `AmazonElasticContainerRegistryPublicReadOnly` policy to your IAM identities. This policy grants read-only permissions to Amazon ECR Public resources, including the ability to describe public registries, list and describe public repositories, describe images, and pull images with the Docker CLI.

To view the permissions for this policy, see [AmazonElasticContainerRegistryPublicReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticContainerRegistryPublicReadOnly.html) in the *AWS Managed Policy Reference*.

## Amazon ECR Public updates to AWS managed policies
<a name="public-security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon ECR Public since the time that this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon ECR Public Document history page.

 


| Change | Description | Date | 
| --- | --- | --- | 
| Amazon ECR started tracking changes | Amazon ECR started tracking changes for AWS managed policies. | June 24, 2021 | 
| [AmazonElasticContainerRegistryPublicReadOnly](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicReadOnly) – New policy | Amazon ECR added a new policy that grants read-only permissions to Amazon ECR Public. These permissions include the ability to describe public registries, to list and describe public repositories, to describe images within a public repository and to pull images from Amazon ECR Public with the Docker CLI. | December 1, 2020 | 
| [AmazonElasticContainerRegistryPublicPowerUser](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicPowerUser) – New policy | Amazon ECR added a new policy that grants administrative permissions to Amazon ECR Public that allow write access to public repositories. However, these permissions don't allow users to delete public repositories or change the policy documents that are applied to them. | December 1, 2020 | 
| [AmazonElasticContainerRegistryPublicFullAccess](#public-security-iam-awsmanpol-AmazonElasticContainerRegistryPublicFullAccess) – New policy | Amazon ECR added a new policy that grants full access to Amazon ECR Public. | December 1, 2020 | 