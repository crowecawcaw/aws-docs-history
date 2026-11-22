

# COST03-BP02 Implement efficient resource lifecycle management

 When a workload changes, some resources become oversized, idle, or obsolete, and keep running until someone acts. Efficient lifecycle management matches capacity to real demand and retires resources you no longer need, through scaling and decommissioning triggered on a schedule or by events. 

 **Desired outcome:** 
+  Your workload runs no idle or underutilized resources that demand cannot justify. 
+  Your resources scale up and down automatically as demand changes, without manual intervention. 
+  You decommission obsolete resources through a standardized process that runs periodically. 
+  Your architecture tolerates resource termination as part of normal operation. 

 **Common anti-patterns:** 
+  Teams keep excess capacity running for scenarios that might never occur. 
+  Resource utilization reviews happen manually and infrequently, so waste accumulates between them. 
+  Workloads lack automated scaling and stay provisioned for peak demand at all times. 
+  Architecture decisions ignore how resources will be retired, which makes decommissioning disruptive. 

 **Benefits of establishing this best practice:** 
+  Spend falls because the workload consumes only the resources current demand requires. 
+  Capacity adjusts to demand automatically, which improves both cost and performance. 
+  Decommissioning becomes predictable and low-risk because the process is standardized and rehearsed. 
+  Resource consumption tracks business value rather than worst-case assumptions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A workload's resource needs are set at design time, but demand changes continuously. New features, retired products, seasonal traffic, and shifting markets move the line between what you provisioned and what you use. Closing that gap means two things: scaling adjusts capacity for the resources you keep, and decommissioning removes the resources you no longer need. 

 Where you can avoid managing capacity, do so. Serverless services scale automatically, which avoids the lifecycle problem for those components. Adopt a serverless-first approach across compute, integration, and data storage. For components that cannot be serverless, automated scaling matches capacity to demand so you neither pay for idle resources nor run short during peaks. Scaling requires the workload to tolerate resources appearing and disappearing, which you should design in from the start. 

 Decommissioning starts with a trigger. A workload state change, such as a product reaching end of life or a component being replaced, signals that resources can go. External events like shifts in customer demand or product deprecations do the same. Match review effort to what an account stands to save: an account spending a few dollars a month does not warrant the same scrutiny as one spending thousands. 

 Removing a resource can break components that depend on it. Workloads that expect resources to disappear, through health checks, retries, and stateless components, absorb termination without an issue. Workloads that assume permanence fail when a resource is removed. Automating teardown lowers cost and error rate, and defining resources in infrastructure as code makes the operation reversible: a resource defined in a template can be recreated if the decision proves wrong. 

 A standardized decommissioning process reduces the risk that teams will resist to remove their resources. The process confirms the resource is unused, records the metadata needed to recreate it, backs up data where required, restricts access for a cooling-off period, and only then removes the resource. Figure 1 shows this sequence. Restricting access before deletion lets you confirm nothing breaks while retaining the ability to restore the resource. <a name="cost03-bp02-fig1"></a>

![Flowchart of the decommissioning sequence: confirm the resource is unused, record metadata, back up data, restrict access during a cooling-off period, then remove the resource.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/decommissioning-process-flowchart.png)

*Standardized workload decommissioning process*


 AWS provides services for scaling and decommissioning. [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) and [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) adjust capacity for compute and other resources; serverless services such as [AWS Lambda](https://aws.amazon.com/pm/lambda) and [AWS Fargate](https://aws.amazon.com/fargate/) remove capacity management entirely. [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/) surface idle and rightsizing candidates, and [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) recommends which resources to remove or resize. For automated teardown, [Amazon EventBridge](https://aws.amazon.com/eventbridge/) triggers cleanup and [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) manages snapshot retention. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Monitor resources to identify waste:** Configure [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for detailed usage analysis and review [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/) for idle and rightsizing recommendations. Add [custom Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) for utilization signals specific to your workload. Match review frequency to each account's spend, so effort tracks potential savings. 

1.  **Automate scaling for the resources you keep:** Configure [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) for compute and [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) for other supported services. For components that can be serverless, use AWS Lambda, Amazon DynamoDB on-demand capacity, Amazon Aurora Serverless, and [AWS Fargate](https://aws.amazon.com/fargate/) for containers, so capacity follows demand without manual intervention. 

1.  **Design workloads to handle resource changes:** Adopt a serverless-first approach where it fits, and define resources with infrastructure as code so provisioning and teardown are repeatable and reversible. Design components to tolerate resource termination, and use chaos engineering to verify that the workload stays healthy when resources are removed. 

1.  **Standardize your decommissioning process:** Document a repeatable process that verifies the workload and its resources are unused, coordinates with resource owners, records metadata such as public IP addresses, Region, Availability Zone, VPC, subnet, and security groups, and creates backups such as Amazon EBS snapshots or AMIs for critical resources. Confirm whether resources were deployed with AWS CloudFormation, Terraform, or the AWS Cloud Development Kit (AWS CDK) (AWS CDK) so they can be recreated, then restrict access for a cooling-off period before removing them from your domain, DNS, and management tooling. Figure 1 shows the full sequence. 

1.  **Remove all dependencies when decomissioning resources:** When decommissioning Amazon EC2, stop or terminate instances and load balancers, delete Auto Scaling infrastructure, release dedicated hosts, delete Amazon EBS volumes and snapshots, release Elastic IP addresses, deregister Amazon Machine Images (AMIs), and terminate AWS Elastic Beanstalk environments. Terminated instances stay visible briefly and stop incurring charges once they leave the running state. For the full procedure, see [How do I delete or terminate my Amazon EC2 resources?](https://repost.aws/knowledge-center/delete-terminate-ec2) 

1.  **Account for early deletion fees on archived data:** Before deleting archived objects, check the minimum storage duration. Deleting an object from Amazon Glacier storage classes before it meets the minimum duration incurs a prorated early deletion fee. Review [performance across the Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/) for the minimum duration per class, and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) for how the fee is calculated. 

1.  **Automate decommissioning where possible:** Use [AWS Lambda](https://aws.amazon.com/pm/lambda) functions triggered by [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for scheduled cleanup, and apply [Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) to expire temporary Amazon DynamoDB data. Configure [Amazon S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to delete or transition objects, [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) to manage Amazon EBS snapshots, and [automatic task and image cleanup](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/automated_image_cleanup.html) for Amazon ECS. 

1.  **Review and refine on a cadence:** Schedule regular utilization reviews and monitor continuously for cost and usage anomalies. Create feedback loops between operations and development teams so optimization insights reach the people who design resources, and update the decommissioning process as you learn. Align these reviews with the [AWS Well-Architected Framework Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html) to advance efficiency goals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST03-BP01 Track resources over their lifetime](cost03-bp01.md) 
+  [COST03-BP03 Enforce data retention policies](cost03-bp03.md) 
+  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md) 
+  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md) 

 **Related documents:** 
+  [Identifying opportunities with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) 
+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Right-sizing your application services: Rethinking microservices](https://www.youtube.com/watch?v=ZOQwxxgvKJs) 
+  [How do I retain some of my resources when I delete an AWS CloudFormation stack?](https://www.youtube.com/watch?v=T4xgK87mupg) 

 **Related examples:** 
+  [How do I remove active resources that I no longer need in my AWS account?](https://repost.aws/knowledge-center/terminate-resources-account-closure) 
+  [Viewing idle resource recommendations in AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html) 

 **Related tools:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 