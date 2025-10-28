# MLSEC-09: Secure inter-node cluster communications

For frameworks such as TensorFlow, it’s common to share
information like coefficients as part of the inter-node cluster
communications. The algorithms require that exchanged
information stay synchronized across nodes. Secure this
information through encryption in transit.

## Implementation plan

- **Enable inter-node encryption in
  Amazon SageMaker AI**- In distributed computing
  environments, data transmitted between nodes can traverse
  wide networks, or even the internet. Enable inter-node
  encryption through the appropriate controls for the
  technology choices made. You can instruct SageMaker AI to
  automatically encrypt inter-container communication for
  your training job to ensure that data is passed over an
  encrypted tunnel.
- **Enable encryption in transit in
  Amazon EMR** - There are many applications and
  execution engines in the Hadoop ecosystem, providing a
  variety of tools to match the needs of your ML and
  analytics workloads.
  [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") has distributed cluster capabilities and is
  also an option for running training jobs on the data that
  is either stored locally on the cluster or in
  [Amazon S3](https://aws.amazon.com/s3/?nc2=h_m1 "https://aws.amazon.com/s3/?nc2=h_m1"). Amazon EMR makes it easy to create and manage
  fully configured, elastic clusters of Amazon EC2 instances
  running Hadoop and other applications in the Hadoop
  ecosystem. Amazon EMR provides
  [security
  configurations](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md") to set up data encryption at rest
  while stored on Amazon S3 and local
  [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") volumes. It also allows the set-up of Transport
  Layer Security (TLS) certificates for the encryption of
  data in transit.

## Documents

- [Protect
  Communications Between ML Compute Instances in a
  Distributed Training Job](../../../sagemaker/latest/dg/train-encrypt.md "../../../sagemaker/latest/dg/train-encrypt.md")
- [Amazon EMR Management guide - Security Data Protection &
  Encryption Options](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md")
- [Apache
  Hadoop on Amazon EMR](https://aws.amazon.com/emr/features/hadoop/ "https://aws.amazon.com/emr/features/hadoop/")

## Blogs

- [Encrypt
  data in transit using a TLS custom certificate provider
  with Amazon EMR](https://aws.amazon.com/blogs/big-data/encrypt-data-in-transit-using-a-tls-custom-certificate-provider-with-amazon-emr/ "https://aws.amazon.com/blogs/big-data/encrypt-data-in-transit-using-a-tls-custom-certificate-provider-with-amazon-emr/")
- [Secure
  Amazon EMR with Encryption](https://aws.amazon.com/blogs/big-data/secure-amazon-emr-with-encryption "https://aws.amazon.com/blogs/big-data/secure-amazon-emr-with-encryption")

## Examples

- [Protect
  Communications Between ML Compute Instances in a
  Distributed Training Job](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/train-encrypt.md "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/train-encrypt.md")
- [TF
  Encrypted](https://pypi.org/project/tensorflow-encrypted/ "https://pypi.org/project/tensorflow-encrypted/")
