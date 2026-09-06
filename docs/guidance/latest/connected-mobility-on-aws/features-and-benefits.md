

# Features and benefits
<a name="features-and-benefits"></a>

The solution provides the following features:

 **Streamlined Deployment** 

The guidance uses AWS CDK for infrastructure as code, enabling rapid deployment in 33-50 minutes through a phase-based approach. The guidance deploys integrated stacks with clear dependencies, eliminating the complexity of managing multiple independent modules. Deployment automation through Make commands and CDK CLI reduces manual errors and ensures consistent environments.

 **Real-Time Telemetry Processing** 

The solution implements a high-performance telemetry pipeline using Amazon MSK for message streaming and Apache Flink for real-time processing. This architecture handles high-volume data streams from thousands of vehicles simultaneously, detecting trips, identifying safety events, and generating maintenance alerts in real-time. The solution supports two telemetry ingestion modes: MQTT Direct, where the simulator publishes JSON telemetry to IoT Core, and FleetWise Edge, where the AWS IoT FleetWise Edge Agent collects CAN bus signals based on campaign collection schemes and uploads protobuf-encoded telemetry to the cloud.

 **FleetWise Edge Integration** 

The guidance integrates the [AWS IoT FleetWise Edge Agent](https://github.com/aws/aws-iot-fleetwise-edge) as a first-class telemetry source. A catalog-driven campaign system controls which signals the edge agent collects from the vehicle CAN bus. The CampaignSyncProcessor Flink application listens for agent checkins and pushes decoder manifests and collection schemes to the agent through IoT Core MQTT. The FWTelemetryProcessor decodes the protobuf telemetry uploaded by the agent, maps CAN signals to the standard format using the decoder manifest, and feeds the data into the existing processing pipeline. This enables the same downstream processors (trip detection, safety events, maintenance alerts) to work with both MQTT Direct and FleetWise Edge telemetry. For more information about the edge agent, see the [FleetWise Edge Agent repository on GitHub](https://github.com/aws/aws-iot-fleetwise-edge).

 **Fleet Manager Web Application** 

A modern React-based web application provides comprehensive fleet management capabilities including real-time vehicle tracking on interactive maps, trip history and analytics, maintenance alert management, and driver behavior monitoring. The application uses Amazon Location Service for mapping, geocoding, and routing capabilities.

 **Real-Time Vehicle State Management** 

Amazon ElastiCache for Redis implements the Last Known State (LKS) pattern, a core design pattern in connected vehicle platforms. Rather than querying the telemetry database for the latest record on every API call, the Flink telemetry processor writes every signal value to Redis hashes as telemetry arrives. This provides sub-millisecond lookups for the Fleet Manager UI. Redis geospatial indexing enables map-based vehicle proximity queries, and Redis streams provide capped time-series data for sparkline charts. Vehicle state expires automatically when a vehicle goes offline, and the geo index is updated in real-time as vehicles move.

 **Secure Vehicle Connectivity** 

The guidance registers vehicles as AWS IoT Core things to securely monitor vehicles, their certificates, and their policies. Vehicle provisioning uses X.509 certificates with automated fleet provisioning workflows. After registration, vehicles receive individual certificates and key pairs for secure, repeated connections.

 **Scalable Data Storage** 

Amazon DynamoDB tables store vehicle data, trip history, maintenance alerts, and driver information with automatic scaling and point-in-time recovery. Amazon S3 buckets archive telemetry data for long-term analysis. All data is encrypted at rest and in transit.

 **Location Services Integration** 

Amazon Location Service provides real-time vehicle tracking on interactive maps, route calculation and optimization, geocoding and reverse geocoding, and geofencing capabilities. The Fleet Manager displays vehicle positions, historical routes, and enables location-based alerts.

 **Authentication and Authorization** 

Amazon Cognito manages user authentication and authorization for the Fleet Manager application. The solution supports user pools for direct sign-up/sign-in, multi-factor authentication, and identity pools for AWS resource access with fine-grained permissions.

 **Network Security** 

The solution deploys a single Amazon VPC with public and private subnets across multiple Availability Zones. MSK and ElastiCache run in private subnets isolated from the internet. Security groups restrict traffic between components following least-privilege principles. VPC endpoints enable private connectivity to AWS services.

 **API Access** 

RESTful APIs through Amazon API Gateway enable integration with external systems. APIs provide vehicle management, trip queries, alert subscriptions, and location services. AWS Lambda functions process requests and integrate with DynamoDB, ElastiCache, and other AWS services.

 **Integrated Vehicle Simulator** 

A Python-based vehicle simulator generates realistic telemetry data for testing and development. The simulator supports multiple vehicles, configurable routes, and various driving scenarios including normal operation, safety events, and maintenance conditions. The simulator operates in two modes: MQTT Direct mode publishes JSON telemetry directly to IoT Core, while FleetWise Edge mode generates CAN bus signals and runs per-vehicle FWE agent Docker containers that collect signals based on active campaigns and upload protobuf telemetry to the cloud.

 **Remote Vehicle Commands** 

The solution enables bidirectional communication with vehicles through a remote commands system. Fleet managers send commands (door locks, lights, climate control, horn, engine start/stop) from the web application, which are published to vehicles via IoT Core MQTT. The system tracks command execution status (SENT, IN\_PROGRESS, SUCCEEDED, FAILED, TIMEOUT) and measures round-trip latency. The command catalog is dynamically derived from actuatable signals in the signal catalog, making it extensible without code changes.

 **Geofence Management** 

Fleet managers define geographic boundaries (geofences) through the web application. The GeofenceProcessor Flink application evaluates vehicle positions against active geofences in real-time, generating safety events when vehicles cross boundaries. Geofences support vehicle-specific and global (all vehicles) targeting with configurable actions.

 **Cloud Simulation** 

Cloud-based simulation runs on Amazon ECS, with Fargate for MQTT Direct mode and EC2-backed ECS (ARM64 t4g.small) for FleetWise Edge mode. A Lambda orchestrator manages simulation lifecycle through API Gateway. In FleetWise Edge mode, separate ECS tasks for the FWE agent and Python simulator share virtual CAN interfaces on the same EC2 host, enabling realistic CAN bus telemetry generation without deploying to actual vehicles.

 **OEM Telemetry Integration** 

The OEMTelemetryProcessor enables integration with third-party OEM APIs without modifying the core processing pipeline. Customers define transform manifests that map OEM-specific data formats to the signal catalog. Manifests support field mapping, unit conversion (multiply, formula, lookup table), conditional mapping, and validation rules. Transform manifests are stored in S3 with versioning.

 **Signal Catalog and Decoder Manifest** 

The guidance includes a comprehensive signal catalog with 271 signals organized into 15 CAN messages. The catalog follows the [COVESA Vehicle Signal Specification (VSS)](https://covesa.global/) naming convention and maps between DBC signal names, JSON field names, and VSS paths. The signal catalog serves as the single source of truth for the entire platform — it drives decoder manifest generation for FleetWise Edge Agents, defines the command catalog for remote vehicle commands, and provides the field mapping for OEM telemetry transformation. The catalog is extensible through the UI or API without code changes.

 **Fleet Campaign Management** 

Campaigns can be assigned at the fleet level, automatically fanning out to all vehicles in the fleet. Fleet-assigned campaigns are locked at the vehicle level — operators manage them from the fleet detail page. When a fleet campaign is suspended or resumed, the change cascades to all child vehicle records. Individual vehicles can also have directly-assigned campaigns that are independently managed.

 **Warranty Claims Management** 

The Warranty page tracks warranty-eligible failures detected by the telemetry pipeline, filed claims, and OEM recovery. Claims are stored in DynamoDB with status tracking (Submitted, Approved, Paid, Denied). KPIs show total claims, recovered amount, open claims, and pending amount. Recall-related warranty claims are tracked separately.

 **Driver Assignment and Trip Attribution** 

Each vehicle has a default assigned driver (`currentDriverId`). When the Flink trip processor detects a new trip, it attributes the trip to the vehicle’s current driver. Fleet managers can reassign drivers through the vehicle detail page. Safety events during a trip are attributed to the assigned driver for safety scoring.

 **Observability and Monitoring** 

All components send logs and metrics to Amazon CloudWatch. The solution includes pre-configured dashboards for monitoring telemetry flow, processing latency, error rates, and system health. CloudWatch Alarms notify operators of issues requiring attention.