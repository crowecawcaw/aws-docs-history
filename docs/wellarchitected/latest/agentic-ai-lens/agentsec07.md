

# Human oversight protection and agent containment
<a name="agentsec07"></a>

 Human oversight is a key control in agentic systems, but it is only effective if reviewers can make informed decisions without being overwhelmed or misled. At the same time, you must detect and contain agents that deviate from their intended behavior before they can affect other parts of the system. This capability covers both sides: protecting the quality of human review, and implementing detection and containment mechanisms for agents that operate outside their defined boundaries. 


|  AGENTSEC07: How do you protect human oversight from manipulation and detect rogue agents?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-6"></a>
+  Review queues are prioritized and load-balanced, and reviewer workload is monitored for signs of rubber-stamping, so human reviewers make informed decisions rather than approving under pressure. 
+  Each decision presented for review carries calibrated context, including confidence scores, policy-check results, anomaly flags, and similar past decisions, so reviewers match their scrutiny to the actual risk of the action. 
+  High-risk agent actions receive independent review from multiple qualified reviewers, with blind review, consensus logic, and escalation for disagreement. 
+  Behavioral baselines exist for each agent, and deviations trigger rapid containment through credential revocation and circuit-breaker activation, with forensic state captured before isolation. 
+  Security assessments combine continuous automated scanning with scheduled red team and purple team exercises targeted at agent-specific manipulation scenarios, and findings flow back into guardrails, detection rules, and incident response runbooks. Red team exercises are adversarial simulations where a dedicated team attempts to compromise the agent system using the techniques a real attacker would use. Purple team exercises run the same scenarios collaboratively with the defenders so detection rules and runbooks are updated based on what was observed during the simulation. 

## Maturity levels
<a name="maturity-levels-6"></a>

 These levels summarize what each stage of maturity looks like for human oversight protection and agent containment as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Review pipelines are informal and routed to whoever is available, with no workload metrics or priority classification. Reviewers evaluate agent decisions without confidence scores, historical context, or independent verification. Agent behavior is observed only through infrastructure metrics, and containment depends on manual investigation after the fact. Security assessments are one-off or absent.  | 
|  2  |  Emerging  |  Review requests flow through a documented queue with coarse priority tiers, and single-reviewer approval applies to most agent decisions. Agent outputs include generic grounding checks, but reviewers don't see historical patterns or manipulation warnings. Generic security assessments cover agent deployments, and agent-specific red team scenarios are limited.  | 
|  3  |  Defined  |  A prioritized review pipeline backed by [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) tracks time-to-decision and approval-rate metrics, with alarms on rubber-stamping patterns. Reviewers see grounding scores from [Amazon Bedrock Guardrails contextual grounding](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html) checks, deviation flags against historical decisions, and plain-language warnings for flagged manipulation attempts. High-risk operations require independent review from more than one person using [AWS Step Functions parallel states](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html). Behavioral metrics are published as custom metrics with [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html), and findings from [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) and [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) are centralized in [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). Red team exercises run on a defined cadence using the OWASP Top 10 for Agentic Applications as the starting scenario library.  | 
|  4  |  Proactive  |  Review quality is managed through dashboards and composite alarms that automatically escalate or quarantine when review-behavior metrics degrade. Blind review and consensus logic are the default for high-risk operations, with disagreements routed to senior reviewers. Containment is automated through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) rules that capture forensic state to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), revoke credentials by attaching a deny-all policy to the agent's IAM role, and broadcast quarantine events for circuit breakers in dependent workflows. Purple team activities run after each assessment cycle and update [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) configurations, detection rules, and runbooks based on observed patterns.  | 
|  5  |  Optimized  |  Review quality metrics, agent behavioral baselines, and containment procedures are continuously tuned based on outcomes, and new attack techniques feed directly into detection and response tooling. Containment runbooks are regularly exercised through [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to validate that isolation, circuit breakers, and forensic capture behave as expected. Purple team findings, [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) evaluation trends, and runtime threat signals drive continuous refinement of guardrails, detection thresholds, and reviewer training.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-6"></a>
+  Review capacity is planned by volume alone, without metrics that detect rubber-stamping when queues back up, so human oversight degrades silently under load as reviewers approve faster than they can evaluate. 
+  Reviewers see agent recommendations without confidence scores, anomaly flags, or similar past decisions, and apply the same level of scrutiny to high-risk and low-risk actions because they have no basis for calibrating their attention. 
+  High-risk operations depend on a single approver, or multiple reviewers are allowed to see each other's decisions before submitting their own, turning the review process into either a single point of failure or an exercise in anchoring bias. 
+  Rogue-agent detection relies on infrastructure metrics rather than per-agent behavioral baselines, and quarantine requires a human to act, so an agent operating outside its intended scope keeps running for hours as responders mobilize. 
+  Security assessments are one-time, generic, or disconnected from the agents they are meant to protect, so findings never translate into updated guardrails, detection rules, or incident runbooks. 

**Topics**
+ [Capability intent](#capability-intent-6)
+ [Maturity levels](#maturity-levels-6)
+ [Common issues to watch for](#common-issues-to-watch-for-6)
+ [AGENTSEC07-BP01 Implement cognitive load management](agentsec07-bp01.md)
+ [AGENTSEC07-BP02 Clear confidence indicators and manipulation warnings](agentsec07-bp02.md)
+ [AGENTSEC07-BP03 Multiple reviewers for critical operations](agentsec07-bp03.md)
+ [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](agentsec07-bp04.md)
+ [AGENTSEC07-BP05 Regular security assessments and red teaming](agentsec07-bp05.md)