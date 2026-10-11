

# Architecture details
<a name="fip-architecture-details"></a>

The portal runs on the shared platform described in [Shared platform architecture](architecture-details.md). The resources below are specific to the portal.

## Web application
<a name="ui-stack"></a>

The portal’s web application and backend APIs.

The Fleet Intelligence portal provides the web interface and backend APIs.

### CloudFront distribution
<a name="cloudfront-distribution"></a>

Delivers the React application globally with low latency.

 **Configuration:** 
+ Origin: S3 bucket (UI assets)
+ Price class: Use all edge locations
+ TLS: Minimum TLS 1.2
+ Compression: Enabled (gzip, brotli)
+ Caching: Optimized for SPA

 **Cache behaviors:** 
+  `/`: Serve index.html (no cache)
+  `/static/*`: Cache for 1 year
+  `/api/*`: Forward to API Gateway (no cache)

### API Gateway
<a name="api-gateway"></a>

RESTful APIs for fleet management operations.

 **Endpoints:** 


| Method | Path | Description | 
| --- | --- | --- | 
| GET | /vehicles | List all vehicles | 
| GET | /vehicles/{vin} | Get vehicle details | 
| PUT | /vehicles/{vin} | Update vehicle | 
| GET | /vehicles/{vin}/trips | Get vehicle trips | 
| GET | /vehicles/{vin}/alerts | Get vehicle alerts | 
| POST | /alerts/{id}/acknowledge | Acknowledge alert | 
| GET | /drivers | List all drivers | 
| GET | /drivers/{id} | Get driver details | 
| GET | /location/geocode | Geocode address | 
| GET | /location/route | Calculate route | 
| POST | /api/commands/{vehicleId} | Send remote command to vehicle | 
| GET | /api/commands/{vehicleId} | Get command history for vehicle | 
| GET | /api/commands/catalog | List available actuatable commands | 
| POST | /api/geofences | Create a geofence | 
| GET | /api/geofences/{vehicleId} | List geofences for vehicle | 
| DELETE | /api/geofences/{geofenceId} | Deactivate a geofence | 

 **Authorization:** 
+ Cognito User Pool authorizer
+ JWT validation on all requests
+ IAM roles for service-to-service

### Lambda functions
<a name="lambda-functions"></a>

Backend logic for API operations.

 **Functions:** 
+  `vehicles-handler`: CRUD operations on vehicles
+  `trips-handler`: Query trip history
+  `alerts-handler`: Manage alerts
+  `drivers-handler`: Manage drivers
+  `location-handler`: Location Service integration
+  `cache-handler`: ElastiCache operations

 **Configuration:** 
+ Runtime: Python 3.11
+ Memory: 512 MB
+ Timeout: 30 seconds
+ VPC: Private subnets (for ElastiCache access)

### Cognito configuration
<a name="cognito-configuration"></a>

User authentication and authorization.

 **User pool:** 
+ Sign-up: Email verification required
+ MFA: Optional (TOTP)
+ Password policy: 8\+ characters, mixed case, numbers
+ Account recovery: Email

 **Identity pool:** 
+ Authenticated role: Access to API Gateway
+ Unauthenticated role: Denied

### Location Service
<a name="location-service"></a>

Mapping and geocoding capabilities.

 **Resources:** 
+ Map: Esri Street Map
+ Place index: Esri geocoding
+ Route calculator: Esri routing

 **Features:** 
+ Real-time vehicle tracking
+ Historical route visualization
+ Address geocoding
+ Route calculation
+ Geofencing (future)

### Web interface
<a name="web-interface"></a>

React-based web application.

 **Pages:** 
+ Dashboard: Fleet overview with key metrics
+ Vehicles: List and manage vehicles
+ Map: Real-time vehicle tracking
+ Trips: Trip history and analytics
+ Alerts: Maintenance and safety alerts
+ Drivers: Driver management and scoring

 **Technologies:** 
