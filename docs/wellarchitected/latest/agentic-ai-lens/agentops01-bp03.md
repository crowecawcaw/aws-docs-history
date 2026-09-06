

# AGENTOPS01-BP03 Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes
<a name="agentops01-bp03"></a>

 Happy-path testing predicts how agents behave when everything works, while failure testing predicts how they behave in the event of unforeseen issues. A resilience posture built on injected failures, deadlock scenarios, and disrupted business processes is the difference between graceful degradation and an unexpected outage. 

 **Desired outcome:** 
+  You have a failure test suite for every agent covering dependent-component failures, orchestration breakdowns, and business-process disruptions. 
+  You can inject failures into agent workflows on demand and verify that error handling, graceful degradation, and escalation behave as designed. 
+  You maintain known failure patterns as regression tests that run automatically on every behavioral change. 
+  You track failure test pass rates over time as a visible resilience metric. 

 **Common anti-patterns:** 
+  Testing only the happy path without validating agent behavior when tools are unavailable, APIs time out, or data sources return errors. 
+  Running failure tests only in isolated unit environments without simulating multi-agent coordination failures such as deadlocks, message loss, or handoff timeouts. 
+  Treating failure test scenarios as a one-time exercise rather than a living regression suite that grows with each production incident. 
+  Skipping tests for business-process disruptions, upstream format changes, delayed approvals, and downstream rejections, so agents fail silently when the real world shifts. 

 **Benefits of establishing this best practice:** 
+  Failure test suites become a stable benchmark for comparing agent resilience across iterations, providing the empirical basis for improvement decisions. 
+  Standardized testing helps assess every agent change for resilience impact the same way, regardless of who made the change or how urgent the timeline is. 
+  Known failure patterns captured as regression tests help prevent recurrence of previously diagnosed issues. 
+  Visible resilience trends give leadership and operators a shared view of whether the agent portfolio is getting more reliable or more fragile. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Failure modes cluster into three categories, and each requires a different testing posture. 

 Dependent-component failures are the most tractable. Tools return 5xx errors, APIs time out, knowledge bases return empty results, and model inference throttles or degrades. These map cleanly to agent evaluation and synthetic fault injection. [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) provides automated assessment of how agents handle edge cases and failure scenarios, using built-in and custom evaluators to score agent behavior against expected outcomes. For infrastructure-level fault injection such as network latency or capacity exhaustion, [AWS Fault Injection Service](https://aws.amazon.com/fis/) complements agent evaluations by validating that retry policies, fallbacks, and cutoffs behave as documented at the infrastructure layer. 

 Orchestration breakdowns are harder because they require more than a single failing component. Message loss, duplicate delivery, out-of-order messages, deadlocks, handoff timeouts, and context-package corruption all emerge from the interactions between agents rather than any single agent's behavior. Test these scenarios by simulating coordination failures in your multi-agent workflows. Inject handoff timeouts, corrupt context packages, and trigger concurrent requests that expose race conditions. Decide whether to simulate these failures in a shared staging environment or in a dedicated chaos environment. The former catches regressions faster, while the latter reduces the scope of impact during exploratory testing. 

 Business-process disruptions are the category most often missed because they don't look like infrastructure failures. When an upstream team changes an input schema, when a required approval is delayed, or when a downstream system rejects an agent's output, the agent's code is intact and every dependency responds, but the workflow still fails. Test scenarios must cover how the agent behaves when the business process shifts, like graceful failure, meaningful error messages, appropriate escalation, and no silent corruption. These tests protect against the failure mode where the system looks healthy to monitoring but delivers wrong or incomplete outcomes. 

 Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to maintain and run evaluation datasets that capture known failure patterns as regression tests. Integrate the evaluation suite into the CI/CD pipeline as a mandatory gate so deployments are blocked when failure-handling regression appears. Track pass rates in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and configure alarms when resilience metrics degrade. The operational benefit compounds, as every production incident becomes an opportunity to add a test scenario, and the suite gets sharper over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Catalog known failure modes per agent:** Organize by dependent-component failures, orchestration breakdowns, and business-process disruptions, with a named owner for each category. 

1.  **Create tests for dependent-component failures:** Simulate tool unavailability, API timeouts, data-source errors, and model inference degradation using [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) dataset evaluations and custom evaluators. 

1.  **Create tests for orchestration breakdowns:** Cover communication failures, deadlock conditions, handoff errors, and context-package corruption by simulating coordination failures in multi-agent workflows. 

1.  **Create tests for business-process disruptions:** Simulate upstream process changes, input format changes, and downstream system rejections, and verify graceful failure and meaningful escalation. 

1.  **Integrate infrastructure fault injection where appropriate:** Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) for infrastructure-level failures (throttling, capacity exhaustion, network latency) that affect agent workflows. 

1.  **Gate deployments on failure-handling regression:** Make the evaluation suite a mandatory CI/CD stage that blocks promotion when resilience regressions appear. 

1.  **Maintain evaluation datasets as living regression suites:** Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to track pass rates, and alert on degradation via [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). 

1.  **Review and expand scenarios quarterly:** Incorporate failure patterns discovered in production incidents so the suite grows with the system. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs](agentops02-bp01.html) 
+  [AGENTOPS04-BP03 Develop fallback behavior and error handling for tool invocations](agentops04-bp03.html) 
+  [AGENTOPS06-BP01 Design multi-layered testing frameworks](agentops06-bp01.html) 
+  [AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads](agentperf01-bp01.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) 
+  [Planning for failure: How to make generative AI workloads more resilient](https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/) 
+  [Guidance for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Best practices for generative AI observability (COP404)](https://www.youtube.com/watch?v=sRjm6HS6yYU) 
+  [AWS re:Invent 2024 - Unlock the power of generative AI with AWS Serverless (SVS319)](https://www.youtube.com/watch?v=y0jImhzqR1U) 

 **Related examples:** 
+  [GitHub: Open Source Bedrock Agent Evaluation](https://github.com/aws-samples/open-source-bedrock-agent-evaluation) 
+  [GitHub: Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform) 

 **Related services:** 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 