

# AGENTSUS03-BP01 Maintain organizational skills and competencies
<a name="agentsus03-bp01"></a>

 Organizations that automate without deliberately preserving the human expertise behind the automation lose the capacity to train new staff, handle edge cases, and recover when automated systems reach their limits. Keeping a clear distinction between what agents handle autonomously and what stays with human experts sustains organizational capability across the whole lifetime of the deployment. 

 **Desired outcome:** 
+  You have a competency taxonomy that separates human-owned, agent-augmented, and fully automated tasks, with documented criteria for each tier. 
+  Routing in the agent layer escalates high-stakes, ambiguous, or edge-case decisions to human experts automatically. 
+  Rotation programs and workshops keep subject matter experts proficient with the workflows agents otherwise execute. 
+  You monitor escalation rates and expert task distribution to confirm critical competencies stay actively practiced. 

 **Common anti-patterns:** 
+  Automating domain workflows without maintaining documented runbooks or periodic manual execution exercises, reducing the organization's capacity to operate when agent systems are unavailable. 
+  Running agents without clear boundaries between autonomous action and human oversight, producing cases where agents make high-stakes decisions that should have routed to experts. 
+  Scaling agent adoption without workforce planning to preserve critical skills, so short-term productivity gains erode long-term organizational capacity. 
+  Treating escalation as an exception rather than an expected outcome, so the hand-off paths between agents and human experts are undertested and fail when they are needed most. 

 **Benefits of establishing this best practice:** 
+  The organization retains the capacity to operate manually when agent systems are unavailable or encounter situations beyond their training. 
+  Critical expertise stays available for onboarding, edge cases, and evolving business processes that automation has not caught up to. 
+  Adoption paces the organization's ability to maintain oversight, rather than outrunning it. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The threshold question is which competencies must stay with humans and which can move to agents or automation. A three-tier taxonomy, human-owned, agent-augmented, and fully automated, gives teams a shared vocabulary for that decision. The categorization criteria matter more than the labels: 
+  Human-owned means decisions where error tolerance is low and context is highly variable (regulatory judgment, customer escalations, and strategic trade-offs) 
+  Agent-augmented means work where an agent accelerates human output but the human remains the decision-maker (code review, document drafting, and data analysis) 
+  Fully automated means routine tasks where agent accuracy exceeds the cost of errors (routing, classification, and standard form processing) 

 Categorization is reviewed as agent capabilities improve and as organizational priorities shift. 

 [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with Policies and code interceptors can invoke human-in-the-loop workflows based on complexity thresholds, confidence scores, or stakes assessment. [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) enforces the decision boundaries so that high-stakes cases escalate automatically rather than depending on the agent to self-report low confidence. [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs agent outputs against expert-generated baselines, which is how you detect drift in categories where the agent was trusted but is now degrading. 

 The automation that removes a task from expert workflows also removes the practice that kept expertise sharp. Rotation programs assign experts to handle a fraction of cases manually on a recurring basis. For business-critical competencies, a defined minimum (a percentage of cases per quarter, a weekly shift, or a monthly workshop) keeps practice active. Document runbooks for workflows agents now execute so the manual path remains viable when the automated one is unavailable. [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks escalation rates and task distribution, showing whether experts are being kept in the loop often enough to stay sharp. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a competency taxonomy:** Categorize organizational skills into human-owned, agent-augmented, and fully automated tiers with documented criteria and a review cadence. 

1.  **Configure automated escalation:** Use [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) Policies and [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to route high-stakes, ambiguous, or low-confidence decisions to human experts. 

1.  **Establish rotation programs:** Assign subject matter experts to handle a defined percentage of cases manually each quarter for competencies critical to business resilience, and maintain runbooks for manual execution. 

1.  **Validate agent outputs against expert baselines:** Run [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against baselines produced by subject matter experts to detect drift in categories that have been trusted to automation. 

1.  **Monitor escalation and task distribution:** Track escalation rates and expert task distribution through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to confirm that critical competencies remain actively practiced. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSUS03-BP02 Build agents to mirror your organizational skills and competencies](agentsus03-bp02.html) 
+  [AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems](agentsus03-bp03.html) 
+  [MLPERF06-BP01 Include human-in-the-loop monitoring](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf-06.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Human-in-the-loop (HITL) - Amazon Nova Act](https://docs.aws.amazon.com/nova/latest/userguide/nova-act-hitl.html) 
+  [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Evaluations](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 