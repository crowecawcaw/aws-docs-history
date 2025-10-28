# Technical FAQ—Amazon S3

**Q: Where can I get the Amazon Simple Storage Service (Amazon S3) REST API documentation?**

For more
information, refer to the
[Amazon S3 REST API Introduction](../../../AmazonS3/latest/API/Welcome.md "../../../AmazonS3/latest/API/Welcome.md").

**Q: How do I get the Amazon Web Services
AWS Key Management Service (AWS KMS) key details to authenticate
to access the Amazon S3 bucket?**

AWS Partner Network
(APN) shares a policy that includes the key name.

**Q: How do I authenticate Amazon S3 from
Salesforce.com (SFDC)?**

Use the sample code file
[S3_Authentication.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/S3_Authentication.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/S3_Authentication.cls")
to authenticate the Amazon S3 from SFDC.

**Q: How do I upload the file from the AWS
software development kit (SDK) to S3?**

Use the following
AWS CLI command to upload the file to S3.

```

aws s3 cp example.json s3://awsexamplebucket/opportunity- inbound/filename.json --acl bucket-owner-full-control

```

The sample code file
[Sample_AceOutboundBatch.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Sample_AceOutboundBatch.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Sample_AceOutboundBatch.cls")
contains code to upload the data file from SFDC.

**Q: Who owns the Amazon S3 bucket?**

AWS owns and manages the Amazon S3 bucket. You have
programmatic access to your own Amazon S3 bucket with the AWS Identity and Access Management (IAM) user.

**Q: Are there separate folders or buckets for
receiving and sending files?**

There is one bucket with
different folders for receiving and sending the files. Refer to the
user guide for further details on the folders.

**Q: Do I need to access the Amazon S3 bucket using
AWS Lambda, or can I access it directly using the customer
relationship management (CRM) system?**

You can access it both ways.

**Q: Is the Amazon S3 bucket secured or
encrypted?**

Yes. We enable the default encryption
mechanism that Amazon S3 offers.

**Q: Is it possible to enable Amazon Simple Notification Service (Amazon SNS) listening to the Amazon S3 bucket, so I
can only act on the event, instead of polling periodically?**

No. Currently, APN
Customer Engagement (ACE) doesn’t support this feature.

**Q: What folders do I have access
to and what is the purpose of each folder?**

You can find the list of Amazon S3 folders in
[Integration prerequisites](crm-integration-setting-up.md "crm-integration-setting-up.md").
