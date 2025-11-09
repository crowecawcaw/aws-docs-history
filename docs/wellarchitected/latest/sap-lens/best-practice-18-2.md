# Best Practice 18.2 – Use cost as a key

consideration for EC2 instance selection

By selecting the appropriate SAP Certified EC2 instances for your workload, it is
possible to optimize for cost. Perform a thorough analysis of each system, ensuring that
decisions are data driven where possible. Generic guidance can be found in the
Well-Architected Framework [Cost Optimization Pillar - Cost-Effective Resources](../framework/a-cost-effective-resources.md "../framework/a-cost-effective-resources.md").

**Suggestion 18.2.1 – Select the latest generation instances available
within your Region**

The latest generation of Amazon EC2 instances often offers the lowest cost with
better performance and should be used if available and certified for the deployment
scenario.

- AWS Documentation: [Amazon EC2 Instance Types for SAP](../../../sap/latest/general/ec2-instance-types-sap.md "../../../sap/latest/general/ec2-instance-types-sap.md") (includes how to check for instance type
  availability)

###### Note

Some Amazon EC2 instance families (for example `X1` and High Memory) might not
be available across all Availability Zones within a Region. During planning, confirm that
the instance types you require for your SAP workload are available in your target
Availability Zones.

**Suggestion 18.2.2 – Balance cost with performance
requirements**

Each SAP supported Amazon EC2 instance family will provide specific performance measured
in [SAPS](<https://www.sap.com/about/benchmark/measuring.html#:~:text=SAP%20Application%20Performance%20Standard%20(SAPS)%20is%20a%20hardware%2Dindependent,order%20line%20items%20per%20hour.> "https://www.sap.com/about/benchmark/measuring.html#:~:text=SAP%20Application%20Performance%20Standard%20(SAPS)%20is%20a%20hardware%2Dindependent,order%20line%20items%20per%20hour."). You should evaluate each instance family based on your performance
requirements. An understanding of the cost per SAPS and cost per GiB ratios is recommended.

| Compute-optimized (`C*`) | General Purpose (`M*`) | Memory-optimized (`R*`) |
| ------------------------ | ---------------------- | ----------------------- |
| 1 vCPU: 2 GiB            | 1 vCPU: 4 GiB          | 1 vCPU: 8 GiB           |

If a workload component requires more memory over [SAPS](<https://www.sap.com/about/benchmark/measuring.html#:~:text=SAP%20Application%20Performance%20Standard%20(SAPS)%20is%20a%20hardware%2Dindependent,order%20line%20items%20per%20hour.> "https://www.sap.com/about/benchmark/measuring.html#:~:text=SAP%20Application%20Performance%20Standard%20(SAPS)%20is%20a%20hardware%2Dindependent,order%20line%20items%20per%20hour.") (CPU), you should select the instance family that provides the lowest cost
per GiB memory. If the component requires more SAPS (CPU) over memory, you should select
the instance family that provides the lowest cost per SAPS.

SAP Certified instance families powered by an AMD processor typically provide a 10%
cost saving over the comparable Intel-based EC2. For example, the `C5a` is 10%
lower cost than the `C5` family for the same performance KPIs.

For non-production SAP HANA workloads consider using one of the instance families
that meets the requirements detailed in SAP Note: [2271345 - Cost-Optimized SAP
HANA Hardware for Non-Production Usage](https://launchpad.support.sap.com/#/notes/2271345 "https://launchpad.support.sap.com/#/notes/2271345") [Requires SAP Portal Access].

**Suggestion 18.2.3 – Review the predictability of your growth profile
and peak capacity requirements**

An existing SAP landscape on AWS or a homogeneous migration is likely to have more
predictable growth and usage patterns than a new greenfield implementation or
heterogeneous migration.

For systems where you lack data on historical growth, you should consider the cost
benefits of selecting an EC2 instance size sufficient for the short or medium term growth.
Plan to scale the instance size as your requirement changes. You should ensure that your
architecture design provides the flexibility to move between different EC2 instance
families as your resource consumption changes.

Similarly, you should evaluate that changes to peak capacity have been accounted
for.

When sizing an SAP HANA environment consider not only the database size but also the
working memory requirement. Consult SAP HANA sizing reports and tools to estimate your
size and usage.

**Suggestion 18.2.4 – Consider instance commitment
flexibility**

When a component (for example, SAP HANA database) needs to scale up during the
commitment period, evaluate if this will result in moving to a different instance family.
This will impact your pricing model selection.

- AWS Documentation: [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/")
