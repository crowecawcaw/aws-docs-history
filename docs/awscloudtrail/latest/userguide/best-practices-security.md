# Security best practices in AWS CloudTrail

AWS CloudTrail provides a number of security features to consider as you develop and implement
your own security policies. The following best practices are general guidelines and don’t
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

###### Topics

- [CloudTrail detective security best
  practices](#best-practices-security-detective "#best-practices-security-detective")
- [CloudTrail preventative security best
  practices](#best-practices-security-preventative "#best-practices-security-preventative")

## CloudTrail detective security best

practices

**Create a trail**

For an ongoing record of events in your AWS account, you must create a trail.
Although CloudTrail provides 90 days of event history information for management events in the
CloudTrail console without creating a trail, it is not a permanent record, and it does not
provide information about all possible types of events. For an ongoing record, and for a
record that contains all the event types you specify, you must create a trail, which
delivers log files to an Amazon S3 bucket that you specify.

To help manage your CloudTrail data, consider creating one trail that logs management events
in all AWS Regions, and then creating additional trails that log specific event types
for resources, such as Amazon S3 bucket activity or AWS Lambda functions.

The following are some steps you can take:

- [Create a trail for your AWS
  account.](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console")
- [Create a trail for an
  organization.](creating-trail-organization.md "creating-trail-organization.md")

**Create a multi-Region trail**

To obtain a complete record of events taken by an IAM identity, or service in your
AWS account, create a multi-Region trail. Multi-Region trails log events in all
AWS Regions that are [enabled](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") in your AWS account. By logging events in all enabled
AWS Regions, you ensure that you capture activity in all enabled
Regions in your AWS account. This includes logging [global service events](cloudtrail-concepts.md#cloudtrail-concepts-global-service-events "cloudtrail-concepts.md#cloudtrail-concepts-global-service-events"),
which are logged to an AWS Region specific to that service. All trails created using
the CloudTrail console are multi-Region trails.

The following are some steps you can take:

- [Create a trail for your AWS
  account.](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console")
- [Convert an existing single-Region trail](cloudtrail-update-a-trail-console.md "cloudtrail-update-a-trail-console.md") to a multi-Region trail.
- Implement ongoing detective controls to help ensure all trails created are
  logging events in all AWS Regions by using the [multi-region-cloud-trail-enabled](../../../config/latest/developerguide/multi-region-cloudtrail-enabled.md "../../../config/latest/developerguide/multi-region-cloudtrail-enabled.md") rule in AWS Config.

**Enable CloudTrail log file integrity**

Validated log files are especially valuable in security and forensic investigations.
For example, a validated log file enables you to assert positively that the log file
itself has not changed, or that particular IAM identity credentials performed specific
API activity. The CloudTrail log file integrity validation process also lets you know if a log
file has been deleted or changed, or assert positively that no log files were delivered
to your account during a given period of time. CloudTrail log file integrity validation uses
industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital
signing. This makes it computationally unfeasible to modify, delete or forge CloudTrail
log files without detection. For more information, see [Enabling validation and validating files](cloudtrail-log-file-validation-intro.md#cloudtrail-log-file-validation-intro-enabling-and-using "cloudtrail-log-file-validation-intro.md#cloudtrail-log-file-validation-intro-enabling-and-using").

**Integrate with Amazon CloudWatch Logs**

CloudWatch Logs allows you to monitor and receive alerts for specific events captured by CloudTrail.
The events sent to CloudWatch Logs are those configured to be logged by your trail, so make sure
you have configured your trail or trails to log the event types (management events
data events and/or network activity events) that you are interested in monitoring.

For example, you can monitor key security and network-related management events, such
as [failed AWS Management Console sign-in
events](cloudwatch-alarms-for-cloudtrail.md#cloudwatch-alarms-for-cloudtrail-signin "cloudwatch-alarms-for-cloudtrail.md#cloudwatch-alarms-for-cloudtrail-signin").

The following are some steps you can take:

- Review example [CloudWatch
  Logs integrations for CloudTrail](cloudwatch-alarms-for-cloudtrail.md "cloudwatch-alarms-for-cloudtrail.md").
- Configure your trail to [send events to
  CloudWatch Logs](monitor-cloudtrail-log-files-with-cloudwatch-logs.md "monitor-cloudtrail-log-files-with-cloudwatch-logs.md").
- Consider implementing ongoing detective controls to help ensure all trails are
  sending events to CloudWatch Logs for monitoring by using the [cloud-trail-cloud-watch-logs-enabled](../../../config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.md "../../../config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.md") rule in AWS Config.

**Use Amazon GuardDuty**

Amazon GuardDuty is a threat detection service that helps you protect your
accounts, containers, workloads, and the data within your AWS environment.
By using machine learning (ML) models, and anomaly and threat detection capabilities,
GuardDuty continuously monitors different log sources to identify, and prioritize
potential security risks and malicious activities in your environment.

For example, GuardDuty will detect potential credential exfiltration
in case it detects credentials that were created exclusively for an Amazon EC2 instance
through an instance launch role but are being used from another account within
AWS. For more information, see the [_Amazon GuardDuty User Guide_](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md").

**Use AWS Security Hub**

Monitor your usage of CloudTrail as it relates to security best practices by using [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md").
Security Hub uses detective _security controls_ to evaluate resource configurations and _security standards_ to help you comply with various
compliance frameworks. For more information about using Security Hub to evaluate CloudTrail resources, see [AWS CloudTrail controls](../../../securityhub/latest/userguide/cloudtrail-controls.md "../../../securityhub/latest/userguide/cloudtrail-controls.md")
in the _AWS Security Hub User Guide_.

## CloudTrail preventative security best

practices

The following best practices for CloudTrail can help prevent security incidents.

**Log to a dedicated and centralized Amazon S3 bucket**

CloudTrail log files are an audit log of actions taken by an IAM identity or an AWS
service. The integrity, completeness and availability of these logs is crucial for
forensic and auditing purposes. By logging to a dedicated and centralized Amazon S3 bucket,
you can enforce strict security controls, access, and segregation of duties.

The following are some steps you can take:

- Create a separate AWS account as a log archive account. If you use AWS Organizations,
  enroll this account in the organization, and consider [creating an organization trail](creating-trail-organization.md "creating-trail-organization.md")
  to log data for all AWS accounts in your organization.
- If you do not use Organizations but want to log data for multiple AWS accounts, [create a trail](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console") to log
  activity in this log archive account. Restrict access to this account to only
  trusted administrative users who should have access to account and auditing
  data.
- As part of creating a trail, whether it is an organization trail or a trail
  for a single AWS account, create a dedicated Amazon S3 bucket to store log files
  for this trail.
- If you want to log activity for more than one AWS account, [modify the
  bucket policy](cloudtrail-set-bucket-policy-for-multiple-accounts.md "cloudtrail-set-bucket-policy-for-multiple-accounts.md") to allow logging and storing log files for all AWS
  accounts that you want to log AWS account activity.
- If you are not using an organization trail, create trails in all of your AWS
  accounts, specifying the Amazon S3 bucket in the log archive account.

**Use server-side encryption with AWS KMS managed
keys**

By default, the log files delivered by CloudTrail to your S3 bucket are encrypted by using
[server-side encryption with a
KMS key (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md"). To use SSE-KMS with CloudTrail, you create and manage an
[AWS KMS key](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md"), also known as a
KMS key.

###### Note

If you use SSE-KMS and log file validation, and you have modified your Amazon S3 bucket
policy to only allow SSE-KMS encrypted files, you will not be able to create trails
that utilize that bucket unless you modify your bucket policy to specifically allow
AES256 encryption, as shown in the following example policy line.

```
"StringNotEquals": { "s3:x-amz-server-side-encryption": ["aws:kms", "AES256"] }
```

The following are some steps you can take:

- [Review the
  advantages of encrypting your log files with SSE-KMS](encrypting-cloudtrail-log-files-with-aws-kms.md "encrypting-cloudtrail-log-files-with-aws-kms.md").
- [Create a KMS key to use
  for encrypting log files](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md").
- [Configure
  log file encryption for your trails.](create-kms-key-policy-for-cloudtrail-update-trail.md "create-kms-key-policy-for-cloudtrail-update-trail.md")
- Consider implementing ongoing detective controls to help ensure all trails are
  encrypting log files with SSE-KMS by using the [cloud-trail-encryption-enabled](../../../config/latest/developerguide/cloud-trail-encryption-enabled.md "../../../config/latest/developerguide/cloud-trail-encryption-enabled.md") rule in AWS Config.

**Add a condition key to the default Amazon SNS topic
policy**

When you configure a trail to send notifications to Amazon SNS, CloudTrail adds a policy
statement to your SNS topic access policy that allows CloudTrail to send content to an SNS
topic. As a security best practice, we recommend adding an `aws:SourceArn`
(or optionally `aws:SourceAccount`) condition key to the Amazon SNS topic policy
statement. This helps prevent unauthorized account access to your SNS topic. For more
information, see [Amazon SNS topic policy for CloudTrail](cloudtrail-permissions-for-sns-notifications.md "cloudtrail-permissions-for-sns-notifications.md").

**Implement least privilege access to Amazon S3 buckets where you store
log files**

CloudTrail trails log events to an Amazon S3 bucket that you specify. These log files contain an
audit log of actions taken by IAM identities and AWS services. The integrity and
completeness of these log files are crucial for auditing and forensic purposes. In order
to help ensure that integrity, you should adhere to the principle of least privilege
when creating or modifying access to any Amazon S3 bucket used for storing CloudTrail log files.

Take the following steps:

- Review the [Amazon S3 bucket
  policy](create-s3-bucket-policy-for-cloudtrail.md "create-s3-bucket-policy-for-cloudtrail.md") for any and all buckets where you store log files and adjust
  it if necessary to remove any unnecessary access. This bucket policy will be
  generated for you if you create a trail using the CloudTrail console, but can also be
  created and managed manually.
- As a security best practice, be sure to manually add a
  `aws:SourceArn` condition key to the bucket policy. For more
  information, see [Amazon S3 bucket policy for CloudTrail](create-s3-bucket-policy-for-cloudtrail.md "create-s3-bucket-policy-for-cloudtrail.md").
- If you are using the same Amazon S3 bucket to store log files for multiple AWS
  accounts, follow the guidance for [receiving log files
  for multiple accounts](cloudtrail-receive-logs-from-multiple-accounts.md "cloudtrail-receive-logs-from-multiple-accounts.md").
- If you are using an organization trail, make sure you follow the guidance for
  [organization trails](creating-trail-organization.md "creating-trail-organization.md"), and
  review the example policy for an Amazon S3 bucket for an organization trail in [Creating a trail for an organization with the AWS CLI](cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.md "cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.md").
- Review the [Amazon S3 security
  documentation](../../../AmazonS3/latest/userguide/security.md "../../../AmazonS3/latest/userguide/security.md") and the [example walkthrough for securing a bucket](../../../AmazonS3/latest/userguide/walkthrough1.md "../../../AmazonS3/latest/userguide/walkthrough1.md").

**Enable MFA delete on the Amazon S3 bucket where you store log
files**

When you configure multi-factor authentication (MFA), attempts to change the
versioning state of bucket, or delete an object version in a bucket, require additional
authentication. This way, even if a user acquires the password of an IAM user with
permissions to permanently delete Amazon S3 objects, you can still prevent operations that
could compromise your log files.

The following are some steps you can take:

- Review the [MFA
  delete](../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md "../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md") guidance in the _Amazon Simple Storage Service User Guide_.
- [Add an Amazon S3 bucket policy to require MFA](../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-MFA "../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-MFA").

###### Note

You cannot use MFA delete with lifecycle configurations. For more information
about lifecycle configurations and how they interact with other configurations, see
[Lifecycle
and other bucket configurations](../../../AmazonS3/latest/userguide/lifecycle-and-other-bucket-config.md "../../../AmazonS3/latest/userguide/lifecycle-and-other-bucket-config.md") in the
_Amazon Simple Storage Service User Guide_.

**Configure object lifecycle management on the Amazon S3 bucket where
you store log files**

The CloudTrail trail default is to store log files indefinitely in the Amazon S3 bucket
configured for the trail. You can use the [Amazon S3 object lifecycle management rules](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to define your own retention
policy to better meet your business and auditing needs. For example, you might want to
archive log files that are more than a year old to Amazon Glacier, or delete log files
after a certain amount of time has passed.

###### Note

Lifecycle configuration on multi-factor authentication (MFA)-enabled buckets is
not supported.

**Limit access to the AWSCloudTrail_FullAccess
policy**

Users with the [AWSCloudTrail_FullAccess](security_iam_id-based-policy-examples.md#grant-custom-permissions-for-cloudtrail-users-full-access "security_iam_id-based-policy-examples.md#grant-custom-permissions-for-cloudtrail-users-full-access") policy have the ability to disable or reconfigure
the most sensitive and important auditing functions in their AWS accounts. This policy
is not intended to be shared or applied broadly to IAM identities in your AWS
account. Limit application of this policy to as few individuals as possible, those you
expect to act as AWS account administrators.