+ React 18
+ TypeScript
+ AWS Amplify
+ CloudScape Design System
+ MapLibre GL JS (for maps)

## Remote commands and geofences
<a name="commands-stack"></a>

Remote vehicle commands and geofence management.

The remote commands and geofences layer enables bidirectional communication with vehicles by sending commands from the cloud to vehicles through IoT Core MQTT and tracking command execution status.

### Remote commands architecture
<a name="remote-commands-architecture"></a>

The remote commands system uses a request/response pattern over MQTT:

1. Fleet Intelligence portal or API sends a command request

1. Commands Lambda publishes the command to both vehicle telemetry paths via IoT Core MQTT on every command: a protobuf payload to `cms/commands/things/{vin}/executions/{executionId}/request/protobuf` for FWE agents, and a JSON payload to the legacy `cms/commands/{vehicleId}/request` topic for MQTT Direct simulators

1. Command is stored in DynamoDB with status `SENT` 

1. Vehicle (or simulator) executes the command and publishes a response on the matching topic: an FWE agent publishes a `CommandResponse` protobuf to `cms/commands/things/{vin}/executions/{executionId}/response/protobuf`; a simulator publishes JSON to the legacy `cms/commands/{vehicleId}/response` topic

1. A single IoT Rule per response topic triggers the Command Response Handler Lambda, which decodes either payload shape

1. Response Handler updates the command status in DynamoDB (SUCCEEDED, FAILED, TIMEOUT, IN\_PROGRESS)

1. Response Handler calculates round-trip latency in milliseconds

### Command API endpoints
<a name="command-api-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
| POST | /api/commands/{vehicleId} | Send a command to a vehicle | 
| GET | /api/commands/{vehicleId} | List command history for a vehicle | 
| GET | /api/commands/catalog | List available actuatable commands from the signal catalog | 
| POST | /api/geofences | Create a geofence | 
| GET | /api/geofences/{vehicleId} | List geofences for a vehicle (includes global geofences) | 
| DELETE | /api/geofences/{geofenceId} | Deactivate a geofence | 

### Command request payload
<a name="command-request-payload"></a>

When sending a command, the Lambda publishes the following JSON to the MQTT topic `cms/commands/{vehicleId}/request`:

```
{
  "commandId": "a1b2c3d4e5f6",
  "commandName": "lock_doors",
  "vehicleId": "VEH-0049",
  "value": true,
  "issuedAt": "2025-03-08T15:30:00+00:00",
  "issuedAtMs": 1741448200000,
  "timeout": 10000
}
```

### Command response payload
<a name="command-response-payload"></a>

The vehicle publishes a response to `cms/commands/{vehicleId}/response`:

```
{
  "commandId": "a1b2c3d4e5f6",
  "vehicleId": "VEH-0049",
  "status": "SUCCEEDED",
  "reason": "",
  "resultValue": "true"
}
```

 **Status values:** 
+  `SENT` — Command published to MQTT, awaiting vehicle response
+  `IN_PROGRESS` — Vehicle acknowledged receipt, execution in progress
+  `SUCCEEDED` — Command executed successfully
+  `FAILED` — Command execution failed (reason field contains details)
+  `TIMEOUT` — Vehicle did not respond within the timeout period

### Command catalog
<a name="command-catalog"></a>

The command catalog is derived from the signal catalog. Signals with an `actuator` attribute are exposed as available commands. The catalog endpoint returns actuatable signals grouped by category:

 **Categories:** 
+  **doors** — Lock/unlock doors
+  **lights** — Headlights, hazard lights, turn signals
+  **climate** — HVAC on/off, target temperature, seat heating
+  **windows** — Window open/close
+  **trunk** — Trunk lock/unlock
+  **horn** — Horn activation
+  **engine** — Remote start/stop

Each actuator definition includes:
+  `commandName` — The command identifier (for example, `lock_doors`)
+  `valueType` — Data type: boolean, number, enum
+  `min` / `max` — Valid range for numeric values
+  `options` — Valid values for enum types
+  `responseTimeout` — Expected response time in milliseconds
+  `unit` — Unit of measurement (if applicable)

