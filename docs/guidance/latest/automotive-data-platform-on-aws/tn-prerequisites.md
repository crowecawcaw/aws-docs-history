# Prerequisites

This solution extends the [Guidance for Connected Mobility on AWS](../connected-mobility-on-aws/developer-guide.md "../connected-mobility-on-aws/developer-guide.md") pipeline. The following components must be deployed before using the telemetry normalization data product.

Source code: [Connected Mobility on AWS (GitHub)](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws")

## Required CMS stacks

| Stack                     | What It Provides                                                                                                                                                                               | Deploy Phase      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| StorageStack              | DynamoDB tables for vehicles, fleets, fleet enrollment, signal catalog, WebSocket connections, drivers, trips, safety events, and maintenance alerts                                           | Phase 1           |
| MSKStack                  | Amazon MSK (Kafka) cluster with IAM authentication, VPC with private subnets, Amazon ElastiCache (Redis) for vehicle state caching, and security groups for inter-service communication        | Phase 3           |
| TelemetryIntegrationStack | AWS IoT Core rules that route MQTT and FleetWise Edge telemetry to MSK topics, VPC destination for IoT-to-MSK connectivity                                                                     | Phase 3b          |
| IoTStack                  | AWS IoT Core device policies, lifecycle event handlers, MQTT topic subscriptions                                                                                                               | Phase 1           |
| UIStack                   | Amazon API Gateway (REST and WebSocket), Amazon Cognito user pool with `platform-admin`, `fleet-operator`, and `fleet-viewer` groups, Fleet Manager Lambda API, Amazon CloudFront distribution | Phase 1           |
| FlinkStack                | Amazon Managed Service for Apache Flink applications — SimulatorPreprocessor, FWTelemetryProcessor, OEMTelemetryProcessor, and EventDrivenTelemetryProcessor                                   | Phase 4 + Phase 5 |

## Key infrastructure dependencies

- **Amazon MSK** — Kafka topics for telemetry ingestion (`cms-telemetry-raw`, `fw-telemetry-raw`, `cms-telemetry-oem`), normalization (`cms-telemetry-preprocessed`), and per-fleet distribution (`cms-fleet-{fleetId}-telemetry`)
- **Amazon ElastiCache (Redis)** — Latest vehicle state cache, signal catalog cache, and fleet enrollment lookup cache used by the Flink processors and REST API
- **Amazon Cognito** — User authentication with three groups (`platform-admin`, `fleet-operator`, `fleet-viewer`) and `custom:fleetIds` attribute for tenant-scoped access control
- **Signal catalog table** — DynamoDB table (`cms-{stage}-signal-catalog`) that defines every canonical signal name, unit, and data type. All preprocessors normalize to this contract.
- **Fleet enrollment table** — DynamoDB table (`cms-{stage}-storage-fleet-enrollment`) that maps each vehicle to a fleet. Used by the EventDrivenTelemetryProcessor to route telemetry to per-fleet Kafka topics.
- **WebSocket API Gateway** — The real-time distribution endpoint that external consumers connect to. Deployed by the UIStack.

## Deployment order

```
cd connected-mobility-guidance-on-aws/deployment

# Phase 1: Storage + IoT + UI (DynamoDB, Cognito, API Gateway, CloudFront)
make phase1 DEPLOYMENT_STAGE=prod AWS_REGION=us-east-2

# Seed fleet enrollment data
make seed-fleet-enrollment DEPLOYMENT_STAGE=prod AWS_REGION=us-east-2

# Phase 3: MSK cluster (Kafka, VPC, Redis)
make phase3 DEPLOYMENT_STAGE=prod AWS_REGION=us-east-2

# Phase 3b: IoT Core → MSK telemetry routing
make phase3b DEPLOYMENT_STAGE=prod AWS_REGION=us-east-2

# Phase 4: Flink applications
make phase4 DEPLOYMENT_STAGE=prod AWS_REGION=us-east-2

# Phase 5: Configure Flink with MSK bootstrap servers
make configure-flink DEPLOYMENT_STAGE=prod AWS_REGION=us-east-2
```
