# Configure advanced settings

The following section contains details about the advanced settings for your
Firehose stream.

- Server-side encryption - Amazon Data Firehose supports Amazon S3 server-side
  encryption with AWS Key Management Service (AWS KMS) for encrypting
  delivered data in Amazon S3. For more information, see [Protecting Data Using Server-Side Encryption with AWS KMS–Managed Keys
  (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").
- Error logging - Amazon Data Firehose logs errors related to processing and delivery. Additionally, when data transformation is enabled, it can log Lambda invocations and send data delivery errors to CloudWatch Logs. For more information, see [Monitor Amazon Data Firehose Using
  CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").

###### Important

While optional, enabling Amazon Data Firehose error logging during Firehose stream creation is strongly recommended. This practice ensures that you can access error details in case of record processing or delivery failures.

- Permissions - Amazon Data Firehose uses IAM roles for all the permissions that the
  Firehose stream needs. You can choose to create a new role where required permissions
  are assigned automatically, or choose an existing role created for Amazon Data Firehose.
  The role is used to grant Firehose access to various services, including your S3
  bucket, AWS KMS key (if data encryption is enabled), and Lambda function (if
  data transformation is enabled). The console might create a role with
  placeholders. For more information, see [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

###### Note

The IAM role (including placeholders) is created based on the
configuration you choose when creating a Firehose stream. If you make any changes
to the Firehose stream source or destination, you must manually update the IAM
role.

- Tags - You can add tags to organize your AWS resources, track costs, and
  control access.

If you specify tags in the `CreateDeliveryStream` action, Amazon Data Firehose
performs an additional authorization on the
`firehose:TagDeliveryStream` action to verify if users have
permissions to create tags. If you do not provide this permission, requests to
create new Firehose streams with IAM resource tags will fail with an
`AccessDeniedException` such as following.

```
AccessDeniedException
User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.
```

The following example demonstrates a policy that allows users to create a
Firehose stream and apply tags.
Once you've chosen your backup and advanced settings, review your choices, and then choose
**Create Firehose stream**.

The new Firehose stream takes a few moments in the **Creating**
state before it is available. After your Firehose stream is in an **Active** state, you can start sending data to it from your producer.
