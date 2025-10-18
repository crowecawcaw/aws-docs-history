# Creating multiple trails

You can use CloudTrail log files to troubleshoot operational or security issues in your AWS
 account. You can create trails for different users, who can create and manage their own
 trails. You can configure trails to deliver log files to separate S3 buckets or shared S3
 buckets.

###### Note

The first copy of management events in each AWS Region for an account is free. If you create more trails that deliver the same management events to other
 destinations, those subsequent deliveries incur CloudTrail costs. For more information about CloudTrail costs, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail trail costs](cloudtrail-trail-manage-costs.md "cloudtrail-trail-manage-costs.md").

For example, you might have the following users:


* A security administrator creates a trail in the Europe (Ireland) Region and configures KMS
 log file encryption. The trail delivers the log files to an S3 bucket in the Europe (Ireland) Region.
* An IT auditor creates a trail in the Europe (Ireland) Region and configures log file
 integrity validation to ensure the log files have not changed since CloudTrail delivered
 them. The trail is configured to deliver log files to an S3 bucket in the Europe (Frankfurt) Region
* A developer creates a trail in the Europe (Frankfurt) Region and configures CloudWatch alarms to
 receive notifications for specific API activity. The trail shares the same S3 bucket
 as the trail configured for log file integrity.
* Another developer creates a trail in the Europe (Frankfurt) Region and configures SNS. The
 log files are delivered to a separate S3 bucket in the Europe (Frankfurt) Region.
The following image illustrates this example.


![An example of log file delivery for multiple trails](images/eu-shared-01.png)
###### Note

You can create up to five trails per AWS Region. A multi-Region trail counts as one trail per Region.

You can use resource-level permissions to manage a user's ability to perform specific
 operations on CloudTrail.

For example, you might grant one user permission to view trail activity, but restrict the
 user from starting or stopping logging for a trail. You might grant another user full
 permission to create and delete trails. This gives you granular control over your trails and
 user access.

For more information about resource-level permissions, see [Examples: Creating and applying policies for actions on specific trails](security_iam_id-based-policy-examples.md#grant-custom-permissions-for-cloudtrail-users-resource-level "security_iam_id-based-policy-examples.md#grant-custom-permissions-for-cloudtrail-users-resource-level"). 

For more information about multiple trails, see the [CloudTrail FAQs](https://aws.amazon.com/cloudtrail/faqs/ "https://aws.amazon.com/cloudtrail/faqs/").
