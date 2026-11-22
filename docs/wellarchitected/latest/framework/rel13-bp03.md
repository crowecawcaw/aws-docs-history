

# REL13-BP03 Test disaster recovery implementation to validate the implementation

 Assumptions about capacity, permissions, and timing go stale as a system evolves. Test failover regularly, under production conditions, to confirm that recovery works and that the team can perform it within the objectives you set. 

 **Desired outcome:** 
+  You exercise failover to the recovery site on a regular schedule, including in production. 
+  Each test confirms that the workload recovers within its RTO and to a state within its RPO. 
+  Your team follows and improves runbooks during tests, so recovery is a practiced routine. 
+  You keep the number of distinct recovery paths small so each one is tested often. 

 **Common anti-patterns:** 
+  Teams never exercise failover in production and rely on untested assumptions. 
+  Recovery paths multiply until none of them is tested frequently enough to be trusted. 
+  A secondary data store is assumed to handle full production load but is never tested under it. 
+  Test results are not fed back into runbooks, so the same problems recur during the next event. 

 **Benefits of establishing this best practice:** 
+  Recovery works when it is needed because it has been proven under realistic conditions. 
+  The team executes recovery confidently because they have practiced the procedure. 
+  Capacity and configuration gaps surface during a controlled test rather than during an incident. 
+  Recovery time improves as repeated tests refine the procedure and the automation behind it. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Recovery paths that are tested often are the only ones that work in practice. A secondary data store sized correctly at the last test may no longer absorb production load after months of growth. You may not notice until the primary fails and the secondary cannot handle the load. 

 Fewer recovery paths are easier to trust. Establish a small set of recovery patterns and exercise them on a schedule. Test a complex or critical path in production, because a lower environment does not reproduce the scale, traffic, and dependency behavior that break recovery. 

 *Recovery-oriented computing* names the system characteristics that make recovery dependable: 
+  Isolation and redundancy 
+  System-wide rollback 
+  Health monitoring and diagnostics 
+  Automated recovery 
+  Modular design 
+  Component restart 

 Testing verifies that the design holds, and runbooks capture what to fix before the next test. 

 Drills that launch recovery instances in isolation let you rehearse the mechanics and measure timing without redirecting live traffic or risking the production workload. Run drills frequently to keep the team practiced and the recovery environment current, so a real failover repeats a familiar procedure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Engineer workloads for recovery:** Apply recovery-oriented computing traits such as isolation, redundancy, health monitoring, diagnostics, automated recovery, modular design, and restartability, so each recovery path can be exercised reliably. Keep the number of distinct recovery paths small so each one can be tested often. 

1.  **Schedule and run recovery tests:** Exercise each recovery path on a regular cadence, and test complex or critical paths in production. Confirm that recovery completes within the target RTO and reaches a state within the target RPO. Use runbooks during each test to document problems and resolve them before the next test. 

1.  **Use drills to rehearse without disruption:** For Amazon EC2-based workloads, use [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) to launch drill instances that rehearse failover without redirecting production traffic. Run drills frequently to validate readiness and timing. Introduce realistic failures with [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to test how the recovery path behaves under fault conditions, including AZ availability interruption scenarios that simulate an entire zone becoming unavailable and network connectivity disruptions that block traffic between AZs or VPCs, validating that your DR implementation handles these failure modes end to end. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 
+  [REL13-BP05 Automate recovery](rel13-bp05.md) 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 
+  [REL12-BP05 Conduct game days regularly](rel12-bp05.md) 

 **Related documents:** 
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/) 
+  [Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/) 
+  [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) 
+  [APN Partner: partners that can help with disaster recovery](https://partners.amazonaws.com/search/partners?keyword=Disaster+Recovery) 
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Disaster Recovery (DR) with AWS Elastic Disaster Recovery Service (COP356)](https://www.youtube.com/watch?v=IfVpaSe4H4k) 