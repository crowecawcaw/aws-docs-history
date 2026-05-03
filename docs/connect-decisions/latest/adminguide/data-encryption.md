# Data Encryption

This topic provides information specific to Amazon Connect Decisions about encryption in transit and encryption at rest.

## Encryption in transit

All communication between customers and Amazon Connect Decisions and between
Amazon Connect Decisions and its downstream dependencies is protected using TLS 1.2 or
higher connections.

## Encryption at rest

Amazon Connect Decisions stores data at rest using DynamoDB and Amazon Simple Storage Service (Amazon S3). The data
at rest is encrypted using AWS encryption solutions by default.
Amazon Connect Decisions encrypts your data using AWS owned encryption keys from AWS Key Management Service
(AWS KMS). You don't have to take any action to protect the AWS managed keys that
encrypt your data. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS KMS Developer Guide_.

If you change the KMS key used to encrypt data on your Amazon Connect Decisions
instance in the AWS console, you must create a new instance to begin using the new key
to encrypt your data. Any data that were encrypted with the previous key won't be
retained, and only data will be encrypted with the updated key. If you want to maintain
your data from a previous encryption method, you can revert to the key you were using
during those conversations.

Your conversations with Amazon Connect Decisions on the webapp and in chat applications
are only encrypted with AWS-owned keys.
