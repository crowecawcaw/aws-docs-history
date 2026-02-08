# MSFTCOST07-BP02 Improve Amazon Elastic Kubernetes Service cost

tracking with Kubecost

Kubecost improves the cost tracking for your Windows containers.
Kubecost helps right sizing cluster nodes, container requests, and
manages underutilized infrastructure.

**Desired outcome:** Aim to achieve
improved cost tracking for our Windows containers. The desired
outcome is to optimize cluster resource utilization through
right-sizing of nodes and container requests, while effectively
managing underutilized infrastructure. This implementation may
provide better visibility into EKS costs, enabling more informed
decision-making and ultimately leading to cost savings in Kubernetes
deployments.

**Common anti-patterns:**

- Lack of cost monitoring tools, leading to untracked spending and
  no visibility into workload-specific costs across Amazon Elastic Kubernetes Service (EKS) clusters.
- Blindly overprovisioning Windows container resources without
  usage data, resulting in unnecessary infrastructure costs and
  resource waste.

**Benefits of establishing this best
practice:**

- Gain detailed insights into container-level expenses, enabling
  accurate cost allocation across teams, projects, and workloads.
- Identify and right-size underutilized resources, leading to
  significant cost savings and improved cluster efficiency for
  Windows containers.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start by deploying Kubecost into your environment. Configure it to
integrate with your EKS cluster and AWS Cost and Usage Reports.
Set up proper tagging for resources to ensure accurate cost
allocation. Regularly review Kubecost dashboards to identify
cost-saving opportunities, such as right-sizing nodes and
optimizing container requests. Use Kubecost's recommendations to
adjust resource allocations and implement cost controls.
Continuously monitor and refine your cost optimization strategy
based on the insights provided by Kubecost.

### Implementation steps

1. Deploy Kubecost to your EKS clusters, ensuring proper IAM
   roles and permissions are configured
2. Set up AWS Cost and Usage Report integration and configure
   Kubecost to access your billing data
3. Implement a comprehensive resource tagging strategy to
   accurately track costs across teams and applications
4. Configure alerts and thresholds for cost anomalies and
   resource utilization metrics
5. Review initial baseline metrics and identify immediate
   optimization opportunities for Windows containers
6. Establish regular review cycles to analyze Kubecost reports
   and implement recommended optimizations

## Resources

**Related documents:**

- [Gain
  visibility into your Amazon EKS costs](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/kubecost-main.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/kubecost-main.md")
- [Learn
  more about Kubecost](../../../eks/latest/userguide/cost-monitoring-kubecost-bundles.md "../../../eks/latest/userguide/cost-monitoring-kubecost-bundles.md")
