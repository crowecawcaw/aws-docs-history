# Logging Insights events with the CloudTrail console

This section describes how you can enable Insights events on an existing trail
or event data store using the CloudTrail console.

For more information about how to create a new trail to log Insights events, see [Creating a trail with the console](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console").

For more information about how to create a new event data store to
collect Insights events, see [Create an event data store for Insights events with the console](query-event-data-store-insights.md "query-event-data-store-insights.md").

###### Topics

- [Enabling CloudTrail Insights on an existing
  trail with the console](#insights-events-enable-trail "#insights-events-enable-trail")
- [Enabling CloudTrail Insights on an existing
  event data store with the console](#insights-events-enable-lake "#insights-events-enable-lake")

## Enabling CloudTrail Insights on an existing

trail with the console

Use the following procedure to enable CloudTrail Insights on an existing trail.

1. In the left navigation pane of the CloudTrail console, open the
   **Trails** page, and choose a trail name.
2. In **Insights events**, choose **Edit**.

###### Note

Additional charges apply for logging Insights events. For CloudTrail pricing, see
[AWS CloudTrail
Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). 3. In **Event type**, choose **Insights
events**. 4. In **Insights events**, under **Choose Insights
types**, choose **API call rate**,
**API error rate**, or both. Your trail must be logging
**Write** management events to log Insights events for
**API call rate**. Your trail must be logging
**Read** or **Write** management
events to log Insights events for **API error rate**. 5. Choose **Save changes** to save your changes.

CloudTrail may take up to 36 hours to begin delivering Insights events after you enable
Insights events on a trail, provided that unusual activity is detected during that
time.

## Enabling CloudTrail Insights on an existing

event data store with the console

Use the following procedure to enable CloudTrail Insights on an existing event data store.

Additional charges apply for ingesting Insights events in CloudTrail Lake. You will be charged
separately if you enable Insights for both trails and event data stores. For
information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Note

You can only enable CloudTrail Insights on event data stores containing CloudTrail
management events. You cannot enable CloudTrail Insights on other event data store
types.

1. In the left navigation pane of the CloudTrail console, under
   **Lake**, choose **Event data
   stores**.
2. Choose the event data store name.
3. In **Management events**, choose
   **Edit**.
4. Choose **Enable Insights events capture**.
5. Choose the destination event store that will collect Insights events. The
   destination event data store will collect Insights events based upon the management
   event activity in this event data store. For information about how to create
   the destination event data store, see [To create a destination event data store that logs Insights events](query-event-data-store-insights.md#query-event-data-store-insights-procedure "query-event-data-store-insights.md#query-event-data-store-insights-procedure").
6. Choose the Insights types. You can choose **API call
   rate**, **API error rate**, or both. You must
   be logging **Write** management events to log Insights events for
   **API call rate**. You must be logging
   **Read** or **Write** management
   events to log Insights events for **API error rate**.
7. Choose **Save changes** to save your changes.

CloudTrail may take up to 7 days to begin delivering Insights events, provided that
unusual activity is detected during that time.
