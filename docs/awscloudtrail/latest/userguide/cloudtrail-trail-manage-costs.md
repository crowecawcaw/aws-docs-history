# Managing CloudTrail trail costs

You can configure and manage CloudTrail trails in ways that capture the data you
 need while remaining cost-effective. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").


## Trail configuration


CloudTrail offers flexibility in how you configure trails in your account. Some decisions
 that you make during the setup process require that you understand the impacts to your
 CloudTrail bill. The following are examples of how trail configurations can influence your
 CloudTrail bill.




**Multiple trail creation**

The first copy of management events within each region is delivered free
 of charge. For example, if your account has 2 single-Region trails, a trail
 in `us-east-1` and another trail in `us-west-2`, there
 are no CloudTrail charges because there is only one trail logging events in each
 respective Region. However, if your account has a multi-Region trail and an
 additional single-Region trail, the single-Region trail will incur charges
 because the multi-Region trail is already logging events in each Region.


If you create more trails that deliver the same management events to other
 destinations, those subsequent deliveries incur CloudTrail costs. You can do this
 to allow different user groups (such as developers, security personnel, and
 IT auditors) to receive their own copies of log files. For data events, all
 deliveries incur CloudTrail costs, including the first.


As you create more trails, it is especially important to be familiar with
 your logs, and understand the types and volumes of events that are generated
 by resources in your account. This helps you anticipate the volume of events
 that are associated with an account, and plan for trail costs. For example,
 using AWS KMS-managed server-side encryption (SSE-KMS) on your S3 buckets can
 result in a large number of AWS KMS management events in CloudTrail. Larger volumes
 of events across multiple trails can also influence costs.


To help limit the number of events that are logged to
 your trail, you can filter out AWS KMS or Amazon RDS Data API events by choosing
 **Exclude AWS KMS events** or **Exclude Amazon RDS
 Data API events** on the **Create trail** or
 **Update trail** pages. When using basic event
 selectors, you can only filter management events. However, you can use
 advanced event selectors to filter both management and data events.


You can use advanced event selectors to include or exclude data events, giving you
 the ability to log only the data events of interest. For more information, see [Filtering data events by using advanced event
 selectors](filtering-data-events.md "filtering-data-events.md").


You can use advanced event selectors to include or exclude network activity events based on the
 `eventName`, `resources.type`, `resources.ARN`
 , `errorCode`, and `vpcEndpointId` fields, giving you
 the ability to log only the data events of interest. For more information, see [Logging network activity
 events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").


For more information
 about creating and updating a trail, see [Creating a trail with the CloudTrail console](cloudtrail-create-a-trail-using-the-console-first-time.md "cloudtrail-create-a-trail-using-the-console-first-time.md")
 or [Updating a trail with the CloudTrail console](cloudtrail-update-a-trail-console.md "cloudtrail-update-a-trail-console.md") in this
 guide.



**AWS Organizations**

When you set up an Organizations trail with CloudTrail, CloudTrail replicates the trail to each
 member account within your organization. The new trail is created
 *in addition to* any existing trails in member
 accounts. Be sure that the configuration of your organization trail matches
 how you want trails configured for all accounts within an organization,
 because the organization trail configuration propagates to all
 accounts.


Because Organizations creates a trail in each member account, an individual member
 account that creates an additional trail to collect the same management
 events as the Organizations trail is collecting a second copy of events. The account
 is charged for the second copy. Similarly, if an account has a multi-Region
 trail, and creates a second trail in a single Region to collect the same
 management events as the multi-Region trail, the trail in the single Region
 is delivering a second copy of events. The second copy incurs
 charges.




## See also



* [AWS CloudTrail
 Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/")
* [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html")
* [Getting started with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html "https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html")
* [Prepare for creating a trail
 for your organization](creating-an-organizational-trail-prepare.md "creating-an-organizational-trail-prepare.md")
