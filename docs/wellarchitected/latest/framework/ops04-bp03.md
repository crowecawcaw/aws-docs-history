

# OPS04-BP03 Develop and test rollout for consuming external dependencies

 Workloads often depend on external software, from security agents to third-party libraries. Updates to these dependencies can be as disruptive as your own changes, yet they often arrive on the vendor's schedule and bypass your normal controls. Treat external updates as changes you own. Test them, roll them out gradually, and maintain the ability to rollback, so you stay current on security fixes without accepting an unvalidated change straight into production. 

 **Desired outcome:** 
+  You classify external dependencies by the impact their failure would have on production. 
+  Your critical dependency updates pass through testing and controlled rollout before they reach all production systems. 
+  You have documented recovery mechanisms for each critical dependency, including a way to reverse or contain a failed update. 
+  You pin third-party library versions explicitly in your code and build configuration, and you manage updates to them as tracked work in your backlog rather than accepting them implicitly. 
+  You have telemetry that attributes a production issue to a specific dependency update. 

 **Common anti-patterns:** 
+  Teams accept every vendor update automatically, with no validation or staged rollout. 
+  Security software updates are exempted from change management, so they reach production untested. 
+  Updates deploy to all production systems at once, so a faulty update causes a disruption. 
+  Teams have no lower environment in which to test a vendor update before production. 
+  No rollback or recovery procedure exists for a failed external update. 

 **Benefits of establishing this best practice:** 
+  A faulty update affects a limited set of systems instead of the whole fleet, because rollout is staged. 
+  Recovery is faster because each critical dependency has a tested rollback or containment path. 
+  Teams keep pace with security updates without trading away operational stability. 
+  Change data gives clear visibility into which dependency update caused an issue. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A security agent or a critical library often needs to update quickly to close a vulnerability. That same software usually runs with high privilege and deep system access, so a bad update can take down every host it touches. However, in this case, the vendor tested against their environment, not yours. 

 Classify dependencies by scope of impact so you can match controls to impact. A dependency with a failure mode that would halt production earns full change controls, such as testing in a lower environment, staged rollout, and a documented recovery path. A low-impact library needs far less. Repeatable, low-risk updates that follow a policy-enforcing workflow can be standardized, templated, and preauthorized, so they do not require a fresh approval each time. 

 Use the same rollout techniques that protect your own deployments. Push an update to a fraction of systems first, watch for problems, and expand only when the update proves stable. Keep each change small to reduce both the chance of failure and the time to recover. 

 Plan recovery explicitly, because you often cannot modify third-party software the way you can your own code. Decide in advance when a failed update should be rolled back and when a fix-forward is the only option. Document the conditions that force a rollback, such as discovering that an unauthorized change was deployed. Make the rollback plan accessible to everyone involved before the update is released. When a failure cannot be reversed, fast diagnosis depends on change data that shows exactly what changed and when. 

 Track the duration of incidents caused by failed updates and feed that back into your recovery plans. Make change data visible across workload owners so diagnosis is not gated on a single team. [Change Management in the Cloud](https://docs.aws.amazon.com/wellarchitected/latest/change-enablement-in-the-cloud/change-enablement-in-the-cloud.html) describes these controls in depth. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess and classify external dependencies:** Identify the dependencies that could affect production, and set controls and procedures by risk level. Document each dependency's update frequency and consumption options. Standardize, template, and preauthorize repeatable updates that follow a policy-enforcing workflow, and keep each change small so recovery takes less time. 

1.  **Document change-reversal policies:** Require teams to have effective plans to reverse changes within a set period. State when a fix-forward is allowed, require a documented rollback plan that all involved teams can access, and specify the conditions that force a rollback, such as the discovery of an unauthorized change. 

1.  **Establish testing and validation procedures:** Create test environments that mirror production configurations, develop automated tests for updates, and define the acceptance criteria that an update must meet before it is promoted to production. 

1.  **Design controlled rollout procedures:** Deploy in stages, use canary or other fractional rollout strategies, and monitor each phase, so you can decide to stop or reverse a rollout early. 

1.  **Establish recovery mechanisms:** Document a rollback procedure for each critical dependency, maintain backups and recovery points, test the recovery procedures regularly, and confirm that a rollback returns code to the known good state. 

1.  **Create monitoring and visibility:** Add telemetry that detects update-related issues, build dashboards for dependency health, and configure alerts for anomalous behavior. Make change data visible to other workload owners, and measure incident duration during failed updates to drive iterative improvement. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 
+  [OPS03-BP05 Design for efficient patch management](ops03-bp05.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md) 

 **Related documents:** 
+  [Ensuring rollback safety during deployments](https://builder.aws.com/content/3F04j2yRAAMBuPSPs50xwXZqg01/ensuring-rollback-safety-during-deployments) 
+  [Amazon's approach to high-availability deployment](https://builder.aws.com/learn/topics/builders-library) 
+  [Introducing the AWS Integrated Application Test Kit (IATK)](https://aws.amazon.com/blogs/compute/aws-integrated-application-test-kit/) 

 **Related examples:** 
+  [How do I recover AWS resources that were affected by the CrowdStrike Falcon agent?](https://repost.aws/knowledge-center/ec2-instance-crowdstrike-agent) 