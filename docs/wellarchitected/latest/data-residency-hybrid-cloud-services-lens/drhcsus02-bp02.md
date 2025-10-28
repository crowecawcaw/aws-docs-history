# DRHCSUS02-BP02 Before ordering an AWS Outpost, engage with an AWS Outposts specialist to verify that the ordered capacity aligns with your workload requirements

Care should be given to aligning AWS Outposts capacity to actual
resource requirements before placing an order to avoid
overprovisioning capacity that cannot be scaled down after
deployment.

**Desired outcome:** Outposts
configurations will be developed to address workload requirement
while minimizing overprovisioning of capacity

**Benefits of establishing this best
practice:** Only the capacity needed to support your
workload and resiliency requirements will be ordered, minimizing
energy consumption.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS Outposts provide fixed and finite capacity which cannot be
quickly scaled to accommodate changes in demand. Outposts are
instead configured to meet your unique data-residency
requirements, and it is important to work with your AWS account
team to engage AWS hybrid specialists to verify that both
workload and sustainability requirements are considered to
develop the most efficient Outposts configuration before
ordering.

Because Outposts are frequently used to migrate existing
physical or virtual workloads from on-premises data-centers, and
because these workloads are commonly over-provisioned, use tools
such as the
[AWS Migration Evaluator](https://aws.amazon.com/migration-evaluator/getting-started/ "https://aws.amazon.com/migration-evaluator/getting-started/") to correctly size Outposts for the
actual observed demand, plus any margin for resiliency and
growth.
