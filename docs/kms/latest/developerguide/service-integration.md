# Using AWS KMS encryption with AWS services

With AWS Key Management Service, you can provide encryption keys for protecting data in other AWS services.
Using AWS KMS encryption with AWS services refers to the process of integrating AWS KMS with other
AWS services to encrypt and decrypt data at rest or in transit. Developers, system
administrators, and security professionals might be interested in this topic to secure sensitive
data stored or transmitted through AWS services, meet regulatory compliance requirements, or
implement encryption best practices. Common use cases include encrypting Amazon EBS volumes,
Amazon S3 buckets, and Amazon RDS databases. The following sections will cover the steps to
configure and manage AWS KMS encryption keys for specific AWS services, ensuring data
confidentiality and integrity across your AWS environment.For the complete list of AWS services
integrated with AWS KMS, see [AWS Service
Integration](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration").

The following topics discuss in detail how particular services use AWS KMS, including the
KMS keys they support, how they manage data keys, the permissions they require, and how to
track each service's use of the KMS keys in your account.

###### Important

[AWS services that
are integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration") use only symmetric encryption KMS keys to encrypt your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is symmetric or asymmetric, see [Identify different key types](identify-key-types.md "identify-key-types.md").

###### Topics

- [Amazon Elastic Block Store (Amazon EBS)](services-ebs.md "services-ebs.md")
- [Amazon EMR](services-emr.md "services-emr.md")
- [Amazon Redshift](services-redshift.md "services-redshift.md")
