# Security considerations for managed

tiered checkpointing

This section covers important security considerations when using managed tiered
checkpointing. It includes Python pickle usage, Amazon S3 encryption, and network endpoint
security.

**Python pickle usage**

Managed tiered checkpointing uses Python’s pickle module to deserialize checkpoint data
stored in Amazon S3. This implementation has important security implications:

- **Extended trust boundary**: When using managed tiered
  checkpointing with Amazon S3, the Amazon S3 bucket becomes part of your cluster’s trust
  boundary.
- **Code execution risk**: Python’s pickle module can
  execute arbitrary code during deserialization. If an unauthorized user gains write access
  to your checkpoint Amazon S3 bucket, they could potentially craft malicious pickle data that
  executes when loaded by managed tiered checkpointing.
  **Best practices for Amazon S3 storage**

When using managed tiered checkpointing with Amazon S3 storage:

- **Restrict Amazon S3 bucket access**: Ensure that only
  authorized users and roles associated with your training cluster have access to the Amazon S3
  bucket used for checkpointing.
- **Implement bucket policies**: Configure appropriate
  bucket policies to prevent unauthorized access or modifications.
- **Validate access patterns**: Implement logging for
  validating access patterns to your checkpoint Amazon S3 buckets.
- **Validate bucket names**: Use caution with bucket name
  selection to avoid potential bucket hijacking.
  **Network endpoints**

Managed tiered checkpointing enables network endpoints on each of your compute nodes on
the following ports: 9200/TCP, 9209/UDP, 9210/UDP, 9219/UDP, 9220/UDP, 9229/UDP, 9230/UDP,
9239/UDP, 9240/UDP. These ports are necessary for the checkpointing service to function and
maintain data synchronization.

By default, SageMaker’s network configuration restricts access to these endpoints for security
purposes. We recommend that you maintain these default restrictions.

When configuring your network settings for your nodes and VPC, follow AWS best practices
for VPCs, security groups, and ACLs. For more information, see the following:

- [Amazon SageMaker HyperPod prerequisites](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpcCluster "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpcCluster")
- [VPC security best
  practices](../../../vpc/latest/userguide/vpc-security-best-practices.md "../../../vpc/latest/userguide/vpc-security-best-practices.md")
