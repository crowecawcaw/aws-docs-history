# Encryption on Amazon MWAA

The following topics describe how Amazon MWAA protects your data at rest, and in transit. Use this information to learn how Amazon MWAA integrates with AWS KMS to encrypt
data at rest, and how data is encrypted using Transport Layer Security (TLS) protocol in transit.

###### Topics

- [Encryption at rest](#encryption-at-rest "#encryption-at-rest")
- [Encryption in transit](#encryption-in-transit "#encryption-in-transit")

## Encryption at rest

On Amazon MWAA, data _at rest_ is data that the service saves to persistent media.

You can use an [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") for data at rest encryption, or optionally provide a [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for additional encryption when you create an environment. If you choose to use a customer-managed KMS key,
it must be in the same account as the other AWS resources and services you are using with your environment.

To use a customer-managed KMS key, you must attach the required policy statement for CloudWatch access to your key policy. When you use a customer-managed KMS key for your environment,
Amazon MWAA attaches four [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") on your behalf. For more information about the grants Amazon MWAA attaches to a customer-managed KMS key, refer to
[Customer-managed keys for data encryption](custom-keys-certs.md "custom-keys-certs.md").

If you do not specify a customer-managed KMS key, by default, Amazon MWAA uses an AWS owned KMS key for to encrypt and decrypt your data. We recommend using an AWS owned KMS key to manage
data encryption on Amazon MWAA.

###### Note

You pay for the storage and use of AWS owned, or customer-managed KMS keys on Amazon MWAA. For more information, refer to [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### Encryption artifacts

You specify the encryption artifacts used for at rest encryption by specifying an [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") or [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") when you create your Amazon MWAA environment. Amazon MWAA adds the [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") needed to your specified key.

**Amazon S3** – Amazon S3 data is encrypted at the object-level using Server-Side Encryption (SSE). Amazon S3 encryption and decryption takes place on the Amazon S3 bucket where your DAG code and supporting files are stored.
Objects are encrypted when they are uploaded to Amazon S3 and decrypted when they are downloaded to your Amazon MWAA environment. By default, if you are using a customer-managed KMS key, Amazon MWAA uses it to read
and decrypt the data on your Amazon S3 bucket.

**CloudWatch Logs** – If you are using an AWS owned KMS key, Apache Airflow logs sent to CloudWatch Logs are encrypted using SSE with CloudWatch Logs's AWS owned KMS key. If you are using a customer-managed KMS key, you must add a
[key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") to your KMS key to allow CloudWatch Logs to use your key.

**Amazon SQS** – Amazon MWAA creates one Amazon SQS queue for your environment. Amazon MWAA handles encrypting data passed to and from the queue using SSE with either an AWS owned KMS key, or a customer-managed KMS key
that you specify. You must add Amazon SQS permissions to your execution role regardless of whether you are using an AWS owned or customer-managed KMS key.

**Aurora PostgreSQL** – Amazon MWAA creates one PostgreSQL cluster for your environment. Aurora PostgreSQL encrypts the content with either an AWS owned or customer-managed KMS key using SSE.
If you are using a customer-managed KMS key, Amazon RDS adds at least two grants to the key: one for the cluster and one for the database instance. Amazon RDS can create additional grants if you choose to use your customer-managed KMS key
on multiple environments. For more information, refer to [Data protection in Amazon RDS](../../../AmazonRDS/latest/UserGuide/DataDurability.md "../../../AmazonRDS/latest/UserGuide/DataDurability.md").

## Encryption in transit

Data in transit is referred to as data that can be intercepted as it travels the network.

Transport Layer Security (TLS) encrypts the Amazon MWAA objects in transit between your environment's Apache Airflow components and other AWS services that integrate with Amazon MWAA, such as Amazon S3.
For more information about Amazon S3 encryption, refer to [Protecting data using encryption](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md").
