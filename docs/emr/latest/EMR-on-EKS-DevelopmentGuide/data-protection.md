# Data protection

The AWS [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon EMR on EKS. As described in this
model, AWS is responsible for protecting the global infrastructure that runs all of the AWS
Cloud. You are responsible for maintaining control over your content that is hosted on this
infrastructure. This content includes the security configuration and management tasks for the
AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/") . For information
about data protection in Europe, see [the
AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the AWS Security Blog.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual accounts with AWS Identity and Access Management (IAM). That way each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or later.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering and securing personal data that is stored in Amazon S3.
- Use Amazon EMR on EKS encryption options to encrypt data at rest and in transit.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field.
  This includes when you work with Amazon EMR on EKS or other AWS services using the console, API, AWS CLI, or
  AWS SDKs. Any data that you enter into Amazon EMR on EKS or other services might get picked up for
  inclusion in diagnostic logs. When you provide a URL to an external server, don't include
  credentials information in the URL to validate your request to that server.

## Encryption at rest

Data encryption helps prevent unauthorized users from reading data on a cluster and associated data storage systems. This includes data saved to persistent media, known as data at rest, and data that may be intercepted as it travels the network, known as data in transit.

Data encryption requires keys and certificates. You can choose from several options, including keys managed by AWS Key Management Service, keys managed by Amazon S3, and keys and certificates from custom providers that you supply. When using AWS KMS as your key provider, charges apply for the storage and use of encryption keys. For more information, see [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

Before you specify encryption options, decide on the key and certificate management systems you want to use. Then create the keys and certificates for the custom providers that you specify as part of encryption settings.

### Encryption at rest for EMRFS data in Amazon S3

Amazon S3 encryption works with EMR File System (EMRFS) objects read from and written to Amazon S3. You specify Amazon S3 server-side encryption (SSE) or client-side encryption (CSE) as the **Default encryption mode** when you enable encryption at rest. Optionally, you can specify different encryption methods for individual buckets using **Per bucket encryption overrides**. Regardless of whether Amazon S3 encryption is enabled, Transport Layer Security (TLS) encrypts the EMRFS objects in transit between EMR cluster nodes and Amazon S3. For in-depth information about Amazon S3 encryption, see [Protecting Data Using Encryption](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md") in the Amazon Simple Storage Service Developer Guide.

###### Note

When you use AWS KMS, charges apply for the storage and use of encryption keys. For more information, see [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### Amazon S3 server-side encryption

When you set up Amazon S3 server-side encryption, Amazon S3 encrypts data at the object level as it writes the data to disk and decrypts the data when it is accessed. For more information about SSE, see [Protecting Data Using Server-Side Encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md") in the Amazon Simple Storage Service Developer Guide.

You can choose between two different key management systems when you specify SSE in Amazon EMR on EKS:

- **SSE-S3** ‐ Amazon S3 manages keys for you.
- **SSE-KMS** ‐ You use an AWS KMS key to set up with policies suitable for Amazon EMR on EKS.

SSE with customer-provided keys (SSE-C) is not available for use with Amazon EMR on EKS.

### Amazon S3 client-side encryption

With Amazon S3 client-side encryption, the Amazon S3 encryption and decryption takes place in the EMRFS client on your cluster. Objects are encrypted before being uploaded to Amazon S3 and decrypted after they are downloaded. The provider you specify supplies the encryption key that the client uses. The client can use keys provided by AWS KMS (CSE-KMS) or a custom Java class that provides the client-side root key (CSE-C). The encryption specifics are slightly different between CSE-KMS and CSE-C, depending on the specified provider and the metadata of the object being decrypted or encrypted. For more information about these differences, see [Protecting Data Using Client-Side Encryption](../../../AmazonS3/latest/dev/UsingClientSideEncryption.md "../../../AmazonS3/latest/dev/UsingClientSideEncryption.md") in the Amazon Simple Storage Service Developer Guide.

###### Note

Amazon S3 CSE only ensures that EMRFS data exchanged with Amazon S3 is encrypted; not all data on cluster instance volumes is encrypted. Furthermore, because Hue does not use EMRFS, objects that the Hue S3 File Browser writes to Amazon S3 are not encrypted.

### Local disk encryption

Apache Spark supports encrypting temporary data written to local disks. This covers shuffle
files, shuffle spills, and data blocks stored on disk for both caching and broadcast
variables. It does not cover encrypting output data generated by applications with APIs such
as `saveAsHadoopFile` or `saveAsTable`. It also may not cover
temporary files created explicitly by the user. For more information, see [Local
Storage Encryption](https://spark.apache.org/docs/latest/security.html#local-storage-encryption "https://spark.apache.org/docs/latest/security.html#local-storage-encryption") in the Spark documentation. Spark does not support encrypted
data on local disk, such as intermediate data written to a local disk by an executor process
when the data does not fit in memory. Data that is persisted to disk is scoped to the job
runtime, and the key that is used to encrypt the data is generated dynamically by Spark for
every job run. Once the Spark job terminates, no other process can decrypt the data.

For driver and executor pod, you encrypt data at rest that is persisted to the mounted
volume. There are three different AWS native storage options you can use with Kubernetes:
[EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md"),
[EFS](../../../AWSEC2/latest/UserGuide/AmazonEFS.md "../../../AWSEC2/latest/UserGuide/AmazonEFS.md"), and
[FSx for
Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md"). All three offer encryption at rest using a service managed key or an AWS KMS key. For more information see the [EKS Best Practices
Guide](https://aws.github.io/aws-eks-best-practices/security/docs/data "https://aws.github.io/aws-eks-best-practices/security/docs/data"). With this approach, all data persisted to the mounted volume is
encrypted.

### Key management

You can configure KMS to automatically rotate your KMS keys. This rotates your keys once a year while saving old keys indefinitely so that your data can still be decrypted. For additional information, see [Rotating AWS KMS keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").

## Encryption in transit

Several encryption mechanisms are enabled with in-transit encryption. These are open-source features, are application-specific, and may vary by Amazon EMR on EKS release. The following application-specific encryption features can be enabled with Amazon EMR on EKS:

- Spark

      + Internal RPC communication between Spark components, such as the block transfer service and the external shuffle service, is encrypted using the AES-256 cipher in Amazon EMR versions 5.9.0 and later. In earlier releases, internal RPC communication is encrypted using SASL with DIGEST-MD5 as the cipher.
      + HTTP protocol communication with user interfaces such as Spark History Server and HTTPS-enabled file servers is encrypted using Spark's SSL configuration. For more information, see [SSL Configuration](https://spark.apache.org/docs/latest/security.html#ssl-configuration "https://spark.apache.org/docs/latest/security.html#ssl-configuration") in Spark documentation.

  For more information, see [Spark security settings](http://spark.apache.org/docs/latest/security.html "http://spark.apache.org/docs/latest/security.html").

- You should allow only encrypted connections over HTTPS (TLS) using [the aws:SecureTransport condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") on Amazon S3 bucket IAM policies.
- Query results that stream to JDBC or ODBC clients are encrypted using TLS.
