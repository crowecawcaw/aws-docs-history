# AOSREL05-BP01 Implement appropriate compute sizing for

production workloads

Improve OpenSearch Service domain performance by implementing
compute sizing that meets production workload requirements. This
practice helps you avoid CPU throttling due to depleted burst
credits and minimize risks.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: Your OpenSearch Service domain is running on instance families that meet
the required performance and resource needs.

**Benefits of establishing this best
practice:**

- Avoid CPU throttling if burst credits are depleted
- Improve your ability to maintain performance and minimize risks

## Implementation guidance

Avoid using t2 or t3.small instances for production domains, as
they can become unstable under sustained heavy load. t3.medium
instances are an option for small production workloads (both as
data nodes and as dedicated leader nodes).

## Resources

- [Operational
  best practices for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/bp.md#bp-cost-optimization-instances "../../../opensearch-service/latest/developerguide/bp.md#bp-cost-optimization-instances")
