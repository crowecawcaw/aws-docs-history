# Deploy the guidance

This solution uses [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") for infrastructure as code deployment. The CDK application synthesizes AWS CloudFormation templates and deploys them through a phase-based approach that ensures proper dependency management.

## Deployment process overview

The guidance deploys in multiple phases with clear dependencies between stacks. You can deploy all phases automatically using the provided Make commands, or deploy individual phases for more control.

**Total deployment time:** 45-65 minutes

**Deployment phases:**

- Data Processing: Signal Catalog + Transform Manifests (2-3 minutes)
- Phase 1: Storage + IoT + UI (5-8 minutes)
- Phase 3: VPC + MSK + Redis (8-12 minutes)
- Phase 3b: Telemetry Integration (10-15 minutes)
- FleetWise: FWE Rules + VPC Endpoints (3-5 minutes)
- Phase 4: Flink Processing (5-7 minutes)
- Seeding: Decoder Manifest + Campaign + Event Catalog (2-3 minutes)
- Phase 5: Pipeline Configuration (3-5 minutes)
- Simulation: ECS Cloud Simulation — Fargate for MQTT Direct, EC2 for FleetWise Edge (3-5 minutes)
- Commands: Remote Commands + Geofences (2-3 minutes)

Before you launch, review the [cost](plan-your-deployment.md#cost "plan-your-deployment.md#cost"), [architecture](architecture-overview.md "architecture-overview.md"), [security](security.md "security.md"), and other considerations discussed earlier in this guide.

###### Important

Before deploying, review the [cost](plan-your-deployment.md#cost "plan-your-deployment.md#cost"), [architecture](architecture-overview.md "architecture-overview.md"), and [security](security.md "security.md") considerations discussed earlier in this guide.

## Prerequisites

Before deploying, ensure you have the following prerequisites installed and configured:

**Required software:**

- [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") - Command line tool for AWS
- [Node.js 18.x or later](https://nodejs.org/ "https://nodejs.org/") - JavaScript runtime
- [Python 3.9 or later](https://www.python.org/downloads/ "https://www.python.org/downloads/") - Python runtime
- [AWS CDK v2.100.0 or later](../../../cdk/v2/guide/getting_started.md "../../../cdk/v2/guide/getting_started.md") - Infrastructure as code framework
- [Make](https://www.gnu.org/software/make/ "https://www.gnu.org/software/make/") - Build automation tool
- [Git](https://git-scm.com/ "https://git-scm.com/") - Version control system

**AWS account requirements:**

- An AWS account with appropriate permissions to create resources
- AWS credentials configured (via `aws configure` or environment variables)
- Sufficient service quotas for the resources being deployed

**Installation commands for Amazon Linux 2023:**

```
# Install Node.js
sudo dnf install -y nodejs npm

# Install Python and pip
sudo dnf install -y python3 python3-pip

# Install AWS CLI v2
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Install AWS CDK
npm install -g aws-cdk

# Verify installations
aws --version
node --version
python3 --version
cdk --version
```

**Installation commands for macOS:**

```
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required tools
brew install node python aws-cdk awscli

# Verify installations
aws --version
node --version
python3 --version
cdk --version
```

## Step 1: Clone the repository

Clone the repository from GitHub:

```
git clone https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws.git
cd guidance-for-connected-mobility-on-aws
```

## Step 2: Configure deployment

Set environment variables for your deployment:

```
# Set deployment stage (dev, staging, or prod)
export DEPLOYMENT_STAGE=dev

# Set AWS region
export AWS_REGION=us-east-1

# Optional: Set AWS profile if using named profiles
export AWS_PROFILE=your-profile-name
```

You can also create a `.env` file in the deployment directory:

```
cd deployment
cat > .env << EOF
DEPLOYMENT_STAGE=dev
AWS_REGION=us-east-1
AWS_PROFILE=your-profile-name
EOF
```

## Step 3: Install dependencies

Install Python and Node.js dependencies:

```
cd deployment

# Install Python dependencies
make install

# This command will:
# - Create a Python virtual environment
# - Install CDK dependencies
# - Install required Python packages
```

## Step 4: Bootstrap CDK

Bootstrap your AWS account for CDK deployment (required once per account/region):

```
make bootstrap

# Or manually:
cdk bootstrap aws://ACCOUNT-ID/REGION
```

The bootstrap process creates an S3 bucket and other resources needed for CDK deployments.

###### Note

If you’ve already bootstrapped CDK in this account and region, you can skip this step.

## Step 5: Deploy the guidance

You have two deployment options:

### Option 1: Interactive deployment (recommended)

Deploy all phases interactively with prompts:

```
make deploy
```

This command will:

1. Display deployment configuration
2. Prompt for confirmation before each phase
3. Deploy phases in the correct order
4. Display progress and outputs
5. Provide next steps after completion

### Option 2: Automated deployment

Deploy all phases automatically without prompts:

```
make deploy-all
```

###### Warning

This will deploy all stacks without confirmation prompts. Ensure you’ve reviewed the configuration before running this command.

### Option 3: Phase-by-phase deployment

Deploy individual phases for more control:

```
# Data Processing: Signal Catalog + Transform Manifests (2-3 minutes)
make data-processing

# Phase 1: Storage + IoT + UI (5-8 minutes)
make phase1

# Phase 2: Historical demo data seeding (optional, 2-3 minutes)
make phase2

# Phase 3: VPC + MSK + Redis (8-12 minutes)
make phase3

# Phase 3b: Telemetry Integration — IoT → MSK rules + VPC destination (10-15 minutes)
make phase3b

# FleetWise Integration — FWE rules + VPC endpoints (3-5 minutes)
make deploy-fleetwise

# Phase 4: Flink Processing — build JAR + deploy apps (5-7 minutes)
make phase4

# Seed decoder manifest, default campaign, and event catalog (2-3 minutes)
make seed-fleetwise
make seed-event-catalog
make seed-all-demo-data    # Runs all seeders (drivers, vehicles, trips, service, warranty, recalls)
make upload-decoder-manifest  # Uploads DecoderManifest.bin to Flink S3 bucket

# Phase 5: Pipeline Configuration — MSK bootstrap + IAM auth (3-5 minutes)
make phase5

# Cloud Simulation — ECS cluster (Fargate + EC2) + Lambda orchestrator (3-5 minutes)
make deploy-simulation

# Remote Commands — Commands Lambda + Response Handler + IoT Rules (2-3 minutes)
make deploy-commands
```

Or deploy everything at once (recommended):

```
make deploy-all
```

This runs all phases in the correct dependency order: `data-processing → phase1 → phase3 → phase3b → deploy-fleetwise → phase4 → seed-fleetwise → seed-event-catalog → phase5 → deploy-simulation → deploy-commands`.

###### Note

Phases must be deployed in order due to dependencies. `phase3b` depends on `phase3` (MSK must exist before IoT Rules can route to it). `phase4` depends on `phase3b` (Flink needs MSK connectivity). `deploy-simulation` and `deploy-commands` can run in any order after `phase1`.

## Deployment phases detail

### Data Processing: Signal Catalog + Transform Manifests

**Make target:**
`make data-processing`

**Resources created:**

- Signal catalog DynamoDB table seeded with 260 signals (75 original + 185 expanded)
- Transform manifest configuration for OEM telemetry integration
- Signal catalog JSON uploaded to S3

**Duration:** 2-3 minutes

### Phase 1: Storage + IoT + UI

**Make target:**
`make phase1`

**Stacks deployed:**

- `cms-{stage}-storage` — DynamoDB tables and S3 buckets
- `cms-{stage}-iot` — IoT Core configuration and fleet management
- `cms-{stage}-ui` — Fleet Manager web application

**Resources created:**

- DynamoDB tables: vehicles, trips, alerts, drivers, safety events, maintenance alerts, telemetry, signal catalog, commands, geofences, simulations
- S3 buckets: telemetry archive, UI assets
- IoT Core: thing types, policies, certificate management
- CloudFront distribution for React application
- API Gateway REST API with Lambda backend
- Cognito user pool and identity pool
- Amazon Location Service map and place index
- IAM roles and policies

**Duration:** 5-8 minutes

### Phase 3: VPC + MSK + Redis

**Make target:**
`make phase3`

**Stacks deployed:**

- `cms-{stage}-infrastructure` — VPC and caching
- `cms-{stage}-msk` — Kafka cluster

**Resources created:**

- VPC with public and private subnets (2 AZs)
- NAT Gateway (2 AZs)
- ElastiCache for Redis cluster
- MSK cluster (3 brokers)
- Kafka topics: cms-telemetry-raw, cms-telemetry-preprocessed, cms-telemetry-trips, cms-telemetry-safety, cms-telemetry-maintenance, cms-alerts, fw-telemetry-raw, fw-checkin, cms-telemetry-oem
- Security groups

**Duration:** 8-12 minutes

### Phase 3b: Telemetry Integration

**Make target:**
`make phase3b`

**Stacks deployed:**

- `cms-{stage}-telemetry-integration` — IoT to MSK bridge

**Resources created:**

- IoT Rule for MQTT Direct telemetry (`cms/telemetry/+` → `cms-telemetry-raw`)
- VPC Destination for IoT Core to MSK connectivity
- IAM roles for IoT Rules
- IAM role for VPC Destination includes Secrets Manager access (to retrieve MSK SCRAM credentials)
- S3 backup for raw telemetry

**Duration:** 10-15 minutes

### FleetWise Integration

**Make target:**
`make deploy-fleetwise`

**Stacks deployed:**

- `cms-{stage}-fleetwise` — FleetWise IoT Rules and VPC endpoints

**Resources created:**

- IoT Rule for FleetWise telemetry (`cms/fleetwise/vehicles/+/signals` → `fw-telemetry-raw`)
- IoT Rule for FleetWise checkins (`cms/fleetwise/vehicles/+/checkins` → `fw-checkin`)
- S3 backup for FleetWise telemetry
- VPC endpoints for FleetWise connectivity

**Duration:** 3-5 minutes

### Phase 4: Flink Processing

**Make target:**
`make phase4`

**Stacks deployed:**

- `cms-{stage}-flink` — Stream processing applications

**Resources created:**

- Flink JAR built from `modules/flink/` and uploaded to S3
- 10 Managed Apache Flink applications: SimulatorPreprocessor, EventDrivenTelemetryProcessor, TelemetryProcessor, TripProcessor, SafetyProcessor, MaintenanceProcessor, FWTelemetryProcessor, CampaignSyncProcessor, GeofenceProcessor, OEMTelemetryProcessor
- CloudWatch log groups for each application
- CloudWatch alarms for downtime and idle processing
- IAM roles for Flink (MSK, DynamoDB, Redis, IoT Core, S3 access)

**Duration:** 5-7 minutes

### Data Seeding

**Make targets:**
`make seed-fleetwise` and `make seed-event-catalog`

**Resources seeded:**

- Decoder manifest in DynamoDB — maps 260 CAN signal IDs to VSS signal names
- Default campaign — collects all 260 signals from all vehicles
- Event catalog — safety event rules (10 types) and maintenance alert rules (10+ types) with thresholds
- DecoderManifest.bin uploaded to S3 — the Flink CampaignSyncProcessor reads the protobuf decoder manifest from `s3://{flink-jar-bucket}/fwe-config/DecoderManifest.bin` and delivers it to FWE agents on checkin

**Duration:** 2-3 minutes

### Phase 5: Pipeline Configuration

**Make target:**
`make phase5`

**Actions performed:**

- Configures MSK bootstrap server endpoints in all Flink application runtime properties
- Configures IAM authentication for MSK connectivity
- Starts all Flink applications

**Duration:** 3-5 minutes

### Cloud Simulation

**Make target:**
`make deploy-simulation`

**Stacks deployed:**

- `cms-{stage}-simulation` — ECS simulation infrastructure (Fargate + EC2-backed)

**Resources created:**

- ECS cluster for simulation workers
- Task definitions: `sim-worker` (Fargate, MQTT Direct), `fwe-agent` (EC2, FleetWise agent), `fwe-simulator` (EC2, Python simulator)
- Docker image built from `services/simulation/` and pushed to ECR
- Lambda function for simulation API orchestration
- API Gateway routes for `/api/simulation/*`
- DynamoDB table for simulation state tracking
- CloudWatch log group for worker tasks

**Duration:** 3-5 minutes

### Remote Commands

**Make target:**
`make deploy-commands`

**Stacks deployed:**

- `cms-{stage}-commands` — Remote commands infrastructure

**Resources created:**

- Commands Lambda function (send commands, command history, command catalog, geofence CRUD)
- Command Response Handler Lambda function
- IoT Rule on `cms/commands/+/response` to trigger response handler
- API Gateway routes for `/api/commands/` and `/api/geofences/`
- DynamoDB tables: commands, geofences (if not already created in Phase 1)

**Duration:** 2-3 minutes

## Step 6: Verify deployment

After deployment completes, verify the installation:

### Check stack status

```
# Check all stack statuses
make status

# Or use AWS CLI
aws cloudformation describe-stacks \
  --stack-name cms-dev-storage \
  --query 'Stacks[0].StackStatus'
```

All stacks should show `CREATE_COMPLETE` or `UPDATE_COMPLETE` status.

### Access Fleet Manager UI

1. Get the CloudFront URL from stack outputs:

```
aws cloudformation describe-stacks \
  --stack-name cms-dev-ui \
  --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' \
  --output text
```

2. Open the URL in your web browser
3. Sign up for a new account or sign in with existing credentials
4. Verify you can access the Fleet Manager dashboard

### Verify IoT connectivity

1. Get IoT endpoint:

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

2. Test MQTT connection using the vehicle simulator (see [Verify deployment](#step-6-verify-deployment "#step-6-verify-deployment"))

### Verify Flink applications

```
# List Kinesis Data Analytics applications
aws kinesisanalyticsv2 list-applications

# Check application status
aws kinesisanalyticsv2 describe-application \
  --application-name cms-dev-trip-detection
```

Applications should show `RUNNING` status.

## Deployment outputs

After successful deployment, the following outputs are available:

| Output              | Description                       | Stack                      |
| ------------------- | --------------------------------- | -------------------------- |
| CloudFrontURL       | Fleet Manager web application URL | cms-{stage}-ui             |
| UserPoolId          | Cognito user pool ID              | cms-{stage}-ui             |
| IdentityPoolId      | Cognito identity pool ID          | cms-{stage}-ui             |
| ApiGatewayUrl       | REST API endpoint                 | cms-{stage}-ui             |
| IoTEndpoint         | IoT Core data endpoint            | cms-{stage}-iot            |
| MSKClusterArn       | MSK cluster ARN                   | cms-{stage}-msk            |
| VehicleTableName    | DynamoDB vehicles table           | cms-{stage}-storage        |
| TripTableName       | DynamoDB trips table              | cms-{stage}-storage        |
| AlertTableName      | DynamoDB alerts table             | cms-{stage}-storage        |
| ElastiCacheEndpoint | Redis cache endpoint              | cms-{stage}-infrastructure |

View all outputs:

```
# View outputs for a specific stack
aws cloudformation describe-stacks \
  --stack-name cms-dev-ui \
  --query 'Stacks[0].Outputs'

# Or use CDK
cdk outputs --all
```

## Customizing the deployment

### Modify stack configuration

Edit the CDK application file to customize resources:

```
# Edit main CDK app
vi deployment/app.py

# Edit individual stacks
vi deployment/stacks/storage_stack.py
vi deployment/stacks/msk_stack.py
# etc.
```

### Change deployment stage

Deploy to different environments:

```
# Deploy to staging
DEPLOYMENT_STAGE=staging make deploy

# Deploy to production
DEPLOYMENT_STAGE=prod make deploy
```

### Use existing VPC

To use an existing VPC instead of creating a new one:

```
# Set VPC ID environment variable
export VPC_ID=vpc-xxxxx

# Deploy without creating VPC
make deploy
```

### Use existing MSK cluster

To use an existing MSK cluster:

```
# Set MSK cluster ARN
export MSK_CLUSTER_ARN=arn:aws:kafka:region:account:cluster/name/uuid

# Deploy without creating MSK
make deploy
```

## Troubleshooting deployment

### CDK bootstrap fails

**Problem:** Bootstrap command fails with permissions error

**Solution:**

```
# Verify AWS credentials
aws sts get-caller-identity

# Ensure you have AdministratorAccess or equivalent
# Bootstrap with explicit account and region
cdk bootstrap aws://ACCOUNT-ID/REGION
```

### Stack deployment fails

**Problem:** Stack creation fails with resource errors

**Solution:**

1. Check CloudFormation events:

```
aws cloudformation describe-stack-events \
  --stack-name cms-dev-storage \
  --max-items 20
```

2. Review error messages in CloudWatch Logs
3. Verify service quotas are sufficient
4. Delete failed stack and retry:

```
aws cloudformation delete-stack --stack-name cms-dev-storage
make phase1
```

### MSK cluster creation timeout

**Problem:** MSK cluster takes longer than expected

**Solution:**

- MSK cluster creation typically takes 8-12 minutes
- Wait for completion before proceeding to Phase 4
- Check cluster status:

```
aws kafka describe-cluster --cluster-arn CLUSTER-ARN
```

### Flink application fails to start

**Problem:** Kinesis Data Analytics application shows FAILED status

**Solution:**

1. Check CloudWatch Logs for error messages:

```
aws logs tail /aws/kinesis-analytics/cms-dev-trip-detection --follow
```

2. Verify MSK cluster is accessible
3. Verify DynamoDB tables exist
4. Restart application:

```
aws kinesisanalyticsv2 start-application \
  --application-name cms-dev-trip-detection
```

### Insufficient permissions

**Problem:** Deployment fails due to IAM permissions

**Solution:**

Ensure your IAM user or role has the following permissions:

- CloudFormation: Full access
- IAM: Create/update roles and policies
- S3: Create/manage buckets
- DynamoDB: Create/manage tables
- IoT: Full access
- MSK: Full access
- Kinesis Data Analytics: Full access
- Lambda: Create/update functions
- API Gateway: Create/manage APIs
- Cognito: Create/manage user pools
- Location Service: Create/manage resources
- CloudFront: Create/manage distributions
- ElastiCache: Create/manage clusters
- VPC: Create/manage networking resources

## Next steps

After successful deployment:

1. [Run the vehicle simulator](simulation-platform.md "simulation-platform.md") to generate test data
2. Access the Fleet Manager UI to view vehicles and trips
3. Configure alert subscriptions for maintenance notifications
4. Integrate with your existing systems using the REST API
5. Review CloudWatch metrics and alarms for operational monitoring
6. Explore [customization options](developer-guide.md "developer-guide.md") for your use case

## Additional resources

- [GitHub Repository](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws")
- [AWS CDK Documentation](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
- [AWS IoT Core Documentation](../../../iot/latest/developerguide/what-is-aws-iot.md "../../../iot/latest/developerguide/what-is-aws-iot.md")
- [Amazon MSK Documentation](../../../msk/latest/developerguide/what-is-msk.md "../../../msk/latest/developerguide/what-is-msk.md")
- [Kinesis Data Analytics Documentation](../../../kinesisanalytics/latest/java/what-is.md "../../../kinesisanalytics/latest/java/what-is.md")
