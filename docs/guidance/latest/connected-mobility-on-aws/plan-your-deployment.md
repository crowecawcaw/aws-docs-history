# Plan your deployment

This section describes the prerequisites, supported Regions, cost, security, and quota considerations before deploying the guidance.

## Prerequisites

Before deploying the guidance, ensure you have the following prerequisites:

### Software requirements

**Required software:**

- [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") - Command line tool for AWS
- [Node.js 18.x or later](https://nodejs.org/ "https://nodejs.org/") - JavaScript runtime
- [Python 3.9 or later](https://www.python.org/downloads/ "https://www.python.org/downloads/") - Python runtime
- [AWS CDK v2.100.0 or later](../../../cdk/v2/guide/getting_started.md "../../../cdk/v2/guide/getting_started.md") - Infrastructure as code framework
- [Make](https://www.gnu.org/software/make/ "https://www.gnu.org/software/make/") - Build automation tool
- [Git](https://git-scm.com/ "https://git-scm.com/") - Version control system

### AWS account requirements

**Account setup:**

- An AWS account with appropriate IAM permissions
- AWS credentials configured (via `aws configure` or environment variables)
- Sufficient service quotas for the resources being deployed
- CDK bootstrap completed in target account and region

**Required IAM permissions:**

The IAM user or role deploying the guidance needs permissions to create and manage:

- AWS CloudFormation stacks
- IAM roles and policies
- Amazon VPC and networking resources
- Amazon DynamoDB tables
- Amazon S3 buckets
- AWS IoT Core resources
- Amazon MSK clusters
- Amazon Kinesis Data Analytics applications
- AWS Lambda functions
- Amazon API Gateway APIs
- Amazon Cognito user pools
- Amazon Location Service resources
- Amazon CloudFront distributions
- Amazon ElastiCache clusters

We recommend using the `AdministratorAccess` managed policy for initial deployment, then creating a custom policy with least-privilege permissions for production deployments.

### Network requirements

**VPC considerations:**

The solution creates a new VPC by default with the following configuration:

- CIDR block: 10.0.0.0/16 (customizable)
- Public subnets: 2 (across 2 Availability Zones)
- Private subnets: 2 (across 2 Availability Zones)
- NAT Gateway: 1 per Availability Zone
- Internet Gateway: 1

**Existing VPC:**

To use an existing VPC, set the `VPC_ID` environment variable before deployment. The VPC must have:

- At least 2 private subnets across 2 Availability Zones
- Internet connectivity via NAT Gateway or NAT instance
- Sufficient IP address space for MSK and ElastiCache

## Supported AWS Regions

For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

Guidance for Connected Mobility on AWS is supported in the following AWS Regions:

| Region name           | Region code    |
| --------------------- | -------------- |
| US East (Ohio)        | us-east-2      |
| US East (N. Virginia) | us-east-1      |
| US West (Oregon)      | us-west-2      |
| Europe (Ireland)      | eu-west-1      |
| Europe (Frankfurt)    | eu-central-1   |
| Asia Pacific (Tokyo)  | ap-northeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |

###### Note

Not all AWS services are available in all Regions. Verify that Amazon MSK, Amazon Kinesis Data Analytics, and Amazon Location Service are available in your target Region before deployment.

## Cost

You are responsible for the cost of the AWS services used while running this solution. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution.

We recommend creating a [budget](../../../cost-management/latest/userguide/budgets-create.md "../../../cost-management/latest/userguide/budgets-create.md") through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") to help manage costs.

### Cost model assumptions

The cost estimates below are based on the following telemetry profile per vehicle:

- **Telemetry frequency:** 1 message every 2 seconds while driving (260 signals per message)
- **Average driving time:** 2 hours per day per vehicle
- **Messages per vehicle per day:** ~3,600
- **Message size:** ~2 KB (compressed JSON with 260 signals)
- **Data per vehicle per month:** ~216 MB
- **Active fleet percentage:** 30% of vehicles driving at any given time during peak hours

All estimates use US East (N. Virginia) pricing as of March 2026.

### Cost by fleet size

| Fleet Size       | MSK    | Flink  | Infrastructure | Application | Total/Month |
| ---------------- | ------ | ------ | -------------- | ----------- | ----------- |
| 100 vehicles     | $67    | $108   | $58            | $32         | **~$265**   |
| 500 vehicles     | $67    | $108   | $58            | $35         | **~$268**   |
| 1,000 vehicles   | $194   | $108   | $58            | $40         | **~$400**   |
| 5,000 vehicles   | $194   | $324   | $58            | $55         | **~$631**   |
| 10,000 vehicles  | $389   | $540   | $71            | $75         | **~$1,075** |
| 25,000 vehicles  | $583   | $864   | $84            | $120        | **~$1,651** |
| 50,000 vehicles  | $972   | $1,296 | $97            | $200        | **~$2,565** |
| 100,000 vehicles | $1,944 | $2,160 | $130           | $350        | **~$4,584** |

**Cost per vehicle per month:**

| Fleet Size | Total/Month | Per Vehicle |
| ---------- | ----------- | ----------- |
| 100        | $265        | $2.65       |
| 1,000      | $400        | $0.40       |
| 10,000     | $1,075      | $0.11       |
| 50,000     | $2,565      | $0.05       |
| 100,000    | $4,584      | $0.05       |

The per-vehicle cost drops dramatically as fleet size increases because the fixed infrastructure costs (MSK cluster, NAT Gateway, ElastiCache) are amortized across more vehicles. The breakpoint for cost efficiency is around **5,000–10,000 vehicles**, where per-vehicle cost drops below $0.15/month.

### Detailed cost breakdown

#### Amazon MSK (message streaming)

MSK is the largest cost driver (40-50% of total). Cost scales with broker count and instance size.

| Fleet Size     | Configuration                       | Messages/sec (peak) | Monthly Cost |
| -------------- | ----------------------------------- | ------------------- | ------------ |
| Up to 500      | 3 × kafka.t3.small (2 vCPU, 2 GB)   | ~250                | $67          |
| 500–5,000      | 3 × kafka.m5.large (2 vCPU, 8 GB)   | ~2,500              | $194         |
| 5,000–25,000   | 3 × kafka.m5.xlarge (4 vCPU, 16 GB) | ~12,500             | $389–583     |
| 25,000–100,000 | 6 × kafka.m5.xlarge                 | ~50,000             | $972–1,944   |

**Scaling trigger:** Upgrade when average broker CPU exceeds 60% or when consumer lag exceeds 30 seconds.

**Storage:** 100 GB per broker included. Telemetry retention is 7 days. At 1,000 vehicles, daily ingest is ~7 GB, so 100 GB per broker provides comfortable headroom.

#### Amazon Managed Service for Apache Flink (stream processing)

Flink is the second largest cost driver (25-35% of total). Cost scales with KPU count. Each KPU provides 1 vCPU and 4 GB memory at $0.15/hour ($108/month).

The solution runs 7-10 Flink applications. In development, each application uses 1 KPU. In production, data-path processors (SimulatorPreprocessor, EventDrivenTelemetryProcessor, TripProcessor) may need 2-4 KPUs each.

| Fleet Size     | KPU Allocation                           | Monthly Cost       |
| -------------- | ---------------------------------------- | ------------------ |
| Up to 1,000    | 1 KPU × 10 apps = 10 KPUs                | $108 (min billing) |
| 1,000–5,000    | 2 KPU × 3 critical + 1 KPU × 7 = 13 KPUs | $324               |
| 5,000–10,000   | 3 KPU × 3 critical + 1 KPU × 7 = 16 KPUs | $540               |
| 10,000–25,000  | 4 KPU × 3 critical + 2 KPU × 7 = 26 KPUs | $864               |
| 25,000–50,000  | 4 KPU × 5 critical + 2 KPU × 5 = 30 KPUs | $1,296             |
| 50,000–100,000 | 6 KPU × 5 critical + 3 KPU × 5 = 45 KPUs | $2,160             |

**Scaling trigger:** Add KPUs when `millisBehindLatest` exceeds 5,000ms or when checkpoint duration exceeds 50% of the checkpoint interval.

#### Infrastructure (VPC, ElastiCache, NAT Gateway)

These are mostly fixed costs that do not scale linearly with fleet size.

| Service               | Configuration                                        | Monthly Cost |
| --------------------- | ---------------------------------------------------- | ------------ |
| NAT Gateway           | 2 AZs × $0.045/hour + data processing                | $32–65       |
| ElastiCache for Redis | cache.t3.micro (dev) to cache.r6g.large (prod)       | $12–130      |
| VPC endpoints         | DynamoDB + S3 (gateway, free) + IoT Core (interface) | $14          |

**ElastiCache scaling:** The Redis node must hold the Last Known State for all active vehicles. Each vehicle uses ~5 KB in Redis (signals hash + timestamps hash + meta hash + stream). At 10,000 vehicles, that is ~50 MB — well within a cache.t3.micro (0.5 GB). Upgrade to cache.t3.small at 50,000+ vehicles or if geospatial query latency exceeds 5ms.

#### Application layer (Lambda, API Gateway, IoT Core, DynamoDB, S3)

These costs scale with usage but remain a small percentage of total cost.

| Service                 | Cost Driver                   | Monthly Cost (1K vehicles) |
| ----------------------- | ----------------------------- | -------------------------- |
| AWS IoT Core            | $1.00 per million messages    | $3.24                      |
| Amazon DynamoDB         | On-demand read/write capacity | $3.50                      |
| AWS Lambda              | $0.20 per million invocations | $20.00                     |
| Amazon API Gateway      | $3.50 per million calls       | $3.50                      |
| Amazon CloudFront       | $0.085 per GB transfer        | $8.50                      |
| Amazon Location Service | $0.04 per 1K map tiles        | $8.00                      |
| Amazon S3               | $0.023 per GB storage         | $1.50                      |
| Amazon Cognito          | Free tier (50K MAU)           | $0.00                      |

**IoT Core message cost detail:** At 1,000 vehicles × 3,600 messages/day = 3.6M messages/day = 108M messages/month. IoT Core charges $1.00 per million messages (first 1B), so 108M × $1.00/M = $108. However, messages are metered in 5 KB increments, and compressed telemetry is ~2 KB, so each message counts as 1 unit. For 100 vehicles, this drops to $10.80/month.

**DynamoDB cost detail:** On-demand pricing is $1.25 per million write request units and $0.25 per million read request units. The stateful TripProcessor design reduces writes by 80% compared to a stateless approach (see [Trip lifecycle](trip-lifecycle.md "trip-lifecycle.md")).

### Cost breakpoints and optimization

The cost curve has three distinct regions:

**Under 500 vehicles (~$265/month):** Fixed infrastructure dominates. MSK and Flink minimum billing account for 66% of cost. Per-vehicle cost is high ($0.53–$2.65) but total cost is low. Use kafka.t3.small brokers and 1 KPU per Flink app.

**500–10,000 vehicles (~$400–$1,075/month):** The sweet spot. Infrastructure costs are amortized, and usage-based costs (IoT Core, DynamoDB) are still modest. Per-vehicle cost drops to $0.11–$0.40. This is where the architecture is most cost-efficient relative to capability.

**Over 10,000 vehicles (~$1,075+/month):** Usage-based costs begin to dominate. MSK and Flink need to scale horizontally. Per-vehicle cost flattens at ~$0.05. At this scale, consider:

- **MSK Serverless** instead of provisioned — eliminates broker sizing decisions and can reduce cost for bursty workloads
- **Provisioned DynamoDB capacity** with auto-scaling instead of on-demand — 5-10x cheaper for predictable write patterns
- **S3 Intelligent-Tiering** for telemetry archives — automatically moves cold data to cheaper storage classes
- **Reserved capacity** for Flink KPUs if available — reduces hourly rate

### Cost optimization strategies

**Development environment:**

| Change                             | Impact                          | Savings              |
| ---------------------------------- | ------------------------------- | -------------------- |
| kafka.t3.small instead of m5.large | Sufficient for <500 vehicles    | $127/month           |
| 1 KPU per Flink app (minimum)      | Sufficient for <1,000 vehicles  | $0 (already minimum) |
| cache.t3.micro for Redis           | Sufficient for <10,000 vehicles | $0 (already minimum) |
| Single NAT Gateway (1 AZ)          | Reduced availability            | $16/month            |
| **Total development savings**      |                                 | **~$143/month**      |

**Production optimizations:**

- **DynamoDB TTL:** Enable TTL on telemetry records (30 days), safety events (90 days), and commands (7 days) to automatically delete old data and reduce storage costs.
- **S3 lifecycle policies:** Transition telemetry archives to S3 Glacier after 90 days (saves ~$0.02/GB/month).
- **CloudWatch log retention:** Set log retention to 30 days for development, 90 days for production (default is indefinite).
- **Flink checkpointing:** Increase checkpoint interval from 60s to 120s for non-critical processors to reduce state backend I/O.
- **IoT Core message batching:** The simulator compresses telemetry with gzip, reducing message size from ~8 KB to ~2 KB (75% reduction in IoT Core message costs).

## Security

### Data protection

**Encryption at rest:**

- All DynamoDB tables use AWS-managed encryption keys
- All S3 buckets use AES-256 encryption
- MSK cluster uses encryption at rest
- ElastiCache uses encryption at rest

**Encryption in transit:**

- All API calls use TLS 1.2 or higher
- MSK client connections use TLS
- IoT Core connections use TLS with X.509 certificates
- CloudFront uses TLS 1.2 minimum

### Identity and access management

**Authentication:**

- Amazon Cognito manages user authentication for Fleet Manager UI
- AWS IoT Core uses X.509 certificates for vehicle authentication
- IAM roles control service-to-service communication

**Authorization:**

- IAM policies follow least-privilege principles
- IoT policies restrict device access to specific topics
- API Gateway uses Cognito authorizers
- Lambda functions have minimal required permissions

### Network security

**VPC isolation:**

- MSK cluster runs in private subnets
- ElastiCache runs in private subnets
- Security groups restrict traffic between components
- No direct internet access to data stores

**API security:**

- API Gateway endpoints require authentication
- CloudFront uses signed URLs for sensitive content
- CORS policies restrict cross-origin requests

### Monitoring and logging

**CloudWatch Logs:**

- All Lambda functions log to CloudWatch
- Flink applications log to CloudWatch
- API Gateway logs all requests
- Default log retention: 90 days

**CloudTrail:**

- All API calls are logged to CloudTrail
- CloudTrail logs stored in S3 with encryption
- Log file integrity validation enabled

### Compliance

This solution uses AWS services that support various compliance programs:

- SOC 1, 2, 3
- PCI DSS Level 1
- ISO 27001, 27017, 27018
- HIPAA eligible services
- GDPR compliant

For the most current compliance information, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

## Quotas

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

### Service quotas to verify

Before deploying the guidance, verify you have sufficient quotas for the following services:

**Amazon MSK:**

- Clusters per Region: Default 20 (need 1)
- Brokers per cluster: Default 30 (need 3)
- Configuration revisions: Default 50

**Amazon Kinesis Data Analytics:**

- Applications per Region: Default 50 (need 3-5)
- KPUs per application: Default 32 (need 1-4)

**AWS IoT Core:**

- Things per account: Default 500,000
- Certificates per account: Default 500,000
- Policies per account: Default 1,000
- Message broker connections: Default 500,000

**Amazon DynamoDB:**

- Tables per Region: Default 2,500 (need 4)
- On-demand read/write capacity: No limit

**AWS Lambda:**

- Concurrent executions: Default 1,000
- Function storage: Default 75 GB

**Amazon VPC:**

- VPCs per Region: Default 5 (need 1)
- Subnets per VPC: Default 200 (need 4)
- Security groups per VPC: Default 2,500
- NAT gateways per AZ: Default 5 (need 2)

**Amazon ElastiCache:**

- Nodes per Region: Default 300 (need 1)
- Clusters per Region: Default 300 (need 1)

### Requesting quota increases

If you need to increase service quotas:

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/")
2. Select the service
3. Select the quota
4. Choose **Request quota increase**
5. Enter the new quota value
6. Submit the request

Most quota increases are processed within 24-48 hours.

## Deployment sizing

### Small fleet (100-1,000 vehicles)

**Recommended configuration:**

- MSK: 3 × kafka.t3.small brokers
- ElastiCache: cache.t3.micro
- Flink: 1 KPU per application
- DynamoDB: On-demand billing

**Expected cost:** ~$250-300/month

**Telemetry capacity:**

- Messages per second: ~100-500
- Daily messages: ~8-40 million
- Storage per month: ~10-50 GB

### Medium fleet (1,000-10,000 vehicles)

**Recommended configuration:**

- MSK: 3 × kafka.m5.large brokers
- ElastiCache: cache.t3.small
- Flink: 2 KPUs per application
- DynamoDB: On-demand billing

**Expected cost:** ~$410-600/month

**Telemetry capacity:**

- Messages per second: ~500-2,000
- Daily messages: ~40-170 million
- Storage per month: ~50-200 GB

### Large fleet (10,000+ vehicles)

**Recommended configuration:**

- MSK: 6 × kafka.m5.xlarge brokers
- ElastiCache: cache.r6g.large (cluster mode)
- Flink: 4 KPUs per application
- DynamoDB: Provisioned capacity with auto-scaling

**Expected cost:** ~$1,200-2,000/month

**Telemetry capacity:**

- Messages per second: ~2,000-10,000
- Daily messages: ~170-860 million
- Storage per month: ~200-1,000 GB

### Performance considerations

**Message throughput:**

- Each MSK broker handles ~1,000 messages/second
- Flink applications process ~2,000 messages/second per KPU
- DynamoDB on-demand scales automatically

**Latency targets:**

- IoT Core to MSK: <100ms
- MSK to Flink: <500ms
- Flink to DynamoDB: <200ms
- API response time: <500ms
- ElastiCache lookup: <10ms

**Scaling triggers:**

- MSK CPU > 70%: Add brokers
- Flink lag > 60 seconds: Add KPUs
- DynamoDB throttling: Increase capacity
- ElastiCache CPU > 75%: Upgrade node type

## Disaster recovery

### Backup strategy

**Automated backups:**

- DynamoDB: Point-in-time recovery enabled (35 days)
- S3: Versioning enabled on all buckets
- MSK: Automatic snapshots (not exposed to users)

**Manual backups:**

- Export DynamoDB tables to S3 for long-term retention
- Backup IoT certificates and policies
- Export Cognito user pool configuration

### Recovery time objectives

**RTO (Recovery Time Objective):**

- Phase 1-2 recovery: 10-15 minutes
- Phase 3 recovery (MSK): 15-20 minutes
- Phase 5 recovery (Flink): 5-10 minutes
- Full stack recovery: 40-60 minutes

**RPO (Recovery Point Objective):**

- DynamoDB: Up to 5 minutes (PITR)
- S3: Zero data loss (versioning)
- Telemetry in-flight: Up to 5 minutes

### Multi-region considerations

For high availability across regions:

- Deploy solution in multiple regions
- Use Route 53 for DNS failover
- Replicate DynamoDB tables with Global Tables
- Use S3 Cross-Region Replication for archives
- Configure IoT Core custom domains for failover

###### Note

Multi-region deployment increases costs by 2-3x but provides geographic redundancy and lower latency for global fleets.
