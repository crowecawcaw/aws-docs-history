

# ADVSUS04-BP02 Use serverless transaction processing
<a name="advsus04-bp02"></a>

 Implement serverless transaction processing, such as for ad measurement, to reduce the required unit of work and associated resource consumption for your advertising workloads. [Proxy metrics](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html#proxy-metrics), as defined in the Well-Architected Framework Sustainability Pillar, can be used to measure improvements from serverless use. For instance, instead of having long-running vCPU usage and partially-used volumes in a number of workload instances, use a serverless approach, so compute usage only occurs at the time of a transaction. 

## Implementation guidance
<a name="implementation-guidance-71"></a>
+  For ad measurement workloads, use serverless architectures to minimize the required infrastructure and resources per unit of work. 
+  Implement services like [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [AWS Glue](https://aws.amazon.com/glue/), [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), and [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) to build event-driven, scalable, and efficient ad measurement pipelines. 
+  These services automatically scale up or down based on demand, improving resource utilization and reducing waste. 
+  Serverless architectures can help minimize idle resources, further contributing to sustainability goals. 

## Key AWS services
<a name="key-aws-services-42"></a>
+  [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (for energy-efficient compute instances, if using EC2 instances) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) (for optimizing resource utilization, if using EC2 instances) 
+  [Proxy Metrics](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html#proxy-metrics) (AWS Sustainability Pillar) 