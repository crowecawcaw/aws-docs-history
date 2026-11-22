

# PERF02-BP04 Scale your compute resources dynamically

 Dynamic scaling adjusts compute up and down automatically as load changes, so you hold performance during peaks without paying for peak capacity around the clock. Scaling holds performance only when it tracks a metric that reflects real load and handles both scale-out and scale-in without dropping work. 

 **Desired outcome:** 
+  Your compute capacity adjusts automatically to match real demand, holding performance without manual intervention. 
+  Your scaling responds to a metric that tracks how busy the workload actually is. 
+  Your workload handles both scale-out and scale-in events without dropping work or corrupting state. 
+  Your account quotas are set to absorb your expected peak, and you have tested against it. 

 **Common anti-patterns:** 
+  Teams react to alarms by adding capacity manually instead of automating the response. 
+  Teams carry over static, on-premises sizing and never enable elasticity. 
+  Teams scale out for a spike and leave the extra capacity running after demand falls. 
+  Teams scale on a metric that does not reflect real load, such as CPU for a queue-driven job. 
+  Teams enable scaling but never test that the workload survives a scale-in event. 

 **Benefits of establishing this best practice:** 
+  Cost drops because capacity is released when demand falls instead of running continuously at peak. 
+  Performance holds through demand changes because capacity tracks load in real time. 
+  Reliability improves as the workload absorbs traffic swings without manual firefighting. 
+  Capacity planning shifts from guessing peak size to defining a scaling policy. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 *Target-tracking* watches a utilization metric and adjusts capacity to hold it at a set point, which fits workloads with variable but unpredictable load. *Predictive scaling* provisions ahead of recurring daily and weekly patterns, so capacity is already in place when a known peak arrives. *Schedule-based scaling* changes capacity at fixed times for load you can anticipate, such as a nightly batch run. *Service scaling* delegates scaling to a service, such as serverless functions, that scales by design with no policy to tune. Many workloads combine these approaches: predictive scaling for the known daily curve, target-tracking for the variation on top of it. 

 A good scaling metric is a utilization signal that rises and falls in proportion to the number of instances handling the work. CPU utilization fits a web tier, where more requests mean more CPU. It fails for a video transcoding fleet, where every instance runs at 100 percent CPU by design and utilization does not reflect backlog. The right signal there is the depth of the job queue, which grows when you need more capacity and shrinks when you have enough. 

 Removing capacity terminates instances or tasks that may be holding connections, sessions, or in-flight work. A workload that does not drain gracefully drops requests or corrupts state every time it scales down. Test both scale-out and scale-in, and confirm the workload finishes or hands off in-flight work before a resource is removed. 

 Service quotas cap how far you can scale, so a policy that is theoretically elastic will stall at a limit you never raised. Set quotas to cover your expected peak and test against them before you rely on the policy. Data and integration services in the path, such as extract-transform-load jobs, also need matching elasticity, or they become the bottleneck the compute tier was scaled to avoid. 

 On AWS, [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) manages instance capacity. [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) scales services beyond Amazon EC2, such as Amazon ECS tasks, and [Karpenter](https://karpenter.sh/) scales Kubernetes clusters. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select a scaling mechanism for each component:** Match each component to the mechanism that fits its compute model. Use the following as a starting point. 


<table>
<thead>
  <tr><th> Autoscaling mechanism </th><th> Where to use </th></tr>
</thead>
<tbody>
  <tr><td> <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html">Amazon EC2 Auto Scaling</a> </td><td> Provision the right number of <a href="https://aws.amazon.com/ec2/">Amazon EC2</a> instances for application load. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html">Application Auto Scaling</a> </td><td> Scale services beyond EC2, such as <a href="https://aws.amazon.com/ecs/">Amazon ECS</a> tasks or provisioned <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> concurrency. </td></tr>
  <tr><td> <a href="https://karpenter.sh/">Kubernetes Cluster Autoscaler or Karpenter</a> </td><td> Scale Kubernetes cluster capacity. </td></tr>
</tbody>
</table>


1.  **Extend scaling to non-compute services:** Confirm that data and integration services in the request path scale with demand too, such as [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html), so they do not become the bottleneck. 

1.  **Choose a scaling metric that tracks real load:** Pick a utilization metric that rises and falls in proportion to the work per instance. For a queue-driven workload, scale on queue depth rather than CPU, using a [custom metric](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#target-tracking-choose-metrics) where the built-in metrics do not fit. 

1.  **Use dynamic scaling with target tracking:** Configure [dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) rather than [manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html), and use [target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) to hold the chosen metric at its target. 

1.  **Test both scale-out and scale-in:** Verify the workload drains in-flight work before capacity is removed, and review [scaling activity history](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html) to confirm both directions behave as intended. 

1.  **Add predictive scaling for recurring patterns:** Where demand follows daily or weekly cycles, enable predictive scaling so capacity is in place before the peak arrives. 

1.  **Set and test service quotas for peak:** Confirm account service quotas cover your expected peak, and load-test against them so the policy is not capped by an unraised limit. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md) 
+  [PERF02-BP02 Collect compute-related metrics](perf02-bp02.md) 
+  [PERF02-BP03 Configure and right-size compute resources](perf02-bp03.md) 

 **Related documents:** 
+  [Cloud compute with AWS](https://aws.amazon.com/products/compute/) 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) 
+  [Amazon ECS cluster capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Managing Amazon EC2 capacity and availability](https://www.youtube.com/watch?v=TyFMsx9PVeM) 
+  [AWS re:Invent 2023 - What's new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g) 
+  [AWS re:Invent 2023 - Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0) 

 **Related examples:** 
+  [Amazon EC2 Auto Scaling group examples](https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples) 
+  [Amazon EKS workshop](https://www.eksworkshop.com/) 