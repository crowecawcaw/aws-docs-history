

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Maintenance windows
<a name="timestream-for-influx-managing-maintaining-db"></a>

Periodically, Amazon Timestream for InfluxDB performs maintenance on Amazon Timestream for InfluxDB resources. Maintenance most often involves updates to the following resources in your DB instance:
+ Underlying hardware
+ Underlying operating system (OS)
+ Database engine version

Updates to the operating system most often occur for security issues. 

Some maintenance items require that Amazon Timestream for InfluxDB take your DB instance offline for a short time. Maintenance items that require a resource to be offline include required operating system or database patching. Required patching is automatically scheduled only for patches that are related to security and instance reliability. Such patching occurs infrequently, typically once every few months. It seldom requires more than a fraction of your maintenance window.

**Maintenance window**

Every Amazon Timestream for InfluxDB DB instance has a weekly maintenance window during which maintenance is performed. You can configure your maintenance window in two ways:
+ **Service managed (default)**: Amazon Timestream for InfluxDB determines the optimal maintenance window for your resource.
+ **Customer managed**: You specify a preferred maintenance window using the format `ddd:HH:MM-ddd:HH:MM` (for example, `Sun:02:00-Sun:04:00`). The window must be at least 2 hours and no more than 24 hours. Cross-midnight windows are supported.

You can set your preferred maintenance window when creating a DB instance or change it later using the `update-db-instance` API.

**Timezone**

You can specify a timezone for your maintenance window using the `timezone` field. When set, window times are interpreted in the specified timezone. The `timezone` field is required. Use IANA timezone identifiers such as `America/New_York` or `Asia/Tokyo`. The system handles Daylight Saving Time transitions automatically.

**CLI examples**

Create a DB instance with a custom maintenance window:

```
aws timestream-influxdb create-db-instance \
  --name "my-influxdb" \
  --db-instance-type db.influx.medium \
  --allocated-storage 50 \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --maintenance-schedule '{
    "timezone": "America/New_York",
    "preferredMaintenanceWindow": "Sun:02:00-Sun:04:00"
  }' \
  --region us-west-2
```

Update the maintenance window on an existing DB instance:

```
aws timestream-influxdb update-db-instance \
  --identifier <instance-identifier> \
  --maintenance-schedule '{
    "timezone": "Asia/Tokyo",
    "preferredMaintenanceWindow": "Wed:03:00-Wed:06:00"
  }' \
  --region us-west-2
```

Revert to service managed:

```
aws timestream-influxdb update-db-instance \
  --identifier <instance-identifier> \
  --maintenance-schedule '{
    "timezone": "UTC",
    "preferredMaintenanceWindow": ""
  }' \
  --region us-west-2
```

**Important**  
If a required maintenance action has been deferred for more than 25 days, the service may apply maintenance outside of your preferred window to ensure the security and reliability of your resource.

During maintenance, the DB instance status changes to `MAINTENANCE`. After completion, the status returns to `AVAILABLE`.

**Supported timezones**

Use IANA timezone identifiers. Timezone abbreviations such as `EST`, `PST`, and `GMT+5` are not supported.


| **Timezone** | **Description** | 
| --- | --- | 
| UTC | Coordinated Universal Time (default) | 
| America/New\_York | US Eastern | 
| America/Chicago | US Central | 
| America/Denver | US Mountain | 
| America/Los\_Angeles | US Pacific | 
| America/Sao\_Paulo | Brazil | 
| Europe/London | UK | 
| Europe/Paris | Central Europe | 
| Europe/Berlin | Germany | 
| Asia/Tokyo | Japan | 
| Asia/Shanghai | China | 
| Asia/Singapore | Singapore | 
| Asia/Mumbai | India | 
| Asia/Dubai | UAE | 
| Australia/Sydney | Australia Eastern | 
| Pacific/Auckland | New Zealand | 

**Considerations**
+ Maintenance windows define when maintenance *can* occur, not when it *will* occur. Maintenance is performed as needed, typically no more than once per week.
+ Maintenance is required at least once per month for security and reliability patching.
+ For Multi-AZ deployments, maintenance is performed on the standby first, then a failover occurs, minimizing downtime.
+ If you use a timezone with DST transitions, avoid scheduling maintenance between 1:00 AM and 3:00 AM to prevent skipped windows during spring forward.