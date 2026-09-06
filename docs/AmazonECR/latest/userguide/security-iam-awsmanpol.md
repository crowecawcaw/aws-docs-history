

# AWS managed policies for Amazon Elastic Container Registry
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

Amazon ECR provides several managed policies that you can attach to IAM identities or to Amazon EC2 instances. These managed policies allow differing levels of control over access to Amazon ECR resources and API operations. For more information about each API operation mentioned in these policies, see [Actions](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Operations.html) in the *Amazon Elastic Container Registry API Reference*.

**Topics**
+ [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess)
+ [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser)
+ [AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly)
+ [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly)
+ [`AWSECRPullThroughCache_ServiceRolePolicy`](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy)
+ [`ECRReplicationServiceRolePolicy`](#security-iam-awsmanpol-ECRReplicationServiceRolePolicy)
+ [`ECRTemplateServiceRolePolicy`](#security-iam-awsmanpol-ECRTemplateServiceRolePolicy)
+ [Amazon ECR updates to AWS managed policies](#security-iam-awsmanpol-updates)

## AmazonEC2ContainerRegistryFullAccess
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess"></a>

You can attach the `AmazonEC2ContainerRegistryFullAccess` policy to your IAM identities. This policy grants administrative access to Amazon ECR resources and grants an IAM identity (such as a user, group, or role) access to the AWS services that Amazon ECR is integrated with to use all of Amazon ECR features. Using this policy allows access to all of Amazon ECR features that are available in the AWS Management Console.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryFullAccess.html) in the *AWS Managed Policy Reference*.

## AmazonEC2ContainerRegistryPowerUser
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser"></a>

You can attach the `AmazonEC2ContainerRegistryPowerUser` policy to your IAM identities. This policy grants administrative permissions that allow IAM users to read and write to repositories, but doesn't allow them to delete repositories or change the policy documents that are applied to them.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryPowerUser](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPowerUser.html) in the *AWS Managed Policy Reference*.

## AmazonEC2ContainerRegistryPullOnly
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly"></a>

You can attach the `AmazonEC2ContainerRegistryPullOnly` policy to your IAM identities. This policy grants permission to pull container images from Amazon ECR. If the registry is enabled for pull-through cache, it will also allow pulls to import an image from an upstream registry.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryPullOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPullOnly.html) in the *AWS Managed Policy Reference*.

## AmazonEC2ContainerRegistryReadOnly
<a name="security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly"></a>

You can attach the `AmazonEC2ContainerRegistryReadOnly` policy to your IAM identities. This policy grants read-only permissions to Amazon ECR. This includes the ability to list repositories and images within the repositories. It also includes the ability to pull images from Amazon ECR with the Docker CLI.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.html) in the *AWS Managed Policy Reference*.

## `AWSECRPullThroughCache_ServiceRolePolicy`
<a name="security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy"></a>

You can't attach the `AWSECRPullThroughCache_ServiceRolePolicy` managed IAM policy to your IAM entities. This policy is attached to a service-linked role that allows Amazon ECR to push images to your repositories through the pull through cache workflow. For more information, see [Amazon ECR service-linked role for pull through cache](slr-pullthroughcache.md).

## `ECRReplicationServiceRolePolicy`
<a name="security-iam-awsmanpol-ECRReplicationServiceRolePolicy"></a>

You can't attach the `ECRReplicationServiceRolePolicy` managed IAM policy to your IAM entities. This policy is attached to a service-linked role that allows Amazon ECR to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon ECR](using-service-linked-roles.md).

## `ECRTemplateServiceRolePolicy`
<a name="security-iam-awsmanpol-ECRTemplateServiceRolePolicy"></a>

You can't attach the `ECRTemplateServiceRolePolicy` managed IAM policy to your IAM entities. This policy is attached to a service-linked role that allows Amazon ECR to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon ECR](using-service-linked-roles.md).

## Amazon ECR updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon ECR since the time that this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon ECR Document history page.

 


| Change | Description | Date | 
| --- | --- | --- | 
| [Amazon ECR service-linked role for pull through cache](slr-pullthroughcache.md) – Update to an existing policy | Amazon ECR added new permissions to the `AWSECRPullThroughCache_ServiceRolePolicy` policy. These permissions allow Amazon ECR to pull images from ECR private registry. This is required when using a pull through cache rule to cache images from another Amazon ECR private registry.  | March 12, 2025 | 
| [AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly) – New policy | Amazon ECR added a new policy which grants pull-only permissions to Amazon ECR. | October 10, 2024 | 
| [ECRTemplateServiceRolePolicy](slr-rct.md) – New policy | Amazon ECR added a new policy. This policy is associated with the `ECRTemplateServiceRolePolicy` service-linked role for the repository creation template feature. | June 20, 2024 | 
| [AWSECRPullThroughCache\_ServiceRolePolicy](slr-pullthroughcache.md) – Update to an existing policy | Amazon ECR added new permissions to the `AWSECRPullThroughCache_ServiceRolePolicy` policy. These permissions allow Amazon ECR to retrieve the encrypted contents of a Secrets Manager secret. This is required when using a pull through cache rule to cache images from an upstream registry that requires authentication. | November 15, 2023 | 
| [AWSECRPullThroughCache\_ServiceRolePolicy](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy) – New policy | Amazon ECR added a new policy. This policy is associated with the `AWSServiceRoleForECRPullThroughCache` service-linked role for the pull through cache feature. | November 29, 2021 | 
| [ECRReplicationServiceRolePolicy](#security-iam-awsmanpol-ECRReplicationServiceRolePolicy) – New policy | Amazon ECR added a new policy. This policy is associated with the `AWSServiceRoleForECRReplication` service-linked role for the replication feature. | December 4, 2020 | 
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryFullAccess` policy. These permissions allow principals to create the Amazon ECR service-linked role. | December 4, 2020 | 
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryReadOnly` policy which allow principals to read lifecycle policies, list tags, and describe the scan findings for images. | December 10, 2019 | 
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryPowerUser` policy. They allow principals to read lifecycle policies, list tags, and describe the scan findings for images. | December 10, 2019 | 
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryFullAccess` policy. They allow principals to look up management events or AWS CloudTrail Insights events that are captured by CloudTrail. | November 10, 2017 | 
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryReadOnly` policy. They allow principals to describe Amazon ECR images. | October 11, 2016 | 
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser) – Update to an existing policy | Amazon ECR added new permissions to the `AmazonEC2ContainerRegistryPowerUser` policy. They allow principals to describe Amazon ECR images. | October 11, 2016 | 
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) – New policy | Amazon ECR added a new policy which grants read-only permissions to Amazon ECR. These permissions include the ability to list repositories and images within the repositories. They also include the ability to pull images from Amazon ECR with the Docker CLI. | December 21, 2015 | 
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser) – New policy | Amazon ECR added a new policy which grants administrative permissions that allow users to read and write to repositories but doesn't allow them to delete repositories or change the policy documents that are applied to them. | December 21, 2015 | 
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess) – New policy | Amazon ECR added a new policy. This policy grants full access to Amazon ECR. | December 21, 2015 | 
| Amazon ECR started tracking changes | Amazon ECR started tracking changes for AWS managed policies. | June 24, 2021 | 