

# ADVOPS07-BP02 Conduct game days and failure injection exercises

 Regular game days with realistic failure scenarios (SSP adapter outages, manifest generation failures, FAST channel playout interruptions, and innovative ad format rendering degradation) expose monitoring and runbook gaps before they cost revenue. 

 **Desired outcome:** 
+  Publisher teams regularly practice responding to realistic failure scenarios, identifying gaps in runbooks, monitoring, and escalation procedures before real incidents occur. 
+  Each game day produces concrete improvement actions that are tracked and completed before the next exercise. 
+  MTTR for exercised failure scenarios decreases measurably over successive game days, validating that exercises drive operational improvement. 

 **Common anti-patterns:** 
+  Only practicing incident response during real production incidents, developing response patterns under the most stressful conditions rather than in controlled environments. 
+  Conducting game days without structured retrospectives that produce actionable improvements. 
+  Limiting failure simulation to infrastructure-only scenarios without testing ad-tech-specific failure modes (adapter timeout cascades, manifest generation failures, and fill rate collapses). 

 **Benefits of establishing this best practice:** 
+  Proactive identification of monitoring and runbook gaps before real incidents occur. 
+  Improved team confidence and response speed during actual outages. 
+  Validated operational procedures that reduce MTTR for publisher workload failures. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The operational excellence pillar recommends allocating time and resources for ongoing improvements, including simulating production workloads through game days. Regular practice in controlled environments builds faster, more effective response patterns. Game days expose monitoring blind spots and runbook gaps that only appear in failure conditions. Prioritize failure modes that don't occur often enough to build response experience through production alone. Some examples of publisher-specific game day scenarios are: 
+  **SSP adapter outage:** Disable one or more Prebid adapters and verify that the circuit breaker activates within the configured threshold, the remaining auction continues without the failed adapter, and the monitoring dashboard shows the expected fill rate and eCPM changes. Measure time from adapter failure to circuit breaker activation to runbook invocation. 
+  **Manifest generation failure:** Inject a SCTE-35 validation error and verify that the validation alarm fires within the expected period, the automated manifest regeneration runbook activates, CDN cache purge completes, and ad break completion rate recovers. Measure total recovery time. 
+  **FAST channel playout interruption:** Simulate a MediaLive input failure and verify that automatic input failover activates within the configured input-loss threshold, the monitoring alarm fires, and the on-call engineer receives notification. Measure time from input loss to full output restoration. 

 With AWS Fault Injection Service (FIS), you can inject controlled failures for these scenarios: blocking network connectivity to Prebid adapter endpoints, simulating Lambda timeouts for the ADS, or injecting S3 errors for content origins. Use FIS scope-of-impact controls to prevent game day exercises from affecting production traffic. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a quarterly game day calendar with scenarios for each publisher workload theme:** Create a rolling 4-quarter game day schedule that covers Prebid adapter failures, SGAI manifest failures, FAST channel playout interruptions, and innovative ad format rendering degradation. Rotate through different failure modes each quarter so that all major failure categories are exercised annually. Assign game day facilitators and participating teams for each session. 

1.  **Design failure injection scenarios using AWS Fault Injection Service with scope-of-impact controls:** Create FIS experiment templates for each game day scenario. Configure scope-of-impact controls that limit impact to staging or a small fraction of production traffic. Define the success criteria for each experiment: what measurements confirm the exercise scenario is active, what confirms that the expected automated response occurred, and what confirms that the workload recovered within the target time. 

1.  **Execute game days with on-call teams responding as they would to real incidents:** Run game days during normal business hours with the on-call team responding using only standard operational procedures: the same runbooks, monitoring dashboards, and escalation paths they would use in a real incident. Facilitate but don't assist. The value comes from the team exercising their actual capabilities rather than from a facilitator prompting the correct steps. 

1.  **Conduct structured retrospectives and track improvement actions:** Immediately after each game day, run a structured retrospective. Ask: were all alarms correct and timely, were runbook steps accurate and complete, were escalation paths effective, what took longer than expected and why. Produce a list of improvement actions with owners and due dates. Track completion rates between game days. Improvement actions that are never completed indicate process failures that need escalation. 

1.  **Measure MTTR trends across successive game days for the same scenarios:** After three or more game days exercising the same scenario, calculate the MTTR trend. If MTTR is decreasing, the game days and improvement actions are working. If MTTR is flat or increasing, investigate whether runbook improvements are actually being implemented, whether teams are practicing without facilitator assistance, or whether the scenario is becoming too familiar to simulate realistic surprise. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS04-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload](advops04-bp01.md) 

 **Related documents:** 
+  [AWS Fault Injection Service documentation](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) 
+  [AWS Well-Architected OE pillar OPS11-BP09 guidance on allocating time for improvements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/evolve.html) 

 **Related services:** 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 