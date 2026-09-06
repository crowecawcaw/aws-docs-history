

# Monitoring reference
<a name="monitoring-reference"></a>

## CloudWatch alarms
<a name="cloudwatch-alarms"></a>

The solution creates the following CloudWatch alarms automatically:


| Alarm Name | Type | Description | 
| --- | --- | --- | 
| cms-dev-flink-fw-telemetry-processor-down | Downtime | FWTelemetryProcessor has >1 min downtime in 5 min window | 
| cms-dev-flink-trip-processor-down | Downtime | TripProcessor has >1 min downtime in 5 min window | 
| cms-dev-flink-safety-processor-down | Downtime | SafetyProcessor has >1 min downtime in 5 min window | 
| cms-dev-flink-simulator-preprocessor-down | Downtime | SimulatorPreprocessor has >1 min downtime in 5 min window | 
| cms-dev-flink-event-driven-telemetry-processor-down | Downtime | EventDrivenTelemetryProcessor has >1 min downtime in 5 min window | 
| cms-dev-flink-maintenance-processor-down | Downtime | MaintenanceProcessor has >1 min downtime in 5 min window | 
| cms-dev-flink-geofence-processor-down | Downtime | GeofenceProcessor has >1 min downtime in 5 min window | 
| cms-dev-flink-fw-telemetry-processor-idle | Idle | FWTelemetryProcessor processed 0 records in 10 min | 
| cms-dev-flink-trip-processor-idle | Idle | TripProcessor processed 0 records in 10 min | 

 **Downtime alarms** fire when the `downtime` metric exceeds 60,000 ms (1 minute) in a 5-minute evaluation window. This indicates the Flink application has crashed or stopped.

 **Idle processing alarms** fire when `numRecordsInPerSecond` sums to zero over a 10-minute window. Missing data is treated as breaching, so these alarms fire when the application is not running. These alarms indicate a pipeline stall — data should be flowing through these processors continuously when simulations are active.

## Key metrics to monitor
<a name="key-metrics"></a>


| Namespace | Metric | What to Watch | 
| --- | --- | --- | 
| AWS/KinesisAnalytics | downtime | Should be 0 for all processors | 
| AWS/KinesisAnalytics | numRecordsInPerSecond | Should be >0 when telemetry is flowing | 
| AWS/KinesisAnalytics | millisBehindLatest | Should be <5000ms; high values indicate processing lag | 
| AWS/IoT | RuleMessageThrottled | Should be 0; non-zero indicates IoT Rule throttling | 
| AWS/IoT | Failure | Should be 0; non-zero indicates IoT Rule action failures | 
| AWS/DynamoDB | ThrottledRequests | Should be 0; non-zero indicates capacity issues | 
| AWS/ElastiCache | CurrConnections | Monitor for connection exhaustion | 
| AWS/ElastiCache | CacheHitRate | Should be >90% for LKS reads | 