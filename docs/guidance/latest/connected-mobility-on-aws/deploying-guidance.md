# Deploying this Guidance on AWS

This Guidance uses AWS CDK (Cloud Development Kit) for infrastructure as code deployment. The guidance is organized into six phases that can be deployed incrementally:

**Phase 1: Fleet Manager Interface (~15 minutes)** - Deploys the core fleet management interface with AWS IoT Core, DynamoDB, S3, Lambda, Cognito, and CloudFront. Provides complete fleet management UI for vehicle registration, driver assignment, and basic monitoring.

**Phase 2: Historical Data Population (~5 minutes)** - Populates fleet management tables with sample data for demonstration and testing. Enables full UI functionality without requiring physical vehicles.

**Phase 3: Telemetry Infrastructure (~20 minutes)** - Deploys Amazon MSK cluster with VPC, security groups, and encryption. Establishes Kafka infrastructure for real-time telemetry processing.

**Phase 4-6: Stream Processing (~23 minutes)** - Deploys Apache Flink applications for telemetry decoding, trip aggregation, safety event detection, and maintenance alerts. Completes the full connected mobility guidance.

The phased approach provides several benefits:

- **Reduced Initial Complexity** - Start with basic fleet management before adding real-time processing
- **Faster Time-to-Value** - Deploy Phase 1-2 in 20 minutes for immediate fleet management capabilities
- **Operational Learning** - Build team expertise with simpler components before scaling to full production
- **Cost Control** - Deploy only the capabilities needed for current requirements
- **Risk Mitigation** - Validate each phase before proceeding to more complex components
  Organizations can deploy all phases at once for complete functionality or deploy incrementally based on their maturity and requirements.
