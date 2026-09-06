

# Flink application troubleshooting
<a name="flink-troubleshooting"></a>

## Problem: Flink application not running (dead app)
<a name="problem-flink-app-not-running"></a>

A Flink application shows status `READY` instead of `RUNNING`, or has stopped processing records. CloudWatch alarms fire for downtime or idle processing.

### Diagnosis
<a name="diagnosis"></a>

1. Check the application status:

   ```
   # List all CMS Flink applications and their status
   STAGE=dev
   aws kinesisanalyticsv2 list-applications \
     --query "ApplicationSummaries[?contains(ApplicationName, 'cms-$STAGE-flink')].[ApplicationName,ApplicationStatus]" \
     --output table
   ```

1. Check CloudWatch alarms:

   ```
   aws cloudwatch describe-alarms \
     --alarm-name-prefix "cms-dev-flink" \
     --query "MetricAlarms[?StateValue=='ALARM'].[AlarmName,AlarmDescription]" \
     --output table
   ```

1. Check the application logs for errors:

   ```
   APP=cms-dev-flink-trip-processor
   aws logs tail /aws/kinesis-analytics/$APP --since 30m --follow
   ```

### Resolution
<a name="resolution"></a>

 **If the app is in READY state (stopped):** 

```
APP=cms-dev-flink-trip-processor
aws kinesisanalyticsv2 start-application --application-name $APP
```

 **If the app is stuck in UPDATING state:** 

```
# Force stop the application
APP=cms-dev-flink-trip-processor
aws kinesisanalyticsv2 stop-application --application-name $APP --force
# Wait for READY status, then restart
```

 **If the app crashes immediately after starting:** 

This typically indicates a configuration error (wrong bootstrap servers, missing IAM permissions, or invalid JAR). Check the CloudWatch logs for the root cause, then:

```
# Delete and recreate the application with fresh configuration
APP=cms-dev-flink-trip-processor
TIMESTAMP=$(aws kinesisanalyticsv2 describe-application \
  --application-name $APP \
  --query "ApplicationDetail.CreateTimestamp" --output text)
aws kinesisanalyticsv2 delete-application \
  --application-name $APP \
  --create-timestamp $TIMESTAMP

# Redeploy via CDK
cd deployment
make phase4
```

 **Batch restart all Flink applications:** 

The solution includes a helper script to stop all applications, wait for READY status, and reconfigure:

```
cd deployment
./update-all-flink-apps.sh
```

Or to check and fix stuck applications:

```
cd deployment
./fix-flink-apps.sh
```

## Problem: Flink processor Kafka SSL connection errors
<a name="problem-flink-kafka-ssl-errors"></a>

Flink processors log SSL handshake failures or connection reset errors when communicating with MSK. This can occur after MSK broker maintenance, certificate rotation, or extended idle periods.

### Resolution
<a name="resolution-2"></a>

All processors include `KafkaConfig.withReconnect()` settings that handle most transient SSL issues automatically. The reconnect configuration applies:
+  `reconnect.backoff.ms=1000` — Initial reconnect delay
+  `reconnect.backoff.max.ms=10000` — Maximum reconnect delay
+  `connections.max.idle.ms=540000` — Close idle connections after 9 minutes
+  `metadata.max.age.ms=300000` — Refresh broker metadata every 5 minutes
+  `request.timeout.ms=30000` — Request timeout
+  `session.timeout.ms=45000` — Consumer session timeout

If errors persist after the automatic reconnect:

1. Delete and recreate the affected Flink application. Deleting and recreating has a higher success rate than updating in place:

   ```
   APP=cms-dev-flink-fw-telemetry-processor
   TIMESTAMP=$(aws kinesisanalyticsv2 describe-application \
     --application-name $APP \
     --query "ApplicationDetail.CreateTimestamp" --output text)
   aws kinesisanalyticsv2 delete-application \
     --application-name $APP --create-timestamp $TIMESTAMP
   # Redeploy via CDK
   cd deployment && make phase4
   ```

1. After recreation, start the application with `SKIP_RESTORE_FROM_SNAPSHOT` to avoid restoring stale state that may contain cached SSL sessions.

## Problem: Flink application running but processing zero records
<a name="problem-flink-no-records"></a>

The application shows `RUNNING` status but the `numRecordsInPerSecond` metric is zero. The idle processing CloudWatch alarm fires.

### Diagnosis
<a name="diagnosis-2"></a>

1. Verify the upstream Kafka topic has data:

   ```
   # Check topic offsets (requires kafka-tools or MSK client)
   # Look at the IoT Rule metrics to confirm messages are reaching MSK
   aws cloudwatch get-metric-statistics \
     --namespace "AWS/IoT" \
     --metric-name "RuleMessageThrottled" \
     --dimensions Name=RuleName,Value=cms_dev_iot_msk_rule \
     --start-time $(date -u -v-1H +%Y-%m-%dT%H:%M:%S) \
     --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
     --period 300 --statistics Sum
   ```

1. Check if the Flink consumer group is lagging or stuck at an old offset.

1. Verify the Flink application’s runtime properties have the correct Kafka topic name and bootstrap servers.

