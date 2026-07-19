# Deploy the guidance

This solution uses [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") for infrastructure as code deployment. The CDK application synthesizes AWS CloudFormation templates and deploys them through a phase-based approach that ensures proper dependency management.

## Deployment process overview

The guidance deploys in multiple phases with clear dependencies between stacks. You can deploy all phases automatically using the provided Make commands, or deploy individual phases for more control.

**Total deployment time:** 45-65 minutes

**Deployment phases:**

| Phase group                        | Stacks deployed                                                                                                                                                                                 | Duration  |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `phase-foundation`                 | data-processing + `cms-{stage}-storage` + `cms-{stage}-iot` + `cms-{stage}-ui` + `cms-{stage}-msk` + `cms-{stage}-telemetry-integration`                                                        | 15-25 min |
| `phase-streaming`                  | `cms-{stage}-flink` + `cms-{stage}-fleetwise`                                                                                                                                                   | 8-12 min  |
| `phase-seeds`                      | Signal catalog, event catalog, fleet-enrollment seed, FleetWise decoder manifest                                                                                                                | 5-8 min   |
| `phase-services`                   | `cms-{stage}-simulation` + `cms-{stage}-commands` + `cms-{stage}-ws-fanout` + `cms-{stage}-tco`                                                                                                 | 8-15 min  |
| `deploy-bedrock-agents` (optional) | `cms-{stage}-bedrock-agents` — Bedrock supervisor and specialist agents. Not included in `deploy-all`; see [Deploy Bedrock agents (optional)](#deploy-bedrock-agents "#deploy-bedrock-agents"). | 3-5 min   |

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

# Required: password seeded into the Cognito demo user account.
# The CDK synth raises an error if this variable is unset.
export CMS_DEMO_DEFAULT_PASSWORD='YourSecurePassword123!'

# Optional: Set AWS profile if using named profiles
export AWS_PROFILE=your-profile-name
```

### Security context flags

Three CDK context flags control optional demo-permissive behavior. All three default to `false`, which is the production-safe posture. Override only for demonstration environments.

| Flag                         | Default | What it controls                                                                                                                                                                                                                               |
| ---------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cms.allow_self_signup`      | `false` | Enables Cognito User Pool self-registration. When `true`, anyone with an email address can sign up and obtain a JWT. Not recommended for production.                                                                                           |
| `cms.allow_unauth_map_auth`  | `false` | Enables anonymous Identity Pool credentials scoped to Amazon Location Service map tiles. When `true`, the unauthenticated Cognito role is created for anonymous map preview.                                                                   |
| `cms.allow_unauth_websocket` | `false` | Controls WebSocket API `$connect` authorization. When `false` (default), the `$connect` route requires a Cognito JWT (`?token=<jwt>` on the upgrade URL); anonymous upgrades return HTTP 401. When `true`, all WebSocket routes are anonymous. |

To opt in for a demonstration deployment, pass context overrides at synth or deploy time:

```
# Example: enable self-signup and anonymous map for a demo
cdk synth \
  --context cms.allow_self_signup=true \
  --context cms.allow_unauth_map_auth=true
```

Or persist the overrides in your local `cdk.context.json` (this file is gitignored). Do NOT modify `cdk.json` to change the defaults — that file is version-controlled and represents the published reference behavior.

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

For environment-specific wrappers that include pre-flight checks:

```
# Staging (us-west-2)
export CMS_DEMO_DEFAULT_PASSWORD='your-staging-password'
make -C deployment staging-deploy

# Production (us-east-1)
export CMS_DEMO_DEFAULT_PASSWORD='your-prod-password'
make -C deployment prod-deploy
```

###### Warning

This will deploy all stacks without confirmation prompts. Ensure you have reviewed the configuration before running this command.

### Option 3: Phase-by-phase deployment

Deploy using the grouped phase targets that reflect the current Makefile structure:

```
# Phase group 1: Foundation — data-processing + storage + iot + ui + msk + telemetry-integration
make phase-foundation

# Phase group 2: Streaming — flink + fleetwise (order matters)
make phase-streaming

# Phase group 3: Seeds — signal/event catalog + fleet-enrollment + fleetwise decoder
make phase-seeds

# Phase group: Services — simulation + commands + ws-fanout + tco (8-15 minutes)
make phase-services
```

Or deploy individual stacks for finer control:

```
# Data Processing: Signal Catalog + Transform Manifests (2-3 minutes)
make data-processing

# Phase 1: Storage + IoT + UI (5-8 minutes)
make phase1

# Phase 2: Historical demo data seeding (optional, 2-3 minutes)
make phase2

# Phase 3: VPC + MSK + Redis (8-12 minutes)
make phase3

# Phase 3b: Telemetry Integration — IoT to MSK rules + VPC destination (10-15 minutes)
make phase3b

# FleetWise Integration — FWE rules + VPC endpoints (3-5 minutes)
make deploy-fleetwise

# Phase 4: Flink Processing — build JAR + deploy apps (5-7 minutes)
make phase4

# Seed decoder manifest, default campaign, and event catalog (2-3 minutes)
make seed-fleetwise
make seed-event-catalog
make seed-all-demo-data    # Runs all seeders (drivers, vehicles, trips, service, warranty, recalls)
make generate-and-upload-decoder-manifest  # Uploads DecoderManifest.bin to Flink S3 bucket

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

This runs all phase groups in the correct dependency order: `phase-foundation` → `phase-streaming` → `phase-seeds` → `phase-services`.

###### Note

Phases must be deployed in order due to dependencies. `phase-streaming` depends on `phase-foundation` (MSK must exist before Flink can connect to it). `phase-services` can be deployed in any order after `phase-foundation`.

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

###### Note

`phase5` is an optional standalone target for manual or advanced Flink reconfiguration. Its actions are already performed by `phase-streaming` during `make deploy-all`, so a standard deployment does not need to run `phase5` separately. Run it only when you need to reconfigure MSK endpoints or restart Flink applications outside of a full deployment.

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
  --stack-name cms-staging-storage \
  --query 'Stacks[0].StackStatus'
```

All stacks should show `CREATE_COMPLETE` or `UPDATE_COMPLETE` status.

### Access Fleet Manager UI

1. Get the CloudFront URL from stack outputs:

```
aws cloudformation describe-stacks \
  --stack-name cms-staging-ui \
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
  --application-name cms-staging-trip-detection
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
  --stack-name cms-staging-ui \
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

### Container image customization

The simulation service uses two ARM64 container images. By default, `make deploy-simulation` pulls pre-built published images from public ECR — no local container builder is required.

```
# Default: uses published images from public ECR (no local Docker needed)
make -C deployment deploy-simulation DEPLOYMENT_STAGE=dev AWS_REGION=us-east-1
```

To use images from your own registry, set `PUBLIC_ECR_REGISTRY` and `PUBLIC_ECR_TAG`:

```
# Point to a custom registry and tag
PUBLIC_ECR_REGISTRY=123456789012.dkr.ecr.us-east-1.amazonaws.com \
PUBLIC_ECR_TAG=v1.2.3 \
  make -C deployment deploy-simulation DEPLOYMENT_STAGE=dev AWS_REGION=us-east-1
```

For local development builds (when actively modifying simulation Dockerfiles), use `SIM_IMAGE_MODE=asset` to build images locally instead of pulling from a registry. This requires a local container builder such as Docker, Finch, or Podman.

```
# Build images locally (requires Docker, Finch, or Podman)
SIM_IMAGE_MODE=asset CDK_DOCKER=finch \
  make -C deployment deploy-simulation DEPLOYMENT_STAGE=dev AWS_REGION=us-east-1
```

###### Note

`SIM_IMAGE_MODE=asset` is intended for active Dockerfile development only. Standard deployments should use the default published images to avoid a dependency on a local container builder.

### Deploy Bedrock agents (optional)

The Bedrock multi-agent stack (`cms-{stage}-bedrock-agents`) deploys a supervisor agent and specialist agents powered by Amazon Bedrock. This stack is intentionally excluded from `make deploy-all` because it incurs additional Amazon Bedrock inference costs. Customers who do not need the in-UI conversational assistant can skip this step entirely.

To deploy the Bedrock agents stack after the core deployment completes:

```
make -C deployment deploy-bedrock-agents DEPLOYMENT_STAGE=dev AWS_REGION=us-east-1
```

To tear down the Bedrock agents stack independently without affecting other stacks:

```
# Replace {stage} with your deployment stage (dev, staging, or prod)
cdk destroy cms-staging-bedrock-agents --require-approval never
```

###### Note

Amazon Bedrock inference costs depend on usage volume and the number of agent hops per conversation turn. Review the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") before deploying. If the `cms-{stage}-bedrock-agents` stack has not been deployed, the in-UI conversational assistant feature is unavailable but all other Fleet Manager functionality operates normally.

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
  --stack-name cms-staging-storage \
  --max-items 20
```

2. Review error messages in CloudWatch Logs
3. Verify service quotas are sufficient
4. Delete failed stack and retry:

```
aws cloudformation delete-stack --stack-name cms-staging-storage
make phase-foundation
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
aws logs tail /aws/kinesis-analytics/cms-staging-trip-detection --follow
```

2. Verify MSK cluster is accessible
3. Verify DynamoDB tables exist
4. Restart application:

```
aws kinesisanalyticsv2 start-application \
  --application-name cms-staging-trip-detection
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
