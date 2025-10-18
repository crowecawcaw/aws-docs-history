# Working with CloudTrail event history

CloudTrail is enabled by default for your AWS account and you automatically have access to the CloudTrail event history. 
 The event history provides a viewable, searchable, downloadable, and immutable record of the past 90 days of management events
 in an AWS Region. These events capture activity made through the AWS Management Console, AWS Command Line Interface, and AWS SDKs
 and APIs. The event history records events in the AWS Region where the event happened. There are no CloudTrail charges for viewing the event history.

You can look up events related to the creation, modification, or deletion of resources
 (such as IAM users or Amazon EC2 instances) in your AWS account on a by-Region basis on the CloudTrail console 
 by viewing the **Event history** page. You can also look up these events by running the [`aws cloudtrail
 lookup-events`](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/lookup-events.html "https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/lookup-events.html") command or by using the [`LookupEvents`](../APIReference/API_LookupEvents.md "../APIReference/API_LookupEvents.md") API.
 

 You can use the **Event history** page on the CloudTrail console to view,
 search, download, archive, analyze, and respond to account activity across your AWS
 infrastructure. You can [customize the
 view](view-cloudtrail-events-console.md#displaying-cloudtrail-events "view-cloudtrail-events-console.md#displaying-cloudtrail-events") of the **Event history** page on the console by selecting
 how many events to display on each page and which columns to display or hide. You can also
 compare the details of events in event history side-by-side. You can programmatically [look up events](view-cloudtrail-events-cli.md "view-cloudtrail-events-cli.md") by using the AWS SDKs or
 AWS Command Line Interface.

 

###### Note

Over time, AWS services might add additional events. CloudTrail records these events in
 event history, but a full 90-day record of activity that
 includes added events won't be available until 90 days after it adds the events.

The event history is separate from any trails or event data
 stores that you create for your account. Changes you make to your event data stores or
 trails do not affect the event history.

The sections which follow describe how to look up recent management events by using the CloudTrail console and the AWS CLI, and 
 describe how to download a file of events. For information about using the
 `LookupEvents` API to retrieve information from CloudTrail events, see [LookupEvents](../APIReference/API_LookupEvents.md "../APIReference/API_LookupEvents.md") 
 in the *AWS CloudTrail API Reference*.

**Topics**


* [Limitations of Event history](#event-history-limitations "#event-history-limitations")
* [Viewing recent management events with
 the console](view-cloudtrail-events-console.md "view-cloudtrail-events-console.md")
* [Viewing recent management events with the AWS CLI](view-cloudtrail-events-cli.md "view-cloudtrail-events-cli.md")

## Limitations of Event history


The following limitations apply to the event history.



* The **Event history** page on the CloudTrail console only shows management events. It does not show data events, Insights events, or network activity events.
* The event history is limited to the past 90 days of events. For an ongoing record of events in your AWS account, create an [event data store](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md") or a [trail](cloudtrail-create-a-trail-using-the-console-first-time.md "cloudtrail-create-a-trail-using-the-console-first-time.md").
* When you download events from the **Event history** page on
 the CloudTrail console, you can download up to 200,000 events in a single file. If you reach the 200,000 event limit, 
 the CloudTrail console will provide the option to download additional files.
* The event history doesn't provide organization level event aggregation. To record events across your organization, create an organization event data store or trail.
* An event history search is limited to a single AWS account, only returns events from a single AWS Region, and cannot query multiple attributes. 
 You can only apply one attribute filter and a time range filter.


You can create a CloudTrail Lake event data store to query across multiple attributes and AWS Regions. You can also query across multiple AWS accounts in an AWS Organizations organization. 
 In CloudTrail Lake, you can query multiple event types, including management events, data events, Insights events, AWS Config
 configuration items, Audit Manager evidence, and non-AWS events. CloudTrail Lake queries offer a deeper and more
 customizable view of events than simple key and value lookups on the **Event
 history** page, or by running `LookupEvents`. For more information,
 see [Working with AWS CloudTrail Lake](cloudtrail-lake.md "cloudtrail-lake.md") and [Create an event data store for CloudTrail
 events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md").
* You cannot exclude AWS KMS or Amazon RDS Data API events from event history; settings that you apply to a trail or event data store do not apply to event history.
