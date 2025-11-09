# Virtual Private Cloud (VPC)

The guidance deploys a dedicated VPC with public and private subnets across multiple Availability Zones, providing network isolation and high availability for the MSK cluster and Flink applications.

**VPC Architecture**:

- **CIDR Block**: 10.0.0.0/16 (65,536 IP addresses)
- **Availability Zones**: 2 AZs for high availability and fault tolerance
- **Private Subnets**: /24 subnets (256 IPs each) for MSK brokers and Flink applications
- **Public Subnets**: /24 subnets for NAT gateways and bastion hosts
- **NAT Gateway**: Single NAT gateway for cost optimization (1 per AZ recommended for production)

**Network Isolation**:

- **MSK Cluster**: Deployed in private subnets with no direct internet access
- **Flink Applications**: Deployed in same private subnets as MSK for low-latency connectivity
- **Outbound Internet**: Routed through NAT gateway for software updates and AWS service access
- **VPC Endpoints**: Optional VPC endpoints for S3, DynamoDB, and Secrets Manager to avoid NAT gateway costs

**Security Groups**:

- **MSK Security Group**:
  **Port 9092: Kafka PLAINTEXT (disabled in production)**Port 9094: Kafka TLS (mTLS disabled for simplicity)
  **Port 9096: Kafka SASL_SCRAM (IoT Core access)**Port 9098: Kafka SASL_IAM (Flink access)
  **Self-referencing rule: Allows broker-to-broker communication**Source CIDR: 10.0.0.0/8 (private IP ranges only)
- **Flink Security Group**:
  **Outbound: All traffic allowed for MSK, DynamoDB, S3 access**Inbound: No inbound rules required (Flink initiates all connections)

**Network ACLs**:

- Default VPC NACLs allow all traffic
- Custom NACLs can be configured for additional security layers
- Recommended: Allow only necessary ports (9096, 9098, 443) for production

**Scalability**:

- **Subnet Sizing**: /24 subnets support 251 usable IPs (sufficient for 100+ brokers and Flink tasks)
- **VPC Expansion**: Additional subnets can be added without downtime
- **Multi-Region**: Deploy separate VPCs in multiple regions for disaster recovery
- **VPC Peering**: Connect to existing VPCs for hybrid architectures

**Cost Optimization**:

- **Single NAT Gateway**: $0.045/hour (~$32/month) for dev/test environments
- **Multi-AZ NAT**: Deploy NAT gateway per AZ for production high availability
- **VPC Endpoints**: Eliminate NAT gateway data transfer costs for S3 and DynamoDB access
- **Data Transfer**: Intra-AZ traffic is free; cross-AZ traffic is $0.01/GB
