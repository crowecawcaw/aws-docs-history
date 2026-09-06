

# Control plane
<a name="control-plane"></a>

The control plane manages what data is collected from vehicles, how vehicles are configured, and how fleet operators interact with the system. While the data plane handles the flow of telemetry, the control plane determines what telemetry to collect and provides the tools to act on it.

![Cloud-Native Control Plane for Dynamic Vehicle Data Collection](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/cloud-native-control-plane-dynamic-data-collection.png)


## Signal catalog
<a name="signal-catalog"></a>

The signal catalog is the single source of truth for every telemetry signal the platform understands. It is stored in the `cms-{stage}-signal-catalog` DynamoDB table and defines canonical field names, units, data types, and VSS paths for 260\+ CAN bus signals across 55 CAN messages, plus GPS signals and metadata fields.

Every component in the platform references the signal catalog:
+  **Flink preprocessors** — Map source-specific signal names to canonical `json_field` values
+  **Decoder manifests** — Map integer CAN signal IDs to VSS paths, which the signal catalog then maps to `json_field` names
+  **Transform manifests** — Map OEM-specific field names to `json_field` values
+  **Fleet Manager UI** — Displays signal names, units, and values from the catalog
+  **Commands Lambda** — Derives the actuatable command catalog from signals with an `actuator` attribute

The catalog is loaded into Redis by the `SignalCatalogLoader` (shared across all Flink processors) and hot-reloads when the catalog version changes — no Flink restart required.

## Campaign management (FleetWise Edge)
<a name="campaign-management-fleetwise-edge"></a>

Campaigns control what data the FWE agent collects from the vehicle CAN bus. A campaign specifies target vehicles, which signals to collect, the collection interval, and trigger conditions. This enables dynamic data collection — you can start collecting high-frequency brake pressure data across your fleet for a safety investigation, then stop collection when complete, all without touching vehicle software.

The campaign lifecycle:

1.  **Create campaign** — Platform admin creates a campaign in the Fleet Manager UI, selecting target vehicles (by VIN or fleet), signals from the signal catalog, collection frequency, and optional trigger conditions.

1.  **Store campaign** — The campaign is written to the `cms-{stage}-campaigns` DynamoDB table with status `RUNNING`.

1.  **Agent checkin** — The FWE agent periodically publishes a checkin message to `cms/fleetwise/vehicles/{vin}/checkins`. This message contains the agent’s current decoder manifest version and collection scheme version.

1.  **CampaignSyncProcessor** (Flink) — Reads checkin messages from the `fw-checkin` Kafka topic. For each checkin, it queries DynamoDB for active campaigns targeting that vehicle, resolves the decoder manifest and collection scheme, and publishes them to IoT Core topics that the FWE agent subscribes to:
   +  `cms/fleetwise/vehicles/{vin}/decoder_manifests` — The binary decoder manifest defining how to decode CAN frames
   +  `cms/fleetwise/vehicles/{vin}/collection_schemes` — The collection scheme specifying which signals to collect and when

1.  **Agent applies configuration** — The FWE agent receives the decoder manifest and collection scheme, persists them locally, and begins collecting the specified signals from the CAN bus at the configured frequency.

## Decoder manifests
<a name="decoder-manifests"></a>

A decoder manifest defines how to decode raw CAN bus frames into named signals. It maps integer signal IDs to CAN parameters (message ID, start bit, bit length, factor, offset, byte order) and VSS-path fully qualified names.

Decoder manifests are stored in the `cms-{stage}-decoder-manifest` DynamoDB table and can be created through:
+  **DBC file upload** — The Data Processing API parses standard DBC (CAN database) files and generates decoder manifest entries
+  **Fleet Manager UI** — The Decoder Manifest Wizard provides a visual interface for creating and editing manifests
+  **API** — Direct creation via the Data Processing REST API

## Remote commands
<a name="remote-commands"></a>

The remote commands system enables bidirectional communication with vehicles. Commands are sent directly through IoT Core MQTT — not through Kafka or Flink — because commands are low-volume, latency-sensitive, and request/response.

 **Command send flow:** 

1. Fleet Manager UI → API Gateway → Commands Lambda

1. Lambda validates the command against the signal catalog (only signals with `actuator` attribute)

1. Lambda publishes to two MQTT topics simultaneously:
   + FWE protobuf: `cms/commands/things/{vin}/executions/{commandId}/request/protobuf` — Binary `CommandRequest` protobuf with signal ID, typed value, and timeout
   + JSON: `cms/commands/{vehicleId}/request` — JSON payload for MQTT Direct simulators

1. Lambda stores the command in DynamoDB with status `SENT` 

 **Command response flow:** 

1. Vehicle executes the command and publishes a response

1. Two IoT Rules route responses to the Command Response Handler Lambda:
   +  `cms/commands/things/+/executions/+/response/protobuf` — FWE protobuf responses (base64-encoded by the IoT Rule SQL)
   +  `cms/commands/+/response` — JSON responses from simulators

1. The Response Handler decodes the response, updates the command status in DynamoDB (SUCCEEDED, FAILED, TIMEOUT), and calculates round-trip latency

The command catalog is dynamically derived from the signal catalog — 48 actuatable commands across categories including doors, lights, climate, windows, trunk, horn, and engine.

## Fleet Manager UI
<a name="fleet-manager-ui"></a>

The Fleet Manager is a React web application built with [Cloudscape Design System](https://cloudscape.design/), served via Amazon CloudFront and Amazon S3. It connects to two API Gateway endpoints:
+  **Fleet Management API** — CRUD operations for fleets, vehicles, drivers, trips, safety alerts, maintenance alerts, subscriptions, and user management. Backed by a Lambda function that reads live vehicle state from Redis and persistent data from DynamoDB.
+  **Commands API** — Remote vehicle commands and geofence management. Backed by a separate Lambda function with IoT Core publish permissions.

Authentication is handled by Amazon Cognito with three user groups (`platform-admin`, `fleet-operator`, `fleet-viewer`). The API Lambda extracts the user’s group and `custom:fleetIds` attribute from the JWT token and scopes every query to the user’s authorized fleets.

## Location services
<a name="location-services"></a>

Amazon Location Service provides three capabilities:
+  **Maps** — Interactive vehicle tracking maps in the Fleet Manager UI showing real-time vehicle positions from the Redis geo index
+  **Place index** — Geocoding and reverse geocoding for trip start/end locations
+  **Route calculator** — Route calculation for the vehicle simulator to generate realistic GPS trajectories following actual road networks