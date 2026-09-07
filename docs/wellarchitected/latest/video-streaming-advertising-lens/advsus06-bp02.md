

# ADVSUS06-BP02 Continuously monitor and right-size your AWS resources, and use the minimum resources required to meet your workload needs
<a name="advsus06-bp02"></a>

 Monitoring workloads allows you to optimize and elastically scale your workloads to meet demand. Using serverless offerings can also help you automatically scale to reduce resource usage and improve the ability to meet sustainability targets. Consider how your requirements change based on advertising campaigns, and take advantage of the elasticity and agility of cloud to optimize your resource usage. 

## Implementation guidance
<a name="implementation-guidance-74"></a>
+  Advertising SSPs and DSPs should use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards for visibility into active connections and bytes process per endpoint to drive resource usage. 
+  Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify the optimal resources for workloads. For example, when using [Amazon EMR](https://aws.amazon.com/emr/) to analyze ad impression and click-through data, Compute Optimizer can recommend the optimal EC2 instance types based on utilization data. 
+  Monitor boot time for improvements, such as pre-installing dependent libraries in container images for bidder processing.  
+  For downstream analytics and reporting of bidder transactions, use [Amazon Kinesis](https://aws.amazon.com/pm/kinesis/) Data Streams and Amazon Data Firehose to send data to Amazon S3. The use of a data stream enables faster responses and allows independent scaling for components of the real-time bidding architecture. 
+  Ad servers and click-through servers should be in [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) to automatically scale in when load is reduced. 

## Key AWS services
<a name="key-aws-services-43"></a>
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Karpenter](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/) (Open-Source Kubernetes cluster autoscaler built with AWS) 