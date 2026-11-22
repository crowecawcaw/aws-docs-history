

# REL07-BP02 Obtain resources upon detection of impairment to a workload

 Adding or replacing unhealthy resources automatically can restore service before your customers feel the impact. This requires quick detection and a defined response. Reactive scaling is a recovery mechanism, distinct from scaling that anticipates rising demand. 

 **Desired outcome:** 
+  Health checks and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms detect impairment or degraded customer experience across all workload components. 
+  A defined response, automated where possible, scales or replaces the affected resources to restore availability. 
+  Recovery begins from a detection signal rather than from a customer report or a manual discovery. 
+  The response is tuned so that transient blips do not trigger unnecessary scaling actions. 

 **Common anti-patterns:** 
+  Teams rely on customer reports to learn that a component is impaired, which delays recovery. 
+  Health checks confirm only that a process is running, not that it can serve requests correctly. 
+  Recovery procedures are undocumented, so response time depends on who is on call. 
+  Teams treat every brief error as an impairment, which causes the workload to scale in response to noise. 

 **Benefits of establishing this best practice:** 
+  Availability is restored faster because recovery starts from an automated signal, not a human discovery. 
+  Mean time to recovery becomes predictable because the response is defined in advance rather than improvised. 
+  On-call load drops because routine impairments are handled by automation instead of manual intervention. 
+  Recovery behaves consistently regardless of which individual responds to the event. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Reactive scaling responds to *impairment*, a state where a component can no longer serve its share of work correctly. This differs from demand-driven scaling, which responds to healthy growth in traffic. Demand scaling triggers on rising utilization, while impairment scaling triggers on failing health signals. A workload needs both kinds of scaling, each with its own trigger. 

 A health check that only confirms that a process is listening on a port might report the component as healthy while it returns errors on every request. Effective health checks exercise the real work path, such as a request that touches its dependencies, so they fail when the component cannot serve traffic. The criteria on these checks define what "impaired" means for your workload. Set them deliberately. 

 Manual scaling can work for rare events with clear ownership, such as changing a scaling group's instance count or a table's throughput. Prefer automation wherever the pattern is understood, because it removes the delay of paging a human and the variance in how people respond. Automation acts on whatever signal you give it, so a poorly tuned health check drives it to scale on transient errors. Tune sensitivity through evaluation periods and thresholds to prevent brief blips from triggering unnecessary actions. 

 This best practice depends on observability across the whole workload. Monitor every component whose failure affects the customer, not only the entry point. Scaling procedures vary by each component's technology, because EC2 instance groups, container services, serverless functions, and managed databases each expose different controls for adding capacity. Container services such as Amazon ECS and AWS Fargate scale through [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) service policies and [ECS capacity auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-autoscaling-best-practice.html). AWS Lambda scales concurrency automatically within your configured [reserved and provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) limits. Define the response per component, matched to how that component scales. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Instrument components with meaningful health checks:** Configure health checks that exercise the real work path for each component, so a check fails when the component cannot serve requests correctly rather than only when its process stops. Establish the criteria that define impairment for your workload. For broad monitoring coverage, see [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md). 

1.  **Define the scaling response per component:** Write the procedure that restores each component, matched to how that component scales. Compute groups managed by [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) replace unhealthy instances and hold the group between minimum and maximum limits. Container services scale through [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) policies and [ECS capacity auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-autoscaling-best-practice.html). AWS Lambda adjusts concurrency within your configured [reserved and provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) limits. Tables using [DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) adjust provisioned throughput in response to traffic. 

1.  **Automate the response where the pattern is understood:** Connect detection to the scaling action so recovery begins without manual intervention. Reserve manual response for rare events with clear ownership, and prefer automation elsewhere. 

1.  **Tune sensitivity to avoid reacting to noise:** Set evaluation periods and thresholds so that a sustained impairment triggers the response while a transient blip does not. For example, configure [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) with multiple evaluation periods before entering ALARM state. Verify the tuning against real traffic patterns rather than accepting defaults. 

1.  **Notify responders and record the event:** Alert the appropriate team when a scaling action fires, whether automated or manual, so a human can confirm recovery and investigate the root cause. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL07-BP01 Use automation when obtaining or scaling resources](rel07-bp01.md) 
+  [REL07-BP03 Obtain resources upon detection that more resources are needed for a workload](rel07-bp03.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 

 **Related documents:** 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) 
+  [Optimizing Amazon ECS service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-autoscaling-best-practice.html) 
+  [Managing throughput capacity automatically with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) 
+  [Configuring reserved concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 

 **Related tools:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 