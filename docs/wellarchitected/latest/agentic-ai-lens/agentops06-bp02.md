

# AGENTOPS06-BP02 Evaluate and track ongoing agent performance
<a name="agentops06-bp02"></a>

 Pre-deployment evaluation validates that an agent is ready to ship. Post-deployment evaluation validates that it still works. Without continuous assessment, gradual quality degradation from data drift, model updates, and shifting user patterns goes unnoticed until it is expensive to fix. 

 **Desired outcome:** 
+  Agent performance is continually evaluated against defined quality benchmarks. 
+  Automated pipelines detect degradation in output quality, reasoning accuracy, and business outcome alignment. 
+  Teams have clear visibility into performance trends over time and can correlate quality changes with specific configuration, model, or data updates. 
+  Evaluation results drive prioritized improvement actions and provide objective evidence for stakeholder reporting. 

 **Common anti-patterns:** 
+  Evaluating agent performance only at deployment time without continuous post-deployment assessment, missing gradual degradation from data drift, model updates, or changing user patterns. 
+  Relying solely on automated metrics without periodic human evaluation, missing quality dimensions that automated metrics can't fully capture (like nuance, appropriateness, and business context alignment). 
+  Using generic evaluation criteria across all agents without tailoring metrics to each agent's specific use case and business objectives, producing evaluation results that don't reflect actual value. 
+  Treating evaluation as separate from operations rather than integrating it into the operational workflow, creating evaluation debt that accumulates over time. 

 **Benefits of establishing this best practice:** 
+  Continuous evaluation provides an empirical foundation for evidence-based improvement, identifying which agents need attention and which changes produce measurable gains. 
+  Performance trend tracking reveals patterns that inform systematic improvement, turning evaluation data into practical insights. 
+  Multi-dimensional scoring catches quality issues that a single metric would miss. 
+  Correlation between quality shifts and configuration changes compresses root-cause analysis. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) is an evaluation service for continuous assessment. Its on-demand mode runs benchmarks during development, and its online mode samples and evaluates live interactions in production without requiring manual triggers. Thirteen built-in evaluators cover correctness, helpfulness, safety, and tool selection accuracy, with custom evaluators available for business-specific requirements. [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) supplements this with model-level assessment, and periodic human evaluation covers the dimensions automated metrics miss. 

 Evaluation frameworks need multiple dimensions because a single metric misses too much. For example: 
+  Output quality (relevance, accuracy, coherence) measures whether responses are good. 
+  Safety (hallucination rate, toxicity, guardrail adherence) measures whether responses are safe. 
+  Efficiency (task completion rate, tool invocation success) measures whether the agent is economical. 
+  Business alignment (outcome achievement, user satisfaction, SLA compliance) measures whether the agent delivers value. 

 Weighting depends on the use case. For instance, a customer-support agent might weigh satisfaction higher than efficiency, while an internal automation agent might weigh efficiency higher than relevance. Generic weighting produces generic results. 

 Dashboards that show evaluation scores over time make degradation visible before it becomes an incident. Alerting on threshold violations and on persistent negative trends, as opposed to single-point dips, catches the slow-moving problems that are hardest to diagnose after the fact. Correlate evaluation shifts with configuration and model changes so attribution is fast when a metric moves. 

 LLM-as-a-Judge patterns can use multiple evaluator prompts covering different quality dimensions to produce a composite score that is more reliable than any single prompt. Periodic human review validates the automated scores and catches the blind spots. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html):** Use on-demand mode for development benchmarking and online mode for continuous production monitoring. 

1.  **Define a multi-dimensional evaluation framework:** Apply use-case-specific weighting across quality, safety, efficiency, and business alignment. 

1.  **Implement LLM-as-judge patterns:** Use multiple evaluator prompts and supplement with periodic human evaluation. 

1.  **Build evaluation dashboards:** Show trends over time with alerting for threshold violations and persistent negative trends. 

1.  **Correlate evaluation results with change events:** Tag deployments, configuration updates, and model changes so quality shifts can be attributed quickly. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS06-BP01 Design multi-layered testing frameworks](agentops06-bp01.html) 
+  [AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows](agentops06-bp03.html) 
+  [AGENTOPS02-BP04 Maintain feedback control loops for continuous improvement](agentops02-bp04.html) 
+  [AGENTOPS05-BP04 Define and track KPIs for agent workflows](agentops05-bp04.html) 
+  [AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads](agentperf01-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Evaluate models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) 
+  [LLM-as-a-judge on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/) 
+  [Evaluating AI agents for production: A practical guide to Strands Evals](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-for-production-a-practical-guide-to-strands-evals/) 
+  [From AI agent prototype to product: Lessons from building AWS DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent) 

 **Related workshops:** 
+  [Getting started with Amazon Bedrock AgentCore, Lab 5: Evaluate Agent Performance](https://catalog.workshops.aws/agentcore-getting-started/en-US/65-evaluation) 
+  [Diving Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 