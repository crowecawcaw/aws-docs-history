

# AGENTREL05-BP02 Facilitate reliable adaptation through evaluation-driven improvement cycles
<a name="agentrel05-bp02"></a>

 Agents degrade quietly when no one is watching, and runtime self-modification based on noisy feedback makes things worse. Structured feedback collection with offline evaluation and validated deployments keeps adaptation reliable because every change is measured before it reaches users. 

 **Desired outcome:** 
+  You collect action-level, task-level, and session-level feedback signals on every agent interaction. 
+  You run automated and LLM-as-a-judge evaluations periodically, comparing current behavior against golden-path examples. 
+  You validate prompt and configuration changes offline before deploying through gradual rollout. 

 **Common anti-patterns:** 
+  Deploying agents without feedback collection, missing the chance to identify systematic errors. 
+  Applying automated behavioral changes at runtime without offline validation, risking regression from noisy feedback. 
+  Skipping monitoring of the feedback loop itself, so silent pipeline failures block adaptation from happening. 

 **Benefits of establishing this best practice:** 
+  Task execution quality improves steadily through structured feedback collection and validated adjustments. 
+  Systematic errors get identified and corrected faster because automated analysis catches patterns humans miss. 
+  Manual intervention drops because evaluation-driven prompt optimization with controlled rollout replaces manual tuning. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Feedback is only useful at the granularity you collect it. Three tiers cover most of the signal. Action-level captures whether a tool call succeeded, task-level captures whether the agent completed the task correctly, and session-level captures whether the interaction achieved the user's goal. Action-level feedback tends to come from automated validators that compare outputs against expected schemas. Task-level feedback can be automated for deterministic success criteria and needs LLM-as-a-judge for subjective quality dimensions. Session-level feedback usually comes from users, either directly or through behavioral signals like follow-up questions. 

 [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs the periodic quality assessments against representative task sets, comparing outputs against golden-path examples and flagging regressions. Store evaluation results alongside task records so the agent's performance over time becomes a labeled dataset you can query. When evaluations indicate systematic degradation, that is the signal to trigger an offline prompt optimization workflow, test alternative formulations against evaluation benchmarks and deploy the highest-performing version through gradual rollout. 

 The discipline that keeps this reliable is validated before deployed, not modified at runtime. Runtime self-modification is tempting because it produces faster feedback, but noisy feedback can push agents into worse behavior. The scope of impact of a bad auto-update is the entire production fleet. Offline validation with gradual rollout keeps improvements under control. Monitor feedback loop health through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Track collection rates, processing latency, and evaluation frequency, with alarms when pipeline failures block the improvement cycle from operating. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement multi-tier feedback collection:** Capture action-level, task-level, and session-level signals for every interaction. 

1.  **Deploy automated outcome validators for deterministic criteria:** Compare outputs against expected schemas where the success criteria are unambiguous. 

1.  **Use AgentCore Evaluations with LLM-as-a-judge for subjective quality:** Run [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) on a periodic schedule against golden-path examples. 

1.  **Trigger offline prompt optimization when evaluations show degradation:** Validate candidates against benchmarks offline, then deploy through gradual rollout rather than runtime self-modification. 

1.  **Monitor feedback loop health:** Track collection rates, processing latency, and evaluation frequency through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms for pipeline failures. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL02-BP03 Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html) 
+  [AGENTREL05-BP01 Design modular, fault-tolerant agentic reasoning components](agentrel05-bp01.html) 
+  [AGENTREL05-BP03 Ground agent cognition in real information](agentrel05-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Evaluate models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) 
+  [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) 
+  [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Using Strands Agents to build autonomous, self-improving AI agents (AIM426)](https://www.youtube.com/watch?v=RQfW7eQsXqk) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 