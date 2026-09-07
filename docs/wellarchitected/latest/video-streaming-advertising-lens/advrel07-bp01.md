

# ADVREL07-BP01 Design your workloads to withstand failures of individual components, such as compute instances, queues, databases, and caches
<a name="advrel07-bp01"></a>

 Build building resilient advertising systems by identifying critical components, and implement fault tolerance through cell-based architectures and distributed resources across Availability Zones. 

## Implementation guidance
<a name="implementation-guidance-31"></a>

 Determine which components of your workload are in a critical path to maintain operations for real-time bidding, ad serving, and other crucial functions. Identify AWS services that provide built-in fault tolerance mechanisms which are within your workload's response time, RTO, and RPO targets. Use cell-based architectures, with resources spread across multiple availability zones, to reduce the scope of a disruptive event. Where consistent communications are necessary, implement static stability mechanisms to reduce the dependency on control plane actions. 

## Key AWS services
<a name="key-aws-services-17"></a>
+  [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS Availability Zones and Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) 
+  [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) 
+  [Monitoring and Alerting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) 

## Resources
<a name="resources-26"></a>
+  [Reducing the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html) 
+  [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) 
+  [Control planes and data planes](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html) 