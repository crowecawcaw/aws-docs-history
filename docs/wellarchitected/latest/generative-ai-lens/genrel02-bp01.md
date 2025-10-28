# GENREL02-BP01 Implement redundant network connections between

model endpoints and supporting infrastructure

Implement network connection redundancy between components in your
generative AI application.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by reducing the likelihood of performance
degradation due to network configuration.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](../framework/rel-dp.md "../framework/rel-dp.md")
across multiple components using a reliable network backbone.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Deploy your generative AI application across multiple subnets within
a VPC. Use AWS PrivateLink or a similar network technology to
facilitate secure, private network communications between VPC-hosted
applications and other AWS services. Use a multi-AZ architecture,
with applications deployed across at least two Availability Zones.
In addition to deploying applications with high availability, deploy
vector databases and agentic systems across multiple Availability
Zones as well. With vector database solutions like Amazon OpenSearch Service
Serverless, customers can configure their OpenSearch cluster
deployment across multiple Availability Zones, creating VPC
Endpoints to have reliable network connectivity to the cluster.
Similar considerations should be extended to agentic workflows. On
Amazon Bedrock, agent workflows make calls to API endpoints and AWS Lambda functions. Consider deploying these capabilities in a
multi-AZ deployment as well.

For multi-Region deployments, continue deploying resources into
VPCs, but consider using one of the various multi-Region VPC
communication services to facilitate secure, reliable network
connectivity for your services and applications. Customers can use
network configuration tools like VPC peering, AWS Transit Gateway,
or Amazon VPC Lattice to connect their applications and services in
VPCs across Regions. Consider combining this capability with Amazon Bedrock's cross-Region inference capabilities for high availability
network connectivity across Regions.

### Implementation steps

1. Determine the VPCs that host complementary systems for your
   generative AI workload.
   - Develop reliable network communications across (for
     example, VPC peering, VPC Lattice, or Transit Gateway).

2. Create private network connections across the various service
   and application endpoints in consideration.
3. Ensure private network connections are replicated across
   subnets in multiple Availability Zones within a Region.
   - Consult a network specialist for multi-Region deployments
     which suit your architecture requirements. Consider using
     Amazon VPC Lattice, Amazon Transit Gateway, or other
     cross-Region networking solutions to facilitate network
     traffic.

## Resources

**Related practices:**

- [REL02-BP01](../reliability-pillar/rel_planning_network_topology_ha_conn_users.md "../reliability-pillar/rel_planning_network_topology_ha_conn_users.md")
- [REL02-BP02](../reliability-pillar/rel_manage_service_limits_limits_considered.md "../reliability-pillar/rel_manage_service_limits_limits_considered.md")

**Related guides, videos, and documentation:**

- [Securely Access Services Over AWS PrivateLink](../../../whitepapers/latest/aws-privatelink/aws-privatelink.md "../../../whitepapers/latest/aws-privatelink/aws-privatelink.md")

**Related examples:**

- [Use AWS PrivateLink to set up private access to Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/use-aws-privatelink-to-set-up-private-access-to-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/use-aws-privatelink-to-set-up-private-access-to-amazon-bedrock/")
- [Overseeing
  AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/ "https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/")
