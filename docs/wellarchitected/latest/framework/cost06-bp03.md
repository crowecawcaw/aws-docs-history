

# COST06-BP03 Select resource type, size, and number automatically based on metrics

 Use metrics from the running workload to adjust resource type, size, and number as conditions shift. Drive these adjustments through a feedback loop, such as managed automatic scaling, automatic storage tiering, or custom code in the workload. 

 **Desired outcome:** 
+  Your workloads adjust capacity automatically in response to live metrics rather than staying fixed at their initial size. 
+  You monitor resource utilization continuously and act on right-sizing recommendations. 
+  Your compute and storage select tiers or types automatically as usage patterns change. 
+  Your scaling responds to demand without requiring an engineer to intervene for routine changes. 

 **Common anti-patterns:** 
+  Sizing a workload for its highest potential load and leaving that capacity running at all times. 
+  Running a workload that could scale without configuring any scaling. 
+  Identifying right-sizing opportunities and never acting on them. 
+  Treating every capacity change as a manual operation, so adjustments lag demand. 
+  Teams run every instance of a recurring job with one fixed default configuration, whatever the size of that run. 

 **Benefits of establishing this best practice:** 
+  Workloads carry the capacity they need for current demand without paying for idle headroom. 
+  Capacity tracks demand automatically, which removes the operational cost of manual resizing. 
+  Storage cost falls automatically as data access patterns cool, without performance impact. 
+  Continuous measurement surfaces underused resources that a one-time sizing exercise would miss. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 A resource sized from data is correct only for the demand present when you measured it. Real workloads move: traffic follows daily and seasonal cycles, data cools as it ages, and growth shifts the profile over months. Static sizing forces a choice between provision for the peak and waste money during every trough, or provision for the average and fail during every spike. A feedback loop resolves this by using live metrics to drive capacity, so the workload holds enough for current demand and no more. 

 A feedback loop reads metrics from the running workload, compares them against targets, and changes resources when they drift. Managed automatic scaling implements this loop, as does custom code when a service has no managed option. The point is that a script that stops an instance, changes its type, and starts it back up will right-size a workload for you, instead of someone making that same change manually. 

 Reactive and predictive scaling answer different demand shapes. Reactive scaling responds to metrics as they cross thresholds, which suits demand that rises gradually enough for new capacity to come online in time. It struggles with sudden spikes because provisioning is not instant, and the workload can degrade before capacity arrives. Predictive scaling forecasts demand from historical patterns and provisions ahead. It handles known cycles well but fails when actual demand departs from the forecast. Workloads with both a predictable baseline and unpredictable bursts often combine reactive and predictive scaling. 

 Automation carries its own failure modes. Tune scaling policies to react quickly to real demand shifts without causing thrash. Thrash scales resources up and down repeatedly, and each change carries a cost. Metrics that do not reflect user experience send the wrong signal. The workload then scales on CPU when memory or a downstream dependency is the actual constraint. Establish sound observability before automating scaling. 

 Some services perform automatic selection without a custom loop. [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) moves objects between access tiers as usage changes, and [Amazon EFS Infrequent Access](https://docs.aws.amazon.com/efs/latest/ug/) does the same for file storage. Both lower cost as data cools without performance impact or operational overhead. For compute, use [attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) to define instance requirements such as vCPU and memory. The scaling group then adopts newer, more cost-effective instance types automatically. 

 For jobs that run repeatedly, one default configuration oversizes small runs and fails on large ones. Predict each run's configuration from its own characteristics, such as data volume and prior resource use, using historical run data. For example, [AWS Batch](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) lets you override vCPU and memory for each job when you submit it. Validate each prediction against set bounds, and fall back to the job's last known-good configuration when it falls outside them, so a bad prediction does not become a failed run. This needs enough run history and periodic model retraining as workloads change. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure workload metrics for observability:** Capture the metrics that reflect the customer experience and the resource dimensions that scaling will act on, such as CPU and memory utilization. Install the [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) where memory metrics are needed, since instances do not report memory by default. For object storage, use [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) to see usage and activity trends across buckets. 

1.  **Review right-sizing and idle recommendations:** Use [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html), [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html), or [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html) to find over-provisioned resources. Identify instances whose maximum CPU and memory utilization stays below 40 percent over a four-week window as candidates to resize. Compute Optimizer also flags [idle resources](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html) and covers Amazon RDS and Aurora databases alongside EC2, Auto Scaling groups, Amazon EBS, Lambda, and ECS on Fargate, so include databases and idle candidates in the review. Reviewing recommendations is not the same as acting on them: [Compute Optimizer automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules.html) implement matching recommendations on a recurring schedule, scoped by criteria such as Region and resource tags, so that a decision taken once keeps being applied. 

1.  **Automate compute scaling:** Configure [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) so capacity follows demand, choosing reactive policies for gradual demand and [predictive scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) for known cycles. Apply [attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) so the group adopts cost-effective instance types automatically, and combine On-Demand with Spot, Reserved Instances, or Savings Plans to lower the rate. 

1.  **Automate storage tier selection:** Enable [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) for objects with changing or unknown access patterns, and [Amazon EFS Infrequent Access](https://docs.aws.amazon.com/efs/latest/ug/) for file data, so storage cost tracks access without manual intervention. 

1.  **Tune and monitor the loop:** Set scaling thresholds and cooldowns that avoid thrash, and confirm the loop scales on metrics that reflect the real constraint. Review scaling behavior against cost and performance data periodically and adjust the policies. 

1.  **Predict per-run sizing with a fallback:** For recurring jobs, predict each run's resources from historical run data, check the prediction against safe bounds, and fall back to the last known-good configuration when it fails the check. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST06-BP01 Perform cost modeling](cost06-bp01.md) 
+  [COST06-BP02 Select resource type, size, and number based on data](cost06-bp02.md) 
+  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md) 
+  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md) 

 **Related documents:** 
+  [What is Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [AWS Compute Optimizer supported resources](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html) 
+  [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html) 
+  [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) 
+  [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) 
+  [Amazon EFS storage classes](https://docs.aws.amazon.com/efs/latest/ug/) 
+  [Attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) 
+  [Identifying opportunities to right size](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ec2-metrics-analyzed.html) 

 **Related examples:** 
+  [Faster scaling with Amazon EC2 Auto Scaling Target Tracking](https://aws.amazon.com/blogs/compute/faster-scaling-with-amazon-ec2-auto-scaling-target-tracking/) 
+  [Optimize compute resources on Amazon ECS with Predictive Scaling](https://aws.amazon.com/blogs/containers/optimize-compute-resources-on-amazon-ecs-with-predictive-scaling/) 
+  [Introducing Automated Amazon EBS Volume Optimization in AWS Compute Optimizer](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-automated-amazon-ebs-volume-optimization-in-aws-compute-optimizer/) 

 **Related workshops:** 
+  [CFM TIPs: Amazon EC2 compute playbook](https://catalog.workshops.aws/awscff/en-US/playbooks/compute/ec2) 