# Viewing Insights events for trails

This section describes how you can lookup the last 90 days of Insights events for a trail with CloudTrail Insights enabled. For information about how to view CloudTrail Insights for an event data store,
see [Viewing the Insights dashboard for an
event data store](insights-events-view-lake.md#insights-events-view-lake-dashboard "insights-events-view-lake.md#insights-events-view-lake-dashboard").

You can view, filter, and download the last 90 days of Insights events for a trail from the
**Insights** page on the console.

You can lookup the last 90 days of Insights events programmatically by running the AWS CLI
[lookup-events](../../../cli/latest/reference/cloudtrail/lookup-events.md "../../../cli/latest/reference/cloudtrail/lookup-events.md") command, or the [LookupEvents](../APIReference/API_LookupEvents.md "../APIReference/API_LookupEvents.md") API operation.

For descriptions of Insights events record fields for trails, see [CloudTrail record contents for Insights events for trails](cloudtrail-insights-fields-trails.md "cloudtrail-insights-fields-trails.md").

###### Note

The **Insights** page and AWS CLI `lookup-events` command only list Insights events if you've enabled Insights on a trail that is logging management events. For information
about enabling Insights on a trail, see [Enabling CloudTrail Insights on an existing
trail with the console](insights-events-enable.md#insights-events-enable-trail "insights-events-enable.md#insights-events-enable-trail") and
[Logging Insights events for a trail using
the AWS CLI](insights-events-CLI-enable.md#insights-events-CLI-enable-trails "insights-events-CLI-enable.md#insights-events-CLI-enable-trails").

To log Insights events on the API call rate, the trail must log `write` management events.
To log Insights events on the API error rate, the trail must log `read` or `write` management events.

###### Topics

- [Viewing Insights events for trails with the console](view-insights-events-console.md "view-insights-events-console.md")
- [Viewing Insights events for trails with the AWS CLI](view-insights-events-cli.md "view-insights-events-cli.md")
