

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the prerequisites, supported Regions, cost, security, and quota considerations before deploying the guidance.

## Prerequisites
<a name="prerequisites"></a>

Before deploying the guidance, ensure you have the following prerequisites:

### Software requirements
<a name="software-requirements"></a>

 **Required software:** 
+  [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) - Command line tool for AWS
+  [Node.js 20.x or later](https://nodejs.org/) - JavaScript runtime (Node.js 20 LTS is the recommended version for Vite 5 compatibility)
+  [Yarn 4 via Corepack](https://yarnpkg.com/) - Package manager; enable with `corepack enable && corepack prepare yarn@4.6.0 --activate` 
+  [Python 3.9 or later](https://www.python.org/downloads/) - Python runtime
+  [AWS CDK v2.100.0 or later](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) - Infrastructure as code framework
+  [Java 11 (OpenJDK or Amazon Corretto 11)](https://adoptium.net/) - Required to build the Apache Flink JAR that packages all stream-processing applications
+  [Apache Maven 3.6 or later](https://maven.apache.org/download.cgi) - Required to compile and package the Flink applications (`mvn package` under `modules/flink/`)
+  [Make](https://www.gnu.org/software/make/) - Build automation tool
+  [Git](https://git-scm.com/) - Version control system

 **Optional software:** 
+  [Docker](https://docs.docker.com/get-docker/) - Required only when `SIM_IMAGE_MODE=asset` is set to build simulation container images locally rather than pulling from the public Amazon ECR registry. By default the solution pulls pre-built images from the public registry and Docker is not needed.

### AWS account requirements
<a name="aws-account-requirements"></a>

 **Account setup:** 
+ An AWS account with appropriate IAM permissions
+ AWS credentials configured (via `aws configure` or environment variables)
+ Sufficient service quotas for the resources being deployed (see [Quotas](#quotas))
+ CDK bootstrap completed in target account and region
+ The environment variable `CMS_DEMO_DEFAULT_PASSWORD` set to a strong password used to seed demo user accounts during the `phase-seeds` deployment phase

 **Required IAM permissions:** 

The IAM user or role deploying the guidance needs permissions to create and manage:
+ AWS CloudFormation stacks
+ IAM roles and policies
+ Amazon VPC and networking resources
+ Amazon DynamoDB tables
+ Amazon S3 buckets
+ AWS IoT Core resources
+ Amazon MSK clusters
+ Amazon Kinesis Data Analytics applications
+ AWS Lambda functions
+ Amazon API Gateway APIs
+ Amazon Cognito user pools
+ Amazon Location Service resources
+ Amazon CloudFront distributions
+ Amazon ElastiCache clusters

We recommend using the `AdministratorAccess` managed policy for initial deployment, then creating a custom policy with least-privilege permissions for production deployments.

### Network requirements
<a name="network-requirements"></a>

 **VPC considerations:** 

The solution creates a new VPC by default with the following configuration:
+ CIDR block: 10.0.0.0/16 (customizable)
+ Public subnets: 2 (across 2 Availability Zones)
+ Private subnets: 2 (across 2 Availability Zones)
+ NAT Gateway: 1 per Availability Zone
+ Internet Gateway: 1

 **Existing VPC:** 

To use an existing VPC, set the `VPC_ID` environment variable before deployment. The VPC must have:
+ At least 2 private subnets across 2 Availability Zones
+ Internet connectivity via NAT Gateway or NAT instance
+ Sufficient IP address space for MSK and ElastiCache

## Supported AWS Regions
<a name="supported-aws-regions"></a>

For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

Guidance for Connected Mobility on AWS is supported in the following AWS Regions:


| Region name | Region code | 
| --- | --- | 
| US East (Ohio) | us-east-2 | 
| US East (N. Virginia) | us-east-1 | 
| US West (Oregon) | us-west-2 | 
| Europe (Ireland) | eu-west-1 | 
| Europe (Frankfurt) | eu-central-1 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | 
| Asia Pacific (Sydney) | ap-southeast-2 | 

**Note**  
Not all AWS services are available in all Regions. Verify that Amazon MSK, Amazon Kinesis Data Analytics, and Amazon Location Service are available in your target Region before deployment.

**Note**  
The solution applies a cross-region namespace discipline — all globally-scoped AWS resources (S3 bucket names, IAM role names, and CloudFront aliases) include a region suffix so that the same stage name can be deployed to multiple AWS Regions without collision. This pattern has been validated across all 34 commercial AWS Regions. Asia Pacific (Tokyo) (`ap-northeast-1`) has been end-to-end validated as a reference secondary deployment Region alongside US West (Oregon).

## Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs.

### Cost model assumptions
<a name="cost-model-assumptions"></a>

The cost estimates below are based on the following telemetry profile per vehicle:
+  **Telemetry frequency:** 1 message every 2 seconds while driving (260 signals per message)
+  **Average driving time:** 2 hours per day per vehicle
+  **Messages per vehicle per day:** \~3,600
+  **Message size:** \~2 KB (compressed JSON with 260 signals)
+  **Data per vehicle per month:** \~216 MB
+  **Active fleet percentage:** 30% of vehicles driving at any given time during peak hours

All estimates use US East (N. Virginia) pricing as of March 2026.

The cost model separates two categories of expense:
+  **Telemetry processing costs** (Table A) — services that scale with vehicle count and message volume: Amazon MSK, Amazon Managed Service for Apache Flink, AWS IoT Core, telemetry S3 storage, VPC/NAT Gateway networking, and Amazon ElastiCache. These dominate total cost and scale predictably with fleet size.
+  **Other component costs** (Table B) — platform services and optional components: the Fleet Manager web application, API layer, Amazon Cognito authentication, Amazon Location Service, Amazon DynamoDB, AWS Lambda, Amazon CloudFront, Amazon ECS Fargate workers (OEM connector, simulation, WebSocket fan-out), and optionally Amazon Bedrock agent invocations and Amazon Bedrock AgentCore runtime. These include a fixed baseline plus variable usage costs.

The $400 per month baseline figure used in the overview applies to 1,000 vehicles at moderate usage: Table A (\~$364) \+ Table B fixed baseline (\~$44) is approximately $408, which rounds to the approximately $400 per month figure cited in the overview. All figures are estimates. Bedrock agent invocations, ECS Fargate worker uptime, and AgentCore runtime are variable additions on top of this baseline and are flagged as estimates below.

### Table A: Telemetry processing costs
<a name="cost-telemetry-processing"></a>

These costs scale with vehicle count and message volume. They represent the core data pipeline: ingestion, stream processing, and the infrastructure that supports it.


| AWS Service | What it does | 1,000 vehicles/month | Scales with | 
| --- | --- | --- | --- | 
| Amazon MSK | Kafka message streaming backbone for all telemetry topics | $194.00 | Broker count and instance size; scales with fleet size and message throughput | 
| Amazon Managed Service for Apache Flink | 10 stream-processing applications (trip detection, safety events, maintenance alerts, FleetWise decode, OEM telemetry transform, campaign sync, geofence, event-driven, telemetry processor, simulator preprocessor) | $108.00 | KPU count per application; data-path processors may need additional KPUs at larger fleet sizes | 
| AWS IoT Core | MQTT message ingestion (Basic Ingest path) from vehicles and simulators | $3.24 | Messages per month (metered in 5 KB increments) | 
| Amazon S3 | Telemetry archival (raw and preprocessed topic sink, long-term storage) | $1.50 | Data volume written per month | 
| Amazon VPC / NAT Gateway | Private networking for MSK and ElastiCache; 2 Availability Zones | $45.00 | Mostly fixed; slight increase with data transfer volume | 
| Amazon ElastiCache for Redis | Last Known State cache and geospatial index for all active vehicles | $12.00 | Node type; upgrade when active-vehicle count exceeds node memory | 
|  **Telemetry processing subtotal**  |  |  **\~$364**  |  | 

### Table B: Other component costs
<a name="cost-other-components"></a>

These costs cover the Fleet Manager application layer, optional ECS Fargate workers, and optional Bedrock agent components. The fixed baseline is approximately $44 per month at 1,000 vehicles. Variable additions depend on whether optional components are deployed and how heavily they are used.


| AWS Service | What it does | 1,000 vehicles/month | Notes | 
| --- | --- | --- | --- | 
| Amazon CloudFront | Fleet Manager UI global content distribution | $8.50 | Fixed; scales slowly with user count | 
| Amazon API Gateway | REST API for Fleet Manager and remote commands | $3.50 | Per million API calls | 
| AWS Lambda | API handlers, response processing, admin operations, orchestration | $20.00 | Per invocation; free-tier eligible for low usage | 
| Amazon Cognito | User authentication for Fleet Manager (platform-admin, fleet-operator, fleet-viewer groups) | $0.00 | Free tier covers up to 50,000 monthly active users | 
| Amazon DynamoDB | Vehicle, trip, alert, driver, campaign, command, and geofence storage (on-demand billing) | $3.50 | On-demand; scales with read/write request volume | 
| Amazon Location Service | Fleet map tiles, geocoding, and route calculation | $8.00 | Per map tile request and geocode call | 
| Amazon S3 (application) | UI assets, signal catalogs, decoder manifests, transform manifests | Included in Table A S3 row | Negligible incremental cost | 
|  **Other components fixed subtotal**  |  |  **\~$44**  |  | 
| Amazon ECS Fargate — OEM connector | Cloud-to-cloud OEM telemetry ingestion worker (gRPC streaming, lands on `cms-telemetry-oem` topic) | Variable (\~$5–$15 estimate) | Scales with connector uptime; $0 when not running | 
| Amazon ECS Fargate — simulation | Cloud vehicle simulation in MQTT Direct mode (on-demand; stops when simulation ends) | Variable (\~$2–$10 estimate) | On-demand only; $0 when idle | 
| Amazon ECS — FleetWise simulation | FleetWise Edge simulation on EC2 (t4g.small ARM64) with virtual CAN isolation | Variable (\~$5–$20 estimate) | Per active simulation session | 
| Amazon ECS Fargate — WebSocket fan-out | Kafka-to-WebSocket bridge for real-time telemetry in the Fleet Manager UI | Variable (\~$3–$10 estimate) | Scales with connected UI sessions | 
| Amazon Bedrock (agent invocations) | Supervisor and specialist multi-agent calls for the in-UI conversational fleet assistant (opt-in: `make deploy-bedrock-agents`) | Variable (\~$5–$50 estimate) | Highly variable; depends on assistant usage, token counts, and number of specialist agent hops. $0 if `deploy-bedrock-agents` is not run. | 
| Amazon Bedrock AgentCore Runtime | AgentCore text and bidirectional runtime hosting for the fleet assistant | Variable (\~$0–$20 estimate) | Per-invocation fee structure; verify current pricing at deploy time. $0 if not deployed. | 
|  **Variable additions subtotal**  |  |  **\~$20–$105 estimate**  | Flagged as estimates; actual cost depends on deployment choices and usage patterns | 

**Note**  
Bedrock agent invocations and AgentCore Runtime costs are estimates only. Actual costs depend on the number of assistant sessions, the length of each conversation, and how many specialist agent hops occur per query. These components are opt-in and are not deployed by `make deploy-all`. To omit Bedrock costs entirely, skip the `make deploy-bedrock-agents` step.

### Cost reconciliation to baseline
<a name="cost-reconciliation"></a>

The approximately $400 per month baseline used in this guide is the sum of Table A and the Table B fixed baseline at 1,000 vehicles (approximately $408 itemized, which rounds to the \~$400 figure used elsewhere in this guide):


| Cost category | Monthly estimate | 
| --- | --- | 
| Table A: Telemetry processing (MSK \+ Flink \+ IoT Core \+ S3 \+ VPC/NAT \+ ElastiCache) | \~$364 | 
| Table B: Other components fixed (CloudFront \+ API Gateway \+ Lambda \+ Cognito \+ DynamoDB \+ Location Service) | \~$44 | 
|  **Baseline total (1,000 vehicles, no optional components)**  |  **\~$408 (rounds to \~$400)**  | 
| Table B: Variable additions (ECS Fargate workers \+ Bedrock agents \+ AgentCore, when deployed) | \~$20–$105 estimate | 
|  **Total with optional components at moderate usage**  |  **\~$428–$513 estimate**  | 

### Cost by fleet size
<a name="cost-by-fleet-size"></a>


| Fleet Size | MSK | Flink | Infrastructure | Application | Total/Month | 
| --- | --- | --- | --- | --- | --- | 
| 100 vehicles | $67 | $108 | $58 | $32 |  **\~$265**  | 
| 500 vehicles | $67 | $108 | $58 | $35 |  **\~$268**  | 
| 1,000 vehicles | $194 | $108 | $58 | $40 |  **\~$400**  | 
| 5,000 vehicles | $194 | $324 | $58 | $55 |  **\~$631**  | 
| 10,000 vehicles | $389 | $540 | $71 | $75 |  **\~$1,075**  | 
| 25,000 vehicles | $583 | $864 | $84 | $120 |  **\~$1,651**  | 
| 50,000 vehicles | $972 | $1,296 | $97 | $200 |  **\~$2,565**  | 
| 100,000 vehicles | $1,944 | $2,160 | $130 | $350 |  **\~$4,584**  | 

**Note**  
The totals above reflect Table A (telemetry processing) and the Table B fixed baseline only. Variable Table B additions (Bedrock agents, ECS Fargate workers) are not included in these totals. Add the Table B variable estimate to the applicable fleet-size row for a total-cost projection when optional components are deployed.

 **Cost per vehicle per month:** 


| Fleet Size | Total/Month | Per Vehicle | 
| --- | --- | --- | 
| 100 | $265 | $2.65 | 
| 1,000 | $400 | $0.40 | 
| 10,000 | $1,075 | $0.11 | 
| 50,000 | $2,565 | $0.05 | 
| 100,000 | $4,584 | $0.05 | 

The per-vehicle cost drops as fleet size increases because the fixed infrastructure costs (MSK cluster, NAT Gateway, ElastiCache) are amortized across more vehicles. The breakpoint for cost efficiency is around **5,000–10,000 vehicles**, where per-vehicle cost drops below $0.15/month.

### Detailed cost breakdown
<a name="cost-breakdown-detail"></a>

#### Amazon MSK (message streaming)
<a name="msk-costs"></a>

MSK is the largest cost driver (40-50% of total). Cost scales with broker count and instance size.


| Fleet Size | Configuration | Messages/sec (peak) | Monthly Cost | 
| --- | --- | --- | --- | 
| Up to 500 | 3 × kafka.t3.small (2 vCPU, 2 GB) | \~250 | $67 | 
| 500–5,000 | 3 × kafka.m5.large (2 vCPU, 8 GB) | \~2,500 | $194 | 
| 5,000–25,000 | 3 × kafka.m5.xlarge (4 vCPU, 16 GB) | \~12,500 | $389–583 | 
| 25,000–100,000 | 6 × kafka.m5.xlarge | \~50,000 | $972–1,944 | 

 **Scaling trigger:** Upgrade when average broker CPU exceeds 60% or when consumer lag exceeds 30 seconds.

 **Storage:** 100 GB per broker included. Telemetry retention is 7 days. At 1,000 vehicles, daily ingest is \~7 GB, so 100 GB per broker provides comfortable headroom.

#### Amazon Managed Service for Apache Flink (stream processing)
<a name="flink-costs"></a>

Flink is the second largest cost driver (25-35% of total). Cost scales with KPU count. Each KPU provides 1 vCPU and 4 GB memory at $0.15/hour ($108/month).

The solution runs 10 Flink applications. In development, each application uses 1 KPU. In production, data-path processors (SimulatorPreprocessor, EventDrivenTelemetryProcessor, TripProcessor) may need 2-4 KPUs each.


| Fleet Size | KPU Allocation | Monthly Cost | 
| --- | --- | --- | 
| Up to 1,000 | 1 KPU × 10 apps = 10 KPUs | $108 (min billing) | 
| 1,000–5,000 | 2 KPU × 3 critical \+ 1 KPU × 7 = 13 KPUs | $324 | 
| 5,000–10,000 | 3 KPU × 3 critical \+ 1 KPU × 7 = 16 KPUs | $540 | 
| 10,000–25,000 | 4 KPU × 3 critical \+ 2 KPU × 7 = 26 KPUs | $864 | 
| 25,000–50,000 | 4 KPU × 5 critical \+ 2 KPU × 5 = 30 KPUs | $1,296 | 
| 50,000–100,000 | 6 KPU × 5 critical \+ 3 KPU × 5 = 45 KPUs | $2,160 | 

 **Scaling trigger:** Add KPUs when `millisBehindLatest` exceeds 5,000ms or when checkpoint duration exceeds 50% of the checkpoint interval.

#### Infrastructure (VPC, ElastiCache, NAT Gateway)
<a name="infrastructure-costs"></a>

These are mostly fixed costs that do not scale linearly with fleet size.


| Service | Configuration | Monthly Cost | 
| --- | --- | --- | 
| NAT Gateway | 2 AZs × $0.045/hour \+ data processing | $32–65 | 
| ElastiCache for Redis | cache.t3.micro (dev) to cache.r6g.large (prod) | $12–130 | 
| VPC endpoints | DynamoDB \+ S3 (gateway, free) \+ IoT Core (interface) | $14 | 

 **ElastiCache scaling:** The Redis node must hold the Last Known State for all active vehicles. Each vehicle uses \~5 KB in Redis (signals hash \+ timestamps hash \+ meta hash \+ stream). At 10,000 vehicles, that is \~50 MB — well within a cache.t3.micro (0.5 GB). Upgrade to cache.t3.small at 50,000\+ vehicles or if geospatial query latency exceeds 5ms.

#### Application layer (Lambda, API Gateway, IoT Core, DynamoDB, S3)
<a name="application-costs"></a>

These costs scale with usage but remain a small percentage of total cost.


| Service | Cost Driver | Monthly Cost (1K vehicles) | 
| --- | --- | --- | 
| AWS IoT Core | $1.00 per million messages | $3.24 | 
| Amazon DynamoDB | On-demand read/write capacity | $3.50 | 
| AWS Lambda | $0.20 per million invocations | $20.00 | 
| Amazon API Gateway | $3.50 per million calls | $3.50 | 
| Amazon CloudFront | $0.085 per GB transfer | $8.50 | 
| Amazon Location Service | $0.04 per 1K map tiles | $8.00 | 
| Amazon S3 | $0.023 per GB storage | $1.50 | 
| Amazon Cognito | Free tier (50K MAU) | $0.00 | 

 **IoT Core message cost detail:** At 1,000 vehicles × 3,600 messages/day = 3.6M messages/day = 108M messages/month. IoT Core charges $1.00 per million messages (first 1B), so 108M × $1.00/M = $108. However, messages are metered in 5 KB increments, and compressed telemetry is \~2 KB, so each message counts as 1 unit. For 100 vehicles, this drops to $10.80/month.

 **DynamoDB cost detail:** On-demand pricing is $1.25 per million write request units and $0.25 per million read request units. The stateful TripProcessor design reduces writes by 80% compared to a stateless approach (see [Trip lifecycle](trip-lifecycle.md)).

### Cost breakpoints and optimization
<a name="cost-breakpoints"></a>

The cost curve has three distinct regions:

 **Under 500 vehicles (\~$265/month):** Fixed infrastructure dominates. MSK and Flink minimum billing account for 66% of cost. Per-vehicle cost is high ($0.53–$2.65) but total cost is low. Use kafka.t3.small brokers and 1 KPU per Flink app.

 **500–10,000 vehicles (\~$400–$1,075/month):** The sweet spot. Infrastructure costs are amortized, and usage-based costs (IoT Core, DynamoDB) are still modest. Per-vehicle cost drops to $0.11–$0.40. This is where the architecture is most cost-efficient relative to capability.

 **Over 10,000 vehicles (\~$1,075\+/month):** Usage-based costs begin to dominate. MSK and Flink need to scale horizontally. Per-vehicle cost flattens at \~$0.05. At this scale, consider:
+  **MSK Serverless** instead of provisioned — eliminates broker sizing decisions and can reduce cost for bursty workloads
+  **Provisioned DynamoDB capacity** with auto-scaling instead of on-demand — 5-10x cheaper for predictable write patterns
+  **S3 Intelligent-Tiering** for telemetry archives — automatically moves cold data to cheaper storage classes
+  **Reserved capacity** for Flink KPUs if available — reduces hourly rate

### Cost optimization strategies
<a name="cost-optimization-strategies"></a>

 **Development environment:** 


| Change | Impact | Savings | 
| --- | --- | --- | 
| kafka.t3.small instead of m5.large | Sufficient for <500 vehicles | $127/month | 
| 1 KPU per Flink app (minimum) | Sufficient for <1,000 vehicles | $0 (already minimum) | 
| cache.t3.micro for Redis | Sufficient for <10,000 vehicles | $0 (already minimum) | 
| Single NAT Gateway (1 AZ) | Reduced availability | $16/month | 
|  **Total development savings**  |  |  **\~$143/month**  | 

 **Production optimizations:** 
+  **DynamoDB TTL:** Enable TTL on telemetry records (30 days), safety events (90 days), and commands (7 days) to automatically delete old data and reduce storage costs.
+  **S3 lifecycle policies:** Transition telemetry archives to S3 Glacier after 90 days (saves \~$0.02/GB/month).
+  **CloudWatch log retention:** Set log retention to 30 days for development, 90 days for production (default is indefinite).
+  **Flink checkpointing:** Increase checkpoint interval from 60s to 120s for non-critical processors to reduce state backend I/O.
+  **IoT Core message batching:** The simulator compresses telemetry with gzip, reducing message size from \~8 KB to \~2 KB (75% reduction in IoT Core message costs).
+  **Bedrock cost control:** Deploy `make deploy-bedrock-agents` only in environments where the in-UI conversational fleet assistant is needed. Omitting this stack from development environments eliminates Bedrock invocation costs entirely.

## Security
<a name="security-arch"></a>

### Data protection
<a name="data-protection-overview"></a>

 **Encryption at rest:** 
+ All DynamoDB tables use AWS-managed encryption keys
+ All S3 buckets use AES-256 encryption
+ MSK cluster uses encryption at rest
+ ElastiCache uses encryption at rest

 **Encryption in transit:** 
+ All API calls use TLS 1.2 or higher
+ MSK client connections use TLS
+ IoT Core connections use TLS with X.509 certificates
+ CloudFront uses TLS 1.2 minimum

### Identity and access management
<a name="identity-and-access-management"></a>

 **Authentication:** 
+ Amazon Cognito manages user authentication for Fleet Manager UI
+ AWS IoT Core uses X.509 certificates for vehicle authentication
+ IAM roles control service-to-service communication

 **Authorization:** 

Fleet Manager implements role-based access control through three Amazon Cognito user groups:
+  `platform-admin` — full cross-fleet access; required for bulk fleet lifecycle operations (enroll, unenroll, status sync) and OEM connector management
+  `fleet-operator` — per-fleet access scoped by the `custom:fleetIds` Cognito claim; can manage vehicles within their assigned fleets
+  `fleet-viewer` — read-only access to fleet and vehicle data
+ IAM policies follow least-privilege principles
+ IoT policies restrict device access to specific topics
+ API Gateway uses Cognito authorizers
+ Lambda functions have minimal required permissions

 **Security-relevant CDK context flags:** 

Three CDK context flags control optional access behaviors. All three default to `false` for a production-safe posture:
+  `cms.allow_self_signup` (default `false`) — controls whether end users can self-register in the Cognito user pool. Set to `true` only for demo environments.
+  `cms.allow_unauth_map_auth` (default `false`) — controls whether the Cognito identity pool issues unauthenticated credentials for map tile requests. Keep `false` in production to require authentication before loading the fleet map.
+  `cms.allow_unauth_websocket` (default `false`) — controls whether the WebSocket API `$connect` authorizer permits unauthenticated connections. Keep `false` in production to require a valid Cognito JWT on WebSocket upgrade.

To enable any of these flags for a demo environment, pass the context override at deploy time rather than changing `cdk.json` defaults:

```
cdk deploy --context cms.allow_self_signup=true <stack-name>
```

### Network security
<a name="network-security"></a>

 **VPC isolation:** 
+ MSK cluster runs in private subnets
+ ElastiCache runs in private subnets
+ Security groups restrict traffic between components
+ No direct internet access to data stores

 **WebSocket API security:** 

The Fleet Manager real-time telemetry feed uses an API Gateway WebSocket API. The `$connect` route is protected by a Cognito JWT Lambda REQUEST authorizer. Clients must include a valid JWT as the `token` query parameter on the WebSocket upgrade URL (`wss://<endpoint>?token=<jwt>`). Unauthenticated upgrade attempts return HTTP 401. Fleet-operator connections receive only the telemetry topics for their assigned fleets; platform-admin connections receive all-fleet fan-out.

 **API security:** 
+ API Gateway endpoints require Cognito authentication
+ CloudFront distributions can optionally use a trusted key group (signed cookies or signed URLs) to restrict access to authorized users — a standard AWS CloudFront access-control pattern
+ CORS policies restrict cross-origin requests

### Monitoring and logging
<a name="monitoring-and-logging"></a>

 **CloudWatch Logs:** 
+ All Lambda functions log to CloudWatch
+ Flink applications log to CloudWatch
+ API Gateway logs all requests
+ Default log retention: 90 days

 **CloudTrail:** 
+ All API calls are logged to CloudTrail
+ CloudTrail logs stored in S3 with encryption
+ Log file integrity validation enabled

### Compliance
<a name="compliance"></a>

This solution uses AWS services that support various compliance programs:
+ SOC 1, 2, 3
+ PCI DSS Level 1
+ ISO 27001, 27017, 27018
+ HIPAA eligible services
+ GDPR compliant

For the most current compliance information, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

## Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

### Service quotas to verify
<a name="service-quotas-to-verify"></a>

Before deploying the guidance, verify you have sufficient quotas for the following services:

 **Amazon MSK:** 
+ Clusters per Region: Default 20 (need 1)
+ Brokers per cluster: Default 30 (need 3)
+ Configuration revisions: Default 50

 **Amazon Kinesis Data Analytics (Managed Service for Apache Flink):** 
+ Applications per Region: Default 50 (need 10 — the solution deploys 10 Flink applications). Note: the prior default for some accounts was 8; if your account shows a default of 8, request an increase to 10 or more before deploying.
+ KPUs per application: Default 32 (need 1-4)

 **AWS IoT Core:** 
+ Things per account: Default 500,000
+ Certificates per account: Default 500,000
+ Policies per account: Default 1,000
+ Message broker connections: Default 500,000

 **Amazon DynamoDB:** 
+ Tables per Region: Default 2,500 (need 4)
+ On-demand read/write capacity: No limit

 **AWS Lambda:** 
+ Concurrent executions: Default 1,000
+ Function storage: Default 75 GB

 **Amazon VPC:** 
+ VPCs per Region: Default 5 (need 1)
+ Subnets per VPC: Default 200 (need 4)
+ Security groups per VPC: Default 2,500
+ NAT gateways per AZ: Default 5 (need 2)

 **Amazon ElastiCache:** 
+ Nodes per Region: Default 300 (need 1)
+ Clusters per Region: Default 300 (need 1)

 **Amazon ECS (when using simulation or OEM connector):** 
+ Fargate task vCPU per Region: Default varies by Region. For large simulations running multiple concurrent vehicle sessions, verify the Fargate task concurrency limit in your target Region and request an increase if needed.

 **Amazon Bedrock (when `make deploy-bedrock-agents` is run):** 
+ Invocations per minute for `us.anthropic.claude-sonnet-4-6`: Soft limit, Region-dependent. Check the Bedrock console Service Quotas page in your target Region before deploying the Bedrock agents stack at scale.

### Requesting quota increases
<a name="requesting-quota-increases"></a>

If you need to increase service quotas:

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/) 

1. Select the service

1. Select the quota

1. Choose **Request quota increase** 

1. Enter the new quota value

1. Submit the request

Most quota increases are processed within 24-48 hours.

## Deployment sizing
<a name="deployment-sizing"></a>

### Small fleet (100-1,000 vehicles)
<a name="small-fleet-100-1000-vehicles"></a>

 **Recommended configuration:** 
+ MSK: 3 × kafka.t3.small brokers
+ ElastiCache: cache.t3.micro
+ Flink: 1 KPU per application
+ DynamoDB: On-demand billing

 **Expected cost:** \~$250-300/month (telemetry processing \+ fixed platform baseline; excludes optional Bedrock/ECS variable components)

 **Telemetry capacity:** 
+ Messages per second: \~100-500
+ Daily messages: \~8-40 million
+ Storage per month: \~10-50 GB

### Medium fleet (1,000-10,000 vehicles)
<a name="medium-fleet-1000-10000-vehicles"></a>

 **Recommended configuration:** 
+ MSK: 3 × kafka.m5.large brokers
+ ElastiCache: cache.t3.small
+ Flink: 2 KPUs per application
+ DynamoDB: On-demand billing

 **Expected cost:** \~$410-600/month (telemetry processing \+ fixed platform baseline; excludes optional Bedrock/ECS variable components)

 **Telemetry capacity:** 
+ Messages per second: \~500-2,000
+ Daily messages: \~40-170 million
+ Storage per month: \~50-200 GB

### Large fleet (10,000\+ vehicles)
<a name="large-fleet-10000-vehicles"></a>

 **Recommended configuration:** 
+ MSK: 6 × kafka.m5.xlarge brokers
+ ElastiCache: cache.r6g.large (cluster mode)
+ Flink: 4 KPUs per application
+ DynamoDB: Provisioned capacity with auto-scaling

 **Expected cost:** \~$1,200-2,000/month (telemetry processing \+ fixed platform baseline; excludes optional Bedrock/ECS variable components)

 **Telemetry capacity:** 
+ Messages per second: \~2,000-10,000
+ Daily messages: \~170-860 million
+ Storage per month: \~200-1,000 GB

### Performance considerations
<a name="performance-considerations"></a>

 **Message throughput:** 
+ Each MSK broker handles \~1,000 messages/second
+ Flink applications process \~2,000 messages/second per KPU
+ DynamoDB on-demand scales automatically

 **Latency targets:** 
+ IoT Core to MSK: <100ms
+ MSK to Flink: <500ms
+ Flink to DynamoDB: <200ms
+ API response time: <500ms
+ ElastiCache lookup: <10ms

 **Scaling triggers:** 
+ MSK CPU > 70%: Add brokers
+ Flink lag > 60 seconds: Add KPUs
+ DynamoDB throttling: Increase capacity
+ ElastiCache CPU > 75%: Upgrade node type

## Disaster recovery
<a name="disaster-recovery"></a>

### Backup strategy
<a name="backup-strategy"></a>

 **Automated backups:** 
+ DynamoDB: Point-in-time recovery enabled (35 days)
+ S3: Versioning enabled on all buckets
+ MSK: Automatic snapshots (not exposed to users)

 **Manual backups:** 
+ Export DynamoDB tables to S3 for long-term retention
+ Backup IoT certificates and policies
+ Export Cognito user pool configuration

### Recovery time objectives
<a name="recovery-time-objectives"></a>

 **RTO (Recovery Time Objective):** 
+ Phase 1-2 recovery: 10-15 minutes
+ Phase 3 recovery (MSK): 15-20 minutes
+ Phase 5 recovery (Flink): 5-10 minutes
+ Full stack recovery: 40-60 minutes

 **RPO (Recovery Point Objective):** 
+ DynamoDB: Up to 5 minutes (PITR)
+ S3: Zero data loss (versioning)
+ Telemetry in-flight: Up to 5 minutes

### Multi-region considerations
<a name="multi-region-considerations"></a>

For high availability across regions:
+ Deploy solution in multiple regions
+ Use Route 53 for DNS failover
+ Replicate DynamoDB tables with Global Tables
+ Use S3 Cross-Region Replication for archives
+ Configure IoT Core custom domains for failover

**Note**  
Multi-region deployment increases costs by 2-3x but provides geographic redundancy and lower latency for global fleets.