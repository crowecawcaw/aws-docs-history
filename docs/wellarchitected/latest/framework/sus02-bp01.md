

# SUS02-BP01 Implement elasticity for variable workloads

 For workloads with variable or unpredictable demand, implement elasticity through serverless technologies and auto-scaling capabilities to allow your infrastructure to dynamically adjust to actual demand. This approach verifies that resources are only consumed when needed and automatically scaled back during periods of low activity, significantly reducing idle capacity and wasted resources. 

 This dynamic scaling approach stands in contrast to static provisioning, where resources might sit idle during low demand periods or be insufficient during traffic spikes. 

 Event-driven architectures take elasticity a step further. Rather than running components continuously so they are ready to detect work, the arrival of an event triggers the resources that process it. Components publish events, a router or queue delivers them to consumers, and consumers exist only for as long as there is something to process. This removes two sources of waste that automatic scaling alone cannot address: the polling loops that consume resources to check for work that has not arrived, and the idle waiting inside synchronous request chains where compute is held open while a downstream component responds. Because producers and consumers are decoupled, each one also scales on its own demand signal rather than being provisioned for the peak of the whole chain. 

 Using elasticity, your workload can maintain optimal performance while minimizing its environmental footprint by using only the resources necessary at any given moment. 

 **Desired outcome:** 
+  You run infrastructure that scales up and down in response to actual demand, maintaining performance while minimizing resource waste. 
+  You keep resources actively serving workloads rather than sitting idle, which raises utilization and lowers the environmental impact across your cloud environment. 
+  You trigger work from events instead of discovering it by polling, so components consume resources only when there is something to process. 

 **Common anti-patterns:** 
+  Static provisioning for variable workloads, leading to idle and underused resources during low-demand periods. 
+  Manual scaling of resources in response to changing demand. 
+  Using auto-scaling for self-healing only. 
+  Over-provisioning to handle peak loads that occur infrequently. 
+  Using the same scaling approach for all components regardless of their unique demand patterns. 
+  Implementing auto-scaling without proper monitoring or tuning of scaling parameters. 
+  Polling a queue, table, or partner endpoint on a fixed schedule so resources are consumed at a constant rate regardless of whether work has arrived. 
+  Keeping always-on listeners or long-running processes to handle work that arrives intermittently. 
+  Chaining components synchronously so each one holds compute open while it waits for a downstream response. 
+  Adding an event router or queue between components without letting consumers scale on the resulting event or depth metric, so the decoupling adds hops without reducing idle capacity. 

 **Benefits of establishing this best practice:** 
