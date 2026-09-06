

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon EventBridge event notifications
<a name="influxdb3-eventbridge-events"></a>

Amazon Timestream for InfluxDB 3 publishes events to Amazon EventBridge when your clusters undergo state changes. Events are emitted for lifecycle operations including cluster creation, deletion, compute scaling, parameter group updates, maintenance windows, node addition/removal, engine type conversion, and reboot—covering both successful completions and failures.

Events are published to the default EventBridge event bus in your account with source `aws.timestream-influxdb` and detail-type `Timestream InfluxDB DB Cluster Event`. The `SourceType` field is `DB_CLUSTER` for all InfluxDB 3 events.

You can use EventBridge rules to:
+ Trigger automation when a scaling operation or node addition completes.
+ Route failure events for immediate on-call alerting.
+ Persist all events to Amazon CloudWatch Logs or Amazon S3 for audit trails.
+ Suppress monitoring alerts during maintenance windows.

**Example: Match all InfluxDB 3 cluster failure events**

```
{
  "source": ["aws.timestream-influxdb"],
  "detail-type": ["Timestream InfluxDB DB Cluster Event"],
  "detail": {
    "EventCategories": ["failure"]
  }
}
```

**Example: Match scaling events for a specific cluster**

```
{
  "source": ["aws.timestream-influxdb"],
  "detail": {
    "SourceIdentifier": ["my-influxdb3-cluster"],
    "EventID": ["TIDB-EVENT-22001", "TIDB-EVENT-22011"]
  }
}
```

For the complete event schema, event reference tables, setup instructions, common patterns, and troubleshooting guidance, see [Amazon Timestream for InfluxDB event notifications with Amazon EventBridge](influxdb-eventbridge-events.md).

There is no additional charge for publishing events. Standard Amazon EventBridge pricing applies for rule evaluation and target delivery.