

# Platform components
<a name="cms-on-aws-stacks-and-services"></a>

The high-level architectural descriptions for the Platform components are as follows:

## Networking and caching
<a name="networking-caching"></a>

The InfrastructureStack provides the foundational networking and caching infrastructure for the guidance.

 **Amazon Virtual Private Cloud (Amazon VPC)** – A logically isolated virtual network with public and private subnets across multiple Availability Zones. The VPC includes a NAT Gateway for secure outbound internet access from private subnets. For more details, see [Amazon VPC](https://aws.amazon.com/vpc).

 **Amazon ElastiCache for Redis** – A managed in-memory caching service that implements the Last Known State (LKS) pattern for connected vehicles. The Flink telemetry processor writes every signal value, timestamp, and vehicle metadata to Redis hashes on each telemetry message, maintaining a continuously updated snapshot of each vehicle’s state. The Fleet Manager API reads this snapshot for sub-millisecond vehicle detail lookups and uses Redis geospatial indexing (GEOADD/GEOSEARCH) for map-based vehicle proximity queries. Redis streams provide capped time-series data for UI sparkline charts. All keys expire automatically when a vehicle stops sending telemetry. For more details, see [Amazon ElastiCache](https://aws.amazon.com/elasticache).

## Data storage
<a name="data-storage-overview"></a>

The StorageStack deploys all data storage resources for the guidance.

 **Amazon DynamoDB** – Four tables store vehicle data, trip history, maintenance alerts, and driver information. All tables use on-demand billing for automatic scaling and have point-in-time recovery enabled for data protection. For more details, see [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

 **Amazon S3** – Buckets store archived telemetry data for long-term analysis and host the Fleet Manager web application assets. All buckets have versioning and encryption enabled. For more details, see [Amazon S3](https://aws.amazon.com/s3/).

## Message streaming
<a name="message-streaming"></a>

The MSKStack creates the streaming data platform for high-throughput telemetry processing.

 **Amazon MSK (Managed Streaming for Apache Kafka)** – A three-broker Kafka cluster deployed across multiple Availability Zones provides fault-tolerant, high-throughput message streaming. The cluster includes pre-configured topics for telemetry data, trip events, and maintenance alerts. For more details, see [Amazon MSK](https://aws.amazon.com/msk/).

## Vehicle connectivity
<a name="vehicle-connectivity"></a>

The IoTStack configures vehicle connectivity and fleet management capabilities.

 **AWS IoT Core** – Manages secure device connectivity using X.509 certificates and MQTT protocol. Thing types define vehicle categories, and IoT policies control device permissions. The stack includes certificate management and device provisioning workflows. For more details, see [AWS IoT Core](https://aws.amazon.com/iot-core).

## Telemetry ingestion
<a name="telemetry-ingestion-overview"></a>

The TelemetryIntegrationStack connects IoT Core to the MSK streaming platform.

 **AWS IoT Rules** – Route incoming telemetry messages from vehicles to Amazon MSK topics. Rules use VPC Destinations to securely connect IoT Core to the MSK cluster within the VPC. For more details, see [AWS IoT Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html).

## Stream processing
<a name="stream-processing-overview"></a>

The FlinkStack deploys real-time stream processing applications.

 **Amazon Kinesis Data Analytics for Apache Flink** – Runs Flink applications that process telemetry streams in real-time. Applications detect trip start/end events, identify safety violations (speeding, harsh braking), and generate predictive maintenance alerts based on vehicle sensor data. The FWTelemetryProcessor decodes FleetWise Edge protobuf uploads and maps CAN signals to the standard standard format. The CampaignSyncProcessor listens for FWE agent checkins and pushes decoder manifests and collection schemes through IoT Core MQTT. The GeofenceProcessor evaluates vehicle positions against active geofences and generates boundary crossing events. The OEMTelemetryProcessor transforms third-party OEM telemetry using S3-hosted transform manifests. Processed results are written to DynamoDB tables and ElastiCache for immediate access. For more details, see [Amazon Kinesis Data Analytics](https://aws.amazon.com/kinesis/data-analytics/).

## Remote commands and geofences
<a name="remote-commands-geofences"></a>

The CommandsStack enables bidirectional communication with vehicles through remote commands.

 **AWS Lambda** – Two Lambda functions handle command operations. The Commands Lambda sends commands to vehicles by publishing to IoT Core MQTT topics and exposes a REST API for command management, command history, and geofence CRUD operations. The Command Response Handler Lambda processes vehicle command acknowledgments received through an IoT Rule on the response topic. For more details, see [AWS Lambda](https://aws.amazon.com/lambda/).

 **AWS IoT Core MQTT** – Commands are published to `cms/commands/{vehicleId}/request` and responses are received on `cms/commands/{vehicleId}/response`. The command catalog is derived from actuatable signals in the signal catalog, supporting door locks, lights, climate control, windows, trunk, horn, and remote engine start/stop.

## Fleet simulation
<a name="fleet-simulation"></a>

The SimulationStack deploys cloud-based simulation infrastructure.

 **Amazon ECS (Fargate \+ EC2)** – An ECS cluster runs simulation tasks on demand using two launch types. In MQTT Direct mode, a single Fargate task runs the Python simulator container. In FleetWise Edge mode, EC2-backed ECS (t4g.small ARM64, Amazon Linux 2023 ECS-optimized AMI) runs two separate tasks on the same host using HOST network mode: the FWE agent task (long-lived, runs the FleetWise Edge Agent binary) and the simulator task (per-trip, runs the Python telemetry simulator). Both tasks share virtual CAN interfaces (vcan0, vcan1, vcan2…​) on the host kernel for per-vehicle isolation. An Auto Scaling Group (min=0, max=3) with an ECS Capacity Provider manages EC2 instances. A Lambda function serves as the API orchestrator, receiving simulation requests through API Gateway and launching ECS tasks. Worker logs stream to CloudWatch for monitoring. Simulation state is tracked in a DynamoDB table.

## FleetWise Edge integration
<a name="fleetwise-integration"></a>

The FleetWiseStack deploys AWS IoT FleetWise resources for edge agent integration.

 **AWS IoT FleetWise** – Manages signal catalogs, vehicle models, decoder manifests, and campaign definitions for FleetWise Edge Agent integration. The stack creates the FleetWise signal catalog from the signal catalog, configures decoder manifests for CAN bus signal mapping, and provisions campaign infrastructure. For more details, see [AWS IoT FleetWise](https://aws.amazon.com/iot-fleetwise/).

## Fleet Manager application
<a name="fleet-manager-app"></a>

The UIStack provides the Fleet Manager web application and backend APIs.

 **Amazon CloudFront** – Distributes the React-based Fleet Manager web application globally with low latency. The application provides real-time fleet monitoring, vehicle tracking, trip analytics, and alert management. For more details, see [Amazon CloudFront](https://aws.amazon.com/cloudfront/).

 **Amazon API Gateway** – Exposes RESTful APIs for the web application to interact with backend services. APIs handle vehicle management, trip queries, alert subscriptions, and location services. For more details, see [Amazon API Gateway](https://aws.amazon.com/api-gateway/).

 **AWS Lambda** – Serverless functions process API requests, query DynamoDB and ElastiCache, and integrate with other AWS services. Functions are written in Python and use the AWS SDK (boto3). For more details, see [AWS Lambda](https://aws.amazon.com/lambda/).

 **Amazon Cognito** – Manages user authentication and authorization for the Fleet Manager application. Supports user pools for direct sign-up/sign-in and identity pools for AWS resource access. For more details, see [Amazon Cognito](https://aws.amazon.com/cognito/).

 **Amazon Location Service** – Provides mapping, geocoding, and routing capabilities for real-time vehicle tracking. The Fleet Manager displays vehicle positions on interactive maps, calculates routes, and supports geofencing. For more details, see [Amazon Location Service](https://aws.amazon.com/location/).