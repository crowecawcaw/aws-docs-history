

# OPS03-BP04 Fully automate integration and deployment

 Manual steps in integration and deployment are where errors and delay accumulate. A developer who logs into a console to promote a change, or waits for a scheduled release window, adds risk and lead time. Full automation of the path from code commit through build, test, deployment, and validation removes those steps, so changes flow to production consistently. 

 **Desired outcome:** 
+  Your developers promote changes to production through tooling, without logging into a console to deploy. 
+  Your pipeline runs build, test, deployment, and validation automatically on every change. 
+  You have a full audit trail of every change and configuration, meeting governance and compliance needs. 
+  Your integration and deployment process is standardized and repeatable across teams. 

 **Common anti-patterns:** 
+  A developer finishes a feature on Friday and waits until the next scheduled release window on Monday to check it in, delaying feedback for days. 
+  A developer fixes a critical production issue, then emails change management for manual approval before the fix can deploy. 
+  A developer logs into the console to create a development environment manually, using non-standard methods that no one else can reproduce. 
+  Teams tag resources inconsistently, so automated operations cannot reliably target the right resources. 
+  A team gates every pipeline stage with a fixed-duration bake timer, regardless of whether the deployment has actually been exposed to representative production traffic. 
+  Engineers manually dig through multiple dashboards and logs to diagnose why a pipeline blocked, instead of using integrated automated diagnosis. 

 **Benefits of establishing this best practice:** 
+  Automation removes the manual steps that introduce errors and slow delivery. 
+  Developers focus on delivering business value instead of operating releases. 
+  Changes reach production faster, which increases the frequency and speed of delivery. 
+  A consistent, audited process satisfies governance and compliance requirements. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Continuous integration merges and tests every commit against the shared codebase. Continuous delivery extends that: it keeps every tested change deployable and automates the release to production. Many organizations automate integration but stop short of automating deployment, which leaves a manual gate that reintroduces delay and inconsistency. 

 Manual gates slow delivery, and a rushed human approval catches little that automated tests do not. Invest in the tests, health checks, and automated rollback that let the pipeline decide whether to promote. If you're new to this, keep an approval step for production while you build confidence, and remove it as your test coverage matures. 

 Environments created manually drift apart. Each is slightly different, none is reproducible, and defects in them cannot be traced. Define environments as code and create them through the pipeline. Every environment is then identical and disposable, so a failure in one environment reproduces in every other. 

 Automated operations need a consistent tagging strategy to find the resources they act on. Tags attach metadata for organization, cost accounting, access control, and automation targeting. Otherwise, automation cannot tell which resources belong to which workload or environment, so it either acts too broadly or fails outright. Agree on the tagging strategy before you scale automation. Use [Resource tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) and [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html) with a documented [tagging strategy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/building-your-tagging-strategy.html). 

 On AWS, [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) builds and tests artifacts, and [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) automates deployment across compute types with built-in rollback. 

 When your pipeline holds a deployment at a stage for a bake period, define the period by an observed signal rather than a fixed clock duration. A fixed timer can promote a deployment before it has seen representative load, or hold back a healthy one for no reason. Promote once a traffic or request-volume metric sustains a defined share of its historical peak across consecutive observations, and keep automated rollback on health-check failure active alongside it. Revisit the threshold as traffic patterns shift. See [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) for bake time in staged rollouts. 

 Full automation should also cover triage of blocked pipelines. Treat repeated manual investigation across logs and dashboards as an automation gap. Use tooling that correlates failures across build, test, and deployment stages and proposes a fix. Route proposed fixes through your normal code review and build verification gates so automation does not bypass them. See [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) for agentic investigation. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Automate the full path from commit to production:** Configure the pipeline to trigger on every commit and run build, test, deployment, and validation with no manual steps. Remove scheduled release windows so changes flow as soon as they pass their gates. 

1.  **Define environments as code:** Create development, test, and production environments through the pipeline from version-controlled definitions, so every environment is identical and reproducible. Stop creating environments manually in the console. 

1.  **Build and test automatically:** Use [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) to compile artifacts and run tests on each change, and fail the pipeline when a gate does not pass. 

1.  **Deploy automatically with rollback:** Use [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) to promote validated artifacts through to production, with automated rollback on deployment or health-check failure. Replace manual approvals with automated checks as your test coverage matures. 

1.  **Apply a consistent tagging strategy:** Tag resources with [resource tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) and [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html) so automated operations can target the right resources. Follow a documented [tagging strategy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/building-your-tagging-strategy.html) for organization, cost accounting, and access control. 

1.  **Use signal-based bake time, not fixed timers:** Replace fixed-duration bake timers with a signal-based gate that monitors a traffic or request-volume metric against a historical peak baseline, and configure the pipeline to promote once the deployment sustains a defined percentage of that baseline across multiple consecutive data points. 

1.  **Automate pipeline failure diagnosis and remediation:** Integrate automated diagnostic tooling into your pipeline that detects failures, correlates root cause across build, test, and deployment stages, and proposes a fix through your standard code review process rather than requiring manual cross-dashboard investigation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS03-BP01 Adopt a configuration, build, and release pipeline](ops03-bp01.md) 
+  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 

 **Related documents:** 
+  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) 
+  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) 
+  [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) 
+  [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html) 
+  [Tagging Best Practices Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 

 **Related workshops:** 
+  [Tagging Workshop](https://catalog.workshops.aws/tagging/en-US) 

 **Related services:** 
+  [AWS CodeBuild](https://aws.amazon.com/codebuild/) 
+  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) 