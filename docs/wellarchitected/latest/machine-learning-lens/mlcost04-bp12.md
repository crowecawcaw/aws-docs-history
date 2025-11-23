# MLCOST04-BP12 Set up a budget and use resource tagging to track

costs

Setting up budgets and implementing resource tagging for machine
learning workloads provides clear visibility into your ML-related
expenses and optimizes costs across your organization. By tracking
costs effectively, you can make data-driven decisions about resource
allocation and identify opportunities for cost optimization.

**Desired outcome:** You gain
complete visibility into your machine learning costs across
development, training, and production environments. You can track
expenses by project, business unit, or environment, allowing for
accurate cost allocation and forecasting. Through tagging and
budgeting tools, you can proactively manage your ML spending,
receive alerts before exceeding budgeted amounts, and make informed
decisions about resource provisioning and termination.

**Common anti-patterns:**

- Running ML workloads without cost monitoring mechanisms in
  place.
- Using generic cost tracking that doesn't differentiate between
  ML projects or environments.
- Failing to tag ML resources consistently, making cost allocation
  difficult.
- Ignoring budget alerts or failing to take action when exceeding
  thresholds.

**Benefits of establishing this best
practice:**

- Clear visibility into where ML spending occurs across your
  organization.
- Ability to accurately allocate costs to specific projects or
  business units.
- Early warning through alerts when costs exceed or are forecasted
  to exceed budgeted amounts.
- Improved governance and financial accountability for ML
  initiatives.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Cost management is a critical aspect of running machine learning
workloads in the cloud. Without proper cost tracking and budget
controls, ML expenses can quickly escalate due to
compute-intensive training jobs, large storage requirements for
datasets, and continuous inference endpoints. By implementing
comprehensive budgeting and tagging strategies, you gain
visibility and control over these costs.

AWS provides several tools that work together to track, analyze,
and optimize your ML costs. AWS Budgets allows you to set custom
budgets for your SageMaker AI resources, while AWS Cost Explorer
provides visualization and analysis capabilities to understand
spending patterns. Resource tagging serves as the foundation for
detailed cost tracking, enabling you to categorize expenses by
project, team, environment, or other dimension important to your
organization.

For example, you might tag resources related to a fraud detection
model with a Project tag value of
FraudDetection and an
Environment tag value of
Production. This allows you to track the total
cost of this specific ML use case across its components, from
development notebooks to training jobs to deployment endpoints.

### Implementation steps

1. **Set up AWS Budgets for ML cost
   tracking**. Create customized budgets in AWS
   Budgets to monitor your Amazon SageMaker AI costs across
   development, training, and hosting. Configure the budget to
   track specific services (such as SageMaker AI) or specific
   tagged resources. Set thresholds for actual costs and
   forecasted costs to receive notifications before you exceed
   your budget. This gives you time to make adjustments to your
   resource usage if needed. Access your budgets through the
   [AWS Budgets console](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/") to track progress and make
   adjustments as necessary.
2. **Implement a tagging strategy for ML
   resources**. Develop a consistent tagging strategy
   for all your ML resources. Define mandatory tags such as
   Project, BusinessUnit, Environment (dev/test/prod), and
   Owner. Document your tagging standards and verify that team
   members understand and follow these standards. Apply these
   tags to relevant resources, including
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") notebook instances, training jobs, models,
   endpoints, and related resources like
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") buckets for dataset storage.
3. **Activate cost allocation
   tags**. After implementing your tagging strategy,
   activate your tags as cost allocation tags in the AWS Billing and Cost Management console. Note that it may take up to 24 hours for
   newly activated tags to appear in your cost management
   tools. Once activated, you can use your tags to filter and
   group costs in AWS Cost Explorer and other cost reporting
   tools.
4. **Configure detailed cost analysis
   using AWS Cost Explorer**. Use
   [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") to visualize and analyze your ML costs
   over time. Create custom reports that filter costs by
   specific tags (like Project or Environment) or by specific
   services like SageMaker AI. Set up regular reports to track
   spending trends, identify cost spikes, and understand usage
   patterns. Use the insights gained to optimize your resource
   allocation and scheduling for ML workloads.
5. **Create cost anomaly
   detection**. Set up
   [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/ "https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/") to automatically identify
   unusual spending patterns in your ML workloads. Configure
   alerts to notify relevant stakeholders when anomalies are
   detected. This assists you in quickly identifying and
   addressing unexpected cost increases, which can happen with
   ML workloads due to extended training times or inefficient
   resource usage.
6. **Establish cost governance
   processes**. Create clear processes for reviewing
   costs, responding to budget alerts, and making cost
   optimization decisions. Assign responsibility for cost
   monitoring to specific individuals or teams. Conduct regular
   cost reviews with stakeholders to discuss spending trends,
   identify optimization opportunities, and align ML resource
   usage with business priorities. Document cost-saving actions
   taken and their impact on the overall budget.
7. **Optimize ML resources based on cost
   data**. Use the cost insights gained from your
   tagging and budgeting tools to optimize ML resource usage.
   Identify underutilized notebook instances that can be
   stopped when not in use. Select appropriate instance types
   based on workload requirements. Consider using
   [Amazon SageMaker AI Managed Spot Training](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md") to reduce training
   costs by up to 90%. Implement auto-scaling for inference
   endpoints to match capacity with demand.

## Resources

**Related documents:**

- [Managing
  your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md")
- [Organizing
  and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
- [Getting
  started with AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/getting-started-ad.md "../../../cost-management/latest/userguide/getting-started-ad.md")
- [Best
  Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")
- [Cost
  Optimization Pillar - AWS Well-Architected Framework](../cost-optimization-pillar/welcome.md "../cost-optimization-pillar/welcome.md")
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/")
- [AWS Cloud Financial Management](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/")
- [Analyze
  Amazon SageMaker AI spend and determine cost optimization
  opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/ "https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/")
