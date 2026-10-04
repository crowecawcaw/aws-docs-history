

# Deploy the guidance
<a name="deploy-the-solution"></a>

This solution uses [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) for infrastructure as code deployment. The CDK application synthesizes AWS CloudFormation templates and deploys them through a phase-based approach that ensures proper dependency management.

## Deployment process overview
<a name="deployment-process-overview"></a>

The guidance deploys in multiple phases with clear dependencies between stacks. You can deploy all phases automatically using the provided Make commands, or deploy individual phases for more control.

 **Total deployment time:** 45-65 minutes

 **Deployment phases:** 


| Phase group | Stacks deployed | Duration | 
| --- | --- | --- | 
|  `phase-foundation`  | data-processing \+ `cms-{stage}-storage` \+ `cms-{stage}-iot` \+ `cms-{stage}-ui` \+ `cms-{stage}-msk` \+ `cms-{stage}-telemetry-integration` \+ `cms-{stage}-fleet-intelligence-analytics`  | 15-25 min | 
|  `phase-streaming`  |  `cms-{stage}-flink` \+ `cms-{stage}-fleetwise`  | 8-12 min | 
|  `phase-seeds`  | Signal catalog, event catalog, fleet-enrollment seed, FleetWise decoder manifest | 5-8 min | 
|  `phase-services`  |  `cms-{stage}-simulation` \+ `cms-{stage}-commands` \+ `cms-{stage}-ws-fanout`  | 8-15 min | 

Before you launch, review the [cost](plan-your-deployment.md#cost), [architecture](architecture-overview.md), [security](security.md), and other considerations discussed earlier in this guide.

**Important**  
Before deploying, review the [cost](plan-your-deployment.md#cost), [architecture](architecture-overview.md), and [security](security.md) considerations discussed earlier in this guide.

## Prerequisites
<a name="prerequisites-deploy"></a>

Before deploying, ensure you have the following prerequisites installed and configured:

 **Required software:** 
+  [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) - Command line tool for AWS
+  [Node.js 18.x or later](https://nodejs.org/) - JavaScript runtime
+  [Python 3.9 or later](https://www.python.org/downloads/) - Python runtime
+  [AWS CDK v2.100.0 or later](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) - Infrastructure as code framework
+  [Make](https://www.gnu.org/software/make/) - Build automation tool
+  [Git](https://git-scm.com/) - Version control system

 **AWS account requirements:** 
+ An AWS account with appropriate permissions to create resources
+ AWS credentials configured (via `aws configure` or environment variables)
+ Sufficient service quotas for the resources being deployed

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
<a name="step-1-clone-the-repository"></a>

Clone the repository from GitHub:

```
git clone https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws.git
cd guidance-for-connected-mobility-on-aws
```

## Step 2: Configure deployment
<a name="step-2-configure-deployment"></a>

Set environment variables for your deployment:

**Note**  
This guidance now ships as a single-environment deployment. The former `cms-prod- ` stack lineage in `us-east-1` was removed as part of the v0.4.0 release; `staging` is the canonical deploy target and its stacks (`cms-staging-`) are what the Makefile targets described below act on. See the CMS `CHANGELOG.md` v0.4.0 "Breaking" entry for the env-collapse background.

```
# Set deployment stage (staging is the canonical target)
export DEPLOYMENT_STAGE=staging

# Set AWS region (staging deploys to us-west-2 by convention;
# any AWS Region supported by the required services is valid)
export AWS_REGION=us-west-2

# Required: password seeded into the Cognito demo user account.
# The CDK synth raises an error if this variable is unset.
export CMS_DEMO_DEFAULT_PASSWORD='YourSecurePassword123!'

# Optional: Set AWS profile if using named profiles
export AWS_PROFILE=your-profile-name
```

### Security context flags
<a name="security-context-flags"></a>

Three CDK context flags control optional demo-permissive behavior. All three default to `false`, which is the production-safe posture. Override only for demonstration environments.


| Flag | Default | What it controls | 
| --- | --- | --- | 
|  `cms.allow_self_signup`  |  `false`  | Enables Cognito User Pool self-registration. When `true`, anyone with an email address can sign up and obtain a JWT. Not recommended for production. | 
|  `cms.allow_unauth_map_auth`  |  `false`  | Enables anonymous Identity Pool credentials scoped to Amazon Location Service map tiles. When `true`, the unauthenticated Cognito role is created for anonymous map preview. | 
|  `cms.allow_unauth_websocket`  |  `false`  | Controls WebSocket API `$connect` authorization. When `false` (default), the `$connect` route requires a Cognito JWT (`?token=<jwt>` on the upgrade URL); anonymous upgrades return HTTP 401. When `true`, all WebSocket routes are anonymous. | 

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
DEPLOYMENT_STAGE=staging
AWS_REGION=us-west-2
AWS_PROFILE=your-profile-name
EOF
```

## Step 3: Install dependencies
<a name="step-3-install-dependencies"></a>

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
<a name="step-4-bootstrap-cdk"></a>

Bootstrap your AWS account for CDK deployment (required once per account/region):

```
make bootstrap

# Or manually:
cdk bootstrap aws://ACCOUNT-ID/REGION
```

The bootstrap process creates an S3 bucket and other resources needed for CDK deployments.

**Note**  
If you’ve already bootstrapped CDK in this account and region, you can skip this step.

## Step 5: Deploy the guidance
<a name="step-5-deploy-the-solution"></a>

You have two deployment options:

### Option 1: Interactive deployment (recommended)
<a name="option-1-interactive-deployment-recommended"></a>

Deploy all phases interactively with prompts:

```
make deploy
```

This command will:

1. Display deployment configuration

1. Prompt for confirmation before each phase

1. Deploy phases in the correct order

1. Display progress and outputs

1. Provide next steps after completion

### Option 2: Automated deployment
<a name="option-2-automated-deployment"></a>

Deploy all phases automatically without prompts:

```
make deploy-all
```

For the environment-specific wrapper with pre-flight checks:

```
# Staging (us-west-2)
export CMS_DEMO_DEFAULT_PASSWORD='your-staging-password'
make -C deployment staging-deploy
```

**Warning**  
This will deploy all stacks without confirmation prompts. Ensure you have reviewed the configuration before running this command.

### Option 3: Phase-by-phase deployment
<a name="option-3-phase-by-phase-deployment"></a>

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

**Note**  
Phases must be deployed in order due to dependencies. `phase-streaming` depends on `phase-foundation` (MSK must exist before Flink can connect to it). `phase-services` can be deployed in any order after `phase-foundation`.

## Deployment phases detail
<a name="deployment-phases-detail"></a>

### Data Processing: Signal Catalog \+ Transform Manifests
<a name="phase-data-processing"></a>

 **Make target:** `make data-processing` 

 **Resources created:** 
+ Signal catalog DynamoDB table seeded with 260 signals (75 original \+ 185 expanded)
+ Transform manifest configuration for OEM telemetry integration
+ Signal catalog JSON uploaded to S3

 **Duration:** 2-3 minutes

### Phase 1: Storage \+ IoT \+ UI
<a name="phase-1-storage-iot-ui"></a>

 **Make target:** `make phase1` 

 **Stacks deployed:** 
+  `cms-{stage}-storage` — DynamoDB tables and S3 buckets
+  `cms-{stage}-iot` — IoT Core configuration and fleet management
+  `cms-{stage}-ui` — Fleet Manager web application

 **Resources created:** 
+ DynamoDB tables: vehicles, trips, alerts, drivers, safety events, maintenance alerts, telemetry, signal catalog, commands, geofences, simulations
+ S3 buckets: telemetry archive, UI assets
+ IoT Core: thing types, policies, certificate management
+ CloudFront distribution for React application
+ API Gateway REST API with Lambda backend
+ Cognito user pool and identity pool
+ Amazon Location Service map and place index
+ IAM roles and policies

 **Duration:** 5-8 minutes

### Phase 3: VPC \+ MSK \+ Redis
<a name="phase-3-vpc-msk-redis"></a>

 **Make target:** `make phase3` 

 **Stacks deployed:** 
+  `cms-{stage}-infrastructure` — VPC and caching
+  `cms-{stage}-msk` — Kafka cluster

 **Resources created:** 
+ VPC with public and private subnets (2 AZs)
+ NAT Gateway (2 AZs)
+ ElastiCache for Redis cluster
+ MSK cluster (3 brokers)
+ Kafka topics: cms-telemetry-raw, cms-telemetry-preprocessed, cms-telemetry-trips, cms-telemetry-safety, cms-telemetry-maintenance, cms-alerts, fw-telemetry-raw, fw-checkin, cms-telemetry-oem
+ Security groups

 **Duration:** 8-12 minutes

### Phase 3b: Telemetry Integration
<a name="phase-3b-telemetry-integration"></a>

 **Make target:** `make phase3b` 

 **Stacks deployed:** 
+  `cms-{stage}-telemetry-integration` — IoT to MSK bridge

 **Resources created:** 
+ IoT Rule for MQTT Direct telemetry (`cms/telemetry/+` → `cms-telemetry-raw`)
+ VPC Destination for IoT Core to MSK connectivity
+ IAM roles for IoT Rules
+ IAM role for VPC Destination includes Secrets Manager access (to retrieve MSK SCRAM credentials)
+ S3 backup for raw telemetry

 **Duration:** 10-15 minutes

### FleetWise Integration
<a name="phase-fleetwise"></a>

 **Make target:** `make deploy-fleetwise` 

 **Stacks deployed:** 
+  `cms-{stage}-fleetwise` — FleetWise IoT Rules and VPC endpoints

 **Resources created:** 
+ IoT Rule for FleetWise telemetry (`cms/fleetwise/vehicles/+/signals` → `fw-telemetry-raw`)
+ IoT Rule for FleetWise checkins (`cms/fleetwise/vehicles/+/checkins` → `fw-checkin`)
+ S3 backup for FleetWise telemetry
+ VPC endpoints for FleetWise connectivity

 **Duration:** 3-5 minutes

### Phase 4: Flink Processing
<a name="phase-4-flink-processing"></a>

 **Make target:** `make phase4` 

 **Stacks deployed:** 
+  `cms-{stage}-flink` — Stream processing applications

 **Resources created:** 
+ Flink JAR built from `modules/flink/` and uploaded to S3
+ 10 Managed Apache Flink applications: SimulatorPreprocessor, EventDrivenTelemetryProcessor, TelemetryProcessor, TripProcessor, SafetyProcessor, MaintenanceProcessor, FWTelemetryProcessor, CampaignSyncProcessor, GeofenceProcessor, OEMTelemetryProcessor
+ CloudWatch log groups for each application
+ CloudWatch alarms for downtime and idle processing
+ IAM roles for Flink (MSK, DynamoDB, Redis, IoT Core, S3 access)

 **Duration:** 5-7 minutes

### Data Seeding
<a name="phase-seeding"></a>

 **Make targets:** `make seed-fleetwise` and `make seed-event-catalog` 

 **Resources seeded:** 
+ Decoder manifest in DynamoDB — maps 260 CAN signal IDs to VSS signal names
+ Default campaign — collects all 260 signals from all vehicles
+ Event catalog — safety event rules (10 types) and maintenance alert rules (10\+ types) with thresholds
+ DecoderManifest.bin uploaded to S3 — the Flink CampaignSyncProcessor reads the protobuf decoder manifest from `s3://{flink-jar-bucket}/fwe-config/DecoderManifest.bin` and delivers it to FWE agents on checkin

 **Duration:** 2-3 minutes

### Phase 5: Pipeline Configuration
<a name="phase-5-pipeline-configuration"></a>

 **Make target:** `make phase5` 

**Note**  
 `phase5` is an optional standalone target for manual or advanced Flink reconfiguration. Its actions are already performed by `phase-streaming` during `make deploy-all`, so a standard deployment does not need to run `phase5` separately. Run it only when you need to reconfigure MSK endpoints or restart Flink applications outside of a full deployment.

 **Actions performed:** 
+ Configures MSK bootstrap server endpoints in all Flink application runtime properties
+ Configures IAM authentication for MSK connectivity
+ Starts all Flink applications

 **Duration:** 3-5 minutes

### Cloud Simulation
<a name="phase-simulation"></a>

 **Make target:** `make deploy-simulation` 

 **Stacks deployed:** 
+  `cms-{stage}-simulation` — ECS simulation infrastructure (Fargate \+ EC2-backed)

 **Resources created:** 
+ ECS cluster for simulation workers
+ Task definitions: `sim-worker` (Fargate, MQTT Direct), `fwe-agent` (EC2, FleetWise agent), `fwe-simulator` (EC2, Python simulator)
+ Docker image built from `services/simulation/` and pushed to ECR
+ Lambda function for simulation API orchestration
+ API Gateway routes for `/api/simulation/*` 
+ DynamoDB table for simulation state tracking
+ CloudWatch log group for worker tasks

 **Duration:** 3-5 minutes

### Remote Commands
<a name="phase-commands"></a>

 **Make target:** `make deploy-commands` 

 **Stacks deployed:** 
+  `cms-{stage}-commands` — Remote commands infrastructure

 **Resources created:** 
+ Commands Lambda function (send commands, command history, command catalog, geofence CRUD)
+ Command Response Handler Lambda function
+ IoT Rule on `cms/commands/+/response` to trigger response handler
+ API Gateway routes for `/api/commands/ ` and `/api/geofences/` 
+ DynamoDB tables: commands, geofences (if not already created in Phase 1)

 **Duration:** 2-3 minutes

## Step 6: Verify deployment
<a name="step-6-verify-deployment"></a>

After deployment completes, verify the installation:

### Check stack status
<a name="check-stack-status"></a>

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
<a name="access-fleet-manager-ui"></a>

1. Get the CloudFront URL from stack outputs:

   ```
   aws cloudformation describe-stacks \
     --stack-name cms-staging-ui \
     --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' \
     --output text
   ```

1. Open the URL in your web browser

1. Sign in as the seeded operator account. See [First sign-in](#first-sign-in) below for the account name and how to retrieve its password.

1. Verify you can access the Fleet Manager console

### First sign-in
<a name="first-sign-in"></a>

The UI stack seeds one Amazon Cognito user so that a fresh deployment is reachable without any manual user creation:


|  | Value | 
| --- | --- | 
| User name |  `FleetManager@example.com`  | 
| Group |  `fleet-operator`  | 
| Password | Generated by AWS Secrets Manager at deploy time and stored at `cms-{stage}-demo-user-password`  | 

The password is generated server-side, 24 characters with mixed character types, and **never appears in the CloudFormation template**. Retrieve it with:

```
aws secretsmanager get-secret-value \
  --secret-id cms-<stage>-demo-user-password \
  --query SecretString \
  --output text
```

Rotate it, or set your own, by updating that secret and then setting the Cognito password for the user from the new value.

 **This account is deliberately not an administrator.** It holds `fleet-operator`, which is the minimum group that allows fleet read and write — including enrolling and unenrolling vehicles — without cross-fleet administration, fleet creation, or user management. If you need those surfaces, create a separate account in the `platform-admin` group rather than elevating this one; keeping the convenience account un-privileged is intentional.

**Note**  
 **Self-signup is disabled unless you opt in.** The user pool enables it only when the CDK context key `cms.allow_self_signup` is set, so on a default deployment the seeded account above is the way in.  
Authority comes from group membership rather than from having an account, so any operator account you add needs an explicit group assignment — see [Fleet management](fleet-manager-console.md#fm-fleet-management) for what `platform-admin`, `fleet-operator` and `fleet-viewer` each permit. The repository carries a static-analysis guard that fails if any account-creation path could produce an account with no group, which is the invariant to preserve if you add your own provisioning.

### Verify IoT connectivity
<a name="verify-iot-connectivity"></a>

1. Get IoT endpoint:

   ```
   aws iot describe-endpoint --endpoint-type iot:Data-ATS
   ```

1. Test MQTT connection using the vehicle simulator (see [Verify deployment](#step-6-verify-deployment))

### Verify Flink applications
<a name="verify-flink-applications"></a>

```
# List Kinesis Data Analytics applications
aws kinesisanalyticsv2 list-applications

# Check application status
aws kinesisanalyticsv2 describe-application \
  --application-name cms-staging-trip-detection
```

Applications should show `RUNNING` status.

## Deployment outputs
<a name="deployment-outputs"></a>

After successful deployment, the following outputs are available:


| Output | Description | Stack | 
| --- | --- | --- | 
| CloudFrontURL | Fleet Manager web application URL | cms-{stage}-ui | 
| UserPoolId | Cognito user pool ID | cms-{stage}-ui | 
| IdentityPoolId | Cognito identity pool ID | cms-{stage}-ui | 
| ApiGatewayUrl | REST API endpoint | cms-{stage}-ui | 
| IoTEndpoint | IoT Core data endpoint | cms-{stage}-iot | 
| MSKClusterArn | MSK cluster ARN | cms-{stage}-msk | 
| VehicleTableName | DynamoDB vehicles table | cms-{stage}-storage | 
| TripTableName | DynamoDB trips table | cms-{stage}-storage | 
| AlertTableName | DynamoDB alerts table | cms-{stage}-storage | 
| ElastiCacheEndpoint | Redis cache endpoint | cms-{stage}-infrastructure | 

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
<a name="customizing-the-deployment"></a>

### Modify stack configuration
<a name="modify-stack-configuration"></a>

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
<a name="change-deployment-stage"></a>

Deploy to different environments:

```
# Deploy to staging (canonical target)
DEPLOYMENT_STAGE=staging make deploy
```

**Note**  
This guidance now ships as a single-environment deployment. If you need multiple isolated environments, deploy separate stack sets under distinct stage names (for example, `staging-eu` and `staging-us`) rather than reintroducing a legacy `prod` alias.

### Use existing VPC
<a name="use-existing-vpc"></a>

To use an existing VPC instead of creating a new one:

```
# Set VPC ID environment variable
export VPC_ID=vpc-xxxxx

# Deploy without creating VPC
make deploy
```

### Use existing MSK cluster
<a name="use-existing-msk-cluster"></a>

To use an existing MSK cluster:

```
# Set MSK cluster ARN
export MSK_CLUSTER_ARN=arn:aws:kafka:region:account:cluster/name/uuid

# Deploy without creating MSK
make deploy
```

### Container image customization
<a name="container-image-customization"></a>

The simulation service uses two ARM64 container images (`cms-sim-service` and `cms-fwe-agent`). By default, `make deploy-simulation` pulls pre-built published images from public ECR — no local container builder is required. The v0.4.0 release republished both images at tag `v0.4.0`; `cms-sim-service:v0.4.0` is rebuilt from this release and carries the vehicle-side SOVD handlers, while `cms-fwe-agent:v0.4.0` is content-identical to `v0.3.2` (AWS IoT FleetWise Edge Agent v1.3.2). The pinned tag lives in `deployment/stacks/_sim_image_config.py`.

```
# Default: uses published images from public ECR (no local Docker needed)
make -C deployment deploy-simulation DEPLOYMENT_STAGE=staging AWS_REGION=us-west-2
```

To use images from your own registry, set `PUBLIC_ECR_REGISTRY` and `PUBLIC_ECR_TAG`:

```
# Point to a custom registry and tag
PUBLIC_ECR_REGISTRY=<account-id>.dkr.ecr.<region>.amazonaws.com \
PUBLIC_ECR_TAG=v0.4.0 \
  make -C deployment deploy-simulation DEPLOYMENT_STAGE=staging AWS_REGION=us-west-2
```

For local development builds (when actively modifying simulation Dockerfiles), use `SIM_IMAGE_MODE=asset` to build images locally instead of pulling from a registry. This requires a local container builder such as Docker, Finch, or Podman.

```
# Build images locally (requires Docker, Finch, or Podman)
SIM_IMAGE_MODE=asset CDK_DOCKER=finch \
  make -C deployment deploy-simulation DEPLOYMENT_STAGE=staging AWS_REGION=us-west-2
```

**Note**  
 `SIM_IMAGE_MODE=asset` is intended for active Dockerfile development only. Standard deployments should use the default published images to avoid a dependency on a local container builder.  
Deployments that inadvertently downgrade to `cms-sim-service:v0.3.2` will find SOVD commands succeed at dispatch but never receive a vehicle-side response — the `v0.3.2` image predates the SOVD handlers. Rebuild against `v0.4.0` (the default) or a later tag before exercising remote diagnostics.

### Conversational assistant (deployed from AVX)
<a name="deploy-bedrock-agents"></a>

The in-UI conversational assistant is **not** deployed by this repository. It is served by the companion Agentic Vehicle Experience (AVX) accelerator’s Amazon Bedrock AgentCore text runtime.

To wire CMS to a deployed AVX assistant, populate the `vsaApiEndpoint` field in `runtimeConfig.json` at UI deploy time — typically by pointing to the AVX API Gateway stage URL. The `ChatAgent` component then routes `/assistant/chat` requests to that endpoint. When `vsaApiEndpoint` is unset, the chat panel reports the assistant as not configured and the remainder of the Fleet Manager application continues to function.

The historical `make deploy-bedrock-agents` target now exits as a no-op stub for backward compatibility. The v0.4.0 release retired the CMS-side `cms-{stage}-bedrock-agents` stack that previously held the Virtual Fleet Operator supervisor and specialist agents; the Tier 1 replacement that fills the fleet-view landing surface is `services/fleet_intelligence/`.

**Note**  
See [Conversational fleet assistant](bedrock-agents-stack.md) in the architecture-details chapter for the CMS-side integration surface, and the AVX accelerator’s own documentation for the AgentCore runtime and supervisor-agent architecture.

## Troubleshooting deployment
<a name="troubleshooting-deployment"></a>

### CDK bootstrap fails
<a name="cdk-bootstrap-fails"></a>

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
<a name="stack-deployment-fails"></a>

 **Problem:** Stack creation fails with resource errors

 **Solution:** 

1. Check CloudFormation events:

   ```
   aws cloudformation describe-stack-events \
     --stack-name cms-staging-storage \
     --max-items 20
   ```

1. Review error messages in CloudWatch Logs

1. Verify service quotas are sufficient

1. Delete failed stack and retry:

   ```
   aws cloudformation delete-stack --stack-name cms-staging-storage
   make phase-foundation
   ```

### MSK cluster creation timeout
<a name="msk-cluster-creation-timeout"></a>

 **Problem:** MSK cluster takes longer than expected

 **Solution:** 
+ MSK cluster creation typically takes 8-12 minutes
+ Wait for completion before proceeding to Phase 4
+ Check cluster status:

  ```
  aws kafka describe-cluster --cluster-arn CLUSTER-ARN
  ```

### Flink application fails to start
<a name="flink-application-fails-to-start"></a>

 **Problem:** Kinesis Data Analytics application shows FAILED status

 **Solution:** 

1. Check CloudWatch Logs for error messages:

   ```
   aws logs tail /aws/kinesis-analytics/cms-staging-trip-detection --follow
   ```

1. Verify MSK cluster is accessible

1. Verify DynamoDB tables exist

1. Restart application:

   ```
   aws kinesisanalyticsv2 start-application \
     --application-name cms-staging-trip-detection
   ```

### Insufficient permissions
<a name="insufficient-permissions"></a>

 **Problem:** Deployment fails due to IAM permissions

 **Solution:** 

Ensure your IAM user or role has the following permissions:
+ CloudFormation: Full access
+ IAM: Create/update roles and policies
+ S3: Create/manage buckets
+ DynamoDB: Create/manage tables
+ IoT: Full access
+ MSK: Full access
+ Kinesis Data Analytics: Full access
+ Lambda: Create/update functions
+ API Gateway: Create/manage APIs
+ Cognito: Create/manage user pools
+ Location Service: Create/manage resources
+ CloudFront: Create/manage distributions
+ ElastiCache: Create/manage clusters
+ VPC: Create/manage networking resources

## Next steps
<a name="next-steps"></a>

After successful deployment:

1.  [Run the vehicle simulator](simulation-platform.md) to generate test data

1. Access the Fleet Manager UI to view vehicles and trips

1. Configure alert subscriptions for maintenance notifications

1. Integrate with your existing systems using the REST API

1. Review CloudWatch metrics and alarms for operational monitoring

1. Explore [customization options](developer-guide.md) for your use case

## Additional resources
<a name="additional-resources"></a>
+  [GitHub Repository](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws) 
+  [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html) 
+  [AWS IoT Core Documentation](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) 
+  [Amazon MSK Documentation](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) 
+  [Kinesis Data Analytics Documentation](https://docs.aws.amazon.com/kinesisanalytics/latest/java/what-is.html) 