### Commands table schema
<a name="command-dynamodb-schema"></a>


| Attribute | Type | Description | 
| --- | --- | --- | 
| commandId | String (PK) | Unique command identifier (UUID prefix) | 
| vehicleId | String | Target vehicle ID (GSI: vehicleId-index) | 
| commandName | String | Command name from catalog | 
| value | String | Command value | 
| status | String | SENT, IN\_PROGRESS, SUCCEEDED, FAILED, TIMEOUT | 
| issuedAt | String | ISO 8601 timestamp when command was sent | 
| respondedAt | String | ISO 8601 timestamp when response was received | 
| latencyMs | Number | Round-trip latency in milliseconds | 
| reason | String | Failure reason (if status is FAILED) | 
| resultValue | String | Value returned by the vehicle | 
| ttl | Number | DynamoDB TTL (7 days after creation) | 

### Geofence management
<a name="geofence-management"></a>

Geofences are managed through the Commands API and evaluated by the GeofenceProcessor Flink application.

 **Geofence schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| geofenceId | String (PK) | Unique geofence identifier | 
| vehicleId | String | Target vehicle ID or `ALL` for global geofences | 
| name | String | Human-readable geofence name | 
| centerLat | Number | Center latitude | 
| centerLng | Number | Center longitude | 
| radiusKm | Number | Radius in kilometers | 
| type | String | Geofence shape (CIRCLE) | 
| action | String | Action on violation (ALERT) | 
| active | Boolean | Whether the geofence is active | 
| createdAt | String | ISO 8601 creation timestamp | 
| ttl | Number | DynamoDB TTL (90 days after creation) | 

## WebSocket telemetry fan-out
<a name="ws-fanout-stack"></a>

Real-time Kafka-to-WebSocket bridge for live vehicle telemetry in the Fleet Intelligence portal.

The WsFanoutStack deploys an ECS Fargate task that consumes per-fleet Kafka topics and pushes live telemetry updates to connected Fleet Intelligence portal clients over WebSocket.

### Fan-out architecture
<a name="ws-fanout-architecture"></a>

The ECS Fargate worker maintains an active Kafka consumer group (`cms-{stage}-ws-fanout-consumer`) and subscribes to per-fleet telemetry topics derived from the MSK cluster. On each Kafka message, the worker queries the `cms-{stage}-storage-ws-connections` DynamoDB table to find all active WebSocket connection IDs for the vehicle’s fleet, then calls the API Gateway Management API (`@connections/{connectionId}`) to push the telemetry payload to each connected browser.

 **Key components:** 
+  **MSK consumer** — Reads from per-fleet telemetry topics using SASL/IAM authentication.
+  **DynamoDB connections table** (`cms-{stage}-storage-ws-connections`) — Stores active connection ID, fleet ID, and connection timestamp for each connected client.
+  **API Gateway WebSocket API** — Manages WebSocket lifecycle (`$connect`, `$disconnect`, `$default` routes).
+  ** `$connect` Lambda authorizer** — A Cognito JWT REQUEST authorizer validates the `?token=<jwt>` query parameter on every WebSocket upgrade request. Connections without a valid token receive HTTP 401 and are rejected before establishing. Fleet-operator connections are scoped to their authorized fleet IDs from the JWT `custom:fleetIds` claim.

### WebSocket security posture
<a name="ws-fanout-security"></a>

Anonymous WebSocket upgrades are disabled by default. The `cms.allow_unauth_websocket` CDK context flag (default `false`) controls whether the `$connect` authorizer allows unauthenticated connections. Set this flag to `true` only for demo or development environments where anonymous map access is acceptable.

## Conversational fleet assistant
<a name="bedrock-agents-stack"></a>

The Fleet Intelligence portal’s conversational assistant is served by the companion Agentic Vehicle Experience (AVX) accelerator.