+  Minimizes idle or underused resources by closely matching supply with actual demand. 
+  Reduces environmental impact through higher resource utilization. 
+  Improves workload performance during demand spikes with automatic scaling. 
+  Reduces the need for manual capacity management of variable workloads. 
+  Removes the resource cost of polling and idle waiting, which persists even when a workload is otherwise well scaled. 
+  Decouples producers from consumers so each component is provisioned for its own demand rather than the peak of the whole request chain. 
+  Reduces operational costs by paying only for resources actually consumed. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing elasticity for variable workloads requires careful selection of appropriate AWS services, configuration of scaling mechanisms, and ongoing optimization. The goal is to create infrastructure that automatically adapts to changing demand patterns while maintaining performance and minimizing resource waste. 

 Treat this as two related decisions. Auto scaling adjusts how much capacity a running component has, while an [event-driven architecture](https://aws.amazon.com/event-driven-architecture/) decides whether the component needs to be running at all. Where work arrives intermittently with a signaled arrival, route that signal through Amazon EventBridge, Amazon SQS, or a service integration, and let the signal invoke the consumer. Where work is continuous, keep the component running and scale it. Applying the correct approach produces a workload wherein resource use tracks demand closely rather than approximately. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Analyze your workload's demand patterns. 

   1.  Use Amazon CloudWatch metrics to understand historical usage patterns and variability. 

   1.  Identify components with variable or unpredictable demand. 

   1.  Determine appropriate scaling metrics that correlate with actual workload demand. 

   1.  Identify components that poll for work, run on a fixed schedule, or stay running to wait for requests. These are candidates for event-driven invocation rather than scaling. 

   1.  Trace synchronous request chains and note where a component holds compute open waiting on a downstream response. 

1.  Select appropriate elastic services for your workload. 

   1.  Consider serverless services such as AWS Lambda for event-driven workloads. 

   1.  Use container services such as Amazon ECS or Amazon EKS with AWS Fargate for microservices. 

   1.  Implement Amazon EC2 Auto Scaling for traditional applications. 

1.  Replace polling and idle waiting with event-driven invocation. 

   1.  Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to route events from producers to consumers so consumers run only when a matching event arrives, and filter with event patterns at the router rather than invoking a consumer that discards most of what it receives. 

   1.  Use native event source mappings, such as Amazon SQS, Amazon Kinesis, Amazon DynamoDB Streams, or Amazon S3 event notifications, to invoke consumers on arrival instead of running a process that checks for new work. 

   1.  Where a queue consumer must poll, use [SQS long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html) rather than short polling on a fixed interval, and scale consumers on queue depth or backlog per instance. 

   1.  Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to coordinate multi-step work, so waiting is held in the workflow state rather than in running compute. Prefer callback and wait-for-completion patterns over polling loops inside application code. 

   1.  Publish events for work that does not need an immediate answer, and return to the caller as soon as the event is accepted. See [SUS02-BP03 Match resource use to business need](sus02-bp03.md) for identifying operations that need a synchronous response. 

   1.  Verify that decoupling actions reduce resource consumption. Confirm consumers scale to zero or near zero when no events arrive, and that the event router or queue has not been added in front of an always-on fleet. 

1.  For EC2 based workloads configure auto scaling mechanisms. 

   1.  Set up target tracking scaling policies for EC2 Auto Scaling groups. 

   1.  Implement Application Auto Scaling for services higher up the stack. 

   1.  Configure appropriate minimum and maximum capacity limits based on your workload needs. 

   1.  Use Amazon EC2 flex instances where your workload will not make use of all of the underlying resources. 

1.  Implement predictive scaling for workloads with predictable patterns. 

   1.  Collect data from your observability tooling. Identify trends and patterns. 

   1.  Enable predictive scaling for EC2 Auto Scaling groups with regular patterns. 

   1.  Configure the prediction window and scaling behavior based on your workload characteristics. 

1.  Test scaling behavior and optimize configurations. 

   1.  Simulate different demand scenarios to verify proper scaling behavior. 

   1.  Monitor scaling activities and resource utilization during normal operations. 

   1.  Refine scaling parameters based on observed behavior and changing workload patterns. 

   1.  Monitor event throughput, consumer concurrency, and backlog age to confirm consumers are invoked in step with event arrival rather than lagging behind it or running ahead of it. 

1.  Size storage appropriately. Scale up and down as needed. 

   1.  Modify Amazon EBS volume using Elastic Volume operations. 

   1.  Extend filesystem after resizing Amazon EBS volumes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS02-BP04 Define the baseload for predictable and steady-state workloads](sus02-bp04.md) 
+  [SUS03-BP02 Flatten demand peaks for consistently high resource utilization](sus03-bp02.md) 
+  [SUS04-BP03 Implement distributed systems appropriately](sus04-bp03.md) 
+  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md) 
+  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md) 
+  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md) 

 **Related documents:** 
+  [Get started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html) 
+  [Serverless on AWS](https://aws.amazon.com/serverless/) 
+  [Introducing Native Support for Predictive Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/) 
+  [Automating Amazon EBS volume resizing with AWS Step Functions and AWS Systems Manager](https://aws.amazon.com/blogs/storage/automating-amazon-ebs-volume-resizing-with-aws-step-functions-and-aws-systems-manager/) 
+  [What is an Event-Driven Architecture?](https://aws.amazon.com/event-driven-architecture/) 
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [Amazon SQS short and long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html) 
+  [Scaling policy based on Amazon SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html) 
+  [Maximize Amazon EKS efficiency: How Auto Mode, Graviton, and Spot work together](https://aws.amazon.com/blogs/containers/maximize-amazon-eks-efficiency-how-auto-mode-graviton-and-spot-work-together/) 
+  [AWS re:Invent 2024 - Amazon EC2 Flex instances: Deliver performance at lower costs](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/events/approved/reinvent-2025/reinvent/2024/slides/cmp/CMP408_Amazon-EC2-flex-instances-Deliver-performance-at-lower-cost.pdf) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Architecting for hypergrowth: Scaling to 200 million users w/ Skyscanner-ARC209](https://www.youtube.com/watch?v=F4N8XiAhXKk) 
+  [Karpenter: Optimize Kubernetes Cluster Scaling](https://aws.amazon.com/video/watch/620b9d34964/) 
+  [AWS re:Invent 2024 - Event-driven architectures at scale: Manage millions of events (API307)](https://www.youtube.com/watch?v=dy7UXS7ur14) 

 **Related examples:** 
+  [Tutorial: Create your first Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-your-first-auto-scaling-group.html) 
+  [Automatically scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) 
+  [Event-driven architecture with AWS Graviton Processors and Amazon EC2 Spot Instances](https://catalog.workshops.aws/well-architected-sustainability/en-US/2-software-and-architecture/event-driven-architecture-with-graviton-spot) 