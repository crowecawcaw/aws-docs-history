

# OEM cloud connector
<a name="connector-stack"></a>

An OEM cloud connector brings telemetry from a vehicle maker’s or telematics provider’s cloud into the platform, for vehicles that send data to that cloud rather than to AWS IoT Core. The `ConnectorStack` deploys one connector per OEM source as an Amazon ECS Fargate task. Each connector writes JSON records to the `cms-telemetry-oem` Kafka topic, tagged with its source, and the rest of the pipeline treats the records like any other telemetry.

## Connector architecture
<a name="connector-stack-architecture"></a>

A connector is a long-lived ECS Fargate container. Three connection modes cover the ways OEM clouds deliver data, selected at deploy time with `CONNECTOR_TYPE`:
+  ** `rest_polling` ** — polls the OEM’s REST API on a schedule.
+  ** `grpc_streaming` ** — holds a long-lived gRPC stream to the OEM’s feed service.
+  ** `websocket_inbound` ** — accepts inbound WebSocket connections from an OEM push service, behind an Application Load Balancer with TLS termination.

 `CONNECTOR_NAME` names the connector (for example, `<oem>-feed`) and sets the `OEM_SOURCE` value stamped on every record, the ECS service and cluster names (`cms-{stage}-connector-<oem>-feed`), and its log group. OEM credentials are held in AWS Secrets Manager and connector settings in AWS Systems Manager Parameter Store, both scoped to the connector.

The connector turns OEM-specific payloads into CMS telemetry JSON and publishes them to `cms-telemetry-oem`. The OEMTelemetryProcessor Flink application then applies the transform manifest in Amazon S3 for the record’s `oem_source` value, mapping the OEM’s signal names and units to the CMS signal catalog, and writes the result to `cms-telemetry-preprocessed` for the core pipeline. Adding an OEM therefore needs a connector and a transform manifest, and no change to downstream processing.

## Vehicle enrollment and quota
<a name="connector-stack-enrollment"></a>

Vehicles that report through an OEM cloud are enrolled into CMS fleets through the connector’s admin Lambda functions, on routes under `/admin/<oem>/` (bulk enroll, bulk unenroll, enrollment quota, preflight, add vehicle, and vehicle state). The connector applies the OEM API’s enrollment rate limit, tracked in Amazon DynamoDB; the reference connector allows four enrollments per hour. Users in the `platform-admin` Cognito group can enroll and unenroll across all fleets, and users in `fleet-operator` are limited to their fleets through the `custom:fleetIds` claim.