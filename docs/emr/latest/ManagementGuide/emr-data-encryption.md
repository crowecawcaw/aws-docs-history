# Encrypt data at rest and in transit with Amazon EMR

Data encryption helps prevent unauthorized users from reading data on a cluster and
associated data storage systems. This includes data saved to persistent media, known as
data _at rest_, and data that may be intercepted as it travels the
network, known as data _in transit_.

Beginning with Amazon EMR version 4.8.0, you can use Amazon EMR security configurations to
configure data encryption settings for clusters more easily. Security configurations
offer settings to enable security for data in-transit and data at-rest in Amazon Elastic Block Store
(Amazon EBS) volumes and EMRFS on Amazon S3.

Optionally, beginning with Amazon EMR release version 4.1.0 and later, you can choose to
configure transparent encryption in HDFS, which is not configured using security
configurations. For more information, see [Transparent encryption in
HDFS on Amazon EMR](../ReleaseGuide/emr-encryption-tdehdfs.md "../ReleaseGuide/emr-encryption-tdehdfs.md") in the _Amazon EMR Release Guide_.

###### Topics

- [Encryption options for Amazon EMR](emr-data-encryption-options.md "emr-data-encryption-options.md")
- [Encryption at rest using a customer KMS key for the EMR WAL service](encryption-at-rest-kms.md "encryption-at-rest-kms.md")
- [Create keys and certificates for data encryption with Amazon EMR](emr-encryption-enable.md "emr-encryption-enable.md")
- [Understanding in-transit encryption](emr-encryption-support-matrix.md "emr-encryption-support-matrix.md")
