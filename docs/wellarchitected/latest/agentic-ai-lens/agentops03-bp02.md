

# AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)
<a name="agentops03-bp02"></a>

 Manual agent deployments and informal testing can keep a project stuck in the pilot phase. An agent-aware pipeline, with behavioral evaluation gates, staged rollout, and automated rollback can help your organization realize the goal of daily deployment of behavioral improvements. 

 **Desired outcome:** 
+  Agent deployments run fully through CI/CD with agent-specific validation gates for prompt quality, tool integration correctness, behavioral regression, and security. 
+  Deployment strategies (blue/green, canary) limit the scope of impact when a regression does slip through. 
+  Automated rollback restores the previous version within minutes if quality thresholds are exceeded. 
+  Infrastructure is defined as code so deployments are reproducible and environments stay consistent. 

 **Common anti-patterns:** 
+  Deploying agent changes through manual console clicks or one-off scripts without automated validation gates, making deployments inconsistent and error-prone. 
+  Running only traditional unit tests without agent-specific behavioral evaluation (prompt quality, tool selection accuracy, hallucination rate), missing regressions that unit tests can't detect. 
+  Deploying directly to production without staged rollout (canary, blue/green), maximizing the scope of impact of any regression. 
+  Treating rollback as a theoretical capability that has never been exercised, so the first time anyone uses it is during an incident. 

 **Benefits of establishing this best practice:** 
+  Automated pipelines help every deployment follow the same validated path regardless of who starts it, reducing deployment inconsistency. 
+  Behavioral validation gates provide empirical evidence that each deployment meets quality standards before reaching production. 
+  Staged rollout and automated rollback compress incident response time from hours to minutes when regressions appear. 
+  Infrastructure as code makes deployments reproducible across environments, removing a common source of failures. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Agent CI/CD shares most of its structure with software CI/CD, with one substantive addition: behavioral evaluation. The stages that fit most agent workloads are: 
+  Source (code, prompts, configurations, and evaluation datasets) 
+  Build (package artifacts and run unit tests) 
+  Evaluate (run behavioral evaluation through [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html)) 
+  Security scan (prompt injection vulnerabilities and IAM scope) 
+  Deploy to production 

 Task completion accuracy, hallucination rate, and tool selection accuracy need explicit thresholds that block promotion when exceeded. Thresholds that are set too loose produce false passes, but thresholds that are set too tight block legitimate iteration. To calibrate, start with thresholds tuned to the current baseline, then tighten them as the agent's quality track record grows. 

 Production deployment uses [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for managed scaling, versioning, and observability. agentcore deploy pushes new versions, and endpoint-based weighted routing handles blue/green and canary patterns. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms watch quality metrics post-deployment and trigger automated rollback when thresholds are exceeded. The same alarms that run during staged rollout double as rollback triggers. Infrastructure as code through [AWS CDK](https://aws.amazon.com/cdk/) or [AWS CloudFormation](https://aws.amazon.com/cloudformation/) helps make every resource reproducible. 

 A rollback procedure that has never been exercised is a procedure that may not work when the team needs it. Deliberate rollback drills during pipeline validation confirm the revert works before the team is depending on it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build the pipeline stages:** Configure source, build, behavioral evaluation, security scan, and production deployment stages with the appropriate tools for each. 

1.  **Set behavioral evaluation as a gate:** Integrate [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) with task completion accuracy and hallucination rate thresholds that block promotion when exceeded. 

1.  **Deploy to [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html):** Use built-in versioning and endpoint-based weighted routing for blue/green or canary rollouts. 

1.  **Automate rollback on quality threshold exceedance:** Wire [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms to revert-deployment workflows so quality threshold violations trigger immediate revert. 

1.  **Version all deployment artifacts:** Tag each artifact set with the pipeline run ID for traceability, and store in a durable versioned store. 

1.  **Validate the full pipeline:** Deliberately trigger a rollback during pipeline validation to confirm revert procedures work before they are needed for real. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance](agentops03-bp01.html) 
+  [AGENTOPS02-BP03 Implement agent behavior versioning and rollback capabilities](agentops02-bp03.html) 
+  [AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows](agentops06-bp03.html) 
+  [AGENTCOST06-BP02 Cost optimize versioning and deployment through efficient artifact management](agentcost06-bp02.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Evolving software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html) 
+  [Deploy AI agents on Amazon Bedrock AgentCore using GitHub Actions](https://aws.amazon.com/blogs/machine-learning/deploy-ai-agents-on-amazon-bedrock-agentcore-using-github-actions/) 
+  [Strands Agents](https://strandsagents.com/) 
+  [CI/CD and automation for serverless AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html) 
+  [Kiro Hooks](https://kiro.dev/docs/hooks/) 

 **Related videos:** 
+  [AWS 2025 - Deploy Production-Ready Agents in 22 Minutes with AgentCore Runtime](https://www.youtube.com/watch?v=Q-tYIAuv9WI) 
+  [AWS 2025 - Deploy ANY AI Agent to Production in Minutes - AgentCore Tutorial](https://www.youtube.com/watch?v=N7FGbBq1mI4) 
+  [AWS 2025 - Strands Agents Observability, Evaluation, & Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE) 
+  [AWS re:Invent 2024 - Building AI Agents with Serverless, Strands, and MCP (NTA405)](https://www.youtube.com/watch?v=LwubRSoJcIM) 
+  [AWS re:Invent 2024 - Develop AI Agents faster with SageMaker AI Studio & AgentCore (AIM388)](https://www.youtube.com/watch?v=UL_7a2GEu10) 

 **Related workshops:** 
+  [Getting started with Amazon Bedrock AgentCore, Lab 4: Deploy to Production](https://catalog.workshops.aws/agentcore-getting-started/en-US/60-add-runtime) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 