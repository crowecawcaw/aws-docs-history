

# MLSUS03-BP01 Minimize idle resources
<a name="mlsus03-bp01"></a>

 Minimize your environmental impact by efficiently managing compute resources in your ML data pipeline. Use serverless architectures that provision resources only when needed, reducing energy consumption and carbon footprint. 

 **Desired outcome:** You implement a serverless, event-driven architecture for your ML data pipelines that only provisions resources when work needs to be done. This approach reduces idle resources, optimizes utilization of computing infrastructure, and reduces your organization's environmental impact while maintaining performance and scalability. 

 **Common anti-patterns:** 
+  Provisioning compute instances that run 24/7 regardless of workload requirements. 
+  Overprovisioning resources rather than scaling dynamically. 
+  Using traditional batch processing with fixed schedules instead of event-driven approaches. 
+  Failing to monitor and optimize resource utilization metrics. 

 **Benefits of establishing this best practice:** 
+  Lower carbon footprint and energy consumption. 
+  Improved resource efficiency across your ML pipeline. 
+  Automatic scaling to match workload demands. 
+  Simplified maintenance with managed services. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Adopting a serverless architecture for your ML data pipelines significantly reduces idle resources by allocating compute power only when needed. This approach uses AWS managed services that automatically scale based on workload, avoiding the need to maintain an always-on infrastructure. When you design your data pipeline using serverless technologies like AWS Glue and AWS Step Functions, you not only optimize resource utilization but also distribute the sustainability impact across the tenants of those services, reducing your individual environmental contribution. 

 The key principle is to transition from a static infrastructure model to an event-driven approach where resources are provisioned in response to triggers. This verifies that compute resources are only active during actual processing tasks rather than sitting idle waiting for work. AWS managed services handle the underlying infrastructure optimization, allowing you to focus on your ML workloads while maintaining efficiency. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate your current infrastructure**. Assess your existing data pipeline architecture to identify components that run continuously but have low utilization. Look for workloads with predictable patterns or batch processes that could benefit from an event-driven approach using [AWS CloudWatch metrics](https://aws.amazon.com/cloudwatch/) to identify utilization patterns. 

1.  **Adopt managed services**. Replace self-managed infrastructure with AWS managed services to distribute sustainability impact across service tenants. Services like [AWS Glue](https://aws.amazon.com/glue/), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) provision resources on-demand and automatically scale with your workloads. 

1.  **Create serverless, event-driven data pipelines**. Use [AWS Glue](https://aws.amazon.com/glue/) for data processing and [AWS Step Functions](https://aws.amazon.com/step-functions/) for orchestration to build ETL and ELT pipelines that only consume resources when triggered. Step Functions can coordinate AWS Glue jobs efficiently, provisioning compute resources only when needed and releasing them immediately after completion. 

1.  **Implement efficient data storage**. Choose appropriate storage solutions like [Amazon S3](https://aws.amazon.com/s3/) for your data lake and [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically move data between access tiers based on usage patterns, reducing storage costs and resource waste. 

1.  **Configure event-based triggers**. Set up event notifications through [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to automatically launch processing jobs when new data arrives. This avoids the need for scheduled jobs that might run when no new data is available, reducing unnecessary compute usage. 

1.  **Optimize compute resources**. For AWS Glue jobs, configure appropriate worker types and dynamically allocate resources based on workload requirements. Use features like [AWS Glue Auto Scaling](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) to automatically adjust capacity as needed during jobs. 

1.  **Implement monitoring and metrics**. Set up comprehensive monitoring of your serverless infrastructure using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track resource utilization, job execution time, and idle periods. Use these metrics to identify further optimization opportunities. 

1.  **Establish automatic cleanup processes**. Implement automated processes to remove temporary resources, intermediate data, and other artifacts after job completion to avoid unnecessary storage costs and reduce digital waste. 

1.  **Optimize data transfer**. Minimize data movement between services by processing data close to where it's stored when possible. Use [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data preparation tasks within the same environment as your data storage. 

1.  **Use AI-powered optimization**. Use Amazon Q data integration in AWS Glue to automatically generate optimized ETL jobs for common data sources. This reduces development time while implementing efficient resource utilization patterns from the start. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
+  [What is Amazon EMR Serverless?](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) 
+  [Using auto scaling for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) 
+  [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [Start an AWS Glue job with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html) 
+  [Serverless Applications Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) 
+  [Optimize AI/ML workloads for sustainability: Part 3, deployment and monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/) 
+  [Fuel your data with Generative AI](https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/) 