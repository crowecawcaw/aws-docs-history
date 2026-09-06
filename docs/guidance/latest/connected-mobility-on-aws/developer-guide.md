

# Developer guide
<a name="developer-guide"></a>

This section provides guidance for customizing and extending the Guidance for Connected Mobility on AWS using AWS CDK, developing Flink applications, extending the Fleet Manager UI, and integrating with external systems.

## Source code
<a name="source-code"></a>

Visit our [GitHub repository](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws) to download the source files for this solution and to share your customizations with others.

The solution uses [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) for infrastructure as code. See the [README.md](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws/blob/main/README.md) file for additional information.

## Development environment setup
<a name="development-environment-setup"></a>

### Prerequisites
<a name="prerequisites-dev"></a>
+ AWS CLI v2
+ Node.js 18.x or later
+ Python 3.9 or later
+ AWS CDK v2.100.0 or later
+ Git
+ IDE (VS Code, PyCharm, or IntelliJ recommended)

### Clone and setup
<a name="clone-and-setup"></a>

```
# Clone repository
git clone https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws.git
cd guidance-for-connected-mobility-on-aws

# Install dependencies
cd deployment
make install

# Activate virtual environment
source .venv/bin/activate
```

## Repository structure
<a name="repository-structure"></a>

```
guidance-for-connected-mobility-on-aws/
├── deployment/
│   ├── app.py                          # CDK application entry point
│   ├── stacks/                         # CDK stack definitions
│   │   ├── bedrock_agents_stack.py     # Bedrock supervisor + specialist agents (opt-in)
│   │   ├── commands_stack.py           # Remote vehicle commands API
│   │   ├── connector_stack.py          # OEM cloud-to-cloud connector (ECS Fargate)
│   │   ├── data_processing_stack.py    # Signal catalog and transform manifests
│   │   ├── fwe_telemetry_stack.py      # FleetWise Edge integration
│   │   ├── flink_stack.py              # Flink stream processing applications
│   │   ├── infrastructure_stack.py     # VPC, subnets, networking
│   │   ├── iot_stack.py                # Fleet management IoT components
│   │   ├── msk_stack.py                # MSK cluster, VPC, and ElastiCache
│   │   ├── predictive_agent_stack.py   # Predictive maintenance AI agent
│   │   ├── simulation_stack.py         # ECS Fargate vehicle simulator
│   │   ├── storage_stack.py            # DynamoDB tables
│   │   ├── tco_stack.py                # TCO and cost analytics
│   │   ├── telemetry_integration_stack.py  # MSK-IoT connectivity
│   │   ├── ui_stack.py                 # Frontend, API Gateway, Cognito
│   │   └── ws_fanout_stack.py          # Kafka to WebSocket real-time fan-out
│   ├── Makefile                        # Deployment automation
│   └── requirements.txt
├── modules/
│   ├── campaign_manager/               # FleetWise campaign management
│   ├── cms_ui/                         # React frontend application
│   │   └── source/
│   │       ├── frontend/               # React app (Cloudscape Design)
│   │       └── handlers/               # API Lambda handlers
│   ├── flink/                          # Java Flink processors (com.cms.telemetry)
│   └── predictive_agent/               # Predictive maintenance agent
├── services/
│   ├── commands/                       # Remote commands Lambda + protobuf
│   ├── connectors/
│   │   └── oem1/                       # OEM1 cloud connector (gRPC streaming)
│   ├── data_processing/                # Data processing service
│   └── simulation/                     # Vehicle simulation service
├── scripts/                            # Utility scripts
└── tests/e2e/                          # End-to-end tests
```

## CDK stacks
<a name="cdk-stacks"></a>

The solution is deployed as a set of modular CDK stacks defined in `deployment/app.py`. Each stack can be deployed independently based on your requirements.

### Stack overview
<a name="stack-overview"></a>


| Stack | Purpose | Condition | 
| --- | --- | --- | 
|  `DataProcessingStack`  | Signal catalog and transform manifests | Always deployed | 
|  `StorageStack`  | DynamoDB tables for vehicles, trips, telemetry, safety events, maintenance alerts, drivers, and more | Always deployed | 
|  `MSKStack`  | VPC, Amazon MSK (Kafka) cluster, and ElastiCache for Redis | Deployed unless `MSK_CLUSTER_ARN` is provided | 
|  `IoTStack`  | Fleet management IoT components | Always deployed | 
|  `TelemetryIntegrationStack`  | MSK-IoT connectivity (IoT rules, VPC destinations) |  `DEPLOY_TELEMETRY_INTEGRATION=true`  | 
|  `FlinkStack`  | Flink stream processing applications (trip detection, safety, maintenance, telemetry, FWE decode, OEM transform, campaign sync, geofence, event-driven, simulator preprocessor) | Always deployed | 
|  `FweTelemetryStack`  | FleetWise Edge IoT rules, VPC endpoints, CampaignSyncProcessor |  `DEPLOY_FLEETWISE=true`  | 
|  `UIStack`  | React frontend (Cloudscape Design), API Gateway, Cognito authentication, Amazon Location Service | Always deployed | 
|  `CommandsStack`  | Remote vehicle commands API via IoT Core MQTT, geofence management | Always deployed | 
|  `ConnectorStack`  | OEM cloud-to-cloud connector — ECS Fargate gRPC streaming worker, landing on `cms-telemetry-oem`  | Always deployed | 
|  `WsFanoutStack`  | Kafka to WebSocket real-time telemetry fan-out for the Fleet Manager UI | Always deployed | 
|  `TcoStack`  | TCO and cost analytics | Always deployed | 
|  `PredictiveAgentStack`  | Predictive maintenance AI agent |  `DEPLOY_PREDICTIVE_AGENT=true`  | 
|  `SimulationStack`  | ECS Fargate vehicle simulation service |  `DEPLOY_SIMULATION=true`  | 
|  `BedrockAgentsStack`  | Bedrock supervisor and specialist agents with Amazon Bedrock AgentCore runtime (opt-in) |  `make deploy-bedrock-agents` (not included in `deploy-all`) | 

