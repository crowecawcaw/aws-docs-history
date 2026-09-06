

# Telemetry pipeline troubleshooting
<a name="telemetry-pipeline-troubleshooting"></a>

## Problem: IoT Rule not routing messages to MSK
<a name="problem-iot-rule-not-routing"></a>

Vehicles are publishing telemetry to IoT Core (visible in MQTT test client) but messages do not appear in Kafka topics.

### Resolution
<a name="resolution-8"></a>

1. Check the IoT Rule error action metrics:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace "AWS/IoT" \
     --metric-name "Failure" \
     --dimensions Name=RuleName,Value=cms_dev_iot_msk_rule \
     --start-time $(date -u -v-1H +%Y-%m-%dT%H:%M:%S) \
     --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
     --period 300 --statistics Sum
   ```

1. Verify the VPC Destination is in `ENABLED` status:

   ```
   aws iot list-topic-rule-destinations \
     --query "destinationSummaries[*].[arn,status]" --output table
   ```

1. If the VPC Destination shows `ERROR` or `DISABLED`, the MSK security group may not allow inbound traffic from the IoT Rule’s ENI. Redeploy the TelemetryIntegrationStack:

   ```
   cd deployment && make phase3b
   ```

1. Verify the IoT Rule SQL statement matches the MQTT topic pattern your vehicles are publishing to (`cms/telemetry/+` for MQTT Direct, `cms/fleetwise/vehicles/+/signals` for FWE).

## Problem: Telemetry reaching MSK but not appearing in DynamoDB
<a name="problem-telemetry-not-reaching-dynamodb"></a>

Messages are in Kafka topics but DynamoDB tables remain empty.

### Resolution
<a name="resolution-9"></a>

Check the processing pipeline in order:

1.  **SimulatorPreprocessor** — Must be running to decode gzip\+base64 MQTT Direct telemetry. If this processor is down, no MQTT Direct data reaches downstream processors.

   ```
   aws kinesisanalyticsv2 describe-application \
     --application-name cms-dev-flink-simulator-preprocessor \
     --query "ApplicationDetail.ApplicationStatus"
   ```

1.  **EventDrivenTelemetryProcessor** — Routes decoded telemetry to domain-specific topics and writes to Redis. If this is down, trip/safety/maintenance processors receive no data.

1.  **TelemetryProcessor** — Writes raw telemetry to the telemetry DynamoDB table.

1.  **TripProcessor / SafetyProcessor / MaintenanceProcessor** — Write to their respective tables.

Start any stopped processors:

```
# Start all stopped Flink apps
for APP in $(aws kinesisanalyticsv2 list-applications \
  --query "ApplicationSummaries[?contains(ApplicationName, 'cms-dev-flink') && ApplicationStatus=='READY'].ApplicationName" \
  --output text); do
  echo "Starting $APP..."
  aws kinesisanalyticsv2 start-application --application-name $APP
done
```

## Problem: Redis not showing vehicle state (map view empty)
<a name="problem-redis-not-showing-vehicle-state"></a>

The Fleet Manager map view shows no vehicles, or vehicle detail pages show no live signal data.

### Resolution
<a name="resolution-10"></a>

1. Verify the EventDrivenTelemetryProcessor is running — this is the processor that writes to Redis:

   ```
   aws kinesisanalyticsv2 describe-application \
     --application-name cms-dev-flink-event-driven-telemetry-processor \
     --query "ApplicationDetail.ApplicationStatus"
   ```

1. Verify ElastiCache is reachable from the Flink VPC. Check the ElastiCache cluster status:

   ```
   aws elasticache describe-cache-clusters \
     --cache-cluster-id cms-dev-redis \
     --show-cache-node-info \
     --query "CacheClusters[0].[CacheClusterStatus,CacheNodes[0].CacheNodeStatus]"
   ```

1. Check the EventDrivenTelemetryProcessor logs for Redis connection errors:

   ```
   aws logs tail /aws/kinesis-analytics/cms-dev-flink-event-driven-telemetry-processor \
     --filter-pattern "Redis" --since 30m
   ```

1. Vehicle state keys expire after 5 minutes of inactivity (configurable via `REDIS_TTL`). If no simulation is running, all vehicle state will have expired. Start a simulation to populate Redis.

1. Verify the signal catalog is loaded in Redis. The SignalCatalogLoader writes `signal_catalog:map` and `signal_catalog:reverse` hashes on startup. If these are missing, the processor cannot map signal IDs to names.