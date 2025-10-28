# MLSUS-04: Minimize idle resources

Adopt a managed and serverless architecture for your data
pipeline so that it only provisions resources when work needs to
be done. By doing so, you are not maintaining compute
infrastructure 24/7 and you minimize idle resources.

## Implementation plan

- **Use managed services** -
  Managed services shift responsibility for maintaining high
  average utilization, and sustainability optimization of
  the deployed hardware to AWS. Use managed services to
  distribute the sustainability impact of the service across
  all tenants of the service, reducing your individual
  contribution.
- **Create a serverless, event-driven
  data pipeline** - Use
  [AWS Glue](https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc") and
  [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/") for data ingestion and
  preprocessing. Step Functions can orchestrate AWS Glue
  jobs to create event-based serverless ETL and ELT
  pipelines. Because AWS Glue and AWS Step Functions are
  serverless, compute resources are only used as needed and
  not in an idle state while waiting.

## Documents

- [Manage
  AWS Glue Jobs with Step Functions](../../../step-functions/latest/dg/connect-glue.md "../../../step-functions/latest/dg/connect-glue.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 1, identify
  business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/")
- [Centralize
  feature engineering with AWS Step Functions and AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/centralize-feature-engineering-with-aws-step-functions-and-aws-glue-databrew/ "https://aws.amazon.com/blogs/big-data/centralize-feature-engineering-with-aws-step-functions-and-aws-glue-databrew/")
- [Optimizing
  your AWS Infrastructure for Sustainability, Part I:
  Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/")

## Metrics

- If using
  [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/"), measure and
  optimize the
  [CPU
  Utilization](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md") of the compute instances involved in
  data preparation.
- If using
  [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/"), measure and
  optimize the
  [CPU
  Utilization](../../../AmazonECS/latest/developerguide/cloudwatch-metrics.md#available_cloudwatch_metrics "../../../AmazonECS/latest/developerguide/cloudwatch-metrics.md#available_cloudwatch_metrics") used in the cluster or service.
- If using
  [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/"), measure
  and optimize the
  [CPU
  Utilization](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md") of your nodes and pods.
- If using
  [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/"), optimize the
  [Idle
  time](../../../emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.md "../../../emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.md") of the cluster.
