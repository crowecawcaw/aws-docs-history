# MLCOST06-BP01 Monitor usage and cost by ML activity

Use cloud resource tagging to manage, identify, organize, search
for, and filter resources. Tags categorize resources by purpose,
owner, environment, or other criteria. Associate costs with
resources using ML activity categories, such as re-training and
hosting, by using tagging to manage and optimize cost in deployment
phases. Tagging can be useful for generating billing reports with
breakdown of cost by associated resources.

**Desired outcome:** You gain
visibility into your machine learning costs by activity type,
allowing for better allocation, forecasting, and optimization of ML
resources. You can track expenses across different phases of the ML
lifecycle including development, training, and deployment. This
enables data-driven decisions about resource allocation and
identifies cost-saving opportunities while maintaining performance.

**Common anti-patterns:**

- Using default AWS account structure without proper tagging
  strategy for ML resources.
- Not separating costs between development, training, and
  production environments.
- Failing to automate tagging as part of resource provisioning.
- Overlooking unused or idle resources that continue to incur
  costs.

**Benefits of establishing this best
practice:**

- Clear visibility into costs associated with different ML
  activities.
- Ability to allocate costs to appropriate business units or
  projects.
- Improved forecasting and budgeting for ML initiatives.
- Identification of cost-saving opportunities across the ML
  lifecycle.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Monitoring and optimizing costs for machine learning workloads
requires a systematic approach to resource tagging and usage
tracking. ML workloads typically have distinct phases—development,
training, inference, and experimentation—each with different
resource requirements and cost profiles. By implementing a
comprehensive tagging strategy, you can track and attribute costs
to specific ML activities, making it more straightforward to
understand where your cloud spend is going and identify
opportunities for optimization.

AWS provides various tools and services to implement cost
monitoring for ML workloads. With proper tagging, you can generate
detailed cost reports, set up budgets with alerts, and make
data-driven decisions about resource allocation. This practice is
particularly important for ML workloads, which can be
compute-intensive and potentially costly if not properly managed.

### Implementation steps

1. **Establish a tagging strategy for ML
   resources**. Create a consistent tagging schema
   that captures relevant dimensions for ML activities. Include
   tags for project name, environment (development, testing,
   and production), ML phase (training, inference, and
   experiment), owner, and cost center. Document this strategy
   and verify that your team members understand and follow it
   when creating resources.
2. **Implement AWS tagging**. A
   [tag](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
   is a label that you or AWS assigns to an AWS resource. Each
   tag consists of a key and a value. For each resource, each
   tag key must be unique, and each tag key can have only one
   value. You can use tags to organize your resources, and cost
   allocation tags to track your AWS costs on a detailed level.
   AWS uses the cost allocation tags to organize your resource
   costs on your cost allocation report. This streamlines
   categorizing and tracking your AWS costs. AWS provides two
   types of cost allocation tags, an AWS-generated tag and
   user-defined tags.
3. **Activate cost allocation
   tags**. After creating your tags, you need to
   activate them for cost tracking in the AWS Billing and Cost Management and Cost
   Management console. Note that it can take up to 24 hours for
   new tags to appear in your billing reports.
4. **Automate resource
   tagging**. Use AWS CloudFormation templates, AWS CDK, or Terraform to automate the application of tags when
   provisioning resources. For SageMaker AI resources, implement
   tagging in your deployment pipelines and notebook
   initialization scripts. Consider using AWS Tag Editor for
   bulk tagging operations on existing resources.
5. **Use AWS Budgets to keep track of
   cost**. AWS Budgets can track your Amazon SageMaker AI cost, including development, training, and hosting. You
   can also set alerts and get a notification when your cost or
   usage exceeds (or is forecasted to exceed) your budgeted
   amount. After you create your budget, you can track the
   progress on the AWS Budgets console.
6. **Implement cost monitoring and
   reporting**. Use AWS Cost Explorer to visualize and
   analyze your ML costs across different dimensions. Create
   custom reports filtered by your ML activity tags to
   understand spending patterns. Schedule regular exports of
   cost reports for stakeholders review.
7. **Establish cost optimization
   processes**. Regularly review resource utilization
   and costs to identify optimization opportunities. Implement
   automated shutdown of idle resources such as SageMaker AI
   notebooks when not in use. Consider using SageMaker AI Managed
   Spot Training to reduce training costs by up to 90%.
8. **Create governance for
   tagging**. Use AWS Config Rules or AWS CloudFormation Hooks to enforce tagging policies. Implement
   processes to review and correct untagged or incorrectly
   tagged resources. Consider using AWS Organizations Tag
   Policies to standardize tags across multiple accounts.
9. **Implement enhanced cost tracking
   with improved tagging**. Use enhanced AWS tagging
   capabilities with better automation and governance features
   to make your cost allocation more consistent across ML
   workloads and improve your visibility into spending
   patterns.
10. **Use cost optimization
    services**. Use AWS Cost Anomaly Detection to
    identify unusual spending patterns in your ML workloads.
    Consider AWS Compute Optimizer for recommendations on
    right-sizing your ML compute resources based on historical
    utilization data.

## Resources

**Related documents:**

- [Organizing
  and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
- [Managing
  your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md")
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")
- [Getting
  started with AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/getting-started-ad.md "../../../cost-management/latest/userguide/getting-started-ad.md")
- [What
  is Tag Editor?](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
- [Best
  Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")
- [Analyze
  Amazon SageMaker AI spend and determine cost optimization
  opportunities based on usage, Part 1: Overview](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/ "https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/")
- [Analyze
  Amazon SageMaker AI spend and determine cost optimization
  opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/ "https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/")
