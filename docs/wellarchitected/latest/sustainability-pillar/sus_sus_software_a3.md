# SUS03-BP02 Remove or refactor workload components with low or

no use

Remove components that are unused and no longer required, and refactor
components with little utilization to minimize waste in your workload.

**Common anti-patterns:**

- You do not regularly check the utilization level of individual components of your workload.
- You do not check and analyze recommendations from AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/").

**Benefits of establishing this best practice:** Removing unused components
minimizes waste and improves the overall efficiency of your cloud workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Unused or underutilized components in a cloud workload consume unnecessary compute, storage or network resources. Remove or refactor these components to directly reduce waste and improve the overall efficiency of a cloud workload. This is an iterative improvement process which can be initiated by changes in demand or the release of a new cloud service. For example, a significant drop in [AWS Lambda](../../../lambda.md "../../../lambda.md") function run time can be indicate a need to lower the memory size. Also, as AWS releases new services and features, the optimal services and architecture for your workload may change.

Continually monitor workload activity and look for opportunities to improve the utilization level of individual components. By removing idle components and performing rightsizing activities, you meet your business requirements with the fewest cloud resources.

### Implementation steps

- **Inventory your AWS resourceds:** Create an inventory of your AWS resources. In AWS, you can turn on [AWS Resource Explorer](../../../resource-explorer/latest/userguide/welcome.md "../../../resource-explorer/latest/userguide/welcome.md") to explore and organize your AWS resources. For more details, see [AWS re:Invent 2022 - How to manage resources and applications at scale on AWS](https://www.youtube.com/watch?v=bbgUnKq6PAU "https://www.youtube.com/watch?v=bbgUnKq6PAU").
- **Monitor utilization:** Monitor and capture the utilization metrics for critical components of your workload (like CPU utilization, memory utilization, or network throughput in [Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")).
- **Identify unused components:** Identify unused or under-utilized components in your architecture.
  - For stable workloads, check AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") at regular intervals to identify idle, unused, or underutilized components.
  - For ephemeral workloads, evaluate utilization metrics to identify idle, unused, or underutilized components.

- **Remove unused components:** Retire components and associated assets (like Amazon ECR images) that are no longer needed.
  - [Automated Cleanup of Unused Images in Amazon ECR](https://aws.amazon.com/blogs/compute/automated-cleanup-of-unused-images-in-amazon-ecr/ "https://aws.amazon.com/blogs/compute/automated-cleanup-of-unused-images-in-amazon-ecr/")
  - [Delete unused Amazon Elastic Block Store (Amazon EBS) volumes by using AWS Config and AWS Systems Manager](../../../prescriptive-guidance/latest/patterns/delete-unused-amazon-elastic-block-store-amazon-ebs-volumes-by-using-aws-config-and-aws-systems-manager.md "../../../prescriptive-guidance/latest/patterns/delete-unused-amazon-elastic-block-store-amazon-ebs-volumes-by-using-aws-config-and-aws-systems-manager.md")

- **Refactor underutilized components:** Refactor or consolidate underutilized components with other resources to improve utilization efficiency. For example, you can provision multiple small databases on a single [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") database instance instead of running databases on individual underutilized instances.
- **Evaluate improvements:** Understand the [resources provisioned by your workload to complete a unit of work](evaluate-specific-improvements.md "evaluate-specific-improvements.md"). Use this information to evaluate improvements achieved by removing or refactoring components.
  - [Measure and track cloud efficiency with sustainability proxy metrics, Part I: What are proxy metrics?](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/")
  - [Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/")

## Resources

**Related documents:**

- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/")
- [What
  is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
- [Right Sizing: Provisioning Instances to Match Workloads](../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md "../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md")
- [Optimizing your cost with Rightsizing Recommendations](../../../cost-management/latest/userguide/ce-rightsizing.md "../../../cost-management/latest/userguide/ce-rightsizing.md")

**Related videos:**

- [AWS re:Invent 2023 - Capacity, availability, cost efficiency: Pick three](https://www.youtube.com/watch?v=E0dYLPXrX_w "https://www.youtube.com/watch?v=E0dYLPXrX_w")
