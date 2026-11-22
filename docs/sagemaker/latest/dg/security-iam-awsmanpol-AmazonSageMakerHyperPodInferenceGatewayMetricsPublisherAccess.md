

# AWS managed policy: AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess

This policy provides the permissions that the SageMaker HyperPod inference gateway metrics publisher needs to send gateway metrics to a SageMaker AI global inference gateway. The global inference gateway uses these metrics to decide where to route requests. Attach this policy to the IAM role of the metrics publisher.

The global inference gateway's stream and its encryption key are in an AWS account that SageMaker AI owns, so these permissions are not limited to your account. They allow only writes, only to streams that SageMaker AI names `gig-metrics-*`, and only encryption for those streams. The stream's resource policy controls which accounts can write to it.

**Permission details**

This policy includes the following permissions.
+ `kinesis` – The metrics publisher writes records to the Amazon Kinesis Data Streams stream of the global inference gateway.
+ `kms` – Amazon Kinesis Data Streams generates data keys for the metrics publisher, to encrypt the records it writes to that stream.

To view the permissions for this policy, see [AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess.html) in the AWS Managed Policy Reference.