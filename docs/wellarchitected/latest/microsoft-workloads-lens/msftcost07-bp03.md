# MSFTCOST07-BP03 Change your scale strategy for Windows

Containers on Kubernetes using Karpenter

Karpenter is a Kubernetes cluster autoscaler that dynamically
provisions EC2 instances based on your workload demands,
automatically launching right-sized instances in response to pending
pods and continuously evaluating the cluster to optimize costs by
consolidating workloads onto more efficient instance types. The tool
proactively replaces outdated nodes with newer ones to maintain
security compliance and supports diverse compute requirements by
selecting from a broad range of instance types and purchasing
options, including both On-Demand and Spot instances.

**Desired outcome:** Expect to
achieve improved resource utilization, reduced operational overhead,
and optimized cloud costs. EKS clusters will dynamically scale to
meet application demands, maintain up-to-date and secure
infrastructure, and efficiently manage diverse workloads without
manual intervention, ultimately leading to a more responsive,
cost-effective, and easily managed Kubernetes environment on AWS.

**Common anti-patterns:**

- Teams often configure Karpenter with unnecessarily specific
  instance type constraints or narrow capacity requirements,
  limiting its ability to efficiently provision nodes and
  potentially increasing costs by forcing the use of suboptimal
  instance types.
- Organizations frequently deploy Karpenter without properly
  configuring Pod Disruption Budgets (PDBs), leading to unexpected
  application downtime during node consolidation or replacement
  operations, as Karpenter may terminate nodes without ensuring
  proper workload migration.

**Benefits of establishing this best
practice:**

- By allowing Karpenter to intelligently select from a broad range
  of instance types and automatically consolidate workloads,
  organizations can significantly reduce their AWS compute costs
  while maintaining optimal performance for their applications.
- Teams spend less time on manual cluster management and capacity
  planning, as Karpenter automates node provisioning, scaling, and
  replacement activities, enabling engineers to focus on
  higher-value development tasks.
- With Karpenter's automated node replacement feature, clusters
  maintain better security hygiene through regular updates and
  patches, reducing the risk of vulnerabilities while ensuring
  compliance with security standards without manual intervention.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement Karpenter effectively, define flexible provisioner
configurations that accommodate both Linux and Windows workloads,
ensuring appropriate instance types are available for each OS. Set
up distinct provisioners with OS-specific requirements, configure
Pod Disruption Budgets for critical applications, and establish
proper taints and tolerations to ensure workloads land on
compatible nodes. Regularly monitor cluster behavior and costs to
optimize your configuration.

### Implementation steps

1. Install and configure Karpenter in your EKS cluster,
   ensuring proper IAM permissions and VPC settings
2. Create flexible provisioner configurations for both Linux
   and Windows workloads, specifying appropriate instance types
   and purchasing options
3. Set up Pod Disruption Budgets for critical applications to
   maintain availability during node consolidation
4. Configure monitoring and alerting to track Karpenter's
   performance and cluster resource utilization
5. Regularly review and adjust Karpenter settings based on
   observed cluster behavior and cost metrics

## Resources

**Related documents:**

- [Karpenter](../../../eks/latest/best-practices/karpenter.md "../../../eks/latest/best-practices/karpenter.md")
- [Getting
  Started with Karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/ "https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/")
