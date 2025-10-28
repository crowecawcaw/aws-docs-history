# Use AMS SSP to provision Amazon Simple Email Service in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Simple Email Service (Amazon SES) capabilities directly in your AMS managed account. Amazon Simple Email Service is a cloud-based email sending service designed to help digital marketers and application developers, send marketing,
notification, and transactional emails.

You can use the SMTP interface or one of the AWS SDKs to integrate Amazon SES directly into your
existing applications. You can also integrate the email sending capabilities of Amazon SES into the
software you already use, such as ticketing systems and email clients.

To learn more, see [Amazon Simple Email Service](https://aws.amazon.com/ses/ "https://aws.amazon.com/ses/").

## Amazon SES in AWS Managed Services FAQ

**Q: How do I request access to Amazon SES in my AMS account?**

Request access to Amazon SES by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer_ses_admin_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the prerequisites or dependencies to using Amazon SES in my AMS account?**

- You must configure an S3 bucket policy
  to allow Amazon SES to publish events to the bucket.
- You must use a default (AWS SES), or configure, a CMK key to allow Amazon SES to encrypt emails and
  push events to other service resources such as Amazon S3, Amazon SNS, Lambda, and
  Firehose, belonging to the account.

**Q: What are the restrictions to using Amazon SES in my AMS account?**

You must raise RFCs to create the following resources:

- An SMTP user and IAM service role with PutEvents permission, to a Kinesis Firehose
  stream.
- You must create new AWS resources such as S3 bucket, Firehose stream, SNS topic by using AMS
  change types in order for your Amazon SES rules and configuration sets'
  destinations to work with those resources.
- SMTP credentials. To request new SMTP credentials, use the Change Type
  (Management | Other | Other | Create). AMS creates the credentials and adds them to Secrets Manager for you.
