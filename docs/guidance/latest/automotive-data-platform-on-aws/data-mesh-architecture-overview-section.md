# Architecture overview

The Automotive Data Mesh follows a domain-oriented decentralized architecture with centralized governance.

![Automotive Data Mesh Architecture](/images/guidance/latest/automotive-data-platform-on-aws/images/mesh.png)

## High-Level Architecture

The architecture consists of:

1. **Foundation Layer**: VPC networking with private subnets and VPC endpoints
2. **Catalog Layer**: DataZone domain for data asset management
3. **Compute Layer**: Distributed processing across Glue, SageMaker, Athena, and EMR
4. **Governance Layer**: Centralized policies with federated enforcement
5. **Collaboration Layer**: DataZone V2 producer/consumer projects for team workspaces and subscription workflows

## Multi-Source Data Integration

The platform integrates data from diverse automotive sources:

- **Vehicle Telemetry**: IoT Core for real-time data, S3 for historical data
- **Customer Data**: CRM systems, service records, interaction history
- **Sales and Inventory**: Dealer management systems, supply chain data
- **External Data**: Weather, traffic, maps, and third-party enrichment
- **Operational Data**: Manufacturing, logistics, warranty claims

## Networking Architecture

Secure, private networking foundation:

- **VPC with 3 Availability Zones**: High availability and fault tolerance
- **Private Subnets**: All compute resources in private subnets
- **NAT Gateway**: Controlled outbound internet access
- **VPC Endpoints**: Private connectivity to AWS services (S3, Glue, SageMaker, Athena, Redshift, etc.)
- **Security Groups**: Fine-grained network access control
- **Network Isolation**: Separation between data domains
