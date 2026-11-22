

# OPS04-BP02 Automate testing and rollback

 Automated tests verify changes during deployment, and automated rollback reverses a change when predefined conditions signal failure. Together they shorten recovery time by removing manual delay. 

 **Desired outcome:** 
+  Your automated tests run inside the delivery pipeline and gate promotion between environments. 
+  Your monitoring evaluates defined success criteria during and after deployment, and triggers rollback automatically when they are not met, with agentic tools accelerating detection and response. 
+  Your rollback returns the workload to a known good state without manual intervention, drawing on maintained repositories of known good builds. 
+  You exercise rollback regularly, so an untested rollback is treated as a risk rather than a guarantee. 
+  You use feature flags to release features progressively, which lets you disable a feature without a redeployment. 

 **Common anti-patterns:** 
+  Teams rely on manual post-deployment steps, so detecting a failure and reversing it takes hours and prolongs customer impact. 
+  A single pipeline delivers application, infrastructure, and configuration changes together, so one component's failure forces a rollback of everything. 
+  Teams invest automation effort in rarely used features, which lowers the return on the testing they build. 
+  Deployments run without monitoring workload health, so teams cannot tell whether a rollback is needed or has already happened. 
+  Rollback procedures exist on paper but are never exercised, so they fail when they are finally needed. 

 **Benefits of establishing this best practice:** 
+  Failures surface during deployment instead of after customers report them, because tests run automatically at each stage. 
+  Recovery time drops because rollback starts on a signal rather than after a person investigates. 
+  Test coverage grows and stays consistent, because automation runs the same cases on every change. 
+  Teams deploy with more confidence, because a proven rollback caps the impact of any single change. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A rollback is only useful if it is deterministic — the workload returns to a specific, known good state every time. That property lets you automate rollbacks safely: monitoring detects when success criteria are not met, and the pipeline reverses the change. Recovery time then depends on detection speed. 

 Not every failure calls for rollback. Rolling forward with a fix can be safer, especially when a change has altered persistent state that rollback cannot cleanly reverse. Define which path to take and the conditions that trigger each. Whichever you choose, exercise it. A rollback that has not run recently is unproven — treat it as a risk and flag it to stakeholders until you have practiced it. Run roll-forward, rollback, and roll-forward again to verify every path recovers. 

 Automated testing has a cost, and not all tests are worth that cost. Prioritize cases by the risk they reduce and how often they run. Automation quickly becomes worthwhile for changes that touch high-risk paths, cases repeated on every deployment, and scenarios that span multiple configurations. Develop tests in the same sprint as the code they cover, as deferred testing can accumulate defects and delay releases. 

 Use agentic tools that gather telemetry and recommend actions to shorten recovery time. 

 Bundling unrelated changes into one pipeline couples their failure modes. When application code, infrastructure, patches, and configuration all ship through a single stage, one fault forces a rollback of everything. Separate changes by type and scope of impact so you can roll back only the component that failed. 

 Without health signals tied to your success criteria, automated rollback has no trigger. You also cannot tell whether a service restarted or a rollback already fired. Production testing techniques give you graduated exposure while you watch those signals: canary releases route a small share of traffic to the new version, A/B testing compares two versions across user groups, feature flags toggle features without a redeploy, and regression tests confirm that existing behavior still holds. Each test produces evidence for your rollback criteria to evaluate. For the constraints that keep automated reversal safe, see [Ensuring rollback safety during deployments](https://builder.aws.com/content/3F04j2yRAAMBuPSPs50xwXZqg01/ensuring-rollback-safety-during-deployments). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt a standard testing methodology:** Use your organization's testing methodology to define each stage, from requirements planning through test case development, tool configuration, automated runs, and closure. Derive a workload-specific approach from it, and apply continuous testing across the development lifecycle where it fits. 

1.  **Decide what to automate and set rollback criteria:** Split test cases by the business value and risk of the feature under test, and assign accountability for the cases you keep manual. Define the success criteria a change must meet and the specific failure conditions that trigger automated rollback. 

1.  **Design test cases for reuse:** Write automated test cases so they carry over to future repeatable changes, which lowers the cost of testing each new release. Prioritize cases that run on every deployment and cover high-risk paths. 

1.  **Select integrated testing and rollback tooling:** Choose automated testing and rollback tools that match your business requirements and existing pipeline investments, so they integrate rather than add a parallel workflow. 

1.  **Integrate testing and rollback into the pipeline:** Connect your tests and rollback tools to the CI/CD pipeline, and configure monitoring to evaluate your success criteria during and after each deployment. Reverse the change automatically when rollback conditions are met. 

1.  **Decouple CI from CD in pipelines:** Use image repositories to separate the build, inspection, and testing stages from the deployment stages. This lets you roll a deployment back while changes still in development are fixed forward until they are production-ready, and it lets development continue even when a change freeze blocks deployment to production. 

1.  **Apply progressive production testing techniques:** Run A/B, canary, and regression tests against real traffic before full exposure, and gate exposure with feature flags so you can enable a change gradually and disable it without a redeployment. Feed the results into your rollback criteria. 

1.  **Automate investigation with agentic tools:** Use agentic tools such as [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) to investigate incidents autonomously, correlate telemetry and deployment data for root-cause analysis, and deliver targeted mitigation and recovery recommendations.. 

1.  **Report on and exercise recovery paths:** Build reports that show change success by workload and support a fast rollback decision. Confirm recovery regularly by running roll-forward, rollback, and roll-forward again, and use the reports to find parts of the workflow to optimize. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 
+  [OPS04-BP03 Develop and test rollout for consuming external dependencies](ops04-bp03.md) 
+  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 

 **Related documents:** 
+  [Redeploy and roll back a deployment with AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html) 
+  [Feature Flag Orchestration with AWS DevOps Agent and LaunchDarkly](https://aws.amazon.com/blogs/devops/feature-flag-orchestration-with-aws-devops-agent-and-launchdarkly/) 
+  [Supercharge your cloud operations with the Kiro power for AWS DevOps Agent](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/) 
+  [Implementing feature flags in container environments with AWS AppConfig](https://aws.amazon.com/blogs/containers/implementing-feature-flags-in-container-environments-with-aws-appconfig/) 
+  [Introduction to DevOps on AWS - Deployment strategies](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Move beyond reactive: Transform cloud ops with AWS DevOps Agent (COP362)](https://www.youtube.com/watch?v=JajBEYle67I) 
+  [AWS re:Invent 2025 - Continuous integration and continuous delivery (CI/CD) for AWS (DVT202)](https://www.youtube.com/watch?v=rm9gPOlUxNY) 
+  [AWS re:Invent 2025 - Advanced feature flags: Faster releases and rapid recovery (DEV320)](https://www.youtube.com/watch?v=5yPNR5PwAfE) 

 **Related services:** 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 
+  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) 
+  [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo) 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 