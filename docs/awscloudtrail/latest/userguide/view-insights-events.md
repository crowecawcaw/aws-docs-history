

# Viewing Insights events for trails
<a name="view-insights-events"></a>

This section describes how you can lookup the last 90 days of Insights events for a trail with CloudTrail Insights enabled. For information about how to view CloudTrail Insights for an event data store, see [Viewing the Insights dashboard for an event data store](insights-events-view-lake.md#insights-events-view-lake-dashboard).

You can view, filter, and download the last 90 days of Insights events for a trail from the **Insights** page on the console. 

You can fetch the last 90 days of Insights events programmatically:
+ For Trails logging management events by running the AWS CLI [lookup-events](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/lookup-events.html) command, or the [LookupEvents](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) API operation.
+ For Trails logging data events by running the AWS CLI [list-insights-data](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/list-insights-data.html) command, or the [ListInsightsData](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListInsightsData.html) API operation.

For descriptions of Insights events record fields for trails, see [CloudTrail record contents for Insights events for trails](cloudtrail-insights-fields-trails.md).

**Note**  
The **Insights** page and AWS CLI `lookup-events` or `list-insights-data` command only list Insights events if you've enabled Insights on a trail that is logging management or data events. For information about enabling Insights on a trail, see [Enabling CloudTrail Insights on an existing trail with the console](insights-events-enable.md#insights-events-enable-trail) and [Logging Insights events for a trail using the AWS CLI](insights-events-CLI-enable.md#insights-events-CLI-enable-trails).  
 To log Insights events on the API call rate, the trail must log `write` management or data events. To log Insights events on the API error rate, the trail must log `read` or `write` management or data events. 

**Topics**
+ [Viewing Insights events for trails with the console](view-insights-events-console.md)
+ [Viewing Insights events for trails with the AWS CLI](view-insights-events-cli.md)