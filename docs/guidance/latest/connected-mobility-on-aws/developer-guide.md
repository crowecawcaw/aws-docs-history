# Developer guide

This section provides guidance for customizing and extending the Guidance for Connected Mobility on AWS using AWS CDK, developing Flink applications, extending the Fleet Manager UI, and integrating with external systems.

## Source code

Visit our [GitHub repository](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws") to download the source files for this solution and to share your customizations with others.

The solution uses [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") for infrastructure as code. See the [README.md](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws/blob/main/README.md "https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws/blob/main/README.md") file for additional information.

## Development environment setup

### Prerequisites

- AWS CLI v2
- Node.js 18.x or later
- Python 3.9 or later
- AWS CDK v2.100.0 or later
- Git
- IDE (VS Code, PyCharm, or IntelliJ recommended)

### Clone and setup

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

```
guidance-for-connected-mobility-on-aws/
├── deployment/
│   ├── app.py                          # CDK application entry point
│   ├── stacks/                         # CDK stack definitions
│   │   ├── commands_stack.py           # Remote vehicle commands API
│   │   ├── data_processing_stack.py    # Signal catalog and transform manifests
│   │   ├── fleetwise_stack.py          # FleetWise Edge integration
│   │   ├── flink_stack.py              # Flink stream processing applications
│   │   ├── infrastructure_stack.py     # VPC, subnets, networking
│   │   ├── iot_stack.py                # Fleet management IoT components
│   │   ├── msk_stack.py                # MSK cluster, VPC, and ElastiCache
│   │   ├── oem_processor_stack.py      # OEM telemetry ingestion
│   │   ├── predictive_agent_stack.py   # Predictive maintenance AI agent
│   │   ├── simulation_stack.py         # ECS Fargate vehicle simulator
│   │   ├── storage_stack.py            # DynamoDB tables
│   │   ├── telemetry_integration_stack.py  # MSK-IoT connectivity
│   │   └── ui_stack.py                 # Frontend, API Gateway, Cognito
│   ├── Makefile                        # Deployment automation
│   └── requirements.txt
├── modules/
│   ├── campaign_manager/               # FleetWise campaign management
│   ├── cms_ui/                         # React frontend application
│   │   └── source/
│   │       ├── frontend/               # React app (Cloudscape Design)
│   │       └── handlers/               # API Lambda handlers
│   ├── flink/                          # Java Flink processors
│   └── oem_ingestion/                  # OEM data ingestion consumer
├── services/
│   ├── commands/                       # Remote commands Lambda + protobuf
│   ├── data_processing/                # Data processing service
│   └── simulation/                     # Vehicle simulation service
├── scripts/                            # Utility scripts
└── tests/e2e/                          # End-to-end tests
```

## CDK stacks

The solution is deployed as a set of modular CDK stacks defined in `deployment/app.py`. Each stack can be deployed independently based on your requirements.

### Stack overview

| Stack                       | Purpose                                                                                                          | Condition                                     |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `DataProcessingStack`       | Signal catalog and transform manifests                                                                           | Always deployed                               |
| `StorageStack`              | DynamoDB tables for vehicles, trips, telemetry, safety events, maintenance alerts, drivers, and more             | Always deployed                               |
| `MSKStack`                  | VPC, Amazon MSK (Kafka) cluster, and ElastiCache for Redis                                                       | Deployed unless `MSK_CLUSTER_ARN` is provided |
| `IoTStack`                  | Fleet management IoT components                                                                                  | Always deployed                               |
| `TelemetryIntegrationStack` | MSK-IoT connectivity (IoT rules, VPC destinations)                                                               | `DEPLOY_TELEMETRY_INTEGRATION=true`           |
| `FlinkStack`                | Flink stream processing applications (trip detection, safety, maintenance, telemetry, FWE decode, campaign sync) | Always deployed                               |
| `FleetWiseStack`            | FleetWise Edge IoT rules, VPC endpoints, CampaignSyncProcessor                                                   | `DEPLOY_FLEETWISE=true`                       |
| `UIStack`                   | React frontend (Cloudscape Design), API Gateway, Cognito authentication, Amazon Location Service                 | Always deployed                               |
| `CommandsStack`             | Remote vehicle commands API via IoT Core MQTT, geofence management                                               | Always deployed                               |
| `PredictiveAgentStack`      | Predictive maintenance AI agent                                                                                  | `DEPLOY_PREDICTIVE_AGENT=true`                |
| `SimulationStack`           | ECS Fargate vehicle simulation service                                                                           | `DEPLOY_SIMULATION=true`                      |

### Customizing stacks

Stack definitions are in `deployment/stacks/`. Each stack is a Python class that extends `Stack`.

#### Example: Modify MSK configuration

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

### Flink project structure

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

The TripProcessor demonstrates a key pattern for reducing DynamoDB costs in stream processing: using Flink’s keyed state to eliminate per-message database reads.

**Problem:** A stateless trip processor queries DynamoDB on every telemetry message to find the active trip, check its status, and update the record. For a 20-message trip, this results in ~60 reads and 20 full-record writes.

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

### UI project structure

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

The UI is built with [Cloudscape Design System](https://cloudscape.design/ "https://cloudscape.design/") and deployed via CloudFront with S3 origin. Authentication is handled by Amazon Cognito.

### Example: Add a new page

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

The solution exposes two API Gateway endpoints: the Fleet Management API (deployed by `UIStack`) and the Commands API (deployed by `CommandsStack`).

### Authentication

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

The Fleet Management API is served from the UI stack’s API Gateway endpoint. All endpoints are prefixed with `/api/v1/`.

#### Fleet endpoints

| Method | Path                                | Description              |
| ------ | ----------------------------------- | ------------------------ |
| `GET`  | `/api/v1/fleets`                    | List all fleets          |
| `POST` | `/api/v1/fleets`                    | Create a new fleet       |
| `GET`  | `/api/v1/fleets/{fleetId}`          | Get fleet details        |
| `GET`  | `/api/v1/fleets/{fleetId}/vehicles` | List vehicles in a fleet |

#### Vehicle endpoints

| Method | Path                                              | Description                           |
| ------ | ------------------------------------------------- | ------------------------------------- |
| `GET`  | `/api/v1/vehicles`                                | List all vehicles                     |
| `POST` | `/api/v1/vehicles`                                | Register a new vehicle                |
| `GET`  | `/api/v1/vehicles/locations`                      | Get all vehicle locations             |
| `GET`  | `/api/v1/vehicles/{vehicleId}`                    | Get vehicle details                   |
| `GET`  | `/api/v1/vehicles/{vehicleId}/trips`              | List trips for a vehicle              |
| `GET`  | `/api/v1/vehicles/{vehicleId}/trips/{tripId}`     | Get trip details                      |
| `GET`  | `/api/v1/vehicles/{vehicleId}/safety-alerts`      | List safety alerts for a vehicle      |
| `GET`  | `/api/v1/vehicles/{vehicleId}/maintenance-alerts` | List maintenance alerts for a vehicle |

#### Global endpoints

| Method | Path                                 | Description                 |
| ------ | ------------------------------------ | --------------------------- |
| `GET`  | `/api/v1/trips`                      | List all trips              |
| `GET`  | `/api/v1/safety-alerts`              | List all safety alerts      |
| `GET`  | `/api/v1/maintenance-alerts`         | List all maintenance alerts |
| `GET`  | `/api/v1/dashboard/metrics`          | Get dashboard metrics       |
| `GET`  | `/api/v1/dashboard/fleet-comparison` | Get fleet comparison data   |

#### Real-time endpoints

| Method | Path                     | Description                                |
| ------ | ------------------------ | ------------------------------------------ |
| `GET`  | `/realtime/vehicles`     | Get real-time vehicle data from Redis      |
| `GET`  | `/realtime/trips`        | Get real-time trip data from Redis         |
| `GET`  | `/health`                | API health check                           |
| `GET`  | `/discover-iot-endpoint` | Get IoT Core endpoint for MQTT connections |

### Commands API

The Commands API enables sending remote commands to vehicles via IoT Core MQTT and managing geofences. It is served from a separate API Gateway endpoint deployed by the `CommandsStack`.

#### Command endpoints

| Method | Path                        | Description                        |
| ------ | --------------------------- | ---------------------------------- |
| `POST` | `/api/commands/{vehicleId}` | Send a command to a vehicle        |
| `GET`  | `/api/commands/{vehicleId}` | Get command history for a vehicle  |
| `GET`  | `/api/commands/catalog`     | List available actuatable commands |

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

| Method   | Path                         | Description                    |
| -------- | ---------------------------- | ------------------------------ |
| `POST`   | `/api/geofences`             | Create a geofence              |
| `GET`    | `/api/geofences/{vehicleId}` | List geofences for a vehicle   |
| `DELETE` | `/api/geofences/{vehicleId}` | Delete (deactivate) a geofence |

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

When a vehicle responds to a command, the response flows through an IoT Rule that matches the topic `cms/commands/+/response`. The rule invokes the `command_response_handler` Lambda, which updates the command status in DynamoDB.

## Testing and debugging

### Test UI locally

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

```
cd deployment
make status
```

## GSI and ISV integration

Global system integrators (GSIs) and independent software vendors (ISVs) can leverage this guidance to build and deploy mobility services quickly and efficiently.

### White-labeling

#### Customize branding

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

GSIs and ISVs can extend this guidance by:

- Adding custom Flink applications for specialized processing
- Integrating with third-party telematics providers
- Building custom dashboards and reports
- Implementing additional API endpoints
- Adding machine learning models for predictive analytics

## Best practices

### Infrastructure as code

- Use CDK constructs for reusable components
- Parameterize stack configurations
- Use environment variables for secrets
- Tag all resources consistently
- Enable CloudFormation stack protection

### Security

- Follow least-privilege IAM policies
- Enable encryption at rest and in transit
- Rotate credentials regularly
- Use AWS Secrets Manager for sensitive data
- Enable CloudTrail logging

### Performance

- Right-size MSK brokers based on throughput
- Optimize Flink parallelism
- Use ElastiCache for frequently accessed data
- Enable DynamoDB auto-scaling
- Implement API caching

### Cost optimization

- Use on-demand billing for variable workloads
- Implement S3 lifecycle policies
- Right-size compute resources
- Enable CloudWatch cost anomaly detection
- Review and optimize regularly
