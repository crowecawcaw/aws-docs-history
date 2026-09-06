

# Stop and start event ingestion with the console
<a name="query-eds-stop-ingestion"></a>

**Note**  
AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md).

By default, event data stores are configured to ingest events. You can stop an event data store from ingesting events by using the console, AWS CLI, or APIs.

The options to **Start ingestion** and **Stop ingestion** are only available on event data stores containing either CloudTrail events (management events, data events, and network activity events), or AWS Config configuration items.

When you stop ingestion on an event data store, the event data store's state changes to `STOPPED_INGESTION`. You can still run queries on any events already in the event data store. You can also copy trail events to the event data store (if it contains only CloudTrail events).

**To stop an event data store from ingesting events**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, under **Lake**, choose **Event data stores**.

1. Choose the event data store.

1. From **Actions**, choose **Stop ingestion**.

1. When you are prompted to confirm, choose **Stop ingestion**. The event data store will stop ingesting live events.

1. To resume ingestion, choose **Start ingestion**.

**To restart event ingestion**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, under **Lake**, choose **Event data stores**.

1. Choose the event data store.

1. From **Actions**, choose **Start ingestion**.