The in-UI conversational assistant that surfaces in the Fleet Intelligence portal is **not** deployed by any stack in this repository. It is deployed by the companion Agentic Vehicle Experience (AVX) accelerator, and CMS consumes it by pointing the Fleet Intelligence portal at the AVX API endpoint. This section describes only the CMS-side integration surface; the supervisor agent, its specialist tools, and the AgentCore runtimes are owned by AVX.

### Amazon Bedrock AgentCore runtime
<a name="bedrock-agents-agentcore-runtime"></a>

The conversational assistant is surfaced in the Fleet Intelligence portal through two Amazon Bedrock AgentCore runtimes deployed from the companion Agentic Vehicle Experience (AVX) repo:
+  **Bidirectional (voice)** — `vsa_supervisor_bidi_staging` — WebSocket-based streaming for voice interactions in the iOS companion app.
+  **Text (HTTP)** — `vsa_supervisor_text_staging` — HTTP unary runtime used by the Fleet Intelligence portal `/assistant/chat` endpoint.

The Fleet Intelligence portal `ChatAgent` component calls `/assistant/chat` on the AVX API Gateway (resolved from the `vsaApiEndpoint` field in `runtimeConfig.json`). AVX proxies the request to the AgentCore text runtime, which invokes the supervisor agent. Persona is inferred from Cognito claims: `fleet_driver` is the default; a `custom:role=service-advisor` claim selects the service-advisor persona.

### Cross-account ADP Knowledge Base retrieval
<a name="bedrock-agents-adp-kb"></a>

The AVX supervisor agent grounds its responses in the Automotive Data Platform (ADP) Knowledge Base — vehicle-specific diagnostic trouble code guides, maintenance bulletins, and recall notices — retrieved through cross-account `bedrock:Retrieve` calls. Both the knowledge base identifier and the cross-account trust are configured on the AVX side; CMS does not carry any Bedrock agent IAM. Operators who prefer to run without the assistant can leave `runtimeConfig.json’s `vsaApiEndpoint` unset — the chat panel then reports the assistant as not configured and the rest of the Fleet Intelligence portal continues to function normally.

## Fleet Intelligence
<a name="fleet-intelligence"></a>

The Fleet Intelligence services read the Automotive Data Platform (ADP) accelerator’s curated products over cross-region Amazon Athena.

The Fleet Intelligence services compute cost per mile, preventive-maintenance compliance, and per-vehicle sell timing for the `/fleet-intelligence/*` screens. The architecture of each fleet intelligence feature is described with the feature: see [Fleet cost intelligence](fleet-cost-intelligence.md), [Dynamic fleet rebalancing](dynamic-fleet-rebalancing.md), and [Recall and warranty management](recall-warranty-management.md).

### FleetIntelligenceAnalyticsStack
<a name="fleet-intelligence-analytics-stack"></a>

The stack deploys an Amazon Athena workgroup and a results S3 bucket in `us-east-1`. Fleet Intelligence services in the `us-west-2` deployment region read cross-region against the Automotive Data Platform (ADP) accelerator’s curated products (`service_records`, `charging_sessions`, `energy_usage`) through that workgroup. The stack lives in the `us-east-1` Region so its resources sit adjacent to the ADP data catalog; the CMS Lambda functions reading through it authenticate via Lake Formation grants owned by the ADP producer account plus a cross-account KMS `Decrypt` scoped by `kms:ViaService=s3.us-east-1.amazonaws.com`.

### Fleet Intelligence services
<a name="fleet-intelligence-consumer"></a>

The `services/fleet_intelligence/` module contains the renderers behind the fleet intelligence routes and their supporting Athena reader (`adp_source.py`). Each renderer reads maintenance cost per vehicle per month directly from ADP curated products. Sell-timing analysis uses a linear-fit of maintenance cost versus straight-line depreciation to compute a crossover month, fit R², and provenance — all deterministic and reproducible for a given `snapshot_date`.