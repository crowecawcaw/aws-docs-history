

# COST08-BP02 Implement a buffer or throttle to manage demand

 Demand rarely arrives at a steady rate. When a workload provisions capacity for every peak, that capacity sits idle between peaks. You pay for the peak, even though average demand is lower. Buffering and throttling smooth the incoming rate so the workload runs closer to average demand. Buffering stores requests for later processing, while throttling asks clients to slow down and retry. 

 **Desired outcome:** 
+  Your workload runs on capacity sized closer to average demand than to peak demand. 
+  You smooth incoming request rates, so short spikes do not force additional provisioning. 
+  You throttle clients that can retry, and serve clients that cannot retry through a buffer. 
+  Your buffering and throttling policies account for the differing priorities of workloads and clients rather than applying one rule to all. 

 **Common anti-patterns:** 
+  Provisioning for peak demand instead of smoothing the demand curve with a buffer or throttle. 
+  Applying uniform throttling or buffering across all requests, ignoring the differing priorities of workloads and clients. 
+  Adding a buffer without designing consumers to handle duplicate messages, which corrupts processing. 
+  Sizing a throttle or buffer without measuring total demand, rate of change, and required response time. 
+  Teams recreate a resource immediately after deleting it in a recurring cycle, which multiplies API calls and monitoring data. 

 **Benefits of establishing this best practice:** 
+  Resource use becomes more efficient, because capacity tracks average demand instead of peak demand. 
+  System reliability improves, because smoothing helps prevent the overloads that cause failures under spikes. 
+  Costs fall, because the workload avoids scaling up to meet every transient peak. 
+  Demand growth is absorbed without major infrastructure change. 
+  Response times stay consistent, which improves the client experience. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Figure 1 shows a demand curve with two peaks and the capacity line provisioned to cover them. Cost follows the provisioned capacity line, so the gap above the demand curve is waste. Buffering and throttling flatten the peaks and lower required capacity and cost. <a name="cost08-bp02-fig1"></a>

![Chart showing a demand curve with two peaks and the capacity line provisioned to cover them, with the gap above the demand curve highlighted as waste.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/provisioned-capacity-1.png)

*Provisioned capacity sized to cover demand peaks*


 The client's retry behavior decides which technique fits. When the source of a request can retry, throttling works. The workload declines a request it cannot serve now, and the client waits and tries again. When the source cannot retry, a declined request is lost, so a buffer holds the request until the workload can process it. 

 Throttling caps resource use and cost. Throttled requests are delayed or declined, so an aggressive limit degrades legitimate traffic. Use [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to throttle requests at the API layer. Set per-client limits to protect capacity and treat client tiers differently. 

 A buffer decouples request arrival from processing. Three parts make it work: *producers* send messages, a *queue* or *stream* holds them, and *consumers* read and process them at a sustainable pace. [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) provides a queue where a single consumer reads each message. [Amazon Kinesis](https://aws.amazon.com/kinesis/) provides a stream where many consumers can read the same messages. Because a message can arrive more than once, consumers must handle duplicate work without corrupting results. 

 Size both mechanisms from the demand analysis. Measure total demand, its rate of change, and the required response time, then size the throttle limit or buffer depth accordingly. 

 Your own automation can also generate demand. When a workload repeatedly deletes and recreates a resource, such as a scheduled validation stack, each cycle triggers API calls, metric data points, and configuration evaluations in every service that observes the resource. A cooldown between the delete and the next create limits that churn in the same way throttling limits client requests. Set the delay from how quickly the new resource must be available. If a worker would otherwise wait, schedule the next action with an [Amazon SQS message timer](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html) so no compute sits idle. Timers are limited to 15 minutes, so use [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html) for longer cooldowns. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze client retry capability and demand:** Determine whether each request source can retry. Route retry-capable sources toward throttling and sources that cannot retry toward a buffer. Measure total demand, rate of change, and required response time to size the mechanism you choose. 

1.  **Implement throttling for retry-capable clients:** Configure request throttling with [Amazon API Gateway](https://aws.amazon.com/api-gateway/). Set the rate and burst limits to the ceiling you established during sizing, and set separate limits per client tier where some traffic matters more than others. 

1.  **Implement buffering for clients that cannot retry:** Place requests on a buffer so consumers process them at a sustainable rate. Use an [Amazon SQS](https://aws.amazon.com/sqs/) queue when a single consumer processes each message, or an [Amazon Kinesis](https://aws.amazon.com/kinesis/) stream when many consumers read the same messages. Design consumers to process duplicate messages safely. 

1.  **Add a cooldown to recreate cycles:** In any recurring delete-and-recreate cycle, add a configurable delay before the next create. Schedule it with an SQS message timer for delays up to 15 minutes, or EventBridge Scheduler for longer ones, instead of holding a worker. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST08-BP01 Perform an analysis on the workload demand](cost08-bp01.md) 
+  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md) 
+  [SUS03-BP02 Flatten demand peaks for consistently high resource utilization](sus03-bp02.md) 
+  [REL05-BP02 Throttle requests](rel05-bp02.md) 

 **Related documents:** 
+  [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html) 
+  [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) 

 **Related examples:** 
+  [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/) 
+  [Throttling a tiered, multi-tenant REST API at scale using API Gateway](https://aws.amazon.com/blogs/architecture/throttling-a-tiered-multi-tenant-rest-api-at-scale-using-api-gateway-part-1/) 
+  [Enabling tiering and throttling in a multi-tenant Amazon EKS SaaS solution using Amazon API Gateway](https://aws.amazon.com/blogs/apn/enabling-tiering-and-throttling-in-a-multi-tenant-amazon-eks-saas-solution-using-amazon-api-gateway/) 
+  [Application integration using queues and messages](https://aws.amazon.com/blogs/architecture/application-integration-using-queues-and-messages/) 

 **Related services:** 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) 
+  [Amazon Kinesis](https://aws.amazon.com/kinesis/) 