### Resolution
<a name="resolution-3"></a>
+ If no data is reaching MSK: Check the IoT Rules and VPC Destination configuration (see [Problem: IoT Rule not routing messages to MSK](telemetry-pipeline-troubleshooting.md#problem-iot-rule-not-routing)).
+ If data is in MSK but Flink is not consuming: The consumer group may be stuck. Delete and recreate the Flink application to reset the consumer offset to `latest`.
+ If the SimulatorPreprocessor is not running: Downstream processors will not receive data because MQTT Direct telemetry requires decompression before processing.

## Problem: Flink checkpoint failures
<a name="problem-flink-checkpoint-failures"></a>

Checkpoints fail with timeout errors, causing the application to restart repeatedly.

### Resolution
<a name="resolution-4"></a>

1. Check if DynamoDB writes are being throttled:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace "AWS/DynamoDB" \
     --metric-name "ThrottledRequests" \
     --dimensions Name=TableName,Value=cms-dev-storage-trips \
     --start-time $(date -u -v-1H +%Y-%m-%dT%H:%M:%S) \
     --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
     --period 300 --statistics Sum
   ```

1. If DynamoDB is throttled, the tables use on-demand billing and should auto-scale. Wait a few minutes for capacity to adjust.

1. If Redis writes are timing out, check ElastiCache connectivity from the Flink VPC configuration.

1. Increase the checkpoint interval if the application is processing high volumes:

   Update the Flink application runtime properties to set `checkpointing.interval=120000` (2 minutes instead of the default 60 seconds).

## Problem: FleetWise Edge agent not collecting signals
<a name="problem-fleetwise-agent-not-collecting-signals"></a>

The FWE agent starts and checks in but does not collect or upload telemetry data. This typically occurs when the agent has not received a valid collection scheme or decoder manifest.

### Resolution
<a name="resolution-5"></a>

1. Verify the CampaignSyncProcessor Flink application is in RUNNING state:

   ```
   aws kinesisanalyticsv2 describe-application \
     --application-name cms-dev-flink-campaign-sync-processor \
     --query "ApplicationDetail.ApplicationStatus"
   ```

1. Check that the agent’s checkin is reaching the `fw-checkin` Kafka topic by reviewing the CampaignSyncProcessor CloudWatch logs:

   ```
   aws logs tail /aws/kinesis-analytics/cms-dev-flink-campaign-sync-processor --follow
   ```

1. Verify that active campaigns exist in DynamoDB for the vehicle’s VIN:

   ```
   aws dynamodb query --table-name cms-dev-campaigns \
     --index-name targetArn-index \
     --key-condition-expression "targetArn = :arn" \
     --expression-attribute-values '{":arn": {"S": "vehicle:YOUR_VIN"}}'
   ```

1. Confirm the campaign includes `signalsToCollect` with valid signal IDs from the decoder manifest.

1. Check the FWE agent container logs for scheme receipt:

   ```
   # If using the simulation service
   curl http://localhost:5001/api/agent/logs/YOUR_VIN
   # Or directly via Docker
   docker logs fwe-YOUR_VIN --tail 100
   ```

## Problem: FleetWise telemetry not appearing in DynamoDB
<a name="problem-fleetwise-telemetry-not-appearing"></a>

The FWE agent is collecting signals (visible in agent logs) but telemetry records do not appear in the DynamoDB telemetry table.

### Resolution
<a name="resolution-6"></a>

1. Verify the IoT Rule `fw_dev_iot_msk_rule` is routing messages to the `fw-telemetry-raw` Kafka topic. Check IoT Core rule metrics in CloudWatch for error counts:

   ```
   aws cloudwatch get-metric-statistics \
     --namespace "AWS/IoT" \
     --metric-name "Failure" \
     --dimensions Name=RuleName,Value=fw_dev_iot_msk_rule \
     --start-time $(date -u -v-1H +%Y-%m-%dT%H:%M:%S) \
     --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
     --period 300 --statistics Sum
   ```

1. Verify the FWTelemetryProcessor Flink application is RUNNING and not showing SSL or connection errors:

   ```
   aws logs tail /aws/kinesis-analytics/cms-dev-flink-fw-telemetry-processor --follow
   ```

1. If the processor shows stale SSL connection errors, delete and recreate the Flink application with a fresh JAR (see [Problem: Flink processor Kafka SSL connection errors](#problem-flink-kafka-ssl-errors)).

1. Verify the decoder manifest exists in DynamoDB with signal mappings:

   ```
   aws dynamodb scan --table-name cms-dev-decoder-manifest --max-items 5
   ```

1. Check that the FWTelemetryProcessor output topic `cms-telemetry-preprocessed` is being consumed by downstream processors. If the SimulatorPreprocessor is also writing to this topic, verify there are no consumer group conflicts.

## Problem: Campaign not syncing to FWE agent
<a name="problem-fleetwise-campaign-not-syncing"></a>

The CampaignSyncProcessor is running but the agent does not receive collection schemes.

### Resolution
<a name="resolution-7"></a>

1. Check the CampaignSyncProcessor logs for IoT Core MQTT publish errors:

   ```
   aws logs tail /aws/kinesis-analytics/cms-dev-flink-campaign-sync-processor \
     --filter-pattern "ERROR" --since 30m
   ```

1. Verify the Flink application’s IAM role has `iot:Publish` permission on the topic `cms/fleetwise/vehicles/+/collection_schemes_and_decoder_manifests`.

1. Verify the agent is subscribed to the correct MQTT topic. The agent subscribes to `cms/fleetwise/vehicles/{vin}/collection_schemes_and_decoder_manifests` where `{vin}` must match the VIN in the campaign’s target.

1. Check campaign status in DynamoDB. Campaigns in `SUSPENDED` state will cause the processor to push an empty collection scheme, clearing the agent’s active collection.