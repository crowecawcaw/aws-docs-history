# AWS managed policies for

Amazon SageMaker HyperPod

The following AWS managed policies add permissions required to use Amazon SageMaker HyperPod. The
policies are available in your AWS account and are used by execution roles created from the
SageMaker AI console or the HyperPod service-linked role.

###### Topics

- [AWS managed policy: AmazonSageMakerHyperPodTrainingOperatorAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.md "security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.md")
- [AWS
  managed policy: AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md "security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md")
- [AWS
  managed policy: AmazonSageMakerHyperPodServiceRolePolicy](security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md "security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md")
- [AWS
  managed policy: AmazonSageMakerClusterInstanceRolePolicy](security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md "security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md")
- [Amazon SageMaker AI updates to SageMaker HyperPod
  managed policies](#security-iam-awsmanpol-hyperpod-updates "#security-iam-awsmanpol-hyperpod-updates")

## Amazon SageMaker AI updates to SageMaker HyperPod

managed policies

View details about updates to AWS managed policies for SageMaker HyperPod since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the SageMaker AI [Document history page.](doc-history.md "doc-history.md")

| Policy                                                                                                                                                                                                                    | Version | Change                                                                                                                                                                                                                                            | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonSageMakerHyperPodTrainingOperatorAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.md "security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.md") - New policy           | 1       | Initial policy                                                                                                                                                                                                                                    | August 22, 2025   |
| [AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md "security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md") - Updated policy | 2       | Updated the policy to fix the role scope-down to include the `service-role` prefix. Also added permissions for `eks:DeletePodIdentityAssociation` and `eks:UpdatePodIdentityAssociation` that are required for end-to-end administrative actions. | August 19, 2025   |
| [AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md "security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md") - New policy     | 1       | Initial policy                                                                                                                                                                                                                                    | July 10, 2025     |
| [AmazonSageMakerHyperPodServiceRolePolicy](security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md "security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md") - New policy                          | 1       | Initial policy                                                                                                                                                                                                                                    | September 9, 2024 |
| [AmazonSageMakerClusterInstanceRolePolicy](security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md "security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md") - New policy                          | 1       | Initial policy                                                                                                                                                                                                                                    | November 29, 2023 |
