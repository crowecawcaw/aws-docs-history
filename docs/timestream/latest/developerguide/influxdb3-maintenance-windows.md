

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Maintenance windows for Timestream for InfluxDB 3
<a name="influxdb3-maintenance-windows"></a>

Amazon Timestream for InfluxDB performs periodic maintenance on your resources. Maintenance most often involves updates to the underlying hardware, operating system, or database engine. These updates are mandatory. If maintenance is not performed during the designated window, it may be applied during a subsequent window.

## How maintenance windows work
<a name="maintenance-how-it-works"></a>

Every Timestream for InfluxDB resource has a weekly maintenance window during which maintenance is performed.
+ If you specify a preferred maintenance window, maintenance is performed during your chosen window.
+ If you do not specify a preferred maintenance window, the system automatically assigns a maintenance window for your resource.

You can set your preferred maintenance window when creating a resource or change it later using the update APIs.

**Important**  
If a required maintenance action has been deferred for more than 25 days, the service may apply maintenance outside of your preferred window to ensure the security and reliability of your resource.

## Management types
<a name="maintenance-management-types"></a>

Maintenance windows can be managed in two ways:


| **Type** | **Description** | **Behavior** | 
| --- | --- | --- | 
| SERVICE\_MANAGED | AWS manages maintenance (default) | AWS determines the optimal maintenance window | 
| CUSTOMER\_MANAGED | Customer manages maintenance | You must specify a preferredMaintenanceWindow | 

## Preferred maintenance window
<a name="maintenance-preferred-window"></a>

The preferred maintenance window defines the weekly time slot during which maintenance can occur.

**Format:** `ddd:HH:MM-ddd:HH:MM`
+ `ddd` — Day of the week (`Sun`, `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat`). Case-insensitive.
+ `HH:MM` — Time in 24-hour format.

**Examples:**


| **Window** | **Description** | **Duration** | 
| --- | --- | --- | 
| Sun:02:00-Sun:04:00 | Sunday 2:00 AM to 4:00 AM | 2 hours | 
| Sat:22:00-Sun:02:00 | Saturday 10:00 PM to Sunday 2:00 AM | 4 hours | 
| Wed:03:30-Wed:05:30 | Wednesday 3:30 AM to 5:30 AM | 2 hours | 

**Constraints:**


| **Constraint** | **Value** | 
| --- | --- | 
| Minimum window duration | 2 hours | 
| Maximum window duration | 24 hours | 
| Cross-midnight windows | Supported (for example, Sat:22:00-Sun:02:00) | 

Maintenance begins within the first 30 minutes of your specified window. The exact start time is determined by the system and is consistent week to week for the same resource.

## Timezone
<a name="maintenance-timezone"></a>

You can specify a timezone for your maintenance window using the `timezone` field. When set, window times are interpreted in the specified timezone.

The `timezone` field is required in all maintenance schedule requests.

**Format:** IANA timezone identifier. Most timezones in the [IANA Time Zone Database](https://www.iana.org/time-zones) are supported, including common identifiers such as `America/New_York`, `Europe/London`, `Asia/Tokyo`, `Asia/Kolkata`, and `Pacific/Auckland`.

**Note**  
Timezone abbreviations such as `EST`, `PST`, and `GMT+5` are not supported. Use the full IANA identifier instead.

**Daylight Saving Time:** The system handles DST transitions automatically. If your window falls within a skipped DST hour (spring forward), maintenance is skipped that week. To avoid DST-related issues, schedule maintenance outside the 1:00 AM to 3:00 AM range, or use `UTC`.

**Supported timezones:**


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

## During maintenance
<a name="maintenance-during"></a>

When maintenance is being performed, the resource status changes to `MAINTENANCE`. During this time, the resource may be temporarily unavailable. After completion, the status returns to `AVAILABLE`.

## API response fields
<a name="maintenance-response-fields"></a>


| **Field** | **Description** | 
| --- | --- | 
| preferredMaintenanceWindow | The configured maintenance window. Shows system-assigned window if not customer-specified. | 
| timezone | The configured timezone. | 
| nextMaintenanceTime | Next scheduled maintenance time in UTC (ISO 8601). | 
| lastMaintenanceTime | Last completed maintenance time in UTC (ISO 8601). Null if never performed. | 

**Note**  
`nextMaintenanceTime` and `lastMaintenanceTime` are always returned in UTC, regardless of your configured timezone.

## CLI examples
<a name="maintenance-cli-examples"></a>

### Setting a maintenance window when creating a resource
<a name="maintenance-cli-create"></a>

Service managed (default — no maintenance schedule specified):

```
aws timestream-influxdb create-db-cluster \
  --name "my-influxdb3-cluster" \
  --db-instance-type db.influx.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --region us-west-2
```

Customer managed with UTC (default timezone):

```
aws timestream-influxdb create-db-cluster \
  --name "my-influxdb3-cluster" \
  --db-instance-type db.influx.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --maintenance-schedule '{
    "preferredMaintenanceWindow": "Sun:02:00-Sun:04:00"
  }' \
  --region us-west-2
```

Customer managed with a specific timezone:

```
aws timestream-influxdb create-db-cluster \
  --name "my-influxdb3-cluster" \
  --db-instance-type db.influx.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --maintenance-schedule '{
    "timezone": "America/New_York",
    "preferredMaintenanceWindow": "Sun:02:00-Sun:04:00"
  }' \
  --region us-west-2
```

Customer managed with an overnight window:

```
aws timestream-influxdb create-db-cluster \
  --name "my-influxdb3-cluster" \
  --db-instance-type db.influx.2xlarge \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --maintenance-schedule '{
    "timezone": "Europe/London",
    "preferredMaintenanceWindow": "Sat:22:00-Sun:02:00"
  }' \
  --region us-west-2
```

### Updating a maintenance window
<a name="maintenance-cli-update"></a>

Set a custom maintenance window on an existing resource:

```
aws timestream-influxdb update-db-cluster \
  --identifier "my-influxdb3-cluster" \
  --maintenance-schedule '{
    "timezone": "Asia/Tokyo",
    "preferredMaintenanceWindow": "Wed:03:00-Wed:06:00"
  }' \
  --region us-west-2
```

Revert to service managed:

```
aws timestream-influxdb update-db-cluster \
  --identifier "my-influxdb3-cluster" \
  --maintenance-schedule '{
    "timezone": "UTC",
    "preferredMaintenanceWindow": ""
  }' \
  --region us-west-2
```

## Considerations
<a name="maintenance-considerations"></a>
+ Maintenance windows define when maintenance *can* occur, not when it *will* occur. Maintenance is performed as needed, typically no more than once per week.
+ AWS requires maintenance to be performed at least once per month for security and reliability patching.
+ For multi-node clusters using cluster endpoints, traffic is automatically redistributed to available nodes during maintenance.
+ Schedule your maintenance window during periods of lowest traffic to minimize impact on your workload.
+ If you use a timezone with DST transitions, avoid scheduling maintenance between 1:00 AM and 3:00 AM to prevent skipped windows during spring forward.