# Viewing recent management events with
 the console

You can use the **Event history** page in the CloudTrail console to view the
 last 90 days of management events in an AWS Region. You can also download a file with that
 information, or a subset of information based on the filter and time range you choose. You
 can customize your view of **Event history** by selecting how many events
 to display on each page and choosing which columns to display on the console. You can also
 look up and filter events by the resource types available for a particular service. You can
 select up to five events in **Event history** and compare their details
 side-by-side.

Event history does not show data events. To view
 data events, create an [event data
 store](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md") or a [trail](cloudtrail-create-and-update-a-trail.md "cloudtrail-create-and-update-a-trail.md").

After 90 days, events are no longer shown in event history. You
 cannot manually delete events from event history.

You can learn more about the specifics of how CloudTrail logs events for a specific service by
 consulting the documentation for that service. For more information, see [AWS service topics for CloudTrail](cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-list "cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-list").

###### Note

For an ongoing record of activity and events past 90 days, create an
 [event data store](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md") or a [trail](cloudtrail-create-a-trail-using-the-console-first-time.md "cloudtrail-create-a-trail-using-the-console-first-time.md").

###### To view **Event history**

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**. You see a
 filtered list of events, with the most recent events showing first. The default
 filter for events is **Read only**, set to
 **false**. You can clear that filter by choosing
 **X** at the right of the filter.
3. You can filter events on a single attribute, which you can choose from the drop-down list. 
 To filter on an attribute, choose the attribute from the drop-down list and enter the full value for the attribute. For
 example, to view all console login events, choose the **Event
 name** filter, and specify **ConsoleLogin**. Or, to
 view recent S3 management events, choose the **Event
 source** filter, and specify `s3.amazonaws.com`.
4. To view a specific management event, choose the event name. On the event details
 page, you can view details about the event, see any referenced resources, and view
 the event record.
5. To compare events, select up to five events by filling their check boxes in the
 left margin of the **Event history** table. You can view details for
 the selected events side-by-side in the **Compare event details**
 table.
6. You can save event history by downloading it as a file in CSV or JSON format.
 Downloading your event history can take a few minutes.
###### Contents

* [Navigating between pages](view-cloudtrail-events-console.md#navigate-event-history "view-cloudtrail-events-console.md#navigate-event-history")
* [Customizing the display](view-cloudtrail-events-console.md#displaying-cloudtrail-events "view-cloudtrail-events-console.md#displaying-cloudtrail-events")
* [Filtering CloudTrail events](view-cloudtrail-events-console.md#filtering-cloudtrail-events "view-cloudtrail-events-console.md#filtering-cloudtrail-events")
* [Viewing details for an event](view-cloudtrail-events-console.md#viewing-details-for-an-event "view-cloudtrail-events-console.md#viewing-details-for-an-event")
* [Downloading events](view-cloudtrail-events-console.md#downloading-events "view-cloudtrail-events-console.md#downloading-events")
* [Viewing resources referenced with
 AWS Config](view-cloudtrail-events-console.md#viewing-resources-config "view-cloudtrail-events-console.md#viewing-resources-config")

## Navigating between pages


You can navigate between pages in the **Event history** by choosing
 the page you want to view. You can also view the next and previous page in
 **Event history**.


Choose **<** to view the previous page of
 **Event history**.


Choose **>** to view the next page of **Event
 history**.


## Customizing the display


You can customize the view of **Event history** on the CloudTrail console
 by selecting from the following preferences.



* **Page size** - Choose whether you want to display 10, 25, or
 50 events on each page.
* **Wrap lines** - Wrap text so you can see all text for each
 event.
* **Striped rows** - Shade every other row in the table.
* **Event time display** - Choose whether to display the event
 time in UTC or the local time zone.
* **Select visible columns** - Select which columns to display.
 By default, the following columns are displayed:




	+ **Event name**
	+ **Event time**
	+ **User name**
	+ **Event source**
	+ **Resource type**
	+ **Resource name**
###### Note

You cannot change the order of the columns, or manually delete events from
 **Event history**.

###### To customize the display

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**.
3. Choose the gear icon.
4. For **Page size**, choose the number of events to display on
 a page.
5. Choose **Wrap lines** to see all text for each event.
6. Choose **Striped rows** to shade every other row in the
 table.
7. For **Event time display**, choose whether to display the
 event time in UTC or the local time zone. By default, UTC is selected.
8. In **Select visible columns**, select the columns you want to
 display. Turn off columns you do not want to display.
9. When you have finished making your changes, choose
 **Confirm**.

## Filtering CloudTrail events


The default display of events in **Event history** uses an attribute
 filter to exclude read-only events from the list of displayed events. This attribute
 filter is named **Read-only**, and it is set to
 **false**. You can remove this filter to display both read and
 write events. To view only **Read** events, you can change the filter
 value to **true**. You can also filter events by other attributes. You
 can additionally filter by time range.


###### Note

You can only apply one attribute filter and a time range filter. You cannot apply
 multiple attribute filters.




 **AWS access key** 

The AWS access key ID that was used to sign the request. If the request
 was made with temporary security credentials, this is the access key ID of
 the temporary credentials.



 **Event ID** 

The CloudTrail ID of the event. Each event has a unique ID.



 **Event name** 

The name of the event. For example, you can filter on IAM events, such
 as `CreatePolicy`, or Amazon EC2 events, such as
 `RunInstances`.



 **Event source** 

The AWS service to which the request was made, such as
 `iam.amazonaws.com` or `s3.amazonaws.com`. You can
 scroll through a list of event sources after you choose the **Event
 source** filter. 



 **Read only** 

The read type of the event. Events are categorized as read events or write
 events. If set to **false**, read events are not included
 in the list of displayed events. By default, this attribute filter is
 applied and the value is set to **false**.



 **Resource name** 

The name or ID of the resource referenced by the event. For example, the
 resource name might be "auto-scaling-test-group" for an Auto Scaling group or
 "i-12345678910" for an EC2 instance.



 **Resource type** 

The type of resource referenced by the event. For example, a resource type
 can be `Instance` for EC2 or `DBInstance` for RDS.
 Resource types vary for each AWS service. 



 **Time range** 

The time range in which you want to filter events. You can choose either a
 **Relative range** or an **Absolute
 range**. You can filter events for the last 90 days.



 **User name** 

The identity referenced by the event. For example, this can be a user, a
 role name, or a service role.




If there are no events logged for the attribute or time that you choose, the results
 list is empty. You can apply only one attribute filter in addition to the time range. If
 you choose a different attribute filter, your specified time range is preserved.


The following steps describe how to filter by attribute. 


###### To filter by attribute

1. To filter the results by an attribute, choose an attribute from the
 **Lookup attributes** drop-down list, and then type or
 choose a value for the attribute in the text box.
2. To remove an attribute filter, choose the **X** at the right
 of the attribute filter box.

The following steps describe how to filter by a start and end date and time.


###### To filter by a start and end date and time

1. To narrow the time range for the events that you want to see, choose a time
 range in the time range bar. You can choose either a **Relative
 range** or an **Absolute range**.


Choose **Relative range** to select from a preset value or
 choose a custom range. Preset values are 30 minutes, 1 hour, 12 hours, or 1 day.
 To specify a custom time range, choose **Custom**.


Choose **Absolute range** to specify a specific start and end
 time. You can also choose between the local time zone or UTC.
2. To remove a time range filter, choose **Clear and dismiss**
 in the time range bar.

## Viewing details for an event


1. Choose an event in the results list to show its details.
2. Resources referenced in the event are shown in the **Resources
 referenced** table on the event details page.
3. Some referenced resources have links. Choose the link to open the console for
 that resource.
4. Scroll to **Event record** on the details page to see the
 JSON event record, also called the event *payload*.
5. Choose **Event history** in the page breadcrumb to close the
 event details page and return to **Event history**.

## Downloading events


You can download recorded event history as a file in CSV or JSON format. You can
 download up to 200,000 events in a single file. If you reach the 200,000 event limit,
 the CloudTrail console will provide the option to download additional files. Use filters and
 time ranges to reduce the size of the file you download. 


###### Note

CloudTrail event history files are data files that contain information (such as resource
 names) that can be configured by individual users. Some data can potentially be
 interpreted as commands in programs used to read and analyze this data (CSV
 injection). For example, when CloudTrail events are exported to CSV and imported to a
 spreadsheet program, that program might warn you about security concerns. You should
 choose to disable this content to keep your system secure. Always disable links or
 macros from downloaded event history files.


1. Add a filter and time range for events in **Event history**
 that you want to download. For example, you can specify the event name,
 `StartInstances`, and specify a time range for the last three
 days of activity.
2. Choose **Download events**, and then choose
 **Download as CSV** or **Download as
 JSON**. The download starts immediately.


###### Note

Your download might take some time to complete. For faster results, before
 you start the download process, use a more specific filter or a shorter time
 range to narrow the results. You can cancel a download. If you cancel a
 download, a partial download including only some event data might be on your
 local computer. To download the full event history, restart the
 download.
3. After your download is complete, open the file to view the events that you
 specified.
4. To cancel your download, choose **Cancel**, and then confirm
 by choosing **Cancel download**. If you need to restart a
 download, wait until the earlier download is finished canceling.

## Viewing resources referenced with
 AWS Config


AWS Config records configuration details, relationships, and changes to your AWS
 resources. 


On the **Resources referenced** pane, choose the 
![AWS Config timeline icon](images/config-timeline.png)
 in the **AWS Config resource timeline** column to view
 the resource in the AWS Config console.


If the 
![Shows AWS Config timeline](images/config-timeline-gray.png)
 icon is gray, AWS Config isn't turned on, or it's not recording the
 resource type. Choose the icon to go to the AWS Config console to turn on the service or start
 recording that resource type. For more information, see [Set Up AWS Config Using the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html "https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html") in the
 *AWS Config Developer Guide*.


If **Link not available** appears in the column, the resource can't
 be viewed for one of the following reasons:



* AWS Config doesn't support the resource type. For more information, see [Supported Resources,
 Configuration Items, and Relationships](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html "https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html") in the
 *AWS Config Developer Guide*.
* AWS Config recently added support for the resource type, but it's not yet available
 from the CloudTrail console. You can look up the resource in the AWS Config console to see
 the timeline for the resource.
* The resource is owned by another AWS account.
* The resource is owned by another AWS service, such as a managed IAM
 policy.
* The resource was created and then deleted immediately.
* The resource was recently created or updated.

To grant users read-only permission to view resources in the AWS Config console, see [Granting permission to view AWS Config information on the CloudTrail console](security_iam_id-based-policy-examples.md#grant-aws-config-permissions-for-cloudtrail-users "security_iam_id-based-policy-examples.md#grant-aws-config-permissions-for-cloudtrail-users").


For more information about AWS Config, see the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/ "https://docs.aws.amazon.com/config/latest/developerguide/").
