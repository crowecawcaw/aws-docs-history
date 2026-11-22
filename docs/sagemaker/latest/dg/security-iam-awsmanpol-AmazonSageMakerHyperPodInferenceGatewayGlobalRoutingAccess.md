

# AWS managed policy: AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess

This policy provides the permissions that the SageMaker HyperPod inference gateway controller needs to join a SageMaker AI global inference gateway. A global inference gateway gives you one endpoint. That endpoint routes inference requests to inference gateways on SageMaker HyperPod clusters in several AWS Regions. Attach this policy to the IAM role of the inference gateway controller, together with the [AmazonSageMakerHyperPodInferenceGatewayAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerHyperPodInferenceGatewayAccess.html) policy. The controller uses that policy for TLS certificates.

To join a global inference gateway, the controller does the following:
+ Publishes a private network path in front of the Network Load Balancer of the inference gateway. The global inference gateway connects to this path.
+ Stores the TLS server certificate of the inference gateway in your Amazon S3 bucket. The global inference gateway reads the certificate from there.
+ Creates a private path for the load metrics of the inference gateway to the Amazon Kinesis Data Streams stream of the global inference gateway.

Every permission is limited to resources in your own account. Permissions that create or change a resource are limited to resources that the controller creates and tags with `CreatedBy=HyperPodInference`.

**Permission details**

This policy includes the following permissions.
+ `ec2` and `vpce` – The controller creates, tags, changes, and deletes a VPC endpoint service in front of the Network Load Balancer of the inference gateway. The global inference gateway connects to the endpoint service through AWS PrivateLink. The controller also makes the endpoint service available to the Regions that the global inference gateway uses.
+ `ec2` – The controller creates, tags, changes, and deletes an interface VPC endpoint to Amazon Kinesis Data Streams and its security group in the cluster's Amazon VPC. The endpoint is limited to the Amazon Kinesis Data Streams service. It can be in another Region when the stream of the global inference gateway is in another Region.
+ `ec2` and `elasticloadbalancing` – The controller describes VPC endpoint services, VPC endpoints, Regions, and the cluster's Amazon VPC, subnets, and security groups. The controller also describes the load balancer of the inference gateway and its target health. The controller reports the inference gateway as ready only when its load balancer has a healthy target.
+ `s3` – The controller uploads, tags, and deletes the gateway's TLS server certificate in Amazon S3 buckets whose name starts with `hyperpod-tls`. Uploads must carry the tag `CreatedBy=HyperPodInference`.
+ `kms` – The controller generates data keys through Amazon S3 when the TLS bucket is encrypted with an AWS KMS key.
+ `sagemaker` – The controller describes the SageMaker HyperPod cluster.

To view the permissions for this policy, see [AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess.html) in the AWS Managed Policy Reference.