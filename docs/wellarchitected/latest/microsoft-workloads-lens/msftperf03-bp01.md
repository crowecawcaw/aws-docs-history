# MSFTPERF03-BP01 Consider Amazon EBS gp3 volumes for general

workloads

Amazon EBS's newest and most cost-effective SSD option, General
Purpose SSD (gp3) volumes, strikes an optimal balance between price
and performance for a wide range of applications. A key advantage of
gp3 volumes is the ability to adjust performance independently of
storage capacity, allowing users to meet specific performance
requirements without unnecessarily increasing block storage.
Moreover, gp3 volumes offer significant cost savings, with prices
20% lower per GiB compared to their predecessor, General Purpose SSD
(gp2) volumes.

**Desired outcome:** Optimize storage
performance and cost efficiency for Microsoft workloads by
leveraging gp3 volumes that provide independent scaling of IOPS and
throughput from storage capacity, enabling right-sized storage
configurations that meet performance requirements while minimizing
costs.

**Common anti-patterns:**

- Continuing to use gp2 volumes without evaluating gp3 benefits,
  missing opportunities for cost savings and performance
  optimization through independent IOPS and throughput scaling.
- Over-provisioning storage capacity to meet IOPS requirements
  when using gp2 volumes, leading to unnecessary storage costs
  that could be avoided with gp3's independent performance
  scaling.
- Choosing high-performance storage options like io1/io2 for
  workloads that could be adequately served by gp3 with
  appropriate IOPS configuration, resulting in unnecessary costs.

**Benefits of establishing this best
practice:**

- Significant cost savings through 20% lower per-GiB pricing
  compared to gp2 volumes while maintaining or improving
  performance characteristics for Microsoft workloads.
- Enhanced flexibility through independent scaling of IOPS and
  throughput from storage capacity, enabling optimal resource
  allocation without over-provisioning storage.
- Improved performance predictability through consistent baseline
  performance and the ability to provision additional IOPS and
  throughput as needed for specific workload requirements.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing gp3 volumes for Microsoft workloads requires
understanding your storage performance requirements and migrating
from existing volume types where appropriate. Focus on workloads
that can benefit from independent IOPS and throughput scaling
while achieving cost savings.

### Implementation steps

1. Analyze current storage performance requirements for
   Microsoft workloads including IOPS, throughput, and capacity
   needs.
2. Identify existing gp2 volumes and other storage types that
   could benefit from migration to gp3 for cost and performance
   optimization.
3. Plan gp3 volume configurations with appropriate baseline
   performance and additional provisioned IOPS or throughput
   based on workload requirements.
4. Test gp3 performance in non-production environments to
   validate performance characteristics for your specific
   Microsoft applications.
5. Implement migration procedures for existing volumes using
   EBS volume modification or snapshot-based migration
   approaches.
6. Monitor storage performance and costs after migration to
   validate expected benefits and optimize configurations as
   needed.
7. Establish policies for new volume provisioning that default
   to gp3 unless specific requirements dictate alternative
   storage types.
8. Document gp3 configuration standards and include in storage
   provisioning procedures for consistent implementation across
   environments.

## Resources

**Related documents:**

- [General
  Purpose SSD (gp3) volumes](../../../ebs/latest/userguide/general-purpose.md#gp3-ebs-volume-type "../../../ebs/latest/userguide/general-purpose.md#gp3-ebs-volume-type")

**Related tools:**

- [Migrate
  Amazon EBS volumes from gp2 to gp3](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.md")
