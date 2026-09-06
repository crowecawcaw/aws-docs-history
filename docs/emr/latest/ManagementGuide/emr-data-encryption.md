

# Encrypt data at rest and in transit with Amazon EMR
<a name="emr-data-encryption"></a>

Data encryption helps prevent unauthorized users from reading data on a cluster and associated data storage systems. This includes data saved to persistent media, known as data *at rest*, and data that may be intercepted as it travels the network, known as data *in transit*.

Beginning with Amazon EMR version 4.8.0, you can use Amazon EMR security configurations to configure data encryption settings for clusters more easily. Security configurations offer settings to enable security for data in-transit and data at-rest in Amazon Elastic Block Store (Amazon EBS) volumes and EMRFS on Amazon S3. 

Optionally, beginning with Amazon EMR release version 4.1.0 and later, you can choose to configure transparent encryption in HDFS, which is not configured using security configurations. For more information, see [Transparent encryption in HDFS on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-encryption-tdehdfs.html) in the *Amazon EMR Release Guide*.

**Topics**
+ [Encryption options for Amazon EMR](emr-data-encryption-options.md)
+ [Encryption at rest using a customer KMS key for the EMR WAL service](encryption-at-rest-kms.md)
+ [Create keys and certificates for data encryption with Amazon EMR](emr-encryption-enable.md)
+ [Understanding in-transit encryption](emr-encryption-support-matrix.md)