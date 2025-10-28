Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Identity and Access Management in AWS Snowball Edge

Every AWS Snowball Edge job must be authenticated. You do this by creating and managing the
IAM users in your account. Using IAM, you can create and manage users and permissions in
AWS.

AWS Snowball Edge users must have certain IAM-related permissions to access the
AWS Snowball Edge AWS Management Console to create jobs. An IAM user that creates an import or export job
must also have access to the right Amazon Simple Storage Service (Amazon S3) resources, such as the Amazon S3 buckets to be
used for the job, AWS KMS resources, Amazon SNS topic, and Amazon EC2-compatible AMI for edge compute jobs.

###### Important

For information about using IAM locally on your device, see [Using IAM locally on a Snowball Edge](using-local-iam.md "using-local-iam.md").

###### Topics

- [Access Control for Snowball Edge Console
  and Creating Jobs](authentication-and-access-control.md "authentication-and-access-control.md")
