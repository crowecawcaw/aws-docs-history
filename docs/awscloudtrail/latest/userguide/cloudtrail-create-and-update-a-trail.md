# Creating a trail for your AWS account

When you create a trail, you enable ongoing delivery of events as log files to an Amazon S3
 bucket that you specify. Creating a trail has many benefits, including:


* A record of events that extends past 90 days.
* The option to automatically monitor and alarm on specified events by sending log
 events to Amazon CloudWatch Logs.
* The option to query logs and analyze AWS service activity with Amazon Athena.
Beginning on April 12, 2019, you can view trails only in the AWS Regions where they log

 events. If you create a [multi-Region](cloudtrail-multi-region-trails.md "cloudtrail-multi-region-trails.md") trail, 
 it appears in the console in all AWS Regions that are 
 [enabled](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone") in your account. 
 If you create a trail that only logs events in a single Region, you
 can view and manage it only in that Region. As a best practice, we recommend creating
 a multi-Region trail because it captures activity in all enabled Regions. 
 All trails created using the CloudTrail console are multi-Region trails. To create a single-Region trail, you must use the AWS CLI.

If you use AWS Organizations, you can create a trail that will log events for all AWS accounts in
 the organization. A trail with the same name will be created in each member account, and
 events from each trail will be delivered to the Amazon S3 bucket that you specify. 

###### Note

Only the management account or delegated administrator account for an organization can create a trail for the organization.
 Creating a trail for an organization automatically enables integration between CloudTrail and
 Organizations. For more information, see [Creating a trail for an organization](creating-trail-organization.md "creating-trail-organization.md").

If you misconfigure your trail (for example, the S3 bucket is unreachable), 
 CloudTrail will attempt to redeliver the log files to your S3 bucket for 30 days, and 
 these attempted-to-deliver events will be subject to standard CloudTrail charges. 
 To avoid charges on a misconfigured trail, you need to delete the trail.

###### Topics

* [Creating and updating a trail with the console](cloudtrail-create-and-update-a-trail-by-using-the-console.md "cloudtrail-create-and-update-a-trail-by-using-the-console.md")
* [Creating, updating, and managing trails with the AWS CLI](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md")
* [Creating multiple trails](create-multiple-trails.md "create-multiple-trails.md")
