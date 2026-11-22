

# COST08-BP03 Deploy resources dynamically

 With static capacity, you either pay for peak demand around the clock or you fail when demand climbs past what you provisioned. Deploying resources dynamically avoids both problems by adjusting capacity as demand changes. Some demand is predictable by time of day or week. The rest varies with real-time conditions. Match the provisioning method to the type of demand. 

 **Desired outcome:** 
+  Your capacity rises and falls with demand automatically, without manual provisioning. 
+  You meet predictable demand with scheduled or predictive provisioning that has capacity ready before the peak arrives. 
+  You meet variable demand with reactive scaling driven by workload metrics. 
+  You pay only for resources in use, because idle capacity is released when demand subsides. 

 **Common anti-patterns:** 
+  Provisioning and deprovisioning resources manually as demand changes. 
+  Setting scaling policies so aggressive that capacity oscillates, adding cost and instability. 
+  Using reactive scaling for demand that is predictable by time, so capacity arrives after the peak. 
+  Running non-production environments at full capacity outside the hours they are in use. 

 **Benefits of establishing this best practice:** 
+  Costs fall, because resources run only when demand requires them. 
+  Performance holds during peaks, because capacity scales to meet demand. 
+  Operations need less manual effort, because scaling responds to demand automatically. 
+  Resource management simplifies, because policies replace manual adjustments. 
+  Energy use drops, because idle capacity is released. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 You supply resources to meet demand in two forms: start and stop fixed resources on a schedule, or scale a managed group of resources up or down. [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) handles the first form. It starts and stops existing Amazon EC2 and Amazon RDS instances at set times. This suits resources with consistent daily patterns, such as instances that staff use during business hours. Instance Scheduler does not manage instances inside an Auto Scaling group or services such as Amazon Redshift and Amazon OpenSearch Service, because those manage their own capacity. You can configure schedules across accounts and Regions with AWS Systems Manager Quick Setup. <a name="cost08-bp03-fig1"></a>

![Architecture diagram showing AWS Instance Scheduler starting and stopping Amazon EC2 and Amazon RDS instances at scheduled times across accounts and Regions.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/instance-scheduler-diagram.png)

*AWS Instance Scheduler starting and stopping instances on a schedule*


 [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) handles the second form. It adjusts capacity to hold performance and keep cost low, and works with Amazon EC2, Spot Fleet, Amazon ECS, Amazon DynamoDB, and Amazon Aurora. A group can maintain a fixed number of instances, or it can scale through manual, scheduled, dynamic, or predictive [scaling options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling-overview.html). 

 *Demand-based supply* reacts to near real-time demand. It uses metrics to vary resource count, adding capacity during spikes to hold performance and removing capacity when demand falls to save cost. Simple or step scaling adds or removes instances according to thresholds you define. Target tracking adjusts capacity to keep a metric at a target value. Weigh how quickly you can provision new resources and how wide the supply-demand gap will grow during that delay. <a name="cost08-bp03-fig2"></a>

![Chart showing capacity scaling up and down in response to near real-time demand metrics such as request rate or utilization.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/demand-based-supply.png)

*Demand-based supply reacting to real-time demand*


 *Time-based supply* aligns capacity to demand that is predictable by time, independent of current utilization. It makes resources available exactly when they are needed, without waiting for start-up and health checks. Scheduled scaling changes capacity at set times, such as the start of business hours. Predictive scaling learns daily and weekly patterns and scales ahead of them. Assess how consistent the pattern is, plan for pattern changes, and refine the schedule as monitoring reveals drift. <a name="cost08-bp03-fig3"></a>

![Chart showing scheduled or predictive scaling that aligns capacity with predictable daily or weekly demand patterns.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/time-based-supply.png)

*Time-based supply aligning capacity to predictable demand*


 Use [launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) instead of launch configurations. Templates expose the latest features, support mixing Spot and On-Demand Instances and multiple instance types, and can be versioned. Use [attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) to specify requirements such as vCPU, memory, and storage instead of naming instance types. This approach broadens available capacity and adopts newer instance generations automatically. 

 You can also scale vertically by changing an instance size or class, or by modifying an Amazon EBS Elastic Volume in place. You can provision or decommission whole environments with [AWS APIs and SDKs](https://builder.aws.com/build/tools) and [AWS CloudFormation](https://aws.amazon.com/cloudformation/). This suits test environments that run only during set hours. [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) spreads incoming requests across the resources a scaling policy provides so no single instance is overloaded. Scaling policies trigger on [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics such as CPU utilization, network throughput, and request latency. Where possible, use custom metrics that reflect the customer experience for more accurate decisions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Schedule fixed resources for predictable idle periods:** Identify resources used on a consistent schedule, such as development and test instances that sit idle outside business hours. Configure [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) to stop and start those Amazon EC2 and Amazon RDS instances at the required times. Exclude instances managed by an Auto Scaling group, which scales on its own policies. 

1.  **Configure scheduled and predictive scaling for predictable demand:** For demand that follows the clock, configure time-based scaling in AWS Auto Scaling. Use [scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) when peak times are known, such as the start of business hours. Use [predictive scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) when traffic follows recurring daily or weekly patterns, or when instances take long enough to start that reactive scaling would arrive late. 

1.  **Configure dynamic scaling for variable demand:** For demand that cannot be predicted by time, configure dynamic scaling driven by workload metrics with [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html). Set target tracking or step policies on the metrics that reflect load, and confirm the group scales within the response time the workload requires. Launch On-Demand and Spot Instances within one group, and apply Reserved Instances or a Savings Plan to the steady baseline to lower cost further. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST08-BP01 Perform an analysis on the workload demand](cost08-bp01.md) 
+  [COST08-BP02 Implement a buffer or throttle to manage demand](cost08-bp02.md) 
+  [COST06-BP03 Select resource type, size, and number automatically based on metrics](cost06-bp03.md) 

 **Related documents:** 
+  [Getting started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html) 
+  [Scheduled scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) 
+  [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) 
+  [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html) 

 **Related videos:** 
+  [Target tracking scaling policies for Auto Scaling](https://www.youtube.com/watch?v=-RumeaoPB2M) 
+  [AWS Instance Scheduler](https://www.youtube.com/watch?v=nTLEyo2NzUs) 

 **Related examples:** 
+  [Attribute-based instance type selection for Amazon EC2 Auto Scaling and Amazon EC2 Fleet](https://aws.amazon.com/blogs/aws/new-attribute-based-instance-type-selection-for-ec2-auto-scaling-and-ec2-fleet/) 
+  [Optimizing Amazon Elastic Container Service for cost using scheduled scaling](https://aws.amazon.com/blogs/containers/optimizing-amazon-elastic-container-service-for-cost-using-scheduled-scaling/) 
+  [Predictive scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/) 
+  [How do I use Instance Scheduler with AWS CloudFormation to schedule Amazon EC2 instances?](https://repost.aws/knowledge-center/stop-start-instance-scheduler) 

 **Related services:** 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) 