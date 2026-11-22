

# REL13-BP04 Manage configuration drift at the DR site or Region

 Over time, the primary and recovery sites diverge as changes land on the primary but not the recovery site. This drift is only exposed when a failover occurs. Keep infrastructure, configuration, and data in parity so recovery is complete and predictable. 

 **Desired outcome:** 
+  Your recovery site's infrastructure, configuration, and data stay in parity with the primary site. 
+  Changes reach the recovery site through the same automated pipelines that change the primary. 
+  Drift and replication problems are detected and alerted on before an incident, not during one. 
+  You verify service and capacity availability at the recovery site as part of ongoing operations. 

 **Common anti-patterns:** 
+  Teams change the primary site but do not update the recovery site, leaving stale configurations. 
+  Teams overlook service or capacity differences between sites, which cause failures during failover. 
+  Manual, ad hoc updates keep the recovery site in sync, which invites human error and inconsistency. 
+  No drift detection runs, so the recovery site appears ready when it is not. 

 **Benefits of establishing this best practice:** 
+  Recovery succeeds more often because the recovery site mirrors the primary. 
+  Failover surprises drop because differences are caught and corrected in advance. 
+  Recovery is faster because there is no scramble to reconcile configuration during an incident. 
+  Confidence in the recovery site rests on evidence from continuous checks, not assumption. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 *Configuration drift* is the gap that opens between two environments that were once identical. It accumulates from small, individually reasonable changes, such as a patched instance, a tweaked parameter, or a new security rule, applied to the primary and never propagated. Each change is minor, but the cumulative divergence is what fails a recovery. Because drift occurs without notifications or alarms, the recovery site might look ready on a dashboard but be unable to run the workload. 

 To keep sites in parity, make the recovery site a target of the same delivery pipeline that changes the primary. Deploying to both sites at once guarantees parity, but it also carries a bad change to the recovery site at the same moment it breaks production. *Staggered deployment* resolves this. Roll changes to the primary first, observe for a defined period, then promote them to the recovery site. Defects appear in the primary, where you can fix them before they reach the recovery site. 

 Parity in deployment is not enough, because drift also comes from out-of-band changes and manual incident fixes. Continuous configuration monitoring detects when actual state diverges from declared state, and alerts notify you of the divergence. Automated remediation then restores declared state without waiting for a human. 

 Beyond configuration files, a recovery Region might not offer every service or feature the primary uses. Provisioned capacity, service quotas, and throttle limits are set per Region and do not replicate automatically. A failover that relies on matching quotas might stall when the recovery Region throttles a surge of new resource requests. Verify service availability and capacity headroom in the recovery site, because these mismatches do not show up in application configuration drift checks. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Confirm service and feature parity at the recovery site:** Verify that the recovery Region provides every AWS service and feature your disaster recovery plan depends on. Identify gaps early and adjust the plan or the architecture where a service is unavailable. 

1.  **Manage infrastructure and configuration as code:** Define production infrastructure and application configuration as templates, and apply them to the recovery site regularly. Use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) drift detection to compare deployed resources against your templates and surface differences. 

1.  **Deploy to all sites through CI/CD pipelines:** Configure pipelines to deploy application and infrastructure changes to both primary and recovery sites. A service such as [AWS CodePipeline](https://aws.amazon.com/codepipeline/) automates delivery so both sites receive the same changes and manual steps do not introduce drift. 

1.  **Stagger deployments between sites:** Deploy and observe changes in the primary site first, then promote them to the recovery site after an evaluation period. This isolates defects in the primary before they can reach the recovery site and preserves its integrity as a fallback. 

1.  **Monitor configuration continuously and alert on drift:** Continuously evaluate resource configurations in both sites, using a service such as [AWS Config](https://aws.amazon.com/config/) to evaluate configuration against your compliance rules and detect drift. Add alerting for configuration drift and for any data replication lag or interruption so problems surface before an incident. Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) to perform intelligent analysis of detected drift. It explains *why* a specific configuration divergence matters to your resilience posture, prioritizes drift by recovery impact, and recommends targeted remediation rather than treating all drift equally. 

1.  **Automate remediation and audit alignment:** Correct detected drift automatically so the recovery site returns to its declared state without manual intervention. Schedule regular audits and compliance checks to confirm ongoing alignment, including provisioned capacity, service quotas, throttle limits, and version consistency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md) 
+  [REL01-BP01 Aware of service quotas and constraints](rel01-bp01.md) 
+  [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 

 **Related documents:** 
+  [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) 
+  [Detect drift on an entire CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html) 
+  [Remediating Noncompliant Resources with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 

 **Related examples:** 
+  [Introducing AWS Capabilities by Region for easier Regional planning and faster global deployments](https://aws.amazon.com/blogs/aws/introducing-aws-capabilities-by-region-for-easier-regional-planning-and-faster-global-deployments/) 
+  [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) 
+  [Remediating Noncompliant Resources with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) 
+  [Automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) 
+  [Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/) 
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery) 