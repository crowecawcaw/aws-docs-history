

# Architecture overview
<a name="architecture-overview"></a>

This section provides a high-level description of the guidance architecture, including the 14 integrated stacks that comprise the guidance. The architecture uses [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) for infrastructure deployment with a phase-based approach that ensures proper dependency management and efficient deployment.

The solution provides a modern, scalable telemetry architecture designed to handle high-volume, real-time data streams from connected vehicle fleets. Each installation follows the same core architecture with 14 integrated stacks — deployed across four sequential phase groups — that can be customized to meet specific requirements.

## Solution architecture
<a name="solution-architecture"></a>

Deploying this solution with the default parameters creates the following architecture in your AWS account.

**Note**  
The architecture diagrams in this guide are currently being updated to reflect the current stack topology. The narrative text on this page describes the current deployed architecture; the diagrams may not yet show all components described in the narrative.

![The solution deploys six integrated stacks as described in the following sections.](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/architecture-overview.png)


**Note**  
CloudFormation resources are created from [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) constructs.

The solution architecture consists of 14 integrated stacks deployed across four phase groups:

1.  **InfrastructureStack** – Provides the foundational networking and caching infrastructure including Amazon VPC with public and private subnets, NAT Gateway for secure internet access, and Amazon ElastiCache for Redis to maintain real-time vehicle state for sub-second lookups.

1.  **StorageStack** – Deploys Amazon DynamoDB tables for vehicles, trips, alerts, drivers, commands, geofences, and signal catalog with on-demand billing and point-in-time recovery enabled. Also provisions Amazon S3 buckets for telemetry data archival and web application assets.

1.  **MSKStack** – Creates an Amazon MSK (Managed Streaming for Apache Kafka) cluster with three brokers for high-throughput telemetry data streaming. The cluster is deployed in the VPC with appropriate security groups and includes topics for telemetry, trips, alerts, FleetWise telemetry, and OEM telemetry.

1.  **IoTStack** – Configures AWS IoT Core for vehicle connectivity including thing types, IoT policies, and certificate management. This stack handles fleet management operations and device provisioning.

1.  **TelemetryIntegrationStack** – Establishes the connection between AWS IoT Core and Amazon MSK through IoT Rules and VPC Destinations, enabling real-time telemetry data flow from vehicles to the streaming platform.

1.  **FlinkStack** – Deploys Amazon Kinesis Data Analytics for Apache Flink applications that process streaming telemetry data in real-time. Ten applications handle telemetry preprocessing, trip detection, safety events, maintenance alerts, FleetWise protobuf decoding, campaign synchronization, geofence evaluation, and OEM telemetry transformation. CloudWatch alarms monitor processor health and idle processing.

1.  **UIStack** – Provides the Fleet Manager web application through Amazon CloudFront and Amazon S3, with backend APIs via Amazon API Gateway and AWS Lambda. Includes Amazon Cognito for user authentication and Amazon Location Service for real-time vehicle tracking and mapping capabilities.

1.  **CommandsStack** – Enables bidirectional communication with vehicles through remote commands sent via IoT Core MQTT. Includes command catalog derived from the signal catalog, command status tracking with latency measurement, and geofence management APIs.

1.  **SimulationStack** – Deploys cloud-based simulation infrastructure including an EC2-backed ECS cluster with separate task definitions for the FWE agent and Python simulator, plus a Lambda orchestrator. Supports both MQTT Direct (Fargate) and FleetWise Edge (EC2 with HOST network mode and per-vehicle vcan isolation) simulation modes.

1.  **FleetWiseStack** – Deploys AWS IoT FleetWise resources including signal catalogs, decoder manifests, and campaign management infrastructure for FleetWise Edge Agent integration.

1.  **ConnectorStack** – Deploys an Amazon ECS Fargate worker for cloud-to-cloud OEM telemetry ingestion. The gRPC-streaming connector receives telemetry from an OEM vehicle data cloud and lands it on the `cms-telemetry-oem` Kafka topic, where the OEMTelemetryProcessor applies transform manifest normalization before routing through the standard pipeline.

1.  **WsFanoutStack** – Deploys a Kafka-to-WebSocket bridge that fans out per-fleet telemetry topics (`cms-fleet-{fleetId}-telemetry`) to connected Fleet Manager UI clients in real time. The WebSocket API `$connect` route uses a Cognito JWT Lambda REQUEST authorizer, requiring a valid bearer token on upgrade.

1.  **BedrockAgentsStack** (optional, not included in `deploy-all`) – Deploys a Bedrock multi-agent system consisting of a supervisor agent and specialist sub-agents, together with an Amazon Bedrock AgentCore runtime for both bidirectional voice and HTTP text invocation modes. The stack is provisioned separately with `make deploy-bedrock-agents` to let operators control Bedrock inference costs independently.

1.  **TcoStack** – Deploys cost analytics infrastructure for fleet total cost of ownership tracking.

### Deployment flow
<a name="deployment-flow"></a>

The solution uses four sequential phase groups to manage stack dependencies. Run each group as a single `make` target or use `make deploy-all` for a fully automated end-to-end deploy.

 **phase-foundation** – Deploys the data-processing seed stack (signal catalog, decoder manifest), StorageStack, IoTStack, UIStack, MSKStack, and TelemetryIntegrationStack. Duration: 15–20 minutes (MSK cluster creation dominates).

 **phase-streaming** – Deploys FlinkStack (builds the universal Flink JAR and deploys all 10 Flink applications) and the FleetWise integration stacks. Duration: 10–15 minutes.

 **phase-seeds** – Seeds the signal catalog, decoder manifest, event catalog, and default fleet enrollment into DynamoDB. Duration: 3–5 minutes.

 **phase-services** – Deploys SimulationStack, CommandsStack, WsFanoutStack, ConnectorStack, and TcoStack. Also runs `make regenerate-runtime-config` and seeds demo personas. Duration: 5–10 minutes.

 **deploy-bedrock-agents** (optional) – Deploys BedrockAgentsStack as a separate, opt-in step. Operators who do not require the in-UI conversational assistant can skip this target to avoid Bedrock inference costs.

Total deployment time: 45–65 minutes.