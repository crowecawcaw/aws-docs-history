# Solution Components

The solution consists of five main components:

## Normalization Pipeline

Three Apache Flink preprocessors handle the different wire formats, all outputting the same canonical JSON to a shared Kafka topic:

| Preprocessor          | Source Format                   | Processing                                                                                           |
| --------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| SimulatorPreprocessor | gzip+base64 JSON via MQTT       | Decompress only — simulator already uses canonical field names                                       |
| FWTelemetryProcessor  | Protobuf via FleetWise Edge     | Decode protobuf → resolve signal ID to VSS path → map VSS path to canonical field via signal catalog |
| OEMTelemetryProcessor | OEM-specific JSON via cloud API | Load transform manifest from S3 → map OEM fields to canonical fields → apply unit conversions        |

## Cloud-to-Cloud OEM Integration

OEM cloud APIs expose vehicle telemetry through proprietary authentication, data formats, and delivery mechanisms. The solution supports two connector patterns:

**REST polling connector** (AWS Lambda + Amazon EventBridge): For OEMs that expose request/response APIs. A scheduled Lambda authenticates via OAuth 2.0 `client_credentials`, polls the OEM REST API, and writes raw JSON to Kafka.

**Streaming connector** (Amazon ECS Fargate): For OEMs that push telemetry in real-time via WebSocket or webhook. A long-running Fargate task receives data, decodes the wire format, and writes to Kafka. Requires a public endpoint (Application Load Balancer + TLS).

Each OEM’s data is normalized using a **transform manifest** — a JSON configuration stored in Amazon S3 that maps OEM-specific field names, JSONPath source paths, and unit conversions to the canonical schema. The OEM Integration Wizard in the Fleet Manager UI can auto-generate manifests from sample telemetry data.

## Event-Driven Routing

The `EventDrivenTelemetryProcessor` (Flink) reads normalized telemetry and routes each message to multiple destinations:

- **Amazon ElastiCache (Redis)** — Latest vehicle state for sub-millisecond REST API lookups
- **Per-fleet Kafka topics** (`cms-fleet-{fleetId}-telemetry`) — Real-time distribution scoped by fleet
- **Domain topics** — Trip detection, safety event processing, maintenance alert generation
- **Amazon S3 Iceberg sink** — Historical analytics partitioned by fleet and day

Fleet routing uses the fleet enrollment table to look up each vehicle’s fleet assignment (Redis-cached with DynamoDB fallback).

## Real-Time Telemetry Distribution

Fleet operators and external consumers (dashboards, mobile apps, partner integrations) connect via WebSocket to receive live FleetWise Edge telemetry:

```
wss://{endpoint}/live?fleetId=FLEET-001&token={jwt}
```

The distribution architecture:

1. **EventDrivenTelemetryProcessor** writes FWE telemetry to per-fleet Kafka topics
2. **ECS Fargate fanout consumer** subscribes to all fleet topics via regex pattern
3. For each message, the consumer queries the WebSocket connections table for active connections matching the fleet
4. Messages are pushed to connected clients via the API Gateway WebSocket Management API
5. Stale connections are automatically cleaned up

The WebSocket `$connect` handler validates the JWT token and verifies the requested fleet ID matches the user’s `custom:fleetIds` Cognito attribute. Platform admins can subscribe to any fleet.

For consumers that do not support WebSocket, the REST API provides latest vehicle state from Redis (poll-based fallback).

## Historical Analytics (Data Product)

Normalized telemetry is stored in Apache Iceberg tables for fleet operators who need historical trip analytics, utilization reports, and cross-fleet benchmarking:

- **Iceberg tables** — Partitioned by `fleetId` and day for efficient queries and tenant isolation
- **Athena queries** — Pre-built views for fleet utilization, trip history, signal coverage, and vehicle health snapshots
- **Lake Formation** — Row-level security ensures fleet operators can only query their own fleet’s data

## Integration with Other ADP Guidance

The normalized telemetry output integrates with other guidance in this platform:

- **Data Governance** — A Glue ETL job reads from the S3 Iceberg sink, classifies fields as PII or non-PII, and writes to separate governed data stores with Lake Formation access controls. Precise GPS coordinates and driver identifiers are separated from anonymized fleet analytics data.
- **Predictive Maintenance** — Tire pressure signals (`tire_fl`, `tire_fr`, `tire_rl`, `tire_rr`) from the normalized telemetry feed into the predictive maintenance ML pipeline for anomaly detection. Alerts are written back to the CMS maintenance alerts table for display in the Fleet Manager UI.
