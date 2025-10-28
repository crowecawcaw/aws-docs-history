# Working with CloudTrail trails

_Trails_ capture a record of AWS activities, delivering and storing
these events in an Amazon S3 bucket, with optional delivery to [CloudWatch Logs](send-cloudtrail-events-to-cloudwatch-logs.md "send-cloudtrail-events-to-cloudwatch-logs.md") and [Amazon EventBridge](cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-eventbridge "cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-eventbridge").

You can deliver one copy of your ongoing management events to your S3 bucket at no
charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more
information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

You can create both multi-Region and single-Region trails for your AWS account.

**Multi-Region trails**

When you create a multi-Region trail, CloudTrail records events
in all AWS Regions that are [enabled](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") in your AWS account and delivers the CloudTrail event log files to an
S3 bucket that you specify. As a best practice, we recommend creating a
multi-Region trail because it captures activity in all enabled Regions. All trails created
using the CloudTrail console are multi-Region trails. You can convert a single-Region trail
to a multi-Region trail by using the AWS CLI. For
more information, see [Understanding multi-Region trails and
opt-in Regions](cloudtrail-multi-region-trails.md "cloudtrail-multi-region-trails.md"), [Creating a trail with the console](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console"), and [Converting a single-Region trail to a multi-Region trail](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-convert "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-convert").

**Single-Region trails**

When you create a single-Region trail, CloudTrail records the
events in that Region only. It then delivers the CloudTrail event log files to an
Amazon S3 bucket that you specify. You can only create a single-Region trail by
using the AWS CLI. If you create additional single trails, you can have those
trails deliver CloudTrail event log files to the same S3 bucket or to separate
buckets. This is the default option when you create a trail using the AWS CLI
or the CloudTrail API. For more information, see [Creating, updating, and managing trails with the AWS CLI](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md").

###### Note

For both types of trails, you can specify an Amazon S3 bucket from any Region.

If you have created an organization in AWS Organizations, you can create an _organization
trail_ that logs all events for all AWS accounts in that organization.
Organization trails can apply to all AWS Regions, or the current Region. Organization
trails must be created using the management account or delegated administrator account, and
when specified as applying to an organization, are automatically applied to all member
accounts in the organization. Member accounts can see the organization trail, but cannot
modify or delete it. By default, member accounts do not have access to the log files for an
organization trail in the Amazon S3 bucket. For more information, see [Creating a trail for an organization](creating-trail-organization.md "creating-trail-organization.md").

###### Topics

- [Creating a trail for your AWS account](cloudtrail-create-and-update-a-trail.md "cloudtrail-create-and-update-a-trail.md")
- [Creating a trail for an organization](creating-trail-organization.md "creating-trail-organization.md")
- [Understanding multi-Region trails and
  opt-in Regions](cloudtrail-multi-region-trails.md "cloudtrail-multi-region-trails.md")
- [Copying trail events to CloudTrail
  Lake](cloudtrail-copy-trail-to-lake.md "cloudtrail-copy-trail-to-lake.md")
- [Getting and viewing your CloudTrail log files](get-and-view-cloudtrail-log-files.md "get-and-view-cloudtrail-log-files.md")
- [Configuring Amazon SNS notifications for CloudTrail](configure-sns-notifications-for-cloudtrail.md "configure-sns-notifications-for-cloudtrail.md")
- [Using AWS CloudTrail with interface VPC endpoints](cloudtrail-and-interface-VPC.md "cloudtrail-and-interface-VPC.md")
- [Naming requirements for CloudTrail resources, S3 buckets, and KMS keys](cloudtrail-trail-naming-requirements.md "cloudtrail-trail-naming-requirements.md")
- [AWS account closure and trails](cloudtrail-account-closure.md "cloudtrail-account-closure.md")
