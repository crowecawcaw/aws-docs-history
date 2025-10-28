# Viewing Insights events for event data stores

This section describes how you can view Insights events for an Insights
event data store by viewing the **Insights events dashboard** and running sample queries. For information about how to enable CloudTrail Insights
on an event data store, see [Enabling CloudTrail Insights on an existing
event data store with the console](insights-events-enable.md#insights-events-enable-lake "insights-events-enable.md#insights-events-enable-lake").

CloudTrail queries incur charges based upon the amount of data scanned. To help control
costs, we recommend that you constrain queries by adding starting and ending
`eventTime` time stamps to queries. For more information about CloudTrail
pricing, see [AWS CloudTrail
Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

For descriptions of Insights events record fields for event data stores, see
[CloudTrail record contents for Insights events for event data stores](cloudtrail-insights-fields-lake.md "cloudtrail-insights-fields-lake.md").

###### Topics

- [Viewing the Insights dashboard for an
  event data store](#insights-events-view-lake-dashboard "#insights-events-view-lake-dashboard")
- [Viewing sample queries for
  Insights events](#insights-events-lake-queries "#insights-events-lake-queries")

## Viewing the Insights dashboard for an

event data store

The **Insights events dashboard** shows the overall proportion of Insights
events by Insights type, the proportion of Insights events by Insights type for the
top users and services, and the number of Insights events per day. The dashboard
also includes a widget that lists up to 30 days of Insights events.

###### Note

- After you enable CloudTrail Insights for the first time on the source event
  data store, CloudTrail may take up to 7 days to begin delivering Insights
  events, provided that unusual activity is detected during that time. For
  more information, see [Delivery of Insights events](insights-events-understanding.md "insights-events-understanding.md").
- The **Insights events dashboard** only displays information
  about the Insights events collected by the selected event data store,
  which is determined by the configuration of the source event data store.
  For example, if you configure the source event data store to enable
  Insights events on `ApiCallRateInsight` but not
  `ApiErrorRateInsight`, you won't see information about
  Insights events on `ApiErrorRateInsight`.

###### To view the Insights events dashboard

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, under **Lake**, choose
   **Dashboard**.
3. Choose the **Managed and custom dashboards** tab.
4. From **AWS managed dashboards**, choose
   **Insights events dashboard**.
5. Choose your Insights event data store.
6. Choose to filter the dashboard data by an **Absolute
   range** or **Relative range**. Choose
   **Absolute range** to select a specific date and time
   range. Choose **Relative range** to select a predefined
   time range or a custom range. By default, the dashboard displays event data
   for the past 24 hours.

###### Note

CloudTrail Lake queries incur costs based upon the amount of data scanned.
To help control costs, you can filter on a narrower time range. For more
information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). 7. Choose the refresh icon to populate the graphics for the dashboard's
widgets. Each widget indicates the status of the refresh.

For more information about Lake dashboards, see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").

## Viewing sample queries for

Insights events

The CloudTrail console provides a number of sample queries for Insights events that can help you
get started writing your own queries.

###### To view sample queries for Insights events

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose
   **Query**.
3. On the **Query** page, choose the **Sample
   queries** tab.
4. Search for queries for Insights events. Choose the **Query
   name** to open the query in the **Editor**
   tab.

![Example shows sample queries for Insights events](images/ct-insights-sample-queries.png) 5. On the **Editor** tab, choose the Insights event data
store. When you choose the event data store from the list, CloudTrail
automatically populates the event data store ID in the `FROM`
line of the query editor. 6. Choose **Run** to run the query. After the query
completes, you can view the command output and query results.

The **Command output** tab shows you metadata about your
query, such as whether the query was successful, the number of records
matched, and the run time of the query.

The **Query results** tab shows you the event data in the
selected event data store that matched your query.

For more information about editing a query, see [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md"). For
more information about running a query and saving query results, see [Run a query and save query results with the console](query-run-query.md "query-run-query.md").
