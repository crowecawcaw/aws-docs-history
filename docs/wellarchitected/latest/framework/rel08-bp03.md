

# REL08-BP03 Integrate resilience testing as part of your deployment

 Resilience testing introduces failures to measure how a system behaves under disruption and to expose unanticipated weaknesses. Running these tests as part of deployment builds evidence that the system can withstand and recover from real-world failures. 

 **Desired outcome:** 
+  Your deployments include resilience tests that inject failure and measure recovery, not just tests that confirm expected behavior. 
+  Your resilience experiments start in pre-production and progress toward controlled experiments in production during game days. 
+  You detect weak points before they cause customer-facing downtime, and you convert each finding into a documented mitigation. 
+  Your findings feed runbooks and monitoring, so the same failure is handled automatically the next time it occurs. 

 **Common anti-patterns:** 
+  Teams run deployments without the observability and monitoring needed to see how a failure propagates. 
+  Teams rely on people to detect and resolve system failures rather than building automated responses. 
+  Teams focus only on known issues and never experiment to find unknowns. 
+  Teams do not account for the failure of dependencies such as third-party APIs or shared services. 
+  Teams identify failures but never implement the resolution, and they leave findings undocumented. 

 **Benefits of establishing this best practice:** 
+  Hidden weaknesses surface in a controlled setting where you can address them safely. 
+  Recovery becomes faster and more repeatable as findings turn into runbooks and automated mitigations. 
+  Confidence in the system grows because resilience is measured, not assumed. 
+  Dependency failures are understood and contained before they cascade into customer impact. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Functional tests confirm that the system meets known requirements. Resilience tests search for unspecified failures, the conditions that emerge only when a component degrades or a dependency disappears. This makes resilience testing critical for exploring previously-unknown failure modes. 

 *Disaster recovery testing* confirms that you can restore a system after a major event and return to normal operations. It validates your recovery strategy against your recovery time objective (RTO) and recovery point objective (RPO). Recovery strategies range from backup and restore through pilot light, warm standby, and active-active. Define your RTO and RPO first, because those targets determine which strategy is worth testing. 

 *Fault injection* injects controlled disruptions, such as network interruptions or service failures, into a running system to expose vulnerabilities while the blast radius stays contained. You inject a known failure, observe how the system responds, and contain the impact so the experiment does not become an incident. 

 Observability is a prerequisite. Without monitoring that shows how a failure propagates, an experiment produces a broken system and no insight. Start experiments in non-production environments to build confidence, then graduate to production during game days, where real conditions reveal behavior that staging cannot reproduce. 

 A workload can be internally sound and still fail when an AMI, a third-party API, or a proxy server becomes unavailable or changes behavior. Evaluate how each dependency failure would affect availability, and build mechanisms to detect, isolate, and handle those failures. Redundancy, caching, and fallback strategies preserve service continuity when a dependency becomes unavailable. Document each finding and implement its mitigation as part of the test, not as a follow-up. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Update recovery procedures with each significant deployment:** Revise disaster recovery plans and standard operating procedures alongside major changes, so recovery guidance stays current with the deployed system. 

1.  **Integrate continuous resilience assessment into the pipeline:** Define your services in [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) using its auto-discovery and [dependency discovery](https://docs.aws.amazon.com/resilience-hub/latest/userguide/) capabilities. Auto-discovery identifies application components from tags, CloudFormation stacks, and Resource Groups, while dependency discovery uncovers endpoints and access patterns from Amazon Route 53 DNS resolver query logs. [Integrate it into your CI/CD pipeline](https://aws.amazon.com/blogs/architecture/continually-assessing-application-resilience-with-aws-resilience-hub-and-aws-codepipeline/) so resilience is assessed on every deployment. Use its generated code snippets to create recovery procedures as AWS Systems Manager documents and to configure recommended Amazon CloudWatch alarms. Review the [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) experiment recommendations that Resilience Hub produces from each assessment to identify targeted fault injection tests for the deployment. 

1.  **Run disaster recovery tests against defined objectives:** Define your RTO and RPO, then simulate the recovery strategy that meets them, such as backup and restore, pilot light, warm standby, or active-active. Confirm that you can restore the system and return to normal operations. Tools such as [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) support planning and testing. 

1.  **Run controlled fault injection experiments:** Inject disruptions such as network interruptions and service failures in non-production environments first, using [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to contain the blast radius. Build confidence there before running experiments in production during game days. Use FIS [scheduled experiments](https://docs.aws.amazon.com/fis/latest/userguide/) to run tests on a recurring cadence without requiring CI/CD pipeline integration for every execution. 

1.  **Test dependency failures:** Simulate the unavailability or modification of dependencies such as AMIs, third-party APIs, and proxy servers. Confirm that detection, isolation, redundancy, caching, and fallback mechanisms preserve service continuity. 

1.  **Review architectural changes for resilience regressions:** Use [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) to assess how proposed changes affect your application's resilience posture before deployment. It identifies new single points of failure, recovery gaps, and policy violations introduced by the change. For additional human-driven review, use [Kiro](https://kiro.dev/docs/) to perform agentic analysis that reasons about fault tolerance, recovery paths, and blast radius implications that automated assessments may not flag. 

1.  **Document findings and build runbooks:** Record each weakness and its mitigation, and convert repeatable responses into runbooks. Feed the results back into your CI/CD process so the same failure is caught or handled automatically next time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL08-BP02 Integrate functional testing as part of your deployment](rel08-bp02.md) 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 
+  [REL12-BP05 Conduct game days regularly](rel12-bp05.md) 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md) 

 **Related documents:** 
+  [[QA.NT.6] Experiment with failure using resilience testing to build recovery preparedness](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.6-experiment-with-failure-using-resilience-testing-to-build-recovery-preparedness.html) 
+  [Continually assessing application resilience with AWS Resilience Hub and AWS CodePipeline](https://aws.amazon.com/blogs/architecture/continually-assessing-application-resilience-with-aws-resilience-hub-and-aws-codepipeline/) 
+  [Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/) 
+  [Verify the resilience of your workloads using Chaos Engineering](https://aws.amazon.com/blogs/architecture/verify-the-resilience-of-your-workloads-using-chaos-engineering/) 
+  [PRINCIPLES OF CHAOS ENGINEERING - Principles of chaos engineering](https://principlesofchaos.org/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Chaos engineering: A proactive approach to system resilience (ARC326)](https://www.youtube.com/watch?v=MjPRd_UWCS0) 
+  [AWS re:Invent 2023 - Improve application resilience with AWS Fault Injection Service (ARC317)](https://www.youtube.com/watch?v=N0aZZVVZiUw) 
+  [Prepare & Protect Your Applications From Disruption With AWS Resilience Hub](https://www.youtube.com/watch?v=xa4BVl4N1Gw) 

 **Related workshops:** 
+  [Chaos Engineering :: Disaster Recovery on AWS](https://disaster-recovery.workshop.aws/en/intro/concepts/chaos-engineering.html) 