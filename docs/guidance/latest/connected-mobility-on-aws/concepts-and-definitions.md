# Concepts and definitions

**Telemetry Data** - Real-time data streams from vehicle sensors including GPS coordinates, speed, engine diagnostics, fuel consumption, and battery status transmitted via MQTT protocol.

**Fleet Simulator** - Integrated simulation engine that generates realistic vehicle telemetry data for testing, development, and demonstration without requiring physical vehicles.

**Phase-based Deployment** - Incremental deployment strategy allowing organizations to start with basic fleet management and progressively add real-time telemetry capabilities as their connected vehicle program matures.

**SCRAM Authentication** - SASL/SCRAM authentication mechanism used for secure communication between AWS IoT Core and Amazon MSK clusters with credentials managed in AWS Secrets Manager.

**Stream Processing** - Real-time data processing using Apache Flink applications on Amazon Kinesis Data Analytics to decode, transform, and route vehicle telemetry to appropriate data stores.

**Trip Aggregation** - Process of combining individual telemetry messages into complete trip records with route information, statistics, and events.

**Safety Events** - Detected driving behaviors such as harsh braking, rapid acceleration, or sharp cornering that may indicate safety concerns.

**Fleet Management Dashboard** - Web-based user interface built with React and CloudScape Design System for managing vehicles, viewing real-time data, and monitoring fleet operations.

**Vehicle Provisioning** - Process of registering vehicles in AWS IoT Core using X.509 certificates for secure authentication and communication.

**Message Queuing Telemetry Transport (MQTT)** - Lightweight publish-subscribe messaging protocol used by AWS IoT Core for vehicle-to-cloud communication.
