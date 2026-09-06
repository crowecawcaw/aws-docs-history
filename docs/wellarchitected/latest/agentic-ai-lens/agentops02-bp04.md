

# AGENTOPS02-BP04 Maintain feedback control loops for continuous improvement
<a name="agentops02-bp04"></a>

 Agents that improve in step with real-world usage outperform agents frozen at deployment. A working feedback loop connects quality signals, user feedback, behavioral cues, and business outcomes to prioritized improvement actions. 

 **Desired outcome:** 
+  You collect and correlate agent performance data, user feedback, and business outcome metrics systematically, not through ad-hoc surveys. 
+  Feedback loops operate continually, detecting quality trends in near real time rather than through quarterly reviews. 
+  Improvement actions are tracked from identification through implementation and validation. 
+  Feedback signals are attributable to specific agent versions, so teams know which improvements are responding to which problems. 

 **Common anti-patterns:** 
+  Collecting user feedback (like thumbs up and down or ratings) without connecting it to specific agent behaviors or prompt versions, making it impossible to attribute quality changes to improvements. 
+  Relying solely on periodic manual reviews rather than continuous automated feedback processing, allowing quality degradation to persist for weeks before detection. 
+  Collecting feedback data without a defined process for turning insights into improvement actions, creating a growing backlog of signals that never translate into agent changes. 
+  Mixing signal types into a single bucket, so a surge in automated quality alerts drowns out a handful of high-severity user reports that deserve immediate attention. 

 **Benefits of establishing this best practice:** 
+  Structured feedback turns operational data into a continuous source of improvement signals, so agents evolve in response to real usage rather than staying static after deployment. 
+  Feedback-driven prioritization directs development effort toward changes with the greatest measurable impact. 
+  Trend tracking over time reveals patterns (data drift, concept drift, and scope drift) that inform targeted refinement rather than scattershot tweaking. 
+  Improvement validation gives the team evidence that each change delivered the expected gain. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Feedback loops should watch more than one signal to be truly useful. 

 Automated quality metrics from [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) show measurable shifts in output quality. 

 To watch subjective perception, consider checking: 
+  Explicit user feedback 
+  Thumbs up and down 
+  Ratings 
+  Free-text comments 

 To determine whether users are finding what they need, consider checking: 
+  Implicit behavioral signals 
+  Task abandonment 
+  Escalation rates 
+  Retry patterns 

 To determine if the agent is adhering to your organization's goals, consider checking: 
+  Business outcome metrics 
+  Conversion rate 
+  Resolution time 
+  Customer satisfaction 

 Each channel catches failures the others miss, so collecting all four of these metric pathways and routing them through a unified processing pipeline is the minimum viable design. 

 Use event-driven ingestion to keep your pipeline scalable. [Amazon EventBridge](https://aws.amazon.com/eventbridge/) or an equivalent event bus takes feedback events from every channel and routes them to a processing layer that classifies by type (quality issue, capability gap, tool failure, behavioral misalignment), severity, and affected component. Storing processed feedback in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with indexing by agent, feedback type, and time period makes trend analysis and querying practical instead of painful. 

 Consider implementing severity-based routing to avoid drowning your teams in constant alerts. High-severity feedback, a user reporting the agent did something dangerous, or a sudden drop in a quality metric goes straight to an immediate-review queue. Lower-severity feedback aggregates into batch reviews that surface patterns over days rather than requiring immediate reactions. 

 Verify that you have an effective improvement tracking workflow. To keep your feedback process useful and actionable, you need: 
+  A durable workflow 
+  Identification 
+  Root cause analysis 
+  Improvement design 
+  Implementation 
+  Validation 
+  Correlation to the specific feedback that prompted the action 
+  Metrics compared before and after each change 

 Validation is the step most often skipped, and the one that tells the team whether an improvement was truly effective. 

 Dashboards help you address visibility of both feedback and improvements. Feedback trends alongside improvement outcomes provide a clear view of whether the agent's quality trajectory is rising, flat, or falling, and which improvements are responsible for each inflection. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement multi-channel feedback collection:** Cover automated quality metrics (through [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)), explicit user feedback, implicit behavioral signals, and business outcome metrics. 

1.  **Classify feedback at ingestion:** Categorize by type (quality issue, capability gap, tool failure, behavioral misalignment), severity, and affected component. 

1.  **Store processed feedback for trend analysis:** Use [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) indexed by agent, feedback type, and time period. 

1.  **Route by severity:** Send high-severity feedback to immediate review queues through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Aggregate lower-severity items for batch review. 

1.  **Track improvements end to end:** Build a workflow that moves each item from identification through root-cause analysis, implementation, and validation, with metrics compared before and after. 

1.  **Build visibility into trends and outcomes:** Create dashboards that show feedback trends, improvement outcomes, and quality trajectory over time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs](agentops02-bp01.html) 
+  [AGENTOPS05-BP02 Monitor agent behavior patterns and detect anomalies](agentops05-bp02.html) 
+  [AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads](agentperf01-bp01.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) 
+  [Guidance for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Elevate application and generative AI observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs) 
+  [AWS re:Invent 2024 - Responsible generative AI: Evaluation best practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y) 

 **Related examples:** 
+  [GitHub: Open Source Bedrock Agent Evaluation](https://github.com/aws-samples/open-source-bedrock-agent-evaluation) 
+  [GitHub: Sample Bedrock Evaluation Adapter](https://github.com/aws-samples/sample-bedrock-evaluation-adapter) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 