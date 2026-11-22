

# OPS04-BP01 Employ and test safe deployment strategies

 Safe deployment practices control how a change reaches customers, so that a defect affects the fewest of them before you catch it. When you release changes in increments and check health at each step, you limit the scope of impact and shorten recovery time. 

 **Desired outcome:** 
+  Your delivery pipeline releases production changes in incremental stages rather than to all customers at once. 
+  You have automated health checks at each stage that must pass before the change proceeds to the next. 
+  Your deployment strategy matches each workload's fault isolation boundaries, so a failed change is contained to a single host, cell, or Availability Zone. 
+  You select and apply a documented safe deployment strategy for every production change. 

 **Common anti-patterns:** 
+  Teams deploy a change to all of production at once, so a defect reaches every customer at the same time. 
+  An in-place update overwrites the running version, which forces a second change to restore the previous version and extends recovery time. 
+  Release coordination depends on manual planning across several teams, which limits how often teams can ship features. 
+  Deployments proceed without automated health checks, so failures surface only after customers report them. 

 **Benefits of establishing this best practice:** 
+  A defective change affects a fraction of customers instead of all of them, because deployment stops before full rollout. 
+  Recovery is faster because the previous version stays available and traffic can shift back to it. 
+  Teams deploy more often and with more confidence, because safety controls reduce the cost of a failed change. 
+  Emergency releases become rare, because most defects are caught in an early stage. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A fractional deployment releases the change to a small portion of your fleet, verifies it against health signals, then expands in controlled increments. 

 Fractional deployments work best when the increments align with your [fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) — the host, cell, Availability Zone, or Region that contains the effect of a failure. AWS structures this as waves and stages. A *wave* is a fault container, such as a Region, that deploys in parallel with other containers. Within a wave, the change moves through *stages*: a one-box stage that takes one host's worth of traffic, then progressively larger fractions within one Availability Zone. Each stage ends with *bake time* to observe health metrics before the next begins. Without bake time, you expand before problems surface. 

 Several strategies implement this pattern, differing in cost, speed, and rollback behavior. Rolling deployments replace instances in batches and use the least extra capacity, but a failure can leave the fleet in a mixed-version state. Immutable and blue/green deployments create a parallel set of resources running the new version and shift traffic to it. Rollback shifts traffic back, at the cost of running two environments during the transition. Canary releases send a small share of live traffic to the new version, which catches problems that appear only under real load. Feature flags separate deployment from release, so you can turn a change on or off without another deployment. Most teams combine these. 

 Avoid in-place updates for high-risk changes. When you modify a running system in place and the change fails, you have no clean previous version to return to. Recovery then means applying another change under pressure, which lengthens downtime. 

 Take extra care with databases and other stateful resources, because you cannot discard and replace them the way you replace stateless hosts. Blue/green deployments for managed databases create a synchronized staging environment you can test before promoting it, so you validate schema and configuration changes against production-like data before they take traffic. Plan how in-flight transactions and replication are handled during the switch. 

 Figures 1 through 3 show the [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) blue/green workflow for Amazon EC2, Amazon ECS, and AWS Lambda. AWS CodeDeploy automates in-place and blue/green deployments across these compute types and integrates with monitoring, so a failed health check can halt or reverse a rollout. See [Automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) and [My CI/CD pipeline is my release captain](https://builder.aws.com/content/3Ev3XnnYuuBhlgnywbbVFzwibm1/my-cicd-pipeline-is-my-release-captain) for how these stages fit together at scale. <a name="ops04-bp01-fig1"></a>

![Workflow diagram showing the AWS CodeDeploy blue/green deployment process for Amazon EC2, where a new application version is deployed to a replacement environment and traffic shifts after health checks pass.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/deployment-process-ec2.png)

*AWS CodeDeploy blue/green deployment process for Amazon EC2*
<a name="ops04-bp01-fig2"></a>

![Workflow diagram showing the AWS CodeDeploy blue/green deployment process for Amazon ECS, where a new task set is deployed and traffic shifts after health checks pass.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/deployment-process-ecs.png)

*AWS CodeDeploy blue/green deployment process for Amazon ECS*
<a name="ops04-bp01-fig3"></a>

![Workflow diagram showing the AWS CodeDeploy blue/green deployment process for AWS Lambda, where traffic shifts from the current function version to a new version according to a deployment configuration.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/deployment-process-lambda.png)

*AWS CodeDeploy blue/green deployment process for AWS Lambda*


 Decouple your continuous integration (CI) pipeline from your continuous delivery (CD) pipeline. Services such as [Service Catalog](https://aws.amazon.com/servicecatalog/), [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/), and [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo) host build artifacts that CD pipelines consume. Decoupling improves resilience and simplifies deploying across Regions: a single CI pipeline publishes the artifact to multiple Regions or accounts, and a separate instance of the CD pipeline deploys it in each Region, for example through an [AWS CloudFormation StackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html). 

 With the pipelines decoupled, you can stage and sequence deployments to fit release constraints such as change freezes and release schedules. A managed service provider (MSP) or software-as-a-service (SaaS) provider can then serve clients with different acceptance testing and release approvals from a single build. 

 Deployment windows are a separate constraint from fault isolation. Some fleets accept changes only during specific hours, such as Regions with restricted operating-hour windows, or teams spread across time zones with no single window that works for everyone. When a narrow window limits how much of your fleet you can update in one pass, shorten each deployment's duration so more of the fleet completes within the time available. Track how many pipelines have no valid window at all, and widen those windows deliberately. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Gate promotion to production with an approval workflow:** Trigger the production rollout sequence when a change is promoted to production, so the safe deployment stages run consistently for every release. 

1.  **Automate deployments with a managed deployment service:** Use [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) to run your chosen strategy. Its [deployment options](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps.html) include in-place deployments for Amazon EC2 and on-premises instances, and blue/green deployments for Amazon EC2, AWS Lambda, and Amazon ECS. Where useful, [integrate AWS CodeDeploy with other AWS services](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws.html). 

1.  **Apply blue/green deployments to stateful resources:** Use managed blue/green deployments for databases such as [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) and [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html), so you validate changes in a synchronized staging environment before promotion. 

1.  **Monitor each deployment stage:** [Monitor deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring.html) with Amazon CloudWatch, AWS CloudTrail, and Amazon Simple Notification Service (Amazon SNS) notifications, so a stage that breaches its health criteria stops the rollout. 

1.  **Run automated post-deployment tests:** After each stage, run functional, security, regression, integration, and load tests that confirm the change behaves as expected before the next increment begins. 

1.  **Establish deployment troubleshooting procedures:** Document how to [troubleshoot deployment issues](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting.html) and reverse a rollout, so responders act from a known procedure rather than improvising during an incident. 

1.  **Automate scheduling within constrained deployment windows:** For fleets restricted to narrow deployment windows, use [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html) to schedule deployment tasks within the time available, and measure the fraction of your fleet with no valid window so you can prioritize automation that shortens per-deployment duration. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 
+  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) 
+  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 

 **Related documents:** 
+  [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html) 
+  [Working with deployment configurations in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) 
+  [Set up an API Gateway canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html) 
+  [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) 
+  [Blue/green deployments with AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html) 
+  [Fault-isolated, zonal deployments with AWS CodeDeploy](https://aws.amazon.com/blogs/devops/fault-isolated-zonal-deployments-with-aws-codedeploy/) 
+  [New – Fully managed blue/green deployments in Amazon Aurora and Amazon RDS](https://aws.amazon.com/blogs/aws/new-fully-managed-blue-green-deployments-in-amazon-aurora-and-amazon-rds/) 

 **Related examples:** 
+  [Try a sample blue/green deployment in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-blue-green.html) 

 **Related workshops:** 
+  [Building CI/CD pipelines for Lambda canary deployments using AWS CDK](https://catalog.us-east-1.prod.workshops.aws/workshops/5195ab7c-5ded-4ee2-a1c5-775300717f42/en-US) 