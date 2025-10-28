# Prerequisites

Before you begin, make sure that you have completed the following
prerequisites.

**In Amazon S3, make sure you have:**

- [Created an Amazon S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") and copied
  it's name.

###### Note

Your bucket must be in the same AWS Region as your Amazon Q
index, and your index must have permissions to access the bucket that
contains your documents.

- If using Amazon VPC with Amazon S3 connector, made sure that you have
  assigned an Amazon S3 endpoint to your virtual private cloud (VPC). For more
  information about configuring an Amazon S3 connector with Amazon VPC, see [Using Amazon VPC with Amazon S3](s3-vpc-example-1.md "s3-vpc-example-1.md").
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Amazon S3 authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
