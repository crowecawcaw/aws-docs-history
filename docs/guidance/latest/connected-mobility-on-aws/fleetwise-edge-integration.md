

# FleetWise Edge integration
<a name="fleetwise-edge-integration"></a>

The solution supports two telemetry ingestion modes. In **MQTT Direct** mode, the simulator (or a real vehicle application) publishes JSON telemetry directly to IoT Core. In **FleetWise Edge (FWE)** mode, the AWS IoT FleetWise Edge Agent runs on the vehicle (or in a Docker container for simulation), collects raw CAN bus signals based on campaign instructions, encodes them as protobuf, and uploads them to the cloud. Both modes converge on the same `cms-telemetry-preprocessed` Kafka topic, so all downstream processors work identically regardless of the telemetry source.

**Important**  
AWS IoT FleetWise is no longer open to new customers. The [Reference Implementation for AWS IoT FleetWise](https://github.com/aws/aws-iot-fleetwise-edge) (FWE) remains available for developing your own Edge Agent. The Connected Mobility on AWS guidance supports both paths: new customers can develop and deploy their own Edge Agent based on FWE and use MQTT Direct mode without depending on AWS IoT FleetWise APIs, while existing AWS IoT FleetWise customers can continue using the service for full cloud integration — the solution’s Flink applications support FleetWise campaign management and telemetry processing as described on this page. Regardless of which path you choose, the core telemetry pipeline — normalization, routing, storage, and real-time distribution — operates independently of the FleetWise cloud service.

## Agent lifecycle
<a name="fwe-agent-lifecycle"></a>

The FWE agent follows a checkin-based lifecycle:

1.  **Startup** — The agent starts, loads its static configuration (IoT endpoint, certificate, CAN bus interface), and connects to IoT Core using X.509 certificate authentication.

1.  **Checkin** — The agent publishes a protobuf checkin message to `cms/fleetwise/vehicles/{vin}/checkins`. The checkin includes the agent’s current `document_sync_ids` — a list of collection scheme IDs the agent has already received and is actively running.

1.  **IoT Rule routing** — The IoT Rule `fw_{stage}_checkin_rule` encodes the binary protobuf as base64 and routes it to the `fw-checkin` Kafka topic, including the vehicle VIN extracted from the MQTT topic path using `topic(4)`.

1.  **Campaign resolution** — The CampaignSyncProcessor Flink application consumes the checkin, extracts the VIN, and queries the `cms-{stage}-campaigns` DynamoDB table for all campaigns with status `RUNNING` that target this vehicle.

1.  **Scheme generation** — For each active campaign, the processor generates a protobuf `CollectionScheme` message specifying which CAN signal IDs to collect and at what interval. It also generates a `DecoderManifest` protobuf that maps CAN signal IDs to human-readable VSS signal names (for example, signal ID 1 → `Vehicle.Speed`).

1.  **Scheme delivery** — The processor publishes the combined decoder manifest and collection schemes to `cms/fleetwise/vehicles/{vin}/collection_schemes_and_decoder_manifests` via IoT Core MQTT.

1.  **Signal collection** — The agent receives the schemes, configures its CAN bus listeners, and begins collecting the specified signals at the configured intervals.

1.  **Telemetry upload** — The agent batches collected signals into a `VehicleData` protobuf message and publishes it to `cms/fleetwise/vehicles/{vin}/signals`.

1.  **Decode and mapping** — The IoT Rule `fw_{stage}_iot_msk_rule` routes the protobuf to the `fw-telemetry-raw` Kafka topic. The FWTelemetryProcessor Flink application decodes the protobuf, maps each CAN signal ID to its standard JSON field name using the decoder manifest cached from DynamoDB, and outputs standard CMS-format JSON to `cms-telemetry-preprocessed`.

1.  **Standard pipeline** — From this point, the telemetry flows through the same processors as MQTT Direct data: EventDrivenTelemetryProcessor (Redis LKS), TripProcessor, SafetyProcessor, MaintenanceProcessor, and GeofenceProcessor.

## Campaign states
<a name="fwe-campaign-states"></a>

Campaigns stored in DynamoDB have the following lifecycle:
+  **RUNNING** — Active campaign. The CampaignSyncProcessor includes this campaign’s collection scheme when responding to agent checkins.
+  **SUSPENDED** — Paused campaign. When all campaigns for a vehicle are suspended, the processor pushes an empty `CollectionSchemes` protobuf, which clears the agent’s active collection and stops signal upload.
+  **COMPLETED** — Finished campaign. Ignored by the processor.

Campaign sync status is tracked per vehicle:
+  **PENDING** — Campaign scheme has been pushed to the agent but the agent has not confirmed receipt in its checkin `document_sync_ids`.
+  **HEALTHY** — Agent confirmed receipt of the collection scheme.

## Protobuf decode process
<a name="fwe-protobuf-decode"></a>

The FWTelemetryProcessor performs the following steps for each message on the `fw-telemetry-raw` topic:

1. Extract the base64-encoded protobuf payload and the vehicle VIN from the IoT Rule metadata.

1. Base64-decode and parse the `VehicleData` protobuf message.

1. Iterate over each `CapturedSignal` in the protobuf. Each signal has a numeric signal ID and a value.

1. Look up the signal ID in the decoder manifest (cached from DynamoDB) to get the VSS signal name (for example, `Vehicle.Speed`).

1. Map the VSS signal name to the standard JSON field name using the signal catalog (for example, `Vehicle.Speed` → `speed`). The mapping is cached in a `ConcurrentHashMap` and falls back to a built-in defaults map for core signals.

1. Resolve the vehicle’s active trip ID from a local cache (refreshed every 60 seconds from Redis) so the telemetry record can be tagged with the correct `tripId`.

1. Build a standard standard JSON object with all mapped fields, the VIN, timestamp, trip ID, and `source: "fleetwise"`.

1. Output the JSON string to the `cms-telemetry-preprocessed` Kafka topic.

Failed decodes are dropped (not passed through as poison messages) and counted in a `RECORDS_FAILED` metric.