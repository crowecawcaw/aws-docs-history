# Key Capabilities

The solution delivers:

- **Multi-source normalization**: Unified signal schema across direct MQTT, FleetWise Edge (protobuf/CAN), and OEM cloud APIs (REST/streaming)
- **Cloud-to-cloud OEM integration**: Authenticate to multiple OEM cloud APIs using OAuth 2.0, ingest telemetry, and normalize using configurable transform manifests
- **Real-time telemetry distribution**: Fleet operators receive live FleetWise Edge telemetry via WebSocket API, scoped to their enrolled vehicles
- **Historical analytics**: Iceberg tables partitioned by fleet for Athena queries with row-level tenant isolation via Lake Formation
- **Signal catalog contract**: A single DynamoDB table defines every canonical signal name and unit — all preprocessors map to this contract
- **Configuration-driven OEM onboarding**: New OEMs are added by uploading a transform manifest — no code changes required
