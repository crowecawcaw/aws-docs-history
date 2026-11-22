

# REL11-BP03 Automate healing on all layers

 When a component fails, automated actions should remediate it. Some degradations heal through a service's own internal mechanisms, while others need a resource to be restarted, replaced, or removed. Automate healing on all layers to improve recovery time and reduce manual intervention. 

 **Desired outcome:** 
+  Automated actions remediate failures at each layer of the workload without manual intervention. 
+  Stateless components are replaced rather than repaired, so a restart is a safe and reliable recovery action. 
+  Databases fail over or promote replicas through automation, not a manual runbook. 
+  Clusters that do not sit behind a load balancer are sized to survive the loss of at least one node while they recover. 
+  Event-driven automation detects a failure signal and runs remediation logic in response. 

 **Common anti-patterns:** 
+  Teams provision resources without autoscaling. 
+  Teams deploy applications on individual instances or containers with no group to replace them. 
+  Applications that could run in multiple locations are deployed without automatic recovery. 
+  Teams manually heal the failures that autoscaling and automatic recovery were meant to handle. 
+  Databases have no automated failover. 
+  Traffic has no automated way to reach new endpoints after a failure. 

 **Benefits of establishing this best practice:** 
+  Mean time to recovery drops because remediation runs the moment a failure is detected. 
+  Recovery is consistent because automation performs the same steps every time. 
+  Operators are freed from routine restarts and can focus on root causes. 
+  Stateless, replaceable components turn most failures into a simple resource swap. 
+  Event-driven remediation extends healing to failures that autoscaling alone cannot address. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automated healing depends on an early design choice: statelessness. When a component holds no local state, you can replace it instead of repairing it. Replacement is far more reliable than repair because it returns the component to a known-good starting point. In the cloud, the cleanest recovery is often to discard the failed compute instance or function and launch a replacement. Where state is unavoidable, isolate it in a managed data store so the compute tier stays disposable. 

 Handle network calls like component failures. A timeout and an error response from a dependency have the same effect on your system. Apply one strategy to both: a limited number of retries with exponential backoff and jitter. The limit prevents retry traffic from overwhelming the dependency, the backoff spreads attempts over time, and the jitter prevents many clients from retrying at the same time. 

 Stateless tiers behind a load balancer heal through an Auto Scaling group that replaces unhealthy members. Clustered systems that manage their own membership, such as search or streaming clusters, must be sized to keep running after losing a node. They can then serve at reduced capacity while a replacement joins. For large-scale loss, such as an entire Availability Zone, provisioning replacements on demand is the least reliable option. It assumes both a working control plane and spare capacity exactly when both are least certain. Static stability, which holds the spare capacity before the event, is the more resilient choice for that scale. 

 Not every failure fits a built-in recovery feature. When autoscaling and automatic recovery do not apply or fail, use an event-driven pattern. A failure signal such as an alarm or a state change invokes remediation logic that you define. This pattern extends healing beyond compute to almost any resource. Because you write the recovery logic, test it as carefully as the workload it protects. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Heal stateless tiers with Auto Scaling groups:** Deploy stateless application tiers into [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html) so unhealthy members are replaced and capacity adjusts automatically. 

1.  **Front compute with the right load balancer:** Place compute behind [Elastic Load Balancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) and choose the load balancer type that matches the traffic, so requests route only to healthy targets. 

1.  **Automate database healing:** Configure [Amazon RDS automatic failover](https://repost.aws/questions/QU4DYhqh2yQGGmjE_x0ylBYg/what-happens-after-failover-in-rds) to a standby instance, and build automation to promote an Amazon RDS read replica to primary where a standby is not available. 

1.  **Enable automatic recovery for single-location instances:** For applications that cannot run in multiple locations but tolerate a reboot, enable [automatic recovery on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html). Recovery preserves instance metadata, IP addresses, [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html), and mount points to [Amazon EFS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html) or [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html). 

1.  **Size self-managed clusters for node loss:** For clustered systems that do not use a load balancer, provision enough capacity to keep serving after losing at least one node, and trigger a workflow with [AWS Systems Manager](https://docs.aws.amazon.com/resilience-hub/latest/userguide/integrate-ssm.html) to recreate the lost node. 

1.  **Script remediation with event-driven automation:** Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to match failure events such as [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) and invoke [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) or [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to run custom remediation when built-in recovery does not apply. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 
+  [REL11-BP02 Fail over to healthy resources](rel11-bp02.md) 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 
+  [REL07-BP02 Obtain resources upon detection of impairment to a workload](rel07-bp02.md) 

 **Related documents:** 
+  [How scaling plans work](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html) 
+  [Automatic instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) 
+  [What is Amazon Elastic Block Store?](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) 
+  [Use Amazon EFS with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html) 
+  [What is Amazon FSx for Lustre? - FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) 
+  [What is FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) 
+  [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [Integrate Systems Manager Automation with AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/integrate-ssm.html) 
+  [Understand resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/) 

 **Related videos:** 
+  [Multi-AZ with Standby for Amazon OpenSearch Service: Webinar and Demo \| AWS Events](https://www.youtube.com/watch?v=l4ofYA0NAvc) 
+  [Recent enhancements in Amazon RDS Multi-AZ with two readable standbys- AWS Database in 15](https://www.youtube.com/watch?v=mPVb-ljT-vA) 

 **Related examples:** 
+  [Workshop: Amazon EC2 Auto Scaling](https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/10-ec2/ec2-auto-scaling) 
+  [Workshop: Amazon RDS High Availability](https://catalog.us-east-1.prod.workshops.aws/workshops/0135d1da-9f07-470c-9845-44ead3c78212/en-US/highavailability) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Logging and monitoring in AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/security-logging-monitoring.html) 