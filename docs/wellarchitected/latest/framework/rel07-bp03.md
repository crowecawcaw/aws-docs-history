

# REL07-BP03 Obtain resources upon detection that more resources are needed for a workload

 Provisioning enough capacity in advance to cover peak demand wastes money during quiet periods and still risks running short when a peak exceeds the estimate. Provisioning capacity as demand appears removes both problems, but only if the workload can add resources fast enough and the scaling signal reflects real demand. 

 **Desired outcome:** 
+  Compute, database, and other scalable resources adjust automatically to meet current and forecasted demand. 
+  Scaling policies leave enough headroom for a demand burst to be served while additional resources come online. 
+  Minimum and maximum limits are set so the workload never starves during a peak or over-provisions without bound. 
+  The scaling metric correlates with actual demand, so resources track load rather than a proxy that lags or misleads. 

 **Common anti-patterns:** 
+  Teams provision a fixed number of resources and treat elastic capacity as static. 
+  A scaling metric is chosen that does not correlate with actual demand. 
+  Scaling policies leave no headroom, so a burst is throttled while capacity is still being added. 
+  Policies add capacity too late, so existing resources are exhausted before replacements reach full service. 
+  Minimum and maximum counts are misconfigured, which causes scaling to fail at the boundary. 

 **Benefits of establishing this best practice:** 
+  The workload has the resources it needs to meet demand and hold to its service-level objectives. 
+  Cost falls during low demand because idle capacity is removed rather than paid for continuously. 
+  Peak capacity does not have to be estimated and statically allocated in advance. 
+  Availability improves because capacity grows with load instead of being capped at a guessed maximum. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Not every component can scale by adding copies of itself. Automatic scaling applies to *horizontally scalable* components, those that provide identical resources and behave the same way, so that any replica can serve any request. Compute instances configured alike, container tasks, and container orchestration pods fit this model, and they usually sit behind a load balancer that distributes work across the replicas. Replicated data stores such as read replicas, [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables, and cache clusters also scale this way. Identify horizontally scalable components first, because scaling a component that holds unique state can corrupt it. 

 Container architectures scale with both pods or tasks that serve requests and the compute capacity those pods run on. Both of these scaling mechanisms need to keep pace with each other, which requires a plan. If the pod layer scales without the capacity layer following, new pods have nowhere to schedule. 

 A *scaling metric* is a signal that rises and falls with demand. To find one, load test in a non-production environment: hold the resource count fixed, increase demand slowly, and watch which signals move in step with load. CPU utilization, work queue depth, active user count, and network throughput are common choices. Memory utilization is a common trap. Memory often rises as an application warms up and then stays elevated even after demand falls, so it does not track demand in both directions. Choosing it as a scaling metric produces a workload that scales out under load and never scales back in. 

 Scaling is not instant, and treating it as instant causes capacity exhaustion. Metric-based scaling is a *latent operation*: utilization metrics take time to propagate, the scaler waits for a clear signal before acting, and newly created resources take further time to reach full service. Because of this latency, setting a scaling target close to full utilization, such as 90 percent CPU, risks exhausting existing capacity before replacements arrive. Targets in the range of 50 to 70 percent give the scaler room to react, with the exact figure depending on how bursty demand is and how long new resources take to provision. 

 Three scaling methods combine to address different demand patterns: 
+  **Metric-based scaling** reacts to a live signal and suits demand that is hard to predict. 
+  **Scheduled scaling** provisions capacity against the calendar and suits demand with a known rhythm, such as business hours or a sales event. 
+  **Predictive scaling** uses machine learning on the history of a metric to provision ahead of anticipated demand, which offsets provisioning latency for workloads with a repeating pattern. 

 Many workloads use predictive or scheduled scaling to establish a baseline and metric-based scaling to handle the variation on top of it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Confirm the component is horizontally scalable:** Verify that the component provides identical, stateless replicas that can each serve any request. Exclude components that hold unique state from automatic scaling. For the resources that support managed scaling, see [AWS services that you can use with Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html). 

1.  **Choose the scaling method for the demand pattern:** Select metric-based scaling for unpredictable demand, [scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) for demand that follows a calendar, or [predictive scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) for demand with a repeating historical pattern. Combine methods where a workload has both a baseline and variable load. 

1.  **Select the scaling mechanism for the component:** Use [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) for EC2 instances and [Application Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) for other AWS services and container tasks. For Kubernetes pods, use [Horizontal Pod Autoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) or [Kubernetes Event-driven Autoscaling (KEDA)](https://keda.sh/). For Kubernetes node capacity, use [Karpenter](https://karpenter.sh/) or [Cluster Autoscaler](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/). 

1.  **Determine metrics and targets through load testing:** For metric-based scaling, load test to find the metric that tracks demand and set a utilization target that leaves headroom, typically 50 to 70 percent. For scheduled scaling, determine the resource count needed at each date and time. Establish the maximum resources required to serve expected peak traffic. 

1.  **Configure the scaler and verify its limits:** Apply the policies, metrics, and schedules you determined, and confirm that minimum and maximum limits are set correctly so scaling does not fail at the boundary. 

1.  **Validate scaling behavior before and after production:** Load test the configuration in a non-production environment and observe how the system reacts, then adjust. When you enable scaling in production, configure alarms that notify you of unexpected scaling behavior. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL07-BP01 Use automation when obtaining or scaling resources](rel07-bp01.md) 
+  [REL07-BP04 Load test your workload](rel07-bp04.md) 
+  [REL07-BP02 Obtain resources upon detection of impairment to a workload](rel07-bp02.md) 
+  [REL12-BP03 Test scalability and performance requirements](rel12-bp03.md) 

 **Related documents:** 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [AWS services that you can use with Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html) 
+  [Scheduled scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) 
+  [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) 
+  [Managing throughput capacity automatically with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) 
+  [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/) 
+  [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) 

 **Related examples:** 
+  [Avoiding insurmountable queue backlogs](https://builder.aws.com/content/3EuRcgkTP1MI0c7zM8W6HL3WIqA/avoiding-insurmountable-queue-backlogs) 
+  [AWS Marketplace: products that can be used with auto scaling](https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling) 