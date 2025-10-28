# Setting up the IAM policy for asynchronous

synthesis

In order to use the asynchronous synthesis functionality, you will need an IAM policy
that allows the following:

- use of new Amazon Polly operations
- writing to the output S3 bucket
- publishing to the status SNS topic [optional]
  The following policy grants only the necessary permissions required for asynchronous
  synthesis and can be attached to the IAM user.
