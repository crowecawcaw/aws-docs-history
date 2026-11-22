

# AWS managed policy: AmazonSageMakerGlobalInferenceGatewayExecutionAccess

This policy provides the permissions that a SageMaker AI global inference gateway's execution role needs. The global inference gateway uses the role to reach the SageMaker HyperPod clusters in the gateway. You pass the execution role when you create the global inference gateway, and SageMaker AI assumes it. Attach this policy to that role. The role also needs an Amazon EKS access entry on each cluster. Kubernetes role-based access control (RBAC) limits what the role can do in the cluster. Every permission is limited to resources in your own account.

**Permission details**

This policy includes the following permissions.
+ `sagemaker` – The global inference gateway describes the SageMaker HyperPod cluster, to find the cluster's Amazon EKS cluster.
+ `eks` – The global inference gateway calls the cluster's Kubernetes API through the Amazon EKS access entry. It reads the inference gateway configuration and writes the gateway's membership record.
+ `s3` – The global inference gateway reads the gateway's TLS server certificate from Amazon S3 buckets whose name starts with `hyperpod-tls`, when the object carries the tag `CreatedBy=HyperPodInference`.
+ `kms` – The global inference gateway decrypts the certificate through Amazon S3 when the TLS bucket is encrypted with an AWS KMS key.

To view the permissions for this policy, see [AmazonSageMakerGlobalInferenceGatewayExecutionAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerGlobalInferenceGatewayExecutionAccess.html) in the AWS Managed Policy Reference.