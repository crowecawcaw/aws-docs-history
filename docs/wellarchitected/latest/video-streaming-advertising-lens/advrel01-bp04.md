

# ADVREL01-BP04 Implement chaos engineering practices

 Advertising systems have components sensitive to disconnects, latency, and bandwidth changes. Proactive fault injection finds these sensitivities before they affect live campaigns. 

 **Desired outcome:** 
+  You proactively inject controlled failures into your advertising workload to discover faults and fragility before they occur in production. 
+  Chaos experiments are informed by your failure modes and updated as your architecture evolves. 
+  Runbooks and playbooks are validated and updated based on chaos experiment outcomes. 

 **Common anti-patterns:** 
+  Only practicing failure response when real production incidents occur, which surfaces failure modes under the worst possible conditions. 
+  Running chaos experiments without a hypothesis and success criteria, so you get observations but no improvements you can act on. 
+  Limiting experiments to infrastructure failures without testing advertising-specific failure modes (partner DSP latency, user enrichment service unavailability, bid response validation errors). 

 **Benefits of establishing this best practice:** 
+  Faults are discovered in a controlled environment rather than during live campaigns. 
+  Runbooks are validated against real system behavior, not theoretical scenarios. 
+  Team confidence in the system's resilience is grounded in empirical evidence. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising systems have components that are sensitive to disconnects, latency, and bandwidth changes. Use AWS Fault Injection Service (FIS) or open-source tools like Chaos Monkey to inject failures that simulate network disruptions or resource unavailability. Based on the results, update your failure responses, monitoring, and alerts. Then adapt runbooks and playbooks before practicing failure response with relevant teams. 

 For RTB workloads, run these chaos experiments: 
+  Inject latency into user enrichment service calls to verify that the auction proceeds with cached or default data within the bid deadline. 
+  Simulate a DSP endpoint timeout to verify that circuit breakers activate and don't delay other DSP responses. 
+  Fail a database replica to verify that the auction tier automatically routes to the primary without exceeding the bid response SLO. 

 Chaos experiments that involve partner connectivity require partner coordination to avoid triggering false alarms on partner monitoring systems. 

 Use AWS Gamedays for larger-scale resilience exercises. AWS Well-Architected Framework Reviews and Support Countdown engagements improve advertising workload reliability. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create FIS experiment templates for advertising-specific failure modes:** Build FIS experiments targeting the most critical failure scenarios for your advertising platform: Availability Zone-level EC2 instance termination (verify Auto Scaling recovery), DynamoDB throttling injection (verify cache fallback behavior), network latency injection on partner connectivity links (verify circuit breaker activation), and Lambda function concurrency exhaustion (verify graceful degradation). 

1.  **Define hypothesis and success criteria for each experiment:** For each FIS experiment, document before execution: the steady-state definition (what does healthy operation look like), the hypothesis (if we inject this failure, the system should respond in this way), and the success criteria (specific CloudWatch metric thresholds that confirm the hypothesis). Run experiments only in staging initially, then graduate to production canary traffic after staging validation. 

1.  **Run quarterly chaos engineering sessions with defined scope and rollback procedures:** Schedule quarterly chaos days with the on-call team. Define the impact scope controls (maximum percentage of instances to affect, geographic scope, canary traffic percentage) and the rollback trigger (CloudWatch alarm that automatically stops the experiment if customer-facing metrics degrade beyond threshold). Document the rollback procedure before starting each experiment. 

1.  **Use experiment outcomes to update runbooks and alerting:** After each experiment, review: did alarms fire as expected, were runbook steps accurate and complete, what took longer than expected. Update CloudWatch alarm thresholds, add new monitoring points, and revise runbook steps based on observed system behavior. Track the list of improvements made after each chaos session as evidence of ongoing improvement. 

1.  **Validate partner failover with coordinated exercises:** Coordinate with your key SSP and DSP partners to conduct controlled failover tests. Verify that your system correctly handles partner degradation and that your traffic management modules (rate limiters, filters) behave as expected when partner endpoints are slow or unavailable. Document the coordination process and partner contacts for each exercise. 

1.  **Track resilience metrics over time:** Measure and report on MTTD (Mean Time to Detect), MTTR (Mean Time to Recover), and the number of SLO-violating incidents per month. Trend these metrics over time to demonstrate improving resilience posture. Use these trends to prioritize which failure modes to target in the next chaos engineering cycle. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP01 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes](advrel04-bp01.md) 

 **Related documents:** 
+  [Build Your Own Game Day to Support Operational Resilience](https://aws.amazon.com/blogs/architecture/build-your-own-game-day-to-support-operational-resilience/) 

 **Related services:** 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 