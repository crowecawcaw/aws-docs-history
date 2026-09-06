

# Accelerate development and deployment of connected vehicle assets
<a name="solution-overview"></a>

Publication date: *October 2023 ([last update](revisions.md): April 2026)* 

Amazon Web Services (AWS) automotive customers have asked for ways to manage fleets with increased efficiency and reduced vehicle downtime through preventative maintenance, location tracking, improved fleet safety and security, and new software driven vehicle experiences.

The Guidance for Connected Mobility on AWS addresses these needs by providing a modern, scalable telemetry architecture designed to handle high-volume, real-time data streams from connected vehicle fleets. The guidance accelerates development by providing tested, production-ready components that follow AWS Well-Architected principles.

## Multi-source telemetry architecture
<a name="multi-source-telemetry"></a>

A core design principle of this guidance is source-agnostic telemetry processing. The architecture normalizes data from multiple telemetry sources into a common signal catalog format before it enters the processing pipeline. This means the same downstream processors — trip detection, safety events, maintenance alerts, geofence evaluation — work identically regardless of how the data arrives. The guidance supports three telemetry ingestion modes today, and the architecture is extensible to additional sources:
+  **MQTT Direct** — Vehicles or simulators publish JSON telemetry directly to AWS IoT Core via MQTT. IoT rules route messages to Amazon MSK topics for stream processing. This mode is suitable for custom telematics devices, aftermarket hardware, or any system that can publish MQTT messages.
+  **AWS IoT FleetWise Edge Agent** — The [AWS IoT FleetWise Edge Agent](https://github.com/aws/aws-iot-fleetwise-edge) runs on the vehicle ECU (or in a Docker container for simulation) and collects raw CAN bus signals based on campaign-driven collection schemes pushed from the cloud. The agent encodes collected signals as protobuf and uploads them to IoT Core. The FWTelemetryProcessor Flink application decodes the protobuf, maps CAN signal IDs to human-readable names using the decoder manifest, and feeds the normalized data into the standard processing pipeline. This mode enables dynamic data collection — you control which signals are collected, at what frequency, and for which vehicles, all without deploying new software to the vehicle.
+  **Cloud-to-cloud OEM telemetry** — The OEMTelemetryProcessor enables integration with third-party OEM APIs and telematics providers without modifying the core processing pipeline. Customers define transform manifests that map OEM-specific data formats to the signal catalog. Manifests support field mapping, unit conversion (multiply, formula, lookup table), conditional mapping, and validation rules. This mode supports any cloud-based data source — OEM telematics APIs, third-party fleet management platforms, or enterprise data lakes.

## AWS IoT FleetWise integration
<a name="fleetwise-integration-overview"></a>

 [AWS IoT FleetWise](https://aws.amazon.com/iot-fleetwise/) provides a purpose-built service for collecting, transforming, and transferring vehicle data to the cloud. This guidance integrates the [FleetWise Edge Agent](https://github.com/aws/aws-iot-fleetwise-edge) as a first-class telemetry source, bringing several capabilities that differentiate it from traditional MQTT-based telemetry:
+  **Signal catalogs** — A centralized definition of all vehicle signals with standardized naming following the [COVESA Vehicle Signal Specification (VSS)](https://covesa.global/). The catalog maps between raw CAN bus signal names (from DBC files), JSON field names used in the processing pipeline, and VSS paths. The guidance includes a catalog with 271 signals across 15 CAN messages, and the catalog is extensible through the UI or API.
+  **Decoder manifests** — A mapping pushed to the edge agent that tells it how to interpret raw CAN frames. The decoder manifest maps CAN message IDs and signal bit positions to human-readable signal names. When you update the signal catalog, the CampaignSyncProcessor automatically generates and pushes updated decoder manifests to agents on their next checkin.
+  **Campaigns** — Collection campaigns control what data the edge agent collects and when. A campaign specifies target vehicles, which signals to collect, the collection interval, and trigger conditions. This enables dynamic data collection — you can start collecting high-frequency brake pressure data across your fleet for a safety investigation, then stop collection when the investigation is complete, all without touching the vehicle software.
+  **Protobuf encoding** — The edge agent encodes collected signals as Protocol Buffers, which are significantly more compact than JSON. This reduces cellular data costs and improves upload efficiency, particularly important for large fleets or bandwidth-constrained environments.

The same architecture pattern — normalize to signal catalog, then process — applies to any future data source. Adding a new telemetry source requires only a new preprocessor Flink application that maps the source format to the signal catalog.

## Feature summary
<a name="feature-summary"></a>

Provided features allow you to:
+ Ingest telemetry from multiple sources (MQTT Direct, FleetWise Edge Agent, cloud-to-cloud OEM APIs) through a unified processing pipeline
+ Dynamically control vehicle data collection through FleetWise campaigns, signal catalogs, and decoder manifests — without deploying software to vehicles
+ Communicate between vehicles and the AWS Cloud using AWS IoT Core and MQTT protocol
+ Send remote commands to vehicles (door locks, lights, climate, horn, engine start/stop) and track command execution status with latency measurement
+ Define and manage geofences with real-time boundary crossing detection
+ Process telemetry data in real-time using Amazon MSK and Apache Flink
+ Transform third-party OEM telemetry using configurable transform manifests with field mapping and unit conversion
+ Store and query vehicle data, trips, and alerts in Amazon DynamoDB
+ Track vehicles in real-time with Amazon Location Service and interactive maps
+ Manage fleets through a modern React-based web application built with Cloudscape Design System
+ Generate maintenance alerts and safety event notifications automatically
+ Simulate connected vehicle data using MQTT Direct or FleetWise Edge Agent mode, locally or in the cloud
+ Manage fleet-level campaigns that automatically fan out to all vehicles in a fleet, with vehicle-level campaign locking
+ Assign drivers to vehicles with automatic trip attribution for safety event tracking
+ Track warranty claims, eligible failures, and OEM recovery through the Warranty management page
+ Switch between light and dark mode themes with persistent preference
+ Deploy infrastructure using AWS CDK with a streamlined phase-based approach
+ Securely authenticate and authorize users through Amazon Cognito
+ Engage with a conversational in-UI fleet assistant powered by Amazon Bedrock AgentCore and an automotive data knowledge base — fleet-driver and service-advisor personas are inferred from Amazon Cognito user claims
+ Deploy a Bedrock multi-agent stack (supervisor agent and specialist agents) as an opt-in component that powers the in-UI assistant and enables extensible agent-based vehicle operations
+ Manage fleet bulk lifecycle operations — bulk enroll and unenroll vehicles, and synchronize enrollment status — with role-based access control that differentiates platform-administrator (cross-fleet) operations from fleet-operator (per-fleet) operations
+ Enable drivers to claim their own assigned vehicle through the Fleet Manager web application or companion iOS application

The guidance provides an integrated architecture that eliminates months of development time for core connected mobility infrastructure. Original equipment manufacturers (OEMs), tier one suppliers, and fleet operators can deploy the complete solution or customize components for their specific requirements.

Vehicle telemetry data, such as speed, engine temperature, tire pressure, and geolocation generated from car sensors provides near real-time data ingestion for analytics and machine learning (ML) use cases. The guidance makes this data available through RESTful APIs for integration with third-party systems including usage-based insurance, connected accident advisor, and package delivery services.

This implementation guide provides an overview of the guidance, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the guidance to the AWS Cloud.

The intended audience for using this solution’s features and capabilities in their environment includes solutions architects, business decision makers, DevOps engineers, data scientists, and cloud professionals.

Use this navigation table to quickly find answers to these questions:


| If you want to . . . | Read . . . | 
| --- | --- | 
| Know the cost for running this solution.<br />The estimated cost for running this solution in the us-east-1 Region is USD $400.00 per month for processing 1,000 vehicles with moderate usage. |  [Cost](plan-your-deployment.md#cost)  | 
| Understand the security considerations for this solution. |  [Security](security.md)  | 
| Know how to plan for quotas for this solution. |  [Quotas](plan-your-deployment.md#quotas)  | 
| Know which AWS Regions are supported for this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  | 
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the guidance. |  [GitHub repository](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws)  | 