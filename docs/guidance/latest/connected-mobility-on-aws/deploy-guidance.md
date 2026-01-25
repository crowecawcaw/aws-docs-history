# Deploy the guidance

The guidance provides both interactive and manual deployment options. The interactive wizard is recommended for first-time deployments.

**Interactive Deployment Wizard**

Run the interactive deployment command:

```
make deploy
```

The wizard guides you through three configuration steps:

**Step 1: AWS Profile Selection**

```
Available AWS Profiles:
0       default
1       dev-account
2       prod-account

Select profile number (0 for default): 1
✅ Selected profile: dev-account
```

**Step 2: Deployment Stage Selection**

```
Deployment Stage Options:
1. dev (cms-dev-*)
2. prod (cms-prod-*)
3. Custom stage name

Select deployment stage (1-3): 1
✅ Selected stage: dev
```

**Step 3: Phase Selection**

```
Deployment Options:
0. Infrastructure Foundation (~5 min)
1. Fleet Manager Interface (~15 min)
2. Fleet Management Interface (~5 min)
3. Telemetry Pipeline - MSK (~20 min)
4. Telemetry Pipeline - MSK Config (~5 min)
5. Telemetry Pipeline - Flink (~10 min)
6. Telemetry Pipeline - Flink Config (~8 min)
7. Complete Configuration (~5 min)
8. Deploy All Phases (~63 min)

Select deployment option (0-8): 8
🚀 Deploying All Phases
```

The wizard then displays real-time progress for each phase with status indicators and deployment details.

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
