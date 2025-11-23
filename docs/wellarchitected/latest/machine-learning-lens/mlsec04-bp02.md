# MLSEC04-BP02 Secure inter-node cluster communications

Machine learning frameworks require secure communications between
computational nodes to maintain data integrity and protect sensitive
information during model training. By implementing encryption for
inter-node communications, you safeguard coefficient exchanges and
protect synchronized information across distributed environments.

**Desired outcome:** You establish
encrypted communication channels between computational nodes in your
machine learning clusters, protecting sensitive model data,
parameters, and training information as it traverses networks. This
improves data integrity and confidentiality during distributed
training operations while maintaining the performance requirements
of your machine learning workloads.

**Common anti-patterns:**

- Assuming internal network communications are inherently secure
  and don't require encryption.
- Implementing encryption only for external communications but
  neglecting inter-node traffic.
- Using outdated or weak encryption protocols for performance
  reasons.
- Neglecting to rotate encryption certificates and credentials
  regularly.

**Benefits of establishing this best
practice:**

- Protection of proprietary algorithms and model parameters during
  training.
- Prevention of data leakage and unauthorized access to training
  data.
- Improves adherence to data protection regulations and security
  requirements.
- Consistent security posture across your ML infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For machine learning frameworks like TensorFlow that rely on
distributed computing, secure inter-node communication is
essential to protect the integrity and confidentiality of the
training process. During distributed training, nodes exchange
critical information like model coefficients, gradients, and
parameter updates. This information contains valuable intellectual
property about your models and potentially sensitive insights
derived from your training data.

When implementing distributed machine learning workloads, encrypt
that data transmitted between computational nodes using
industry-standard protocols. This is particularly important when
your infrastructure spans across different networks, availability
zones, or even Regions. Encryption in transit stops unauthorized
parties from intercepting or tampering with model data as it moves
between nodes.

AWS services like
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") and
[Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/")
provide built-in capabilities to secure inter-node communications,
making it more straightforward to implement this best practice
without extensive custom configuration.

### Implementation steps

1. **Enable inter-node encryption in
   Amazon SageMaker AI**. Amazon SageMaker AI provides
   automatic encryption for inter-container communication
   during training jobs. When configuring your training job,
   enable encryption to verify that data passed between
   containers traverses over an encrypted tunnel. For
   large-scale distributed training, use
   [Amazon SageMaker AI HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.md") which provides managed, resilient
   clusters with built-in security features including VPC
   integration, automatic health checks, and secure
   node-to-node communication for foundation model training.
   This protects your model parameters and gradients during the
   training process without requiring additional configuration.
2. **Configure TLS for distributed
   TensorFlow workloads**. For TensorFlow-based
   distributed training, implement Transport Layer Security
   (TLS) to secure communications between worker nodes.
   TensorFlow supports TLS configuration through environment
   variables and configuration parameters. Use properly signed
   certificates and configure both client and server-side
   authentication for maximum security.
3. **Enable encryption in transit in
   Amazon EMR**. When using
   [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") for machine learning workloads, implement
   security configurations that enable encryption in transit.
   Amazon EMR makes it simple to create security configurations
   that specify the use of Transport Layer Security (TLS)
   certificates for encrypting data in transit between cluster
   nodes. This protects data whether it's stored locally on the
   cluster or in Amazon S3.
4. **Implement secure key
   management**. Use
   [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to manage the encryption
   keys used for securing inter-node communications. This
   provides centralized control, auditing, and automatic key
   rotation, enhancing your security posture while simplifying
   key management operations.
5. **Configure secure cluster
   authentication**. Implement strong authentication
   mechanisms to verify that only authorized nodes can join
   your cluster and participate in the distributed training
   process. Use certificate-based authentication where possible
   and implement node identity verification as part of your
   security configuration.
6. **Regularly rotate security
   credentials**. Establish a process for regularly
   rotating TLS certificates, encryption keys, and other
   security credentials used in your distributed training
   environment. This limits the potential impact of compromised
   credentials and aligns with security best practices.
7. **Monitor encrypted
   communications**. Implement logging and monitoring
   for your encrypted communications channels to detect
   potential security issues. Configure alerts for unusual
   traffic patterns or authentication failures that might
   indicate attempted security breaches.
8. **Secure foundation model
   communication**. When using distributed training
   for large language models or other foundation models,
   encrypt parameter server communications, as these contain
   valuable intellectual property. For AI workloads on Amazon SageMaker AI, enable inter-container encryption to protect
   model weights and gradients during the training process.

## Resources

**Related documents:**

- [Amazon SageMaker AI HyperPod Prerequisites](../../../sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.md")
- [Protect
  Communications Between ML Compute Instances in a Distributed
  Training Job](../../../sagemaker/latest/dg/train-encrypt.md "../../../sagemaker/latest/dg/train-encrypt.md")
- [Encryption
  options for Amazon EMR](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md")
- [Configure
  security in Amazon SageMaker AI](../../../sagemaker/latest/dg/security.md "../../../sagemaker/latest/dg/security.md")
- [Security
  Pillar - AWS Well-Architected Framework](../security-pillar/welcome.md "../security-pillar/welcome.md")
- [Encrypt
  data in transit using a TLS custom certificate provider with
  Amazon EMR](https://aws.amazon.com/blogs/big-data/encrypt-data-in-transit-using-a-tls-custom-certificate-provider-with-amazon-emr/ "https://aws.amazon.com/blogs/big-data/encrypt-data-in-transit-using-a-tls-custom-certificate-provider-with-amazon-emr/")
- [Building
  secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/")
- [Amazon SageMaker AI Studio Admin Best Practices](../../../whitepapers/latest/sagemaker-studio-admin-best-practices/data-protection.md "../../../whitepapers/latest/sagemaker-studio-admin-best-practices/data-protection.md")

**Related videos:**

- [Architectural
  best practices for machine learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo "https://www.youtube.com/watch?v=fBytsYBVgbo")
- [Secure
  and compliant machine learning for regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg "https://www.youtube.com/watch?v=8p-B3sTLmFg")

**Related examples:**

- [Amazon SageMaker AI secure distributed training examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-python-sdk "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-python-sdk")
