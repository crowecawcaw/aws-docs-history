# OEM cloud connector (ConnectorStack)

The ConnectorStack deploys an ECS Fargate task that ingests telemetry from a third-party OEM telematics API and writes clean JSON records to the `cms-telemetry-oem` Kafka topic.

## Connector architecture

The connector worker runs as a long-lived ECS Fargate container supporting three connection modes, selected at deploy time via the `CONNECTOR_TYPE` environment variable:

- **`grpc_streaming`** — Maintains a long-lived gRPC client connection to the OEM feed service.
  This is the primary mode for OEM1 cloud-to-cloud integration.
- **`rest_polling`** — Poll-sleep loop against an OEM REST API endpoint.
- **`websocket_inbound`** — Accepts inbound WebSocket connections from an OEM push service, with an Application Load Balancer and TLS termination.

The connector transforms incoming OEM-specific payloads into standard CMS telemetry JSON and publishes to the `cms-telemetry-oem` topic.
Downstream, the OEMTelemetryProcessor Flink application applies the S3-hosted transform manifest for the `oem_source` field value and outputs to `cms-telemetry-preprocessed` for the core processing pipeline.

## Vehicle enrollment and quota

OEM1 vehicles are enrolled into CMS fleets through admin Lambda functions exposed on the Fleet Manager API.
A rate limit of four enrollments per hour applies per OEM1 account.
Fleet operators with the `platform-admin` Cognito group can perform bulk enroll and unenroll operations across all fleets.
Users with the `fleet-operator` group are scoped to their assigned fleets via the `custom:fleetIds` JWT claim.
