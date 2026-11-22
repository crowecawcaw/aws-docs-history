

# SUS02-BP02 Provision development, build, and test resources dynamically

 Workloads use non-production resources intermittently and for a limited amount of time along the development lifecycle. Examples are developers' workstations, compute instances for builds, user acceptance tests, and pre-production environments. To reduce the resource consumption of your software development lifecycle, maintain development and test resources only when actively needed, rather than keeping them permanently provisioned. By using automation to create and decommission environments on demand, resources are only consumed during active development and testing phases. 

 This approach applies the principles of infrastructure as code (IaC) and automated provisioning to test environments, treating them as ephemeral resources that exist only when providing value. Auto-stopping resources reduces the environmental impact of idle development infrastructure, such as developer workspaces and notebook servers, and allows the provisioning of more powerful resources when needed. 

 **Desired outcome:** 
+  You provision development, build, and test resources only when they are actively used, with automation to create and decommission environments as needed. 
+  You achieve high utilization during each resource's lifetime and minimize idle capacity in your development infrastructure. 
+  You stay flexible about the underlying resources you consume, for example by allowing mixed EC2 instance types. 

 **Common anti-patterns:** 
+  Permanently maintaining a fixed number of production-sized test environments. 
+  Manually provisioning and decommissioning test infrastructure. 
+  Keeping continuous integration and deployment (CI/CD) pipeline resources running even when no build or test is running. 
+  Constantly running a full-scale development environment for each team member, irrespective of their role or working hours. 
+  Requiring a single compute type across all environments, which prevents the use of mixed instance types, Spot capacity, or AWS Graviton where they would fit. 

 **Benefits of establishing this best practice:** 
+  Development infrastructure is sized appropriately for its actual use. 
+  Creates consistency between environments through automated provisioning. 
+  Hardens the reliability of automated creation and teardown processes, and simplifies the rollout of security and performance changes. 
+  Reduces configuration drift between environments. 
+  Reduces development infrastructure cost. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing on-demand development environments requires a combination of infrastructure as code, automation tools, and operational processes. The goal is to make environment creation and deletion faster and more convenient while maintaining organizational sustainability goals. Developers provision resources only when needed rather than keeping development, build, and test environments perpetually running. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Monitor development, build, and test environment utilization with [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) or [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Metrics. 

1.  Implement infrastructure as code for all environments and stages in the development lifecycle: 

   1.  Use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS CDK](https://aws.amazon.com/cdk/) to define development infrastructure. 

   1.  Parameterize environments to allow for different sizes or configurations based on needs. 

1.  Create automation for environment lifecycle management: 

   1.  Build templates and workflows to provision resources on demand, made available to teams through [Service Catalog](https://aws.amazon.com/servicecatalog/). 

   1.  Implement automated stop or teardown processes based on idle time, schedule with [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/), or use service-specific features in services such as [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/). 

   1.  Use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runbooks to orchestrate complex environment provisioning and teardown, and [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html) to trigger start and stop actions on a schedule. 

1.  Implement scheduling for CI/CD pipelines and their build and test resources: 

   1.  Configure [AWS CodeBuild](https://aws.amazon.com/codebuild/) to run builds and tests with on-demand compute, so build capacity exists only while a build is running. 

   1.  Use CodeBuild as a [managed runner](https://docs.aws.amazon.com/codebuild/latest/userguide/runners.html) for GitHub Actions, self-managed GitLab, or Buildkite jobs rather than maintaining permanently running self-hosted runners, as covered in [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md). 

   1.  Treat [reserved capacity fleets](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html) as a deliberate trade-off, because they shorten build start times but hold capacity between builds. 

   1.  Schedule regular cleanup of build artifacts and unused resources. 

   1.  Consider solutions such as [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) for time-based environment management. 

   1.  Automate and optimize tests (for example, by generating unit tests with [Kiro](https://kiro.dev/)) to keep the durations for running test infrastructure low. 

1.  Optimize environments for quick provisioning: 

   1.  Build and reuse container images or Amazon Machine Images to speed up infrastructure creation. 

   1.  Design modular services adhering to the microservices approach that allow for partial provisioning based on needs. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md) 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 
+  [FND01-BP04 Establish a strategy for experimental and temporary environments](fnd01-bp04.md) 

 **Related documents:** 
+  [Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/) 
+  [AWS re:Invent 2024 - Continuous integration and continuous delivery (CI/CD) for AWS (DOP202) slides](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/events/approved/reinvent-2025/reinvent/2024/slides/dop/DOP202_Continuous-integration-and-continuous-delivery-CI-CD-for-AWS.pdf) 

 **Related examples and solutions:** 
+  [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) 