### Customizing stacks
<a name="customizing-cdk-stacks"></a>

Stack definitions are in `deployment/stacks/`. Each stack is a Python class that extends `Stack`.

#### Example: Modify MSK configuration
<a name="example-modify-msk-configuration"></a>

```
# In deployment/stacks/msk_stack.py

class MSKStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Modify broker instance type
        self.cluster = msk.CfnCluster(
            self, "MSKCluster",
            cluster_name=f"cms-{stage}-cluster",
            kafka_version="3.5.1",
            number_of_broker_nodes=3,
            broker_node_group_info=msk.CfnCluster.BrokerNodeGroupInfoProperty(
                instance_type="kafka.m5.xlarge",  # Changed from m5.large
                storage_info=msk.CfnCluster.StorageInfoProperty(
                    ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                        volume_size=200  # Increased from 100GB
                    )
                ),
            )
        )
```

#### Example: Add a new stack
<a name="example-add-new-stack"></a>

To add a custom stack, create a new file in `deployment/stacks/` and register it in `deployment/app.py`:

```
# 1. Create deployment/stacks/custom_stack.py
from aws_cdk import Stack
from constructs import Construct

class CustomStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Add your resources here

# 2. Add to deployment/app.py
from stacks.custom_stack import CustomStack

custom_stack = CustomStack(
    app,
    f"{stack_prefix}-custom",
    env=env,
    description="Guidance for Connected Mobility (SO9618) - Custom"
)
```

## Developing Flink applications
<a name="developing-flink-applications"></a>

### Flink project structure
<a name="flink-project-structure"></a>

```
modules/flink/
├── pom.xml                              # Maven configuration (Flink 1.18.1)
├── src/
│   └── main/
│       ├── java/
│       │   └── com/cms/telemetry/
│       │       ├── UniversalProcessor.java          # Entry point, routes to processor
│       │       ├── SimulatorPreprocessor.java        # Decodes gzip+base64 simulator telemetry
│       │       ├── TelemetryProcessor.java          # Writes telemetry to DDB
│       │       ├── EventDrivenTelemetryProcessor.java # Routes to domain topics + Redis LKS
│       │       ├── FWTelemetryProcessor.java        # Decodes FWE protobuf, maps CAN signals
│       │       ├── CampaignSyncProcessor.java       # FWE checkin → campaign push via IoT MQTT
│       │       ├── GeofenceProcessor.java           # Evaluates positions against geofences
│       │       ├── OEMTelemetryProcessor.java       # Transforms OEM telemetry via S3 manifests
│       │       ├── KafkaConfig.java                 # Shared Kafka reconnect/keepalive config
│       │       ├── SignalCatalogLoader.java          # Loads signal catalog to Redis
│       │       ├── TripProcessor.java               # Stateful trip detection (v2)
│       │       ├── SafetyProcessor.java             # Safety event detection
│       │       ├── MaintenanceProcessor.java        # Maintenance alerts
│       │       ├── TireTelemetryTransformer.java    # Tire signal normalization
│       │       ├── TelemetryData.java               # Data model
│       │       ├── TelemetryEvent.java              # Event model
│       │       ├── TelemetryDataProcessor.java      # Data processing utilities
│       │       └── sink/
│       │           ├── DynamoDBTelemetrySink.java
│       │           ├── DynamoDBTripsSink.java
│       │           ├── DynamoDBSafetyEventsSink.java
│       │           ├── DynamoDBMaintenanceAlertsSink.java
│       │           ├── RedisTelemetrySink.java
│       │           ├── CloudWatchMetricsSink.java
│       │           └── CloudWatchLogger.java
│       └── proto/                                   # Protobuf definitions for FWE
└── README.md
```

All ten Flink applications share a single JAR. The `UniversalProcessor` entry point reads the application’s runtime properties to determine which processor class to invoke.

### Trip processor: Stateful design pattern
<a name="trip-processor-design"></a>

The TripProcessor demonstrates a key pattern for reducing DynamoDB costs in stream processing: using Flink’s keyed state to eliminate per-message database reads.

 **Problem:** A stateless trip processor queries DynamoDB on every telemetry message to find the active trip, check its status, and update the record. For a 20-message trip, this results in \~60 reads and 20 full-record writes.

 **Solution:** Use `KeyedProcessFunction` with `ValueState<TripState>` keyed by `vehicleId`. All trip state (route buffer, metrics, ignition history) lives in Flink’s managed state. DynamoDB is only written to on state transitions and periodic flushes.

```
// Simplified TripProcessor v2 pattern
public class TripStateFunction
    extends KeyedProcessFunction<String, String, String> {

    // Per-vehicle state managed by Flink
    private ValueState<TripState> tripState;

    @Override
    public void open(Configuration parameters) {
        tripState = getRuntimeContext().getState(
            new ValueStateDescriptor<>("tripState", TripState.class));
    }

    @Override
    public void processElement(String json, Context ctx,
                               Collector<String> out) {
        TripState state = tripState.value();
        boolean prevIgnition = (state != null && state.ignitionOn);
        boolean currIgnition = parseIgnition(json);

        if (!prevIgnition && currIgnition) {
            // Transition: OFF → ON = Start trip
            state = new TripState(generateTripId(), vehicleId);
            writeTripStart(state);           // PutItem (1 write)
        } else if (prevIgnition && currIgnition) {
            // ON → ON = Accumulate in state
            state.addRoutePoint(lat, lng);
            state.updateMetrics(speed);
            if (state.pointsSinceFlush >= 5) {
                flushTripUpdate(state);      // UpdateItem (1 write per 5 msgs)
                state.pointsSinceFlush = 0;
            }
        } else if (prevIgnition && !currIgnition) {
            // Transition: ON → OFF = End trip
            writeTripComplete(state);        // UpdateItem (1 write)
            state = null;                    // Clear state
        }
        tripState.update(state);
    }
}
```

This pattern applies to any stream processing scenario where you need to track entity state across events without querying a database on every message.

### Build and deploy
<a name="build-and-deploy-flink"></a>

```
# Build JAR
cd modules/flink
mvn clean package -DskipTests

# Package as ZIP for Amazon Managed Service for Apache Flink
cd target
zip -j /tmp/cms-telemetry-processor-1.0.0.zip \
  cms-telemetry-processor-1.0.0.jar

# Upload to S3
aws s3 cp /tmp/cms-telemetry-processor-1.0.0.zip \
  s3://cms-dev-flink-flinkjarbucketd8dc3634-d72xj4npneqk/jars/

# Update and restart a Flink application
APP=cms-dev-flink-trip-processor
aws kinesisanalyticsv2 stop-application --application-name $APP
# Wait for READY status...
VERSION=$(aws kinesisanalyticsv2 describe-application \
  --application-name $APP \
  --query "ApplicationDetail.ApplicationVersionId" --output text)
aws kinesisanalyticsv2 update-application \
  --application-name $APP \
  --current-application-version-id $VERSION \
  --application-configuration-update '{
    "ApplicationCodeConfigurationUpdate": {
      "CodeContentUpdate": {
        "S3ContentLocationUpdate": {
          "BucketARNUpdate": "arn:aws:s3:::cms-dev-flink-flinkjarbucketd8dc3634-d72xj4npneqk",
          "FileKeyUpdate": "jars/cms-telemetry-processor-1.0.0.zip"
        }
      }
    }
  }'
aws kinesisanalyticsv2 start-application --application-name $APP
```

## Extending Fleet Manager UI
<a name="extending-fleet-manager-ui"></a>

### UI project structure
<a name="ui-project-structure"></a>

```
modules/cms_ui/source/
├── frontend/                # React application
│   ├── src/
│   │   ├── pages/           # Page components
│   │   ├── components/      # Reusable components
│   │   ├── services/        # API clients
│   │   ├── hooks/           # Custom React hooks
│   │   └── utils/           # Utility functions
│   ├── public/
│   └── package.json
└── handlers/                # API Lambda handlers
    └── main_api/            # Fleet management API handler
```

The UI is built with [Cloudscape Design System](https://cloudscape.design/) and deployed via CloudFront with S3 origin. Authentication is handled by Amazon Cognito.

### Example: Add a new page
<a name="example-add-new-page"></a>

```
// modules/cms_ui/source/frontend/src/pages/CustomPage.tsx

import React, { useState, useEffect } from 'react';
import {
  Container,
  Header,
  Table,
  Button
} from '@cloudscape-design/components';
import { useApi } from '../hooks/useApi';

export const CustomPage: React.FC = () => {
  const [data, setData] = useState([]);
  const { get } = useApi();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    const response = await get('/api/v1/custom-endpoint');
    setData(response.items);
  };

  return (
    <Container
      header={
        <Header
          variant="h1"
          actions={
            <Button onClick={loadData}>Refresh</Button>
          }
        >
          Custom Feature
        </Header>
      }
    >
      <Table
        columnDefinitions={[
          { id: 'id', header: 'ID', cell: item => item.id },
          { id: 'name', header: 'Name', cell: item => item.name }
        ]}
        items={data}
      />
    </Container>
  );
};
```

### Build and deploy
<a name="build-and-deploy-ui"></a>

```
# Build frontend
cd modules/cms_ui/source/frontend
npm install
npm run build

# Redeploy the UI stack to push changes
cd ../../../../deployment
cdk deploy cms-dev-ui
```

## API reference
<a name="api-reference"></a>

The solution exposes two API Gateway endpoints: the Fleet Management API (deployed by `UIStack`) and the Commands API (deployed by `CommandsStack`).

### Authentication
<a name="authentication"></a>

Both APIs use Amazon Cognito for authentication. Obtain an access token before making API calls:

```
# Get access token
TOKEN=$(aws cognito-idp initiate-auth \
  --client-id CLIENT_ID \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME=FleetManager@example.com,PASSWORD=FleetManager123! \
  --query 'AuthenticationResult.AccessToken' --output text)
```

### Fleet Management API
<a name="fleet-management-api"></a>

The Fleet Management API is served from the UI stack’s API Gateway endpoint. All endpoints are prefixed with `/api/v1/`.

#### Fleet endpoints
<a name="fleet-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
|  `GET`  |  `/api/v1/fleets`  | List all fleets | 
|  `POST`  |  `/api/v1/fleets`  | Create a new fleet | 
|  `GET`  |  `/api/v1/fleets/{fleetId}`  | Get fleet details | 
|  `GET`  |  `/api/v1/fleets/{fleetId}/vehicles`  | List vehicles in a fleet | 

#### Vehicle endpoints
<a name="vehicle-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
|  `GET`  |  `/api/v1/vehicles`  | List all vehicles | 
|  `POST`  |  `/api/v1/vehicles`  | Register a new vehicle | 
|  `GET`  |  `/api/v1/vehicles/locations`  | Get all vehicle locations | 
|  `GET`  |  `/api/v1/vehicles/{vehicleId}`  | Get vehicle details | 
|  `GET`  |  `/api/v1/vehicles/{vehicleId}/trips`  | List trips for a vehicle | 
|  `GET`  |  `/api/v1/vehicles/{vehicleId}/trips/{tripId}`  | Get trip details | 
|  `GET`  |  `/api/v1/vehicles/{vehicleId}/safety-alerts`  | List safety alerts for a vehicle | 
|  `GET`  |  `/api/v1/vehicles/{vehicleId}/maintenance-alerts`  | List maintenance alerts for a vehicle | 

#### Global endpoints
<a name="global-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
|  `GET`  |  `/api/v1/trips`  | List all trips | 
|  `GET`  |  `/api/v1/safety-alerts`  | List all safety alerts | 
|  `GET`  |  `/api/v1/maintenance-alerts`  | List all maintenance alerts | 
|  `GET`  |  `/api/v1/dashboard/metrics`  | Get dashboard metrics | 
|  `GET`  |  `/api/v1/dashboard/fleet-comparison`  | Get fleet comparison data | 

#### Real-time endpoints
<a name="realtime-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
|  `GET`  |  `/realtime/vehicles`  | Get real-time vehicle data from Redis | 
|  `GET`  |  `/realtime/trips`  | Get real-time trip data from Redis | 
|  `GET`  |  `/health`  | API health check | 
|  `GET`  |  `/discover-iot-endpoint`  | Get IoT Core endpoint for MQTT connections | 

### Commands API
<a name="commands-api"></a>

The Commands API enables sending remote commands to vehicles via IoT Core MQTT and managing geofences. It is served from a separate API Gateway endpoint deployed by the `CommandsStack`.

#### Command endpoints
<a name="commands-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
|  `POST`  |  `/api/commands/{vehicleId}`  | Send a command to a vehicle | 
|  `GET`  |  `/api/commands/{vehicleId}`  | Get command history for a vehicle | 
|  `GET`  |  `/api/commands/catalog`  | List available actuatable commands | 

 **Send a command:** 

```
curl -X POST https://<commands-api-url>/api/commands/VEH-0049 \
  -H "Content-Type: application/json" \
  -d '{
    "commandName": "lock_doors",
    "value": true,
    "label": "Lock all doors",
    "category": "doors",
    "timeout": 10000
  }'

# Response:
# {
#   "success": true,
#   "commandId": "a1b2c3d4e5f6",
#   "status": "SENT",
#   "topic": "cms/commands/VEH-0049/request"
# }
```

The command is published to both a protobuf topic for FleetWise Edge agents (`cms/commands/things/{vin}/executions/{executionId}/request/protobuf`) and a JSON topic for MQTT Direct simulators (`cms/commands/{vehicleId}/request`).

 **Get command catalog:** 

```
curl -X GET https://<commands-api-url>/api/commands/catalog

# Response includes actuators grouped by category:
# {
#   "actuators": {
#     "doors": [
#       {
#         "commandName": "lock_doors",
#         "label": "Lock Doors",
#         "valueType": "boolean",
#         "responseTimeout": 5000
#       }
#     ],
#     "climate": [...],
#     "lights": [...]
#   },
#   "totalCount": 12
# }
```

#### Geofence endpoints
<a name="geofence-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
|  `POST`  |  `/api/geofences`  | Create a geofence | 
|  `GET`  |  `/api/geofences/{vehicleId}`  | List geofences for a vehicle | 
|  `DELETE`  |  `/api/geofences/{vehicleId}`  | Delete (deactivate) a geofence | 

 **Create a geofence:** 

```
curl -X POST https://<commands-api-url>/api/geofences \
  -H "Content-Type: application/json" \
  -d '{
    "vehicleId": "VEH-0049",
    "name": "Office Parking",
    "centerLat": 40.7128,
    "centerLng": -74.0060,
    "radiusKm": 0.5,
    "type": "CIRCLE",
    "action": "ALERT"
  }'
```

#### Command response flow
<a name="command-response-flow"></a>

When a vehicle responds to a command, the response flows through an IoT Rule that matches the topic `cms/commands/+/response`. The rule invokes the `command_response_handler` Lambda, which updates the command status in DynamoDB.

## Service alerts and predictive maintenance
<a name="testing-and-debugging"></a>

The Connected Mobility platform provides three layers of vehicle health monitoring, each designed for a different failure time scale.

### Alert detection layers
<a name="alert-detection-layers"></a>


| Layer | Detection Method | Time Scale | Example | Cost | 
| --- | --- | --- | --- | --- | 
| Rule-based (Flink) | Event catalog thresholds | Immediate | Tire pressure < 28 PSI | $0 (runs on existing Flink) | 
| Daily batch (Lambda) | Trend analysis over 7 days | Days | Pressure dropping 0.8 PSI/day | $0.60/month | 
| Real-time ML (SageMaker) | Multi-signal anomaly detection | Minutes | Low pressure \+ high speed \+ high temp | $83/month | 

### Event catalog — single source of truth
<a name="event-catalog-single-source-of-truth"></a>

All detection rules are defined in the event catalog DynamoDB table (`cms-{stage}-event-catalog`). The Flink processors, simulator, and UI all read from this catalog. Adding a new event to the catalog makes it immediately detectable by Flink and simulatable in the trip simulator — no code changes required.

Each event defines:
+  `event_id` — unique identifier (e.g., `maintenance.tire_pressure`)
+  `category` — `safety` or `maintenance` 
+  `json_fields` — telemetry field names to evaluate (e.g., `tire_pressure_fl`)
+  `threshold_operator` and `threshold_value` — the detection rule (e.g., `< 28`)
+  `condition_type` — `simple` (single signal) or `composite` (multiple signals with AND/OR logic)
+  `severity` — 1 (low) to 3 (critical)

The platform ships with 41 events: 12 safety events and 29 maintenance events covering tire pressure, engine temperature, oil pressure, battery voltage, brake wear, and more.

### Catalog-driven Flink processing
<a name="catalog-driven-flink-processing"></a>

The `MaintenanceProcessor` loads rules from the event catalog at startup and refreshes every 5 minutes. It evaluates each telemetry message against all maintenance rules using the `EventCatalogEvaluator`:

1. Telemetry arrives on the `cms-telemetry-maintenance` Kafka topic

1. The evaluator loads rules filtered by `category = maintenance` 

1. For each rule, it checks if the telemetry field crosses the threshold

1. For composite rules, it evaluates all conditions with AND/OR logic

1. Matching rules generate alerts written to the `maintenance-alerts` DynamoDB table

The `SafetyProcessor` follows the same pattern for safety events, writing to the `safety-events` table.

Alerts include the vehicle ID, GPS coordinates, odometer reading, estimated repair cost, and the catalog rule that triggered them.

### Estimated repair costs
<a name="estimated-repair-costs"></a>

Each alert type has a realistic cost estimate based on the service type:


| Alert Type | Estimated Cost | 
| --- | --- | 
| Tire pressure (patch/repair) | $35 | 
| Tire rotation | $60 | 
| Tire replacement (set of 4) | $800 | 
| Oil change | $75 | 
| Brake pads | $350 | 
| Battery replacement | $180 | 
| Alternator failure | $650 | 
| Engine overheating | $1,200 | 
| Diagnostic scan | $120 | 
| EV motor overheating | $2,500 | 

### Predictive maintenance integration
<a name="predictive-maintenance-integration"></a>

The platform integrates with the [Tire Predictive Maintenance Guidance](https://docs.aws.amazon.com/guidance/latest/automotive-data-platform/predictive-maintenance.html) for ML-based prediction. Two inference strategies are used:

#### Daily batch — slow leak detection
<a name="daily-batch-slow-leak-detection"></a>

A scheduled Lambda runs daily, queries the last 7 days of tire telemetry, and computes pressure trends using linear regression. Vehicles with consistent pressure loss (> 0.3 PSI/day) receive a `prediction.tire_slow_leak` warning days before the rule-based threshold is crossed.

This approach costs approximately $0.60/month because a slow leak changes over days — checking daily provides the same advance warning as checking every 15 minutes, at a fraction of the cost.

#### Real-time — highway blowout risk
<a name="real-time-highway-blowout-risk"></a>

A SageMaker Random Cut Forest endpoint evaluates multi-signal risk patterns for vehicles at highway speed. The model detects dangerous combinations that no single threshold catches: borderline pressure (29 PSI) \+ high temperature (140°F) \+ high speed (75 mph) \+ worn tread (3.5mm).

The endpoint is only called when:

1. Vehicle speed exceeds 60 mph, AND

1. Any tire pressure is below 30 PSI OR tire temperature exceeds 120°F

This pre-filtering reduces inference calls from \~19,000/day to \~50-100/day, keeping the $83/month endpoint cost justified against the $10,000\+ cost of a highway blowout.

### Simulating service alerts
<a name="simulating-service-alerts"></a>

The trip simulator in the Fleet Manager UI allows selecting specific maintenance and safety events to trigger during a simulated trip. Events are loaded dynamically from the event catalog — the dropdown always reflects the current catalog contents.

When an event is selected, the simulator uses catalog-driven degradation targets to gradually push the relevant signal past its threshold. For example, selecting "Tire pressure below safe threshold" causes tire pressure to drop from 32 PSI toward 20 PSI over approximately 2 minutes, crossing the 28 PSI threshold and triggering the Flink alert.

To simulate a highway blowout risk scenario, select "Highway blowout risk" which creates a composite condition: tire pressure drops below 30 PSI while vehicle speed exceeds 60 mph.

## Testing and debugging
<a name="testing-and-debugging-2"></a>

### Test UI locally
<a name="test-ui-locally"></a>

```
cd modules/cms_ui/source/frontend

# Start development server
npm start

# Run tests
npm test

# Run linter
npm run lint
```

### Debugging Flink applications
<a name="debugging-flink"></a>

```
# View Flink logs
aws logs tail /aws/kinesis-analytics/cms-dev-trip-detection --follow

# Check application status
aws kinesisanalyticsv2 describe-application \
  --application-name cms-dev-trip-detection

# View metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/KinesisAnalytics \
  --metric-name millisBehindLatest \
  --dimensions Name=Application,Value=cms-dev-trip-detection \
  --start-time 2024-10-13T00:00:00Z \
  --end-time 2024-10-13T23:59:59Z \
  --period 300 \
  --statistics Average
```

### Check deployment status
<a name="check-stack-status-dev"></a>

```
cd deployment
make status
```

## GSI and ISV integration
<a name="gsi-and-isv-integration"></a>

Global system integrators (GSIs) and independent software vendors (ISVs) can leverage this guidance to build and deploy mobility services quickly and efficiently.

### White-labeling
<a name="white-labeling"></a>

#### Customize branding
<a name="customize-branding"></a>

```
// modules/cms_ui/source/frontend/src/config/branding.ts

export const branding = {
  companyName: 'Your Company',
  logo: '/assets/logo.png',
  primaryColor: '#0073bb',
  secondaryColor: '#ec7211',
  favicon: '/assets/favicon.ico'
};
```

#### Custom domain
<a name="custom-domain"></a>

```
# In deployment/stacks/ui_stack.py

from aws_cdk import aws_certificatemanager as acm

# Add custom domain
certificate = acm.Certificate.from_certificate_arn(
    self, "Certificate",
    certificate_arn="arn:aws:acm:us-east-1:123456789012:certificate/..."
)

distribution = cloudfront.Distribution(
    self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3Origin(ui_bucket)
    ),
    domain_names=["fleet.yourcompany.com"],
    certificate=certificate
)
```

### Extending functionality
<a name="extending-functionality"></a>

GSIs and ISVs can extend this guidance by:
+ Adding custom Flink applications for specialized processing
+ Integrating with third-party telematics providers
+ Building custom dashboards and reports
+ Implementing additional API endpoints
+ Adding machine learning models for predictive analytics

## CVX assistant integration
<a name="cvx-assistant-integration"></a>

The Fleet Manager UI includes a conversational assistant panel backed by the Amazon Bedrock AgentCore text runtime. The assistant routes user messages to a Bedrock supervisor agent that grounds responses against the Automotive Data Platform Knowledge Base.

### VSA API endpoint helper
<a name="vsa-api-endpoint"></a>

The `getVsaApiEndpoint()` helper in `modules/cms_ui/source/frontend/src/config/api.ts` reads the `vsaApiEndpoint` field from the runtime configuration JSON that CloudFront serves at `/runtimeConfig.json`. The value points to the deployed CVX API Gateway stage URL.

```
// modules/cms_ui/source/frontend/src/config/api.ts

import { getRuntimeConfig } from './runtimeConfig';

export function getVsaApiEndpoint(): string {
  const config = getRuntimeConfig();
  return (
    config.vsaApiEndpoint ||
    process.env.REACT_APP_VSA_API_ENDPOINT ||
    ''
  );
}
```

The helper falls back to an environment variable for local development so the assistant can be tested without a deployed stack.

### Chat message fetch pattern
<a name="chat-agent-fetch-pattern"></a>

The `ChatAgent` component in `modules/cms_ui/source/frontend/src/components/commons/ChatAgent.tsx` sends each user message to the `/assistant/chat` route of the VSA API endpoint using a standard `fetch` call. The AgentCore text runtime (`vsa_supervisor_text_staging` or the production equivalent) handles the request and streams back a text response.

```
// modules/cms_ui/source/frontend/src/components/commons/ChatAgent.tsx
// Simplified excerpt showing the fetch pattern

import { getVsaApiEndpoint } from '../../config/api';

async function sendMessage(userMessage: string): Promise<string> {
  const vsaEndpoint = getVsaApiEndpoint();
  const base = vsaEndpoint.endsWith('/')
    ? vsaEndpoint.slice(0, -1)
    : vsaEndpoint;

  const res = await fetch(`${base}/assistant/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userMessage, sessionId }),
  });

  if (!res.ok) {
    throw new Error(`Assistant request failed: ${res.status}`);
  }
  const data = await res.json();
  return data.response ?? '';
}
```

The Fetch Interceptor in `modules/cms_ui/source/frontend/src/auth/fetchInterceptor.ts` attaches the Cognito access token to requests matching `vsaApiEndpoint`, so no manual `Authorization` header is required in the component.

### Persona inference from Cognito claims
<a name="persona-inference"></a>

The backend AgentCore handler infers the user persona from the Cognito `custom:role` claim that the UI passes as a JWT. The two supported personas are `fleet_driver` (default) and `service_advisor` (when `custom:role=service-advisor`). The supervisor agent selects specialist tools and tone based on the persona.

To add a third persona, update the persona-routing logic in the CVX supervisor agent and ensure the corresponding Cognito user attribute is populated during user provisioning.

## Bedrock agent tool extension
<a name="bedrock-agent-tool-extension"></a>

The `BedrockAgentsStack` in `deployment/stacks/bedrock_agents_stack.py` provisions four Bedrock agents — `cms-cost-agent`, `cms-maintenance-agent`, `cms-rebalancing-agent`, and `cms-recall-warranty-agent` — each with a `prod` alias. Agent configuration is loaded from JSON snapshots in `deployment/scripts/bedrock_agents_snapshot/`.

### Adding a tool to an agent
<a name="adding-a-tool-to-an-agent"></a>

Add the tool implementation to the relevant module under `modules/predictive_agent/agent/` or `modules/campaign_manager/`, then update the corresponding agent snapshot in `deployment/scripts/bedrock_agents_snapshot/` to reference the new action group.

```
# Example: adding an action group to a Bedrock agent snapshot
# File: deployment/scripts/bedrock_agents_snapshot/cms-maintenance-agent.json

{
  "agentName": "cms-maintenance-agent",
  "foundationModel": "us.anthropic.claude-sonnet-4-6",
  "actionGroups": [
    {
      "actionGroupName": "MaintenanceTools",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:<region>:<account-id>:function:cms-<stage>-maintenance-tools"
      },
      "apiSchema": { ... }
    }
  ]
}
```

### Inference-profile IAM pattern
<a name="inference-profile-iam-pattern"></a>

Bedrock cross-region inference profiles require two IAM policy statements: one for the inference profile resource (which includes the account ID) and one for the underlying foundation model (which does not include an account ID). The `BedrockAgentsStack` encodes this pattern automatically based on the resolved inference profile ID.

```
# Pattern used in deployment/stacks/bedrock_agents_stack.py

from aws_cdk import Stack
import aws_cdk.aws_iam as iam

account = Stack.of(self).account
profile_id = "us.anthropic.claude-sonnet-4-6"

# Strip geographic prefix to get the foundation model ID
fm_id = profile_id.split(".", 1)[1]  # "anthropic.claude-sonnet-4-6"

iam.PolicyStatement(
    actions=["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
    resources=[
        # Inference profile ARN — includes account ID
        f"arn:aws:bedrock:*:{account}:inference-profile/{profile_id}",
        # Foundation model ARN — no account ID
        f"arn:aws:bedrock:*::foundation-model/{fm_id}",
    ],
)
```

If you add a new agent that invokes a different inference profile, apply this same two-statement pattern to the agent service role.

## OEM connector extension
<a name="oem-connector-extension"></a>

The `ConnectorStack` in `deployment/stacks/connector_stack.py` deploys the OEM1 cloud-to-cloud connector as an ECS Fargate task. The connector establishes a gRPC streaming connection to the OEM cloud API, receives vehicle telemetry, transforms it via a manifest loaded from Amazon S3, and publishes normalized records to the `cms-telemetry-oem` Kafka topic. The `OEMTelemetryProcessor` Flink application in `modules/flink/src/main/java/com/cms/telemetry/OEMTelemetryProcessor.java` then consumes from that topic and writes to DynamoDB and Redis.

### Connector source layout
<a name="connector-source-layout"></a>

The OEM1 connector implementation lives under `services/connectors/oem1/`:

```
services/connectors/oem1/
├── connector.py          # Kafka consumer and gRPC client
├── main.py               # Entry point
├── token_supplier.py     # OEM OAuth token management
├── kafka_producer.py     # Kafka producer to cms-telemetry-oem
├── typed_data_decoder.py # Signal-type decoding utilities
├── config.py             # Environment variable configuration
├── Dockerfile            # Container image definition
├── admin_bulk_enroll/    # Bulk vehicle enrollment Lambda
├── admin_bulk_unenroll/  # Bulk unenroll Lambda
├── admin_enroll_quota/   # Hourly enroll quota check Lambda
└── _lib/                 # Shared library utilities
```

### Adding a connector for a second OEM
<a name="adding-a-new-oem-connector"></a>

To integrate a second OEM data source, create a new directory `services/connectors/oem2/` following the same layout as `services/connectors/oem1/`. The key integration points are:

1.  **Token management** — implement an `OAuthTokenSupplier` equivalent to `token_supplier.py` that handles your OEM API credentials, stored in AWS Secrets Manager.

1.  **Streaming consumer** — implement the transport layer (REST polling, gRPC streaming, or Kafka bridge) in `connector.py`.

1.  **Kafka producer** — publish normalized records to a dedicated topic (for example, `cms-telemetry-oem2`) to keep OEM data streams isolated.

1.  **Flink processor** — either extend `OEMTelemetryProcessor` to handle the new topic via the `PROCESSOR_TYPE` routing in `UniversalProcessor`, or add a new processor class in `modules/flink/src/main/java/com/cms/telemetry/`.

1.  **Transform manifest** — define the field mapping from OEM signal names to CMS canonical signal names in an S3-hosted JSON manifest and reference it from the Flink processor application properties.

1.  **Stack registration** — add a `ConnectorStack`-derived construct in `deployment/stacks/connector_stack.py` or a new stack file, then wire it into `deployment/app.py`.

Enrollment quota limits and admin Lambda patterns from `services/connectors/oem1/admin_bulk_enroll/` apply equally to any OEM connector; reuse those handlers or adapt them for your OEM-specific enrollment API.

## Fleet Manager Cognito role integration
<a name="fleet-manager-cognito-role-integration"></a>

The Fleet Manager API enforces authorization at the Lambda handler level in `modules/cms_ui/source/handlers/main_api/index.py`. Every API request carries a Cognito JWT, and the handler extracts the user groups and custom claims to determine the caller scope.

### Cognito groups and custom claims
<a name="cognito-groups-and-claims"></a>

Three Cognito groups control access scope:


| Group | Scope | Key claim | 
| --- | --- | --- | 
|  `platform-admin`  | All fleets and vehicles across the deployment. May create and delete fleets, bulk-enroll vehicles, and access all admin operations. | No per-fleet claim required | 
|  `fleet-operator`  | Only the fleets listed in the `custom:fleetIds` attribute. May enroll, unenroll, and manage vehicles within those fleets. |  `custom:fleetIds` — comma-separated list of fleet IDs | 
|  `fleet-viewer`  | Read-only access to the fleets listed in `custom:fleetIds`. |  `custom:fleetIds`  | 

The handler extracts these values from the decoded JWT claims:

```
# Simplified excerpt from modules/cms_ui/source/handlers/main_api/index.py

_OPERATOR_GROUPS = {'platform-admin', 'fleet-operator', 'fleet-viewer'}

def get_user_scope(claims: dict) -> tuple[set[str], list[str]]:
    """Return (user_groups, fleet_ids) from JWT claims."""
    user_groups = set(claims.get('cognito:groups', []))
    fleet_ids = [
        fid.strip()
        for fid in claims.get('custom:fleetIds', '').split(',')
        if fid.strip()
    ]
    return user_groups, fleet_ids

def is_admin(user_groups: set[str]) -> bool:
    return 'platform-admin' in user_groups
```

### Adding a new admin operation
<a name="adding-a-new-admin-operation"></a>

When adding an endpoint that must be gated on `platform-admin`:

1. Add the route handler in `modules/cms_ui/source/handlers/main_api/index.py`.

1. Call `get_user_scope()` at the top of the handler and return HTTP 403 if `is_admin()` returns `False`.

1. For fleet-operator access (per-fleet scope), verify that each requested fleet ID appears in the caller `fleet_ids` list before allowing the operation.

1. Update the Cognito IAM grants in `deployment/stacks/ui_stack.py` if the new endpoint requires Lambda access to additional DynamoDB tables or AWS services.

1. Add unit tests in `modules/cms_ui/source/handlers/main_api/tests/` verifying that:
   + a `platform-admin` token receives HTTP 200,
   + a `fleet-operator` token with a matching fleet ID receives HTTP 200,
   + a `fleet-operator` token with a non-matching fleet ID receives HTTP 403, and
   + an unauthenticated request receives HTTP 401.

### Assigning groups via CLI
<a name="assigning-groups-via-cli"></a>

```
# Add a user to the platform-admin group
aws cognito-idp admin-add-user-to-group \
  --user-pool-id <user-pool-id> \
  --username <email> \
  --group-name platform-admin

# Set the fleet scope for a fleet-operator
aws cognito-idp admin-update-user-attributes \
  --user-pool-id <user-pool-id> \
  --username <email> \
  --user-attributes Name=custom:fleetIds,Value="fleet-001,fleet-002"

# Verify current group membership
aws cognito-idp admin-list-groups-for-user \
  --user-pool-id <user-pool-id> \
  --username <email>
```

## Best practices
<a name="best-practices"></a>

### Infrastructure as code
<a name="infrastructure-as-code"></a>
+ Use CDK constructs for reusable components
+ Parameterize stack configurations
+ Use environment variables for secrets
+ Tag all resources consistently
+ Enable CloudFormation stack protection

### Security
<a name="security-dev"></a>
+ Follow least-privilege IAM policies
+ Enable encryption at rest and in transit
+ Rotate credentials regularly
+ Use AWS Secrets Manager for sensitive data
+ Enable CloudTrail logging

### Performance
<a name="performance"></a>
+ Right-size MSK brokers based on throughput
+ Optimize Flink parallelism
+ Use ElastiCache for frequently accessed data
+ Enable DynamoDB auto-scaling
+ Implement API caching

### Cost optimization
<a name="cost-optimization-dev"></a>
+ Use on-demand billing for variable workloads
+ Implement S3 lifecycle policies
+ Right-size compute resources
+ Enable CloudWatch cost anomaly detection
+ Review and optimize regularly