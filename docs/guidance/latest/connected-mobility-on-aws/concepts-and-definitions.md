# Concepts and definitions

**Stack** – A collection of AWS resources deployed together as a unit using AWS CDK. the guidance consists of modular stacks including StorageStack, MSKStack, IoTStack, FlinkStack, UIStack, CommandsStack, and optional stacks for FleetWise, simulation, and predictive maintenance.

**Phase** – A deployment stage in the guidance’s phase-based deployment approach. Each phase deploys one or more stacks with clear dependencies on previous phases.

**Telemetry** – Data transmitted from vehicles including GPS coordinates, speed, engine metrics, tire pressure, battery levels, and diagnostic information.

**Trip** – A sequence of telemetry messages representing a vehicle journey from ignition on to ignition off. Trips are detected automatically by Flink applications based on vehicle state changes.

**Safety Event** – A driving behavior that violates safety thresholds including speeding, harsh braking, rapid acceleration, or sharp turns. Safety events are detected in real-time and generate alerts.

**Maintenance Alert** – A notification generated when vehicle sensor data indicates a potential maintenance condition such as low tire pressure, high engine temperature, or diagnostic trouble codes.

**Fleet Manager** – The React-based web application that provides fleet management, vehicle tracking, trip analytics, and alert management capabilities.

**Vehicle State** – The current status of a vehicle including location, speed, ignition status, and sensor readings. Vehicle state is maintained in ElastiCache for real-time access.

**Last Known State (LKS)** – A design pattern where the most recent value of every signal for every vehicle is maintained in an in-memory store (Redis). This eliminates the need to query the telemetry database for current values, enabling sub-millisecond lookups. The LKS is updated on every telemetry message and expires automatically when a vehicle goes offline.

**Thing** – An AWS IoT Core representation of a physical device (vehicle). Things have attributes, certificates, and policies that control their connectivity and permissions.

**MQTT** – Message Queuing Telemetry Transport, a lightweight messaging protocol used for vehicle-to-cloud communication over IoT Core.

**FleetWise Edge Agent (FWE)** – An AWS IoT FleetWise software component that runs on the vehicle (or in a Docker container for simulation) and collects CAN bus signals based on collection schemes pushed from the cloud. The agent encodes collected signals as protobuf and uploads them to IoT Core.

**Campaign** – A FleetWise collection campaign that defines which signals the edge agent collects, the collection frequency, and the target vehicles. Campaigns are stored in DynamoDB and pushed to agents as protobuf collection schemes by the CampaignSyncProcessor.

**Decoder Manifest** – A mapping between raw CAN bus signal IDs and human-readable signal names (for example, `Vehicle.Speed`, `Vehicle.TirePressure.FrontLeft`). The decoder manifest is pushed to the FWE agent alongside collection schemes so the agent knows how to interpret CAN frames.

**Collection Scheme** – A protobuf message pushed to the FWE agent that specifies which signals to collect and at what interval. Collection schemes are generated from campaign definitions in DynamoDB.

**Remote Command** – A message sent from the cloud to a vehicle through IoT Core MQTT to trigger an action such as locking doors, activating lights, or starting the engine. Commands follow a request/response pattern with status tracking (SENT, IN\_PROGRESS, SUCCEEDED, FAILED, TIMEOUT) and latency measurement.

**Command Catalog** – The set of available commands derived from actuatable signals in the signal catalog. Each actuatable signal defines a command name, value type, valid range, and expected response timeout.

**Geofence** – A virtual geographic boundary defined by a center point (latitude, longitude) and radius. The GeofenceProcessor evaluates vehicle positions against active geofences in real-time and generates safety events when vehicles cross boundaries.

**Signal Catalog** – A standardized definition of all telemetry signals used throughout the guidance. The catalog maps between CAN bus signal names (DBC), JSON field names, and COVESA Vehicle Signal Specification (VSS) paths. The catalog includes 271 signals organized into 15 CAN messages.

**Transform Manifest** – A configuration file that defines how to convert external data formats (OEM APIs, third-party telematics) into the signal catalog format. Manifests support field mapping, unit conversion, conditional mapping, and validation rules.

**AgentCore Runtime** – An Amazon Bedrock managed runtime environment that hosts the connected vehicle supervisor agent. The AgentCore text runtime receives HTTP requests from the Fleet Manager application and returns text responses. The runtime invokes the Bedrock supervisor agent, which can call specialist agents and retrieve grounded answers from an automotive knowledge base. The runtime is deployed separately from the core CMS stacks and is an opt-in component.

**Data Source** – A classification that describes how a vehicle’s telemetry originates. The guidance uses two data-source types: `vehicle-telemetry` for vehicles that publish directly via MQTT or FleetWise Edge Agent, and `cloud-telemetry` for vehicles whose data arrives through a cloud-to-cloud OEM connector. The data-source type drives routing decisions in the Fleet Manager application and enrollment workflows.

**platform-admin** – An Amazon Cognito user-pool group that grants cross-fleet administrative access. Users in the `platform-admin` group can enroll or unenroll vehicles in any fleet, access bulk lifecycle operations, and manage all fleets within the deployment. Intended for platform administrators, not for individual fleet operators.

**fleet-operator** – An Amazon Cognito user-pool group that grants per-fleet access scoped by the `custom:fleetIds` claim attached to the user’s token. Users in the `fleet-operator` group can manage vehicles, trips, alerts, and drivers within the fleets they are assigned to, but cannot access other fleets or perform cross-fleet bulk operations.

**fleet-viewer** – An Amazon Cognito user-pool group that grants read-only access to fleet data. Users in the `fleet-viewer` group can view vehicle state, trips, alerts, and analytics but cannot modify fleet configuration or enrollment.
