Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Data at rest

Your data is encrypted at rest in the cloud using one of two types of keys through
AWS Key Management Service (AWS KMS). The data is encrypted in Amazon Simple Storage Service (Amazon S3) using an
AWS owned key. Amazon Monitron also stores data in tables in Amazon DynamoDB. By
default, these are encrypted using an AWS owned CMK. However, if a customer chooses
**Custom encryption settings** when setting up a project,
Amazon Monitron uses a customer managed CMK.

See also [Using server-side encryption for the Kinesis stream](monitron-kinesis-export.md#data-export-server-side-encryption "monitron-kinesis-export.md#data-export-server-side-encryption").
