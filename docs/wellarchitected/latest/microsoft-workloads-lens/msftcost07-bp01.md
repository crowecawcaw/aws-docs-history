# MSFTCOST07-BP01 Optimize AWS Fargate tasks with AWS Compute Optimizer

AWS Compute Optimizer can be used to help right size and optimize your workloads running on
AWS Fargate. If not reviewed, long running tasks can be overprovisioned and increase compute
costs.

**Desired outcome:** Aim to achieve optimal resource allocation and
cost efficiency. Right-size our Fargate tasks, avoiding overprovisioning and reducing
unnecessary compute costs. Through regular review and implementation of Compute Optimizer's recommendations,
we expect to maintain well-optimized workloads that balance performance and cost-effectiveness,
ultimately leading to improved resource utilization and significant cost savings in our AWS
environment.

**Common anti-patterns:**

- Deploying Fargate tasks with initial resource configurations and never reviewing or
  adjusting them over time, ignoring Compute Optimizer's recommendations and missing significant cost
  optimization opportunities.
- Deliberately configuring Fargate tasks with excessive CPU and memory as a
  precautionary measure, leading to consistent overprovisioning and unnecessary costs despite
  Compute Optimizer showing opportunities for right-sizing.

**Benefits of establishing this best practice:**

- Regular review and implementation of Compute Optimizer recommendations leads to right-sized
  Fargate tasks, eliminating waste from overprovisioning and reducing monthly compute costs
  while maintaining required performance levels.
- Leveraging Compute Optimizer's ML-powered analytics provides objective, metrics-based insights for
  resource allocation decisions, replacing guesswork with actual usage patterns and ensuring
  optimal task configurations across your workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Enable AWS Compute Optimizer for your organization or account. Establish a monthly review process for
Fargate task recommendations. Implement changes gradually, starting with non-production
workloads. Monitor performance before and after optimizations. Create a feedback loop to
inform future deployments, and consider automating recommendation implementation through
Infrastructure as Code practices for consistency and efficiency.

### Implementation steps

1. Enable AWS Compute Optimizer in your environment through the AWS Management Console and verify it begins
   collecting task utilization data for analysis.
2. Schedule monthly review meetings with relevant stakeholders to assess Compute Optimizer's
   Fargate task recommendations and prioritize which optimizations to implement.
3. Create a change management process that includes testing optimizations in
   non-production environments first, with clear rollback procedures if needed.
4. Implement approved recommendations through your existing Infrastructure as Code
   (IaC) framework, ensuring changes are tracked and reproducible.
5. Set up CloudWatch dashboards or alerts to monitor performance metrics post-optimization,
   ensuring the changes maintain desired service levels while achieving cost savings.

## Resources

**Related documents:**

- [Optimize costs for AWS Fargate tasks on Amazon ECS](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.md")

**Related tools:**

- [What is
  AWS Compute Optimizer?](../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md "../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md")
