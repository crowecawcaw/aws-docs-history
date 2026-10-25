

# AWS managed policy: AmazonSageMakerClusterInstanceRolePolicy
<a name="security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy"></a>

This policy grants permissions commonly needed to use Amazon SageMaker HyperPod.

**Permissions details**

This AWS managed policy includes the following permissions.
+ `cloudwatch` – Allows principals to post Amazon CloudWatch metrics to the `/aws/sagemaker/Clusters` namespace, and to send OpenTelemetry Protocol (OTLP) metrics, which carry no namespace.
+ `logs` – Allows principals to publish CloudWatch log streams.
+ `s3` – Allows principals to list and retrieve lifecycle script files from an Amazon S3 bucket in your account. These buckets are limited to those whose name starts with "sagemaker-".
+ `ssmmessages` – Allows principals to open a connection to AWS Systems Manager.

To view the permissions for this policy, see [AmazonSageMakerClusterInstanceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerClusterInstanceRolePolicy.html) in the AWS Managed Policy Reference.