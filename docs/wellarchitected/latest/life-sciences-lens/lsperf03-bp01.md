# LSPERF03-BP01 Workload-specific performance

analysis

Conduct systematic analysis of workload characteristics to identify
distinct performance requirements and optimization opportunities.
Profile computational patterns, data access behaviors, and resource
utilization across different workflow stages to guide targeted
optimization efforts, allocating resources on empirical performance
needs rather than assumptions.

**Desired outcome:** Implement
systematic workload profiling to identify optimization opportunities
and guide resource allocation based on empirical performance data.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To optimize genomics or life sciences workloads effectively, begin
with systematic analysis using AWS observability tools. Deploy
Amazon CloudWatch with custom metrics and dashboards to establish
baseline performance across your architecture. Configure detailed
monitoring through CloudWatch Container Insights for containerized
workloads or CloudWatch agent for EC2 instances to capture CPU,
memory, disk, and network utilization patterns.

Profile computational patterns by implementing AWS X-Ray tracing
to understand request flows and component interactions throughout
your application stack. For ML-based workloads, use Amazon SageMaker AI Profiler to analyze model training and inference
performance characteristics. These tools help identify
computational bottlenecks and guide decisions about instance
types, model optimization techniques, or architectural changes
that could improve performance.

Analyze data access behaviors using CloudWatch metrics for
services like Amazon S3, Amazon DynamoDB, and Amazon RDS.
Implement S3 Storage Lens to gain visibility into object storage
patterns and optimize data placement strategies. For database
workloads, use RDS Performance Insights or DynamoDB CloudWatch
metrics to identify query patterns that might benefit from
indexing or caching strategies with Amazon ElastiCache.

Map resource utilization across different workflow stages by
correlating metrics from multiple sources in CloudWatch
dashboards. This correlation helps identify how resource
requirements fluctuate throughout your workload lifecycle and
where targeted optimizations would deliver the greatest impact.
Use AWS Cost Explorer, cost allocation tags, and CloudWatch
dashboards together to understand the cost implications of
different resource allocation strategies.

Implement a data-driven optimization approach using AWS Compute Optimizer for right-sizing recommendations and AWS Well-Architected Tool to evaluate your architecture against best
practices. Test optimization hypotheses using A/B testing
methodologies with AWS AppConfig before full deployment. Document
findings and optimization decisions in AWS Systems Manager
documents to build organizational knowledge around performance
optimization practices specific to your Genomics or Lifesciences
workloads.

### Implementation steps

1. Deploy CloudWatch dashboards for workload monitoring.
2. Use SageMaker AI Profiler to analyze model performance.
3. Implement X-Ray tracing for request flow analysis.
4. Create S3 Storage Lens dashboards for data patterns.
5. Optimize with AWS Compute Optimizer recommendations.
