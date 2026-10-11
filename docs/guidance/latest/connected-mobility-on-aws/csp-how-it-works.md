

# How it works
<a name="csp-how-it-works"></a>

The portal’s data model and campaign screens control what each vehicle collects. The subsections below describe the edge agent integration and the three-layer collection model those screens edit.

## FleetWise Edge integration
<a name="fleetwise-edge-integration"></a>

How the AWS IoT FleetWise Edge Agent connects, receives campaigns, collects CAN bus signals, and feeds telemetry into the processing pipeline.

The solution supports two telemetry ingestion modes. In **MQTT Direct** mode, the simulator (or a real vehicle application) publishes JSON telemetry directly to IoT Core. In **FleetWise Edge (FWE)** mode, the AWS IoT FleetWise Edge Agent runs on the vehicle (or in a Docker container for simulation), collects raw CAN bus signals based on campaign instructions, encodes them as protobuf, and uploads them to the cloud. Both modes converge on the same `cms-telemetry-preprocessed` Kafka topic, so all downstream processors work identically regardless of the telemetry source.

**Important**  
AWS IoT FleetWise is no longer open to new customers. The [Reference Implementation for AWS IoT FleetWise](https://github.com/aws/aws-iot-fleetwise-edge) (FWE) remains available for developing your own Edge Agent. The Connected Mobility on AWS guidance supports both paths: new customers can develop and deploy their own Edge Agent based on FWE and use MQTT Direct mode without depending on AWS IoT FleetWise APIs, while existing AWS IoT FleetWise customers can continue using the service for full cloud integration — the solution’s Flink applications support FleetWise campaign management and telemetry processing as described on this page. Regardless of which path you choose, the core telemetry pipeline — normalization, routing, storage, and real-time distribution — operates independently of the FleetWise cloud service.

### Agent lifecycle
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

### Campaign states
<a name="fwe-campaign-states"></a>

Campaigns stored in DynamoDB have the following lifecycle:
+  **RUNNING** — Active campaign. The CampaignSyncProcessor includes this campaign’s collection scheme when responding to agent checkins.
+  **SUSPENDED** — Paused campaign. When all campaigns for a vehicle are suspended, the processor pushes an empty `CollectionSchemes` protobuf, which clears the agent’s active collection and stops signal upload.
+  **COMPLETED** — Finished campaign. Ignored by the processor.

Campaign sync status is tracked per vehicle:
+  **PENDING** — Campaign scheme has been pushed to the agent but the agent has not confirmed receipt in its checkin `document_sync_ids`.
+  **HEALTHY** — Agent confirmed receipt of the collection scheme.

### Protobuf decode process
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

## Dynamic data collection
<a name="dynamic-data-collection"></a>

How the signal catalog, decoder manifest, and campaigns work together to control what data is collected from vehicles.

The solution uses a three-layer data collection model that decouples *what signals exist* from *how they are encoded on the wire* from *which signals to collect right now*. This separation allows fleet operators to change collection behavior without modifying vehicle software or redeploying infrastructure.

### Signal catalog
<a name="signal-catalog-overview"></a>

The signal catalog is the single source of truth for every telemetry signal the platform understands. It is stored in the `cms-{stage}-signal-catalog` DynamoDB table and seeded during deployment with a comprehensive catalog of 260 CAN bus signals across 55 CAN messages, plus 2 GPS signals and 6 metadata fields. The catalog covers a realistic 2026 model-year vehicle with ICE, EV, and hybrid support. It includes 48 actuatable commands for remote vehicle control. The default catalog is a starting point — it is fully customizable to any vehicle platform, OEM signal set, or industry standard.

#### Customizing the signal catalog
<a name="customizing-the-signal-catalog"></a>

The signal catalog is not hardcoded. Customers replace or extend it to match their vehicle fleet:
+  **OEM-specific signals** — Add proprietary signals from your vehicle platform (for example, Toyota-specific hybrid signals, Tesla battery cell voltages, or commercial vehicle J1939 signals).
+  **Subset deployments** — Remove signals your fleet does not produce to reduce processing overhead.
+  **Different units** — Change from imperial (mph, °F, PSI) to metric (km/h, °C, kPa) by updating the unit and conversion factor.
+  **New signal groups** — Add entirely new groups (for example, autonomous driving signals, trailer telemetry, cargo monitoring).

When the signal catalog is updated, the SignalCatalogLoader detects the version change in Redis and hot-reloads across all Flink processors without restart. Downstream consumers (Fleet Intelligence portal, Commands Lambda, FWTelemetryProcessor) automatically pick up the new signals.

#### Signal entry structure
<a name="signal-entry-structure"></a>

Each signal in the catalog contains:


| Field | Description | 
| --- | --- | 
| json\_field | The key used in standard telemetry JSON (for example, `speed`) | 
| signal\_name | Human-readable name (for example, "Vehicle Speed") | 
| vss\_path | COVESA Vehicle Signal Specification fully qualified path (for example, `Vehicle.Speed`) | 
| signal\_group | Logical grouping: engine, transmission, body, tire, safety, battery, climate, maintenance | 
| data\_type | float, int, boolean, or string | 
| unit | Physical unit (mph, PSI, °F, rpm, etc.) | 
| min / max | Valid range for the signal | 
| actuator | If present, this signal can be commanded remotely (see [Remote commands](fip-how-it-works.md#remote-commands-flow)) | 

#### Default signal catalog
<a name="default-signal-catalog"></a>

The solution ships with a comprehensive fleet telemetry catalog covering ICE, EV, and hybrid vehicles. The 260 signals are organized into two tiers:
+  **Original signals (IDs 1–75)** — 15 CAN messages (0x100–0x190) covering core engine, transmission, body, tire, safety, battery, instrument, climate, maintenance, and lighting signals.
+  **Expanded signals (IDs 101–287)** — 40 CAN messages (0x1A0–0x1C7) covering ADAS, cabin climate, connectivity, doors, environment, EV charging, geofence/fleet management, lighting, maintenance, mirrors, powertrain, safety, security, TPMS, vehicle control, windows, and wipers.

All IDs are unique and aligned across the signal catalog, decoder manifest, protobuf encoding, and campaign definitions.

 **Original core signals (15 messages, 75 signals):** 


| Message | CAN ID | Signals | Coverage | 
| --- | --- | --- | --- | 
| ECM\_Engine\_1 | 0x100 | 4 | Speed, RPM, engine temp, ignition | 
| ECM\_Engine\_2 | 0x101 | 6 | Oil pressure, throttle, coolant, intake air, engine hours | 
| ECM\_Engine\_3 | 0x102 | 4 | Acceleration, deceleration, odometer, fuel rate | 
| TCM\_Transmission | 0x110 | 4 | Transmission temp, gear, cruise, parking brake | 
| BCM\_Body\_1 | 0x120 | 12 | Seatbelt, phone, windows, trunk, lights, connectivity | 
| TPMS\_Pressure | 0x130 | 5 | Tire pressure (4 wheels) \+ max tire temp | 
| TPMS\_Tread | 0x131 | 4 | Tire tread depth (4 wheels) | 
| ADAS\_Safety\_1 | 0x140 | 10 | Braking, acceleration, turn, AEB, ABS, ESC, airbag | 
| ADAS\_Safety\_2 | 0x141 | 4 | Phone usage, seatbelt, lateral G, following distance | 
| BMS\_Battery | 0x150 | 3 | 12V battery, alternator, fuel level | 
| BMS\_EV | 0x151 | 4 | EV: SOC, HV voltage, regen power | 
| ICM\_Instrument | 0x160 | 2 | Heading, DTC active | 
| HVAC\_Climate | 0x170 | 4 | HVAC, target temp, cabin temp, seat heat | 
| MAINT\_Indicators | 0x180 | 6 | Oil life, brake wear, filter life, idle hours, brake pressure | 
| LIGHT\_Systems | 0x190 | 3 | Headlights, hazard, turn signal | 

 **Expanded signals (40 messages, 185 signals):** 


| Message Group | CAN IDs | Signals | Coverage | 
| --- | --- | --- | --- | 
| ADAS / ADAS\_1 / ADAS\_2 | 0x1A0–0x1A2 | 18 | Cruise control, adaptive cruise, lane keep, blind spot, AEB, forward collision, parking assist, traffic sign recognition, driver monitoring, auto park | 
| CABIN\_CLIMATE / \_1 / \_2 | 0x1A3–0x1A5 | 13 | HVAC mode, dual-zone temp, fan speed, recirculation, defrost, seat heat/vent (driver \+ passenger), steering wheel heat, remote preconditioning | 
| CONNECTIVITY / \_1 | 0x1A6–0x1A7 | 8 | Cellular signal/network, WiFi, Bluetooth, OTA updates, software version | 
| CORE\_TELEMETRY / \_1 / \_2 | 0x1A8–0x1AA | 10 | Extended core vehicle telemetry | 
| DOORS | 0x1AB | 18 | Per-door open/locked/child-lock (4 doors), all-doors lock, trunk, hood, fuel door, charge door | 
| ENVIRONMENT / \_1 | 0x1AC–0x1AD | 5 | Ambient temp, humidity, barometric pressure, rain intensity, light level | 
| EV\_CHARGING / \_1–\_4 | 0x1AE–0x1B2 | 19 | SOC, SOH, HV voltage/current, battery temp, range, charge rate/type/limit, time-to-full, scheduled charging, regen level, motor torque/RPM/temp, energy consumed | 
| EV\_SPECIFIC / \_1 | 0x1B3–0x1B4 | 5 | Extended EV-specific signals | 
| GEOFENCE / \_1 | 0x1B5–0x1B6 | 14 | Geofence active/center/radius/violation, speed limit, curfew, valet mode, immobilizer | 
| LIGHTING | 0x1B7 | 6 | Headlight mode, high beam, fog lights (front/rear), hazard, interior lights, ambient color | 
| MAINTENANCE / \_1 | 0x1B8–0x1B9 | 8 | Extended maintenance indicators | 
| MIRRORS | 0x1BA | 5 | Per-mirror fold/heat (left/right), fold-all | 
| POWERTRAIN / \_1 / \_2 | 0x1BB–0x1BD | 10 | Transmission gear/mode/temp, turbo boost, throttle, intake/exhaust/catalyst temp, fuel pressure/type, remote start | 
| SAFETY / \_1 | 0x1BE–0x1BF | 10 | Extended safety signals | 
| SECURITY | 0x1C0 | 3 | Horn, alarm armed/triggered, panic mode, find-my-vehicle | 
| TPMS / \_1 | 0x1C1–0x1C2 | 8 | Per-wheel pressure \+ temperature (expanded) | 
| VEHICLE\_CONTROL / \_1 | 0x1C3–0x1C4 | 15 | Vehicle control signals | 
| WINDOWS / \_1 | 0x1C5–0x1C6 | 6 | Per-window position (4 windows), sunroof position/shade | 
| WIPERS | 0x1C7 | 4 | Front wiper mode/active, washer fluid level, rear wiper | 

 **Actuatable commands (48 commands across 6 categories):** 


| Category | Count | Examples | 
| --- | --- | --- | 
| Comfort | 21 | HVAC mode/temp/fan, seat heat/vent, steering wheel heat, window positions, sunroof, mirror fold/heat, remote preconditioning | 
| Security | 11 | Per-door locks, all-doors lock, trunk lock, alarm arm/disarm, horn, panic mode, find-my-vehicle, immobilizer | 
| Fleet | 9 | Geofence enable/center/radius, speed limit, curfew enable/start/end, valet mode | 
| Lighting | 5 | Headlights, fog lights (front/rear), hazard flash, interior lights | 
| Charging | 4 | Charge limit, charge schedule, start/stop charging, charge door | 
| Engine | 1 | Remote start/stop | 

#### VSS path convention
<a name="vss-path-convention"></a>

The signal catalog follows the [COVESA Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/) naming convention. VSS provides a standardized, tree-structured taxonomy for vehicle signals used across the automotive industry. The fully qualified path uses dot notation from the vehicle root:

```
Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure
│       │       │    │    │     │    │    └── Signal name
│       │       │    │    │     │    └── Component
│       │       │    │    │     └── Position
│       │       │    │    └── Assembly
│       │       │    └── Location
│       │       └── System
│       └── Domain
└── Root
```

This hierarchical naming enables:
+ Consistent signal identification across OEMs and platforms
+ Automatic grouping in the Fleet Intelligence portal
+ Compatibility with FleetWise signal catalogs and decoder manifests
+ Industry-standard data exchange with partners and third-party systems

### DBC file format
<a name="dbc-format-overview"></a>

The solution includes a DBC file (`services/simulation/can/cms-fleet.dbc`) that defines the CAN bus message layout. DBC (Database CAN) is the industry-standard format for describing CAN bus communication, used by every major automotive OEM and tool vendor.

#### How a DBC file works
<a name="how-a-dbc-file-works"></a>

A DBC file defines **messages** (CAN frames) and **signals** (data fields within frames):

```
BO_ 256 ECM_Engine_1: 8 Vector__XXX
 SG_ VehicleSpeed : 0|16@1+ (0.1,0) [0|655] "mph" Vector__XXX
 SG_ EngineRPM : 16|16@1+ (1,0) [0|8000] "rpm" Vector__XXX
 SG_ EngineTemp : 32|16@1+ (0.1,-40) [0|370] "degF" Vector__XXX
 SG_ IgnitionOn : 48|1@1+ (1,0) [0|1] "" Vector__XXX
```

Reading this:
+  `BO_ 256 ECM_Engine_1: 8` — CAN message with ID 256 (0x100), named ECM\_Engine\_1, 8 bytes long
+  `SG_ VehicleSpeed : 0|16@1+` — Signal starting at bit 0, 16 bits wide, little-endian, unsigned
+  `(0.1,0)` — Factor 0.1, offset 0. Physical value = raw × 0.1 \+ 0
+  `[0|655]` — Valid range 0 to 655 mph
+  `"mph"` — Unit

#### CAN message layout
<a name="can-message-layout"></a>

The default DBC defines 55 CAN messages with different cycle times based on how frequently the data changes:

 **Original messages (0x100–0x190):** 


| Message | CAN ID | Cycle | Signals | Purpose | 
| --- | --- | --- | --- | --- | 
| ECM\_Engine\_1 | 0x100 | 100ms | 4 | Speed, RPM, engine temp, ignition | 
| ECM\_Engine\_2 | 0x101 | 500ms | 6 | Oil pressure, throttle, coolant, intake air | 
| ECM\_Engine\_3 | 0x102 | 100ms | 4 | Acceleration, deceleration, odometer, fuel rate | 
| TCM\_Transmission | 0x110 | 200ms | 4 | Transmission temp, gear, cruise, parking brake | 
| BCM\_Body\_1 | 0x120 | 500ms | 12 | Seatbelt, phone, windows, trunk, lights, connectivity | 
| TPMS\_Pressure | 0x130 | 1000ms | 5 | Tire pressure (4 wheels) \+ max tire temp | 
| TPMS\_Tread | 0x131 | 5000ms | 4 | Tire tread depth (4 wheels) | 
| ADAS\_Safety\_1 | 0x140 | 100ms | 10 | Braking, acceleration, turn, AEB, ABS, ESC | 
| ADAS\_Safety\_2 | 0x141 | 100ms | 4 | Phone usage, seatbelt, lateral G, following distance | 
| BMS\_Battery | 0x150 | 1000ms | 3 | 12V battery, alternator, fuel level | 
| BMS\_EV | 0x151 | 1000ms | 4 | EV: SOC, HV voltage, regen power | 
| ICM\_Instrument | 0x160 | 200ms | 2 | Heading, DTC active | 
| HVAC\_Climate | 0x170 | 2000ms | 4 | HVAC, target temp, cabin temp, seat heat | 
| MAINT\_Indicators | 0x180 | 5000ms | 6 | Oil life, brake wear, filter life, idle hours | 
| LIGHT\_Systems | 0x190 | 500ms | 3 | Headlights, hazard, turn signal | 

 **Expanded messages (0x1A0–0x1C7):** 


| Message Group | CAN IDs | Signals | Purpose | 
| --- | --- | --- | --- | 
| ADAS (3 messages) | 0x1A0–0x1A2 | 18 | Cruise control, adaptive cruise, lane keep, blind spot, AEB, collision warning, parking assist, traffic sign recognition, driver monitoring | 
| CABIN\_CLIMATE (3 messages) | 0x1A3–0x1A5 | 13 | Dual-zone HVAC, fan speed, defrost, seat heat/vent, steering wheel heat, remote preconditioning | 
| CONNECTIVITY (2 messages) | 0x1A6–0x1A7 | 8 | Cellular signal, WiFi, Bluetooth, OTA updates, software version | 
| CORE\_TELEMETRY (3 messages) | 0x1A8–0x1AA | 10 | Extended core telemetry | 
| DOORS (1 message) | 0x1AB | 18 | Per-door open/locked/child-lock, trunk, hood, fuel door, charge door | 
| ENVIRONMENT (2 messages) | 0x1AC–0x1AD | 5 | Ambient temp, humidity, barometric pressure, rain, light level | 
| EV\_CHARGING (5 messages) | 0x1AE–0x1B2 | 19 | Battery SOC/SOH/voltage/current/temp, range, charge rate/type/limit, motor torque/RPM/temp | 
| EV\_SPECIFIC (2 messages) | 0x1B3–0x1B4 | 5 | Extended EV signals | 
| GEOFENCE (2 messages) | 0x1B5–0x1B6 | 14 | Geofence, speed limit, curfew, valet mode, immobilizer | 
| LIGHTING (1 message) | 0x1B7 | 6 | Headlights, high beam, fog lights, interior, ambient | 
| MAINTENANCE (2 messages) | 0x1B8–0x1B9 | 8 | Extended maintenance indicators | 
| MIRRORS (1 message) | 0x1BA | 5 | Per-mirror fold/heat, fold-all | 
| POWERTRAIN (3 messages) | 0x1BB–0x1BD | 10 | Transmission, turbo, throttle, exhaust/catalyst temp, fuel pressure, remote start | 
| SAFETY (2 messages) | 0x1BE–0x1BF | 10 | Extended safety signals | 
| SECURITY (1 message) | 0x1C0 | 3 | Horn, alarm, panic mode | 
| TPMS (2 messages) | 0x1C1–0x1C2 | 8 | Per-wheel pressure \+ temperature (expanded) | 
| VEHICLE\_CONTROL (2 messages) | 0x1C3–0x1C4 | 15 | Vehicle control signals | 
| WINDOWS (2 messages) | 0x1C5–0x1C6 | 6 | Per-window position, sunroof | 
| WIPERS (1 message) | 0x1C7 | 4 | Front/rear wipers, washer fluid level | 

Safety-critical signals (speed, braking, acceleration) use 100ms cycle times for rapid detection. Slow-changing signals (tire tread, maintenance indicators) use 5000ms cycles to reduce bus load.

#### Customizing the DBC
<a name="customizing-the-dbc"></a>

To adapt the guidance for a different vehicle platform:

1. Create or obtain the DBC file for your vehicle’s CAN bus.

1. Update the signal catalog DynamoDB table to match the new signals.

1. Update the decoder manifest to map the new CAN signal IDs to VSS paths.

1. Create campaigns that reference the new signal IDs.

The Flink processors, Fleet Intelligence portal, and Redis LKS layer automatically adapt to the new signals through the signal catalog — no code changes required.

### Decoder manifest
<a name="decoder-manifest-overview"></a>

The decoder manifest bridges the gap between raw CAN bus data and human-readable signal names. It tells the FleetWise Edge Agent how to interpret the binary CAN frames coming off the vehicle bus. The default decoder manifest covers all 260 CAN signals plus 2 GPS custom decoding signals.

Each entry in the decoder manifest maps:
+  **CAN message ID** — The CAN frame identifier (for example, `0x100` for ECM\_Engine\_1)
+  **Signal bit position and length** — Where the signal sits within the 8-byte CAN frame
+  **Factor and offset** — Scaling values to convert raw integer values to physical units (for example, raw value 655 × factor 0.1 = 65.5 mph)
+  **Signal ID** — A numeric identifier used in the protobuf encoding
+  **VSS signal name** — The human-readable name (for example, `Vehicle.Speed`)

The decoder manifest is defined in a DBC file (`services/simulation/can/cms-fleet.dbc`) that follows the standard automotive DBC format. The CampaignSyncProcessor reads the manifest from DynamoDB and serializes it as a protobuf `DecoderManifest` message for delivery to the FWE agent.

 **Example — how a single signal flows through the decoder manifest:** 

```
CAN bus frame 0x100, bytes [0x02, 0x8F, ...]
  → DBC: signal "VehicleSpeed" at bit 0, length 16, factor 0.1, offset 0
  → Raw value: 0x028F = 655
  → Physical value: 655 × 0.1 = 65.5
  → VSS name: Vehicle.Speed
  → standard JSON field: "speed": 65.5
```

The decoder manifest covers 15 CAN messages with cycle times ranging from 100ms (engine, safety) to 5000ms (tire tread, maintenance indicators). See [Signal catalog reference](csp-architecture-details.md#signal-catalog-reference) for the complete mapping.

### Campaigns
<a name="campaigns-overview"></a>

A campaign defines *what to collect* and *from which vehicles*. Campaigns are the control plane for FleetWise Edge data collection — they determine which signals the agent actively monitors and uploads.

Each campaign record in the `cms-{stage}-campaigns` DynamoDB table contains:
+  **Campaign ID** — Unique identifier
+  **Campaign name** — Human-readable name (for example, "Full Fleet Telemetry")
+  **Status** — `RUNNING`, `SUSPENDED`, or `COMPLETED` 
+  **Target vehicles** — List of VINs or a target ARN pattern
+  **Source fleet ID** — If assigned via fleet-level campaign, the `sourceFleetId` links to the parent fleet campaign. Fleet-assigned campaigns are locked at the vehicle level.
+  **Signals to collect** — List of signal IDs from the decoder manifest (for example, all 66 signals, or a subset like only tire and engine signals)
+  **Collection interval** — How frequently the agent samples signals (for example, every 1000ms)
+  **Condition** — Optional trigger condition (for example, collect only when speed > 0)

#### Campaign lifecycle
<a name="campaign-lifecycle-detail"></a>

1.  **Create** — A campaign is created in DynamoDB with status `RUNNING` and a list of target vehicles and signals.

1.  **Push** — On the next agent checkin, the CampaignSyncProcessor detects the new campaign, generates a `CollectionScheme` protobuf, and publishes it to the agent via IoT Core MQTT.

1.  **Collect** — The agent configures its CAN bus listeners based on the collection scheme and begins sampling the specified signals.

1.  **Upload** — The agent batches collected signals into `VehicleData` protobuf messages and uploads them to IoT Core.

1.  **Suspend** — Setting the campaign status to `SUSPENDED` causes the processor to push an empty collection scheme on the next checkin, which stops the agent from collecting those signals.

1.  **Resume** — Setting the status back to `RUNNING` re-enables collection on the next checkin.

1.  **Complete** — Setting the status to `COMPLETED` permanently ends the campaign.

#### Example campaigns
<a name="campaign-examples"></a>

 **Full fleet telemetry** — Collect all 66 signals from every vehicle at 1-second intervals. This is the default campaign created by the simulation service.

 **Tire health monitoring** — Collect only tire pressure (4 signals) and tire tread (4 signals) from vehicles in a specific fleet at 5-second intervals. Useful for reducing data volume while monitoring a specific concern.

 **Safety investigation** — Collect all ADAS safety signals (10 signals) from a single vehicle at 100ms intervals after a safety incident is reported. High-frequency collection for detailed analysis.

 **EV battery diagnostics** — Collect state of charge, HV battery voltage, regenerative braking power, and motor temperature from EV vehicles only. Uses a condition to collect only when the vehicle is driving (speed > 0).

### How the layers connect
<a name="how-layers-connect"></a>

```
Signal Catalog (what signals exist)
    ↓ defines
Decoder Manifest (how to read signals from CAN bus)
    ↓ referenced by
Campaign (which signals to collect, from which vehicles)
    ↓ pushed as protobuf to
FWE Agent (collects and uploads)
    ↓ decoded by
FWTelemetryProcessor (protobuf → standard JSON)
    ↓ flows into
Standard processing pipeline (trips, safety, maintenance)
```

This layered design means:
+ Adding a new signal requires only a signal catalog update and a decoder manifest entry — no code changes.
+ Changing what a vehicle collects requires only a campaign update — no vehicle software update.
+ Multiple campaigns can target the same vehicle simultaneously — the agent merges the collection schemes.
+ The same downstream processors work regardless of whether data came from MQTT Direct or FleetWise Edge.