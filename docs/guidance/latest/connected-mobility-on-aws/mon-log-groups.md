

# Where each component logs
<a name="mon-log-groups"></a>


| Component | Log group | 
| --- | --- | 
| Stream processing applications |  `/aws/kinesis-analytics/cms-{stage}-flink-<processor>` — one per application: `trip-processor`, `safety-processor`, `maintenance-processor`, `geofence-processor`, `event-driven-telemetry-processor`, `telemetry-enhanced-final`, `simulator-preprocessor`, `fw-telemetry-processor`, `oem-telemetry-processor`, `campaign-sync-processor`  | 
| Managed Streaming for Apache Kafka |  `/aws/msk/cms-{stage}-msk-<suffix>`  | 
| Simulation and edge containers |  `/ecs/cms-{stage}/sim-worker`, `/ecs/cms-{stage}/fwe-simulator`, `/ecs/cms-{stage}/fwe-agent`, `/ecs/cms-{stage}/vehicle-ecu`  | 
| Lambda functions |  `/aws/lambda/cms-{stage}-<function>`  | 

Follow a single processor:

```
aws logs tail /aws/kinesis-analytics/cms-<stage>-flink-trip-processor --follow
```