# Data protection

The AWS [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon EMR Serverless. As described
in this model, AWS is responsible for protecting the global infrastructure that runs all of
the AWS Cloud. You are responsible for maintaining control over your content that is hosted on
this infrastructure. This content includes the security configuration and management tasks for
the AWS services that you use. For more information about data privacy, refer to the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information
about data protection in Europe, refer to [the
AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the AWS Security
Blog.

For data protection purposes, we suggest that you protect AWS account credentials and
set up individual accounts with AWS Identity and Access Management (IAM). That way each
user is given only the permissions necessary to fulfill their job duties. We also recommend that
you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We suggest TLS 1.2 or later.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS
  services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing personal data that is stored in Amazon S3.
- Use Amazon EMR Serverless encryption options to encrypt data at rest and in
  transit.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a
  command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, refer to [Federal
  Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly suggest that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field.
  This includes when you work with Amazon EMR Serverless or other AWS services using the console,
  API, AWS CLI, or AWS SDKs. Any data that you enter into Amazon EMR Serverless or other services
  might get picked up for inclusion in diagnostic logs. When you provide a URL to an external
  server, don't include credentials information in the URL to validate your request to that
  server.

## Encryption at rest

Data encryption helps prevent unauthorized users from reading data on a cluster and
associated data storage systems. This includes data saved to persistent media, known as data
at rest, and data that may be intercepted as it travels the network, known as data in
transit.

Data encryption requires keys and certificates. You can choose from several options,
including keys managed by AWS Key Management Service, keys managed by Amazon S3, and keys and certificates from
custom providers that you supply. When using AWS KMS as your key provider, charges apply for the
storage and use of encryption keys. For more information, refer to [AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

Before you specify encryption options, decide on the key and certificate management
systems you want to use. Then create the keys and certificates for the custom providers that
you specify as part of encryption settings.

### Encryption at rest for EMRFS data in Amazon S3

Each EMR Serverless application uses a specific release version, which includes EMRFS
(EMR File System). Amazon S3 encryption works with EMR File System (EMRFS) objects read from and
written to Amazon S3. You can specify Amazon S3 server-side encryption (SSE) or client-side encryption
(CSE) as the **Default encryption mode** when you enable encryption at
rest. Optionally, specify different encryption methods for individual buckets using
**Per bucket encryption overrides**. Regardless of whether Amazon S3
encryption is enabled, Transport Layer Security (TLS) encrypts the EMRFS objects in transit
between EMR cluster nodes and Amazon S3. If you use Amazon S3 CSE with customer-managed keys, your
execution role used to run jobs in an EMR Serverless application must have access to the
key. For in-depth information about Amazon S3 encryption, refer to [Protecting data using encryption](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md") in
the Amazon Simple Storage Service Developer Guide.

###### Note

When you use AWS KMS, charges apply for the storage and use of encryption keys. For more
information, refer to [AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### Amazon S3 server-side encryption

All Amazon S3 buckets have encryption configured by default, and all new objects that are uploaded to
an S3 bucket are automatically encrypted at rest, Amazon S3 encrypts data at the object level as
it writes the data to disk and decrypts the data when it is accessed. For more information
about SSE, refer to [Protecting data using server-side
encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md") in the Amazon Simple Storage Service Developer Guide.

You can choose between two different key management systems when you specify SSE in
Amazon EMR Serverless:

- **SSE-S3** ‐ Amazon S3 manages keys for you. No
  additional setup is required on EMR Serverless.
- **SSE-KMS** ‐ You use an AWS KMS key to set up
  with policies suitable for EMR Serverless. No additional setup is required on
  EMR Serverless.

To use AWS KMS encryption for data that you write to Amazon S3, you have two
options when you use the `StartJobRun` API. You can either enable encrytion for
everything that you write to Amazon S3, or enable encryption for data that
you write to a specific bucket. For more information about the `StartJobRun` API,
refer to the [EMR Serverless API Reference](https://amazonaws.com/emr-serverless/latest/APIReference/API_StartJobRun.html "https://amazonaws.com/emr-serverless/latest/APIReference/API_StartJobRun.html").

To turn on AWS KMS encryption for all data that you write to Amazon S3, use the
following commands when you call the `StartJobRun` API.

```
--conf spark.hadoop.fs.s3.enableServerSideEncryption=true
--conf spark.hadoop.fs.s3.serverSideEncryption.kms.keyId=`<kms_id>`
```

To turn on AWS KMS encryption for data that you write to a specific bucket, use the
following commands when you call the `StartJobRun` API.

```
--conf spark.hadoop.fs.s3.bucket.`<amzn-s3-demo-bucket1>`.enableServerSideEncryption=true
--conf spark.hadoop.fs.s3.bucket.`<amzn-s3-demo-bucket1>`.serverSideEncryption.kms.keyId=`<kms-id>`
```

SSE with customer-provided keys (SSE-C) is not available for use with
EMR Serverless.

### Amazon S3 client-side encryption

With Amazon S3 client-side encryption, the Amazon S3 encryption and decryption takes place in the
EMRFS client available on every Amazon EMR release. Objects are encrypted before being uploaded
to Amazon S3 and decrypted after they are downloaded. The provider you specify supplies the
encryption key that the client uses. The client can use keys provided by AWS KMS (CSE-KMS) or
a custom Java class that provides the client-side root key (CSE-C). The encryption specifics
are slightly different between CSE-KMS and CSE-C, depending on the specified provider and
the metadata of the object being decrypted or encrypted. If you use Amazon S3 CSE with
customer-managed keys, your execution role used to run jobs in an EMR Serverless
application must have access to the key. Additional KMS charges may apply. For more
information about these differences, refer to [Protecting data using client-side
encryption](../../../AmazonS3/latest/dev/UsingClientSideEncryption.md "../../../AmazonS3/latest/dev/UsingClientSideEncryption.md") in the Amazon Simple Storage Service Developer Guide.

### Local disk encryption

Data stored in ephemeral storage is encrypted with service owned keys using industry
standard AES-256 cryptographic algorithm.

### Key management

You can configure KMS to automatically rotate your KMS keys. This rotates your keys
once a year while saving old keys indefinitely so that your data can still be decrypted. For
additional information, refer to [Rotating customer-managed
keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").

## Encryption in transit

The following application-specific encryption features are available with
Amazon EMR Serverless:

- Spark
  - By default, communication between Spark drivers and executors is authenticated and
    internal. RPC communication between drivers and executors is encrypted.

- Hive
  - Communication between the AWS Glue metastore and EMR Serverless applications happens
    via TLS.

You should allow only encrypted connections over HTTPS (TLS) using [the aws:SecureTransport condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") on Amazon S3 bucket IAM policies.
