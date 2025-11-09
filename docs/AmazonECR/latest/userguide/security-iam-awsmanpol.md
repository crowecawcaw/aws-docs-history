# AWS managed policies for Amazon Elastic Container Registry

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

Amazon ECR provides several managed policies that you can attach to IAM identities or to
Amazon EC2 instances. These managed policies allow differing levels of control over access to
Amazon ECR resources and API operations. For more information about each API operation mentioned
in these policies, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the
_Amazon Elastic Container Registry API Reference_.

###### Topics

- [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess "#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess")
- [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser "#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser")
- [AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly "#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly")
- [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly "#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly")
- [AWSECRPullThroughCache_ServiceRolePolicy](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy "#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy")
- [ECRReplicationServiceRolePolicy](#security-iam-awsmanpol-ECRReplicationServiceRolePolicy "#security-iam-awsmanpol-ECRReplicationServiceRolePolicy")
- [ECRTemplateServiceRolePolicy](#security-iam-awsmanpol-ECRTemplateServiceRolePolicy "#security-iam-awsmanpol-ECRTemplateServiceRolePolicy")
- [Amazon ECR updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AmazonEC2ContainerRegistryFullAccess

You can attach the `AmazonEC2ContainerRegistryFullAccess` policy to your IAM identities.
This policy grants administrative access to Amazon ECR resources and grants an IAM identity
(such as a user, group, or role) access to the AWS services that Amazon ECR is integrated
with to use all of Amazon ECR features. Using this policy allows access to all of Amazon ECR
features that are available in the AWS Management Console.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryFullAccess](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryFullAccess.md") in the _AWS Managed Policy Reference_.

## AmazonEC2ContainerRegistryPowerUser

You can attach the `AmazonEC2ContainerRegistryPowerUser` policy to your
IAM identities. This policy grants administrative permissions that allow IAM users to read and write
to repositories, but doesn't allow them to delete repositories or change the policy
documents that are applied to them.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryPowerUser](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPowerUser.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPowerUser.md") in the _AWS Managed Policy Reference_.

## AmazonEC2ContainerRegistryPullOnly

You can attach the `AmazonEC2ContainerRegistryPullOnly` policy to your
IAM identities. This policy grants permission to pull container images from Amazon ECR. If the registry is enabled for pull-through cache, it will also allow pulls to import an image from an upstream registry.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryPullOnly](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPullOnly.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPullOnly.md") in the _AWS Managed Policy Reference_.

## AmazonEC2ContainerRegistryReadOnly

You can attach the `AmazonEC2ContainerRegistryReadOnly` policy to your
IAM identities. This policy grants read-only permissions to Amazon ECR. This includes the ability to list
repositories and images within the repositories. It also includes the ability to pull
images from Amazon ECR with the Docker CLI.

To view the permissions for this policy, see [AmazonEC2ContainerRegistryReadOnly](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.md") in the _AWS Managed Policy Reference_.

## `AWSECRPullThroughCache_ServiceRolePolicy`

You can't attach the `AWSECRPullThroughCache_ServiceRolePolicy` managed
IAM policy to your IAM entities. This policy is attached to a service-linked role
that allows Amazon ECR to push images to your repositories through the pull through cache
workflow. For more information, see [Amazon ECR service-linked role for pull through
cache](slr-pullthroughcache.md "slr-pullthroughcache.md").

## `ECRReplicationServiceRolePolicy`

You can't attach the `ECRReplicationServiceRolePolicy` managed IAM policy
to your IAM entities. This policy is attached to a service-linked role that allows
Amazon ECR to perform actions on your behalf. For more information, see [Using service-linked roles for
Amazon ECR](using-service-linked-roles.md "using-service-linked-roles.md").

## `ECRTemplateServiceRolePolicy`

You can't attach the `ECRTemplateServiceRolePolicy` managed IAM policy
to your IAM entities. This policy is attached to a service-linked role that allows
Amazon ECR to perform actions on your behalf. For more information, see [Using service-linked roles for
Amazon ECR](using-service-linked-roles.md "using-service-linked-roles.md").

## Amazon ECR updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon ECR since the time that
this service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the Amazon ECR Document history page.

| Change                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [Amazon ECR service-linked role for pull through<br>cache](slr-pullthroughcache.md "slr-pullthroughcache.md")<br>– Update to an existing policy                                                       | Amazon ECR added new permissions to the `AWSECRPullThroughCache_ServiceRolePolicy` policy. These permissions allow Amazon ECR to pull images from ECR private registry.<br>This is required when using a pull through cache rule to cache images from another Amazon ECR private registry.                                                 | March 12, 2025    |
| [AmazonEC2ContainerRegistryPullOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly "#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly")<br>– New policy                         | Amazon ECR added a new policy which grants pull-only permissions to<br>Amazon ECR.                                                                                                                                                                                                                                                         | October 10, 2024  |
| [ECRTemplateServiceRolePolicy](slr-rct.md "slr-rct.md") – New<br>policy                                                                                                                               | Amazon ECR added a new policy. This policy is associated with the<br>`ECRTemplateServiceRolePolicy` service-linked<br>role for the repository creation template feature.                                                                                                                                                                   | June 20, 2024     |
| [AWSECRPullThroughCache_ServiceRolePolicy](slr-pullthroughcache.md "slr-pullthroughcache.md") – Update<br>to an existing policy                                                                       | Amazon ECR added new permissions to the<br>`AWSECRPullThroughCache_ServiceRolePolicy` policy.<br>These permissions allow Amazon ECR to retrieve the encrypted contents of<br>a Secrets Manager secret. This is required when using a pull through cache<br>rule to cache images from an upstream registry that requires<br>authentication. | November 15, 2023 |
| [AWSECRPullThroughCache_ServiceRolePolicy](#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy "#security-iam-awsmanpol-AWSECRPullThroughCache_ServiceRolePolicy") – New<br>policy       | Amazon ECR added a new policy. This policy is associated with the<br>`AWSServiceRoleForECRPullThroughCache` service-linked<br>role for the pull through cache feature.                                                                                                                                                                     | November 29, 2021 |
| [ECRReplicationServiceRolePolicy](#security-iam-awsmanpol-ECRReplicationServiceRolePolicy "#security-iam-awsmanpol-ECRReplicationServiceRolePolicy") – New<br>policy                                  | Amazon ECR added a new policy. This policy is associated with the<br>`AWSServiceRoleForECRReplication` service-linked role<br>for the replication feature.                                                                                                                                                                                 | December 4, 2020  |
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess "#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess") – Update to<br>an existing policy | Amazon ECR added new permissions to the<br>`AmazonEC2ContainerRegistryFullAccess` policy. These<br>permissions allow principals to create the Amazon ECR service-linked<br>role.                                                                                                                                                           | December 4, 2020  |
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly "#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly") – Update to an<br>existing policy       | Amazon ECR added new permissions to the<br>`AmazonEC2ContainerRegistryReadOnly` policy which<br>allow principals to read lifecycle policies, list tags, and describe<br>the scan findings for images.                                                                                                                                      | December 10, 2019 |
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser "#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser") – Update to<br>an existing policy    | Amazon ECR added new permissions to the<br>`AmazonEC2ContainerRegistryPowerUser` policy. They<br>allow principals to read lifecycle policies, list tags, and describe<br>the scan findings for images.                                                                                                                                     | December 10, 2019 |
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess "#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess") – Update to<br>an existing policy | Amazon ECR added new permissions to the<br>`AmazonEC2ContainerRegistryFullAccess` policy. They<br>allow principals to look up management events or AWS CloudTrail Insights<br>events that are captured by CloudTrail.                                                                                                                      | November 10, 2017 |
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly "#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly") – Update to an<br>existing policy       | Amazon ECR added new permissions to the<br>`AmazonEC2ContainerRegistryReadOnly` policy. They<br>allow principals to describe Amazon ECR images.                                                                                                                                                                                            | October 11, 2016  |
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser "#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser") – Update to<br>an existing policy    | Amazon ECR added new permissions to the<br>`AmazonEC2ContainerRegistryPowerUser` policy. They<br>allow principals to describe Amazon ECR images.                                                                                                                                                                                           | October 11, 2016  |
| [AmazonEC2ContainerRegistryReadOnly](#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly "#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly") – New<br>policy                         | Amazon ECR added a new policy which grants read-only permissions to<br>Amazon ECR. These permissions include the ability to list repositories<br>and images within the repositories. They also include the ability to<br>pull images from Amazon ECR with the Docker CLI.                                                                  | December 21, 2015 |
| [AmazonEC2ContainerRegistryPowerUser](#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser "#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser") – New<br>policy                      | Amazon ECR added a new policy which grants administrative permissions<br>that allow users to read and write to repositories but doesn't allow<br>them to delete repositories or change the policy documents that are<br>applied to them.                                                                                                   | December 21, 2015 |
| [AmazonEC2ContainerRegistryFullAccess](#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess "#security-iam-awsmanpol-AmazonEC2ContainerRegistryFullAccess") – New<br>policy                   | Amazon ECR added a new policy. This policy grants full access to<br>Amazon ECR.                                                                                                                                                                                                                                                            | December 21, 2015 |
| Amazon ECR started tracking<br>changes                                                                                                                                                                | Amazon ECR started tracking changes for AWS managed policies.                                                                                                                                                                                                                                                                              | June 24, 2021     |
