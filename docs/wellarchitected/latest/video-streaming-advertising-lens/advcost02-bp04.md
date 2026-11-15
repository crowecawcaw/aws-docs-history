

# ADVCOST02-BP04 Use interruptible spare capacity to reduce compute cost for fault-tolerant bidding workloads
<a name="advcost02-bp04"></a>

 For workloads that can be interrupted, Spot Instances provide the same performance as On-Demand at 60–90% lower cost. Advertising workloads include many interruptible components (batch bid log processing, audience model training, report generation, and A/B test analytics) where Spot Instances save substantial cost when you pair them with fault-tolerance mechanisms. 

 **Desired outcome:** 
+  Interruptible RTB and analytics workloads run on Spot Instances with interruption handling that helps avoid data loss and minimizes wasted compute. 
+  Auto Scaling groups and batch processing systems automatically manage instance replacement. 
+  Spot Instance diversification across multiple instance types and Availability Zones minimizes interruption risk. 

 **Common anti-patterns:** 
+  Running all RTB compute on On-Demand Instances without evaluating which components are interruption-tolerant. 
+  Using a single Spot Instance type and Availability Zone, so a single capacity reclamation can interrupt the entire fleet at once. 
+  Failing to implement interruption handling (checkpointing, graceful draining). 
+  Using Spot for latency-critical bid response paths where a two-minute interruption notice is insufficient to maintain SLAs. 

 **Benefits of establishing this best practice:** 
+  Compute cost savings of 60–90% for eligible workloads compared to On-Demand pricing. 
+  Access to additional compute capacity for burst processing during high-traffic campaign periods. 
+  Encourages fault-tolerant architecture patterns that improve system resilience. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) provide EC2 capacity at a 60-90% discount in exchange for the possibility of interruption on two minutes notice. A workload qualifies if it can lose an instance without data loss or user-visible impact. In advertising, this includes batch log processing, audience model training, report generation, creative transcoding, and offline analytics. Real-time bid evaluation paths don't qualify, because two minutes is not enough time to drain active bid connections without missing exchange deadlines. 

 Interruption probability varies by instance type, Availability Zone, and time of day. A single instance type in a single Availability Zone might have a 15-20% monthly interruption rate, while a diversified fleet across six instance types and three Availability Zones reduces effective interruption probability to under 5%. EC2 reclaims Spot capacity from the pools with lowest demand first. Diversification spreads your workload across pools so that a reclamation event in one pool affects only a fraction of your fleet. The capacity-optimized [allocation strategy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html) automates this by selecting pools with the deepest available capacity. 

 Spot Instances require fault tolerance. Without interruption handling, a terminated instance loses all in-progress work. For a batch job that has been processing bid logs for 45 minutes, interruption without checkpointing wastes those 45 minutes of compute. Checkpoint intermediate state to durable storage often enough that any single interruption loses only a small fraction of the total job. 

 The two-minute interruption notice arrives through [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html). Applications that poll metadata every five seconds can detect the notice and begin graceful shutdown: flushing buffers, writing checkpoints, deregistering from load balancers, and signaling orchestrators to reschedule remaining work. Applications that ignore the notice terminate mid-operation, which shifts costs from instance hours to reprocessing. 

 Use Spot for interruptible overflow and batch processing, and use Savings Plans or Reserved Instances for the steady-state baseline. Using Spot for baseline capacity creates availability risk when EC2 demand is high and interruption rates spike. Layer the purchase options: committed purchases for the predictable minimum, On-Demand for the gap between that minimum and normal peak, and Spot for batch workloads and burst capacity where interruptions are acceptable. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify interruptible workload components:** Document which advertising components are interruption-tolerant: batch log processing, audience segmentation, model training, analytics, and report generation. Explicitly exclude real-time bid evaluation and latency-critical services from Spot eligibility. 

1.  **Configure Auto Scaling groups with Spot diversification:** Specify multiple instance types (both AMD and Intel x86, plus Graviton equivalents) and multiple Availability Zones in your Spot fleet or Auto Scaling group configuration. Use the capacity-optimized allocation strategy to select pools with the lowest likelihood of interruption. This diversification significantly reduces the probability of simultaneous interruptions. 

1.  **Implement Spot interruption handling:** Subscribe to the EC2 Spot Instance interruption notice (two minutes before termination) through instance metadata polling or Amazon EventBridge. Use this notice to: checkpoint in-progress batch work to S3, drain active connections gracefully, and deregister from load balancers. For AWS Batch workloads, enable automatic job retries and application-level checkpointing. 

1.  **Measure cost savings and validate interruption rates:** Track Spot Instance utilization, interruption frequency, and job retry rates using AWS Cost Explorer filtered by purchase option. Compare effective cost-per-job between Spot and On-Demand. Use the EC2 Spot Instance Advisor to monitor interruption rate trends and adjust instance type pools if specific types show elevated interruption frequency. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Guidance for Building a Real Time Bidder for Advertising on AWS](https://aws.amazon.com/solutions/guidance/building-a-real-time-bidder-for-advertising-on-aws/) 
+  [EC2 Fleet and Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) 
+  [Beeswax Uses AWS to Cost-Effectively Process Millions of Bid Requests per Second](https://aws.amazon.com/solutions/case-studies/beeswax-case-study/) 
+  [EC2 instance rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html) 
+  [AWS Fargate for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) 

 **Related services:** 
+  [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) 
+  [AWS Batch](https://aws.amazon.com/batch/) 
+  [AWS Fargate](https://aws.amazon.com/fargate/) 