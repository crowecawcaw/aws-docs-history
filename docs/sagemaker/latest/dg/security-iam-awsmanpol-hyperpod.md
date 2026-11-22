

# AWS managed policies for Amazon SageMaker HyperPod

The following AWS managed policies add permissions required to use Amazon SageMaker HyperPod. The policies are available in your AWS account and are used by execution roles created from the SageMaker AI console or the HyperPod service-linked role.

**Topics**
+ [AWS managed policy: AmazonSageMakerHyperPodTrainingOperatorAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.md)
+ [AWS managed policy: AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md)
+ [AWS managed policy: AmazonSageMakerHyperPodServiceRolePolicy](security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md)
+ [AWS managed policy: AmazonSageMakerClusterInstanceRolePolicy](security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md)
+ [AWS managed policy: AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess.md)
+ [AWS managed policy: AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess.md)
+ [AWS managed policy: AmazonSageMakerGlobalInferenceGatewayExecutionAccess](security-iam-awsmanpol-AmazonSageMakerGlobalInferenceGatewayExecutionAccess.md)
+ [Amazon SageMaker AI updates to SageMaker HyperPod managed policies](#security-iam-awsmanpol-hyperpod-updates)

## Amazon SageMaker AI updates to SageMaker HyperPod managed policies
<a name="security-iam-awsmanpol-hyperpod-updates"></a>

View details about updates to AWS managed policies for SageMaker HyperPod since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the SageMaker AI [Document history page.](doc-history.md)


| Policy | Version | Change | Date | 
| --- | --- | --- | --- | 
| [AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess.md) - New policy | 1 | Initial policy. Lets the inference gateway controller join a global inference gateway. For more information, see [AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess.html) in the AWS Managed Policy Reference. | November 17, 2026 | 
| [AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess.md) - New policy | 1 | Initial policy. Lets the inference gateway metrics publisher send gateway metrics to a global inference gateway. For more information, see [AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess.html) in the AWS Managed Policy Reference. | November 17, 2026 | 
| [AmazonSageMakerGlobalInferenceGatewayExecutionAccess](security-iam-awsmanpol-AmazonSageMakerGlobalInferenceGatewayExecutionAccess.md) - New policy | 1 | Initial policy. Lets a global inference gateway reach the SageMaker HyperPod clusters in the gateway. For more information, see [AmazonSageMakerGlobalInferenceGatewayExecutionAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerGlobalInferenceGatewayExecutionAccess.html) in the AWS Managed Policy Reference. | November 17, 2026 | 
| [AmazonSageMakerClusterInstanceRolePolicy](security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md) - Updated policy | 2 | Changed the `cloudwatch:namespace` condition on `cloudwatch:PutMetricData` from `StringEquals` to `StringEqualsIfExists`. OpenTelemetry Protocol (OTLP) metrics carry no namespace, so you can now send them to Amazon CloudWatch from cluster instances. Metrics that specify a namespace are still limited to `/aws/sagemaker/Clusters`. | October 15, 2026 | 
| [AmazonSageMakerHyperPodTrainingOperatorAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.md) - New policy | 1 | Initial policy | August 22, 2025 | 
| [AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md) - Updated policy | 2 | Updated the policy to fix the role scope-down to include the `service-role` prefix. Also added permissions for `eks:DeletePodIdentityAssociation` and `eks:UpdatePodIdentityAssociation` that are required for end-to-end administrative actions. | August 19, 2025 | 
| [AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md) - New policy | 1 | Initial policy | July 10, 2025 | 
| [AmazonSageMakerHyperPodServiceRolePolicy](security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md) - New policy | 1 | Initial policy | September 9, 2024 | 
| [AmazonSageMakerClusterInstanceRolePolicy](security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md) - New policy | 1 | Initial policy | November 29, 2023 | 