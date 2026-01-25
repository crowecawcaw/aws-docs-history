# Deployment phases

**Phase 0: Infrastructure Foundation (~5 minutes)**

Deploys VPC, subnets, security groups, and ElastiCache Redis cluster.

```
make infrastructure AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 1: Fleet Manager Interface (~15 minutes)**

Deploys IoT Core, DynamoDB tables, S3 buckets, Lambda functions, Cognito user pools, and CloudFront distribution with React UI.

```
make phase1 AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 2: Fleet Management Interface (~5 minutes)**

Seeds DynamoDB tables with sample fleet data and configures historical data injection.

```
make phase2 AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 3: MSK Deployment (~20 minutes)**

Deploys Amazon MSK cluster with VPC configuration, security groups, and KMS encryption.

```
make phase3 AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 3b: MSK Configuration (~5 minutes)**

Associates SCRAM secrets with MSK, creates VPC destination, and deploys IoT rule for telemetry routing.

```
make phase3b AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 4: Flink Deployment (~10 minutes)**

Deploys 5 Flink applications: EventDriven, Enhanced, Trip, Safety, and Maintenance processors.

```
make phase4 AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 5: Flink Configuration (~8 minutes)**

Builds JAR from source, uploads to S3, configures applications with MSK bootstrap servers, IAM authentication, VPC settings, and starts all applications.

```
make phase5 AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phase 6: Complete Configuration (~5 minutes)**

Runs final integration scripts and validates end-to-end pipeline.

```
make phase6 AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Deploy All Phases (~63 minutes)**

Sequential deployment of all phases from 0-7.

```
make deploy-all AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Phased Deployment Approach**

The guidance uses a phased deployment strategy to manage complexity and dependencies. Each phase builds upon the previous one, ensuring proper resource availability and configuration.

**Why Infrastructure First?**

Phase 0 (Infrastructure Foundation) must be deployed first because it creates the foundational networking and caching resources that all other services depend on:

- VPC and Subnets: Provides network isolation and IP address space for MSK, Flink, and other services
- Security Groups: Establishes firewall rules before deploying services that need them
- ElastiCache Redis: Provides high-performance caching for real-time vehicle state (updated every 5 seconds)
- NAT Gateways: Enables private subnet resources to access AWS services and the internet
  Without this foundation, subsequent phases would fail because:

- MSK requires VPC and subnets to deploy brokers
- Flink applications need VPC configuration to connect to MSK
- IoT Core VPC destinations require existing VPC resources
- Lambda functions and APIs benefit from Redis caching for sub-100ms response times

**Deployment Order Logic**

The phases follow this dependency chain:

1. Infrastructure → Networking foundation for all services
2. Storage → DynamoDB tables and S3 buckets for data persistence
3. IoT → Device connectivity and certificate management (depends on Storage for metadata)
4. UI → User interface and authentication (depends on Storage and IoT for data access)
5. MSK → Message streaming backbone (depends on Infrastructure VPC)
6. Telemetry Integration → IoT-to-MSK routing (depends on both IoT and MSK)
7. Flink → Stream processing applications (depends on MSK and Storage)
8. Configuration → Final wiring and validation (depends on all previous phases)
   This approach allows you to:

- Deploy incrementally: Test each layer before adding the next
- Troubleshoot easily: Isolate issues to specific phases
- Scale independently: Add telemetry processing later without redeploying the UI
- Understand architecture: See how components connect in deployment order
