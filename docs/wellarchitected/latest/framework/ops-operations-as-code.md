

# Operations as code

 In the cloud you can apply the same engineering discipline to your operations that you already apply to application code. You can define a workload and everything around it (infrastructure, configuration, policies, and the procedures that operate it) as code, keep it in version control, review it, test it, and deploy it through automation. Treating operations as code is the foundation that most of the operational excellence practices build on, because it makes operational work consistent, repeatable, and reviewable rather than manual and improvised. 

## What you can define as code
<a name="ops-operations-as-code-what-you-can-define-as-code"></a>
+  **Infrastructure:** Provision and change infrastructure with [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the [AWS CDK](https://aws.amazon.com/cdk/) rather than manually, so environments are reproducible and every change is captured. 
+  **Configuration:** Manage application and system configuration through a configuration management system, so state is declared, versioned, and applied consistently. 
+  **Procedures:** Capture routine activities as runbooks and issue-resolution steps as playbooks, and automate them where the steps are well understood. A procedure defined in code runs the same way every time and can be tested. 
+  **Responses:** Trigger operations in response to events, such as scaling, remediation, or notification, so the system reacts consistently and faster than a person can. 

## Why it matters
<a name="ops-operations-as-code-why-it-matters"></a>

 Defining operations as code reduces manual effort and the errors that come with it, produces consistent results, and lets you version, review, and roll back operational changes the same way you handle application changes. It also makes safe experimentation practical: you can stand up a sandbox environment that matches production, rehearse a failure, and discard the environment afterward. The same templates give you development, test, and production environments with increasing levels of operational control. 

## Automating safely
<a name="ops-operations-as-code-automating-safely"></a>

 Automation is valuable because it applies an action consistently and at speed, which is also why an automated mistake propagates quickly. Build guardrails into automated operations: rate limiting, error thresholds that halt a runaway action, and approval steps for changes with a large blast radius. Reserve the strongest controls for high-impact actions, and let low-risk, well-understood tasks run unattended. For more on weighing automation against human oversight, see [Understanding trade-offs](ops-understanding-tradeoffs.md). 

## Supporting practices
<a name="ops-operations-as-code-supporting-practices"></a>

 A consistent [resource tagging strategy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) makes operations as code more effective. Tags let you identify resources for organization, cost accounting, and access control, and let you target automated activities at the right resources. Making frequent, small, reversible changes keeps the blast radius of any single change small and makes automated deployment and rollback practical. 

 Operations as code runs through the whole pillar: the telemetry you build to observe from multiple perspectives, the pipelines and quality gates you automate to manage the flow of change, the deployment safety you engineer to mitigate deployment risks, and the runbooks and automated responses you rely on to support and respond to your workloads in production. 