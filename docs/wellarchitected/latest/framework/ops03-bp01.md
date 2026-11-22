

# OPS03-BP01 Adopt a configuration, build, and release pipeline

 Manual builds and hand-applied configuration changes drift over time and create non-reproducible environments. A pipeline that combines version control, configuration management, and automated release removes that drift by making every change tracked, tested, and repeatable. When the pipeline is shared infrastructure owned centrally, workload teams inherit it and ship changes safely without rebuilding the same tooling. 

 **Desired outcome:** 
+  Your code, infrastructure definitions, and configuration all live in version control, and every change traces to an author and a review. 
+  Your pipeline builds, tests, and deploys changes automatically, with consistent results across development, test, and production. 
+  You can roll back a deployment to a known good state without manual reconstruction. 
+  Your pipeline is governed centrally, so teams inherit compliance controls and audit trails rather than building them individually. 

 **Common anti-patterns:** 
+  Teams store code only on local workstations, so work is lost when a machine fails and no one can trace where the change came from. 
+  Operators apply configuration changes manually across servers, which produces environments that drift into inconsistent states. 
+  Teams deploy without automated testing or validation, and defects reach production undetected. 
+  Manual build steps omit dependencies or assets, so deployments fail or behave differently between environments. 
+  No rollback path exists, so recovering from a bad change requires manual, error-prone work under pressure. 

 **Benefits of establishing this best practice:** 
+  Version control makes every change traceable and reversible. 
+  Automation removes the manual steps that introduce errors and slow delivery. 
+  Consistent build and deployment across environments reduce failures that appear in one place but not another. 
+  Central governance gives every team an audit trail and compliance controls by default. 
+  Teams deploy more often with less effort, which shortens lead time for change. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A delivery pipeline is the path a change travels from a developer's commit to a running production system. Each stage (source control, build, test, and deploy) adds a guarantee about the change before it moves forward. 

 Figure 1 shows how these stages connect into a single tooling chain. <a name="ops03-bp01-fig1"></a>

![Pipeline diagram showing a change moving through source control, build, test, and deploy stages on its path from developer commit to production.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/deployment-pipeline-tooling.png)

*Delivery pipeline stages from source to production*


 Most organizations face a choice between letting each team build its own pipeline and providing a central, governed one that teams extend. Central ownership concentrates security scanning, approval gates, and audit logging, so every team inherits them. The trade-off is flexibility: a workload with unusual build or compliance needs can find a shared pipeline too rigid. We recommend a central foundation that teams customize at the edges. 

 Drift happens when running systems diverge from their defined state because someone made a change outside the pipeline. Configuration management addresses drift by treating configuration as versioned, validated data. When configuration lives in version control alongside code, the same review and rollback mechanisms that protect code also protect configuration. 

 Deployment strategy determines how much risk each release carries. Deploying to every instance at once is straightforward but exposes all users to a bad change. Progressive strategies such as blue/green and canary limit that exposure by shifting traffic gradually, at the cost of more infrastructure and orchestration. Automated rollback matters more than the strategy you pick. 

 Treat the deployment pipeline as a product with measurable service levels. Track deployable time per day, how often the pipeline needs manual intervention to get unblocked, and how long a change takes to reach production. When a pipeline falls short of these levels, prefer automated detection and remediation over a ticket-driven process. 

 [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) orchestrates the flow across stages, [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) compiles and tests artifacts, and [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) manages deployment strategies and rollback. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) records resource configuration and flags drift, and [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) manages application configuration as a versioned, validated artifact. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt or extend a central pipeline:** Start from your organization's shared pipeline and customize it for your workload rather than building one from scratch. This keeps governance and audit controls consistent while you add workload-specific build and test stages. Review the [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/) suite to identify the components you need. 

1.  **Place code and configuration under version control:** Store application code, infrastructure definitions, and configuration in version-controlled repositories, and define a branching and merge strategy your teams agree on. Connect the repository to [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) so that each committed change starts the pipeline automatically. 

1.  **Manage configuration as versioned data:** Define configuration items and their owners, and validate them against compliance rules before they deploy. Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to record resource configuration and detect drift, and [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) to deploy application configuration with validation and controlled rollout. 

1.  **Automate builds and testing:** Configure [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) to compile artifacts, resolve dependencies, and run your test suite on every change. Fail the build when tests or quality gates do not pass, so defects stop before deployment. 

1.  **Automate deployment with a rollback path:** Use [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) to deploy with a progressive strategy such as blue/green or canary, and configure automated rollback triggered by deployment or health-check failures. Match the strategy to the risk tolerance of the workload. 

1.  **Monitor the pipeline against its service levels:** Instrument each stage so that failures, durations, and deployment outcomes are visible on a shared dashboard, and publish custom [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics for pipeline health, such as deployable time per day, manual-intervention count, and time-to-production. Raise an alarm when a pipeline falls outside its target, and use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runbooks to auto-remediate common blockers rather than routing them to a manual ticket queue. Escalate to the owning team only the failures that need a human. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) 
+  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md) 
+  [OPS03-BP05 Design for efficient patch management](ops03-bp05.md) 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 

 **Related documents:** 
+  [What is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) 
+  [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) 
+  [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) 
+  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - How Lockheed Martin builds software faster, powered by DevSecOps](https://www.youtube.com/watch?v=Q1OSyxYkl5w) 

 **Related services:** 
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/) 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 
+  [AWS CodeBuild](https://aws.amazon.com/codebuild/) 
+  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) 
+  [AWS Config](https://aws.amazon.com/config/) 