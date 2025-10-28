# Detective security best

practices for Amazon Keyspaces

The following security best practices are considered detective because they can help you detect potential security
weaknesses and incidents.

**Use AWS CloudTrail to monitor AWS Key Management Service (AWS KMS) AWS KMS key usage**

If you're using a [customer
managed AWS KMS key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for encryption at rest, usage of this key
is logged into AWS CloudTrail. CloudTrail provides visibility into user activity by
recording actions taken on your account. CloudTrail records important information
about each action, including who made the request, the services used, the
actions performed, parameters for the actions, and the response elements
returned by the AWS service. This information helps you track changes made
to your AWS resources and troubleshoot operational issues. CloudTrail makes it
easier to ensure compliance with internal policies and regulatory
standards.

You can use CloudTrail to audit key usage. CloudTrail creates log files that contain a
history of AWS API calls and related events for your account. These log
files include all AWS KMS API requests that were made using the console,
AWS SDKs, and command line tools, in addition to those made through
integrated AWS services. You can use these log files to get information
about when the AWS KMS key was used, the operation that was requested, the
identity of the requester, the IP address that the request came from, and so
on. For more information, see [Logging
AWS Key Management Service API Calls with AWS CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md "../../../kms/latest/developerguide/logging-using-cloudtrail.md") and the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

**Use CloudTrail to monitor Amazon Keyspaces data definition language (DDL) operations**

CloudTrail provides visibility into user activity by recording actions taken on
your account. CloudTrail records important information about each action,
including who made the request, the services used, the actions performed,
parameters for the actions, and the response elements returned by the AWS
service. This information helps you to track changes made to your AWS
resources and to troubleshoot operational issues. CloudTrail makes it easier to
ensure compliance with internal policies and regulatory standards.

All Amazon Keyspaces [DDL operations](cql.md "cql.md") are logged in CloudTrail automatically. DDL
operations let you create and manage Amazon Keyspaces keyspaces and tables.

When activity occurs in Amazon Keyspaces, that activity is recorded in a CloudTrail event
along with other AWS service events in the event history. For more
information, see [Logging Amazon Keyspaces operations by using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md"). You can
view, search, and download recent events in your AWS account. For more

information, see [Viewing

events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail
User Guide_.

For an ongoing record of events in your AWS account, including events for
Amazon Keyspaces, create a [trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md"). A trail enables CloudTrail to deliver log files to an Amazon Simple Storage Service
(Amazon S3) bucket. By default, when you create a trail on the console, the trail
applies to all AWS Regions. The trail logs events from all Regions in the
AWS partition and delivers the log files to the S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and
act upon the event data collected in CloudTrail logs.

**Tag your Amazon Keyspaces resources for identification and automation**

You can assign metadata to your AWS resources in the form of tags. Each

tag is a simple label that consists of a customer-defined key and an
optional value that can make it easier to manage, search for, and filter
resources.

Tagging allows for grouped controls to be implemented. Although there are
no inherent types of tags, they enable you to categorize resources by
purpose, owner, environment, or other criteria. The following are some
examples:

- Access – Used to control access to Amazon Keyspaces resources based on tags. For more information,
  see [Authorization based on
  Amazon Keyspaces tags](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").
- Security – Used to determine requirements such as data
  protection settings.
- Confidentiality – An identifier for the specific
  data-confidentiality level that a resource supports.
- Environment – Used to distinguish between development,
  test, and production infrastructure.

For more information, see [AWS tagging strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/") and [Adding tags and labels to resources](tagging-keyspaces.md "tagging-keyspaces.md").
