# AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs

A prompt shapes agent behavior more directly than almost any other
configuration artifact. Create a prompt lifecycle that applies
code-grade discipline, versioning, review, evaluation, and rollback
to prompts, which helps avoid unnoticed prompt drift and degraded
decisions in agent interactions.

**Desired outcome:**

- You manage agent prompts through a defined lifecycle: authoring,
  review, testing, deployment, monitoring, and retirement.
- Every production prompt has a documented version history, an
  evaluation record, and a clear owner.
- You deploy prompt updates independently of application code and
  roll back to a previous version within minutes.
- You track the performance impact of each prompt change over time
  and can attribute quality shifts to specific versions.

**Common anti-patterns:**

- Hardcoding prompts directly in application code, making it
  impossible to update agent behavior without a full code
  deployment and blocking independent prompt iteration.
- Deploying prompt changes directly to production without
  evaluation against quality benchmarks, discovering regressions
  only after users report them.
- Operating without prompt version history, making it impossible
  to determine which prompt change caused a behavioral regression
  or to roll back to a known-good version.
- Treating prompt changes as too small to require review, letting
  ad-hoc edits accumulate into drift that no one owns.

**Benefits of establishing this best
practice:**

- Behavioral changes follow a consistent, auditable path from
  authoring to deployment, reducing operational risk and enabling
  reliable rollback.
- Prompt performance tracking and evaluation create an empirical
  basis for iteration. Each update is validated against measurable
  quality criteria before reaching production.
- Teams can deploy prompt changes independently of application
  code, shortening the feedback loop between business need and
  runtime behavior.
- Failed prompt updates revert in minutes rather than requiring an
  incident response.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Treat prompts as first-class operational artifacts with the same
discipline applied to application code. Application code moves
through version control, code review, automated tests, staged
deployment, and documented rollback. Most organizations apply none
of these to prompts, which can result in agent behavior drifts.
Apply the same lifecycle to prompts as you do to code, where you
name the stages explicitly and require changes to follow them.

[Amazon
Bedrock Prompt Management](../../../bedrock/latest/userguide/prompt-management.md "../../../bedrock/latest/userguide/prompt-management.md") provides versioning, metadata,
and integration with
[Amazon
Bedrock Evaluations](../../../bedrock/latest/userguide/model-evaluation.md "../../../bedrock/latest/userguide/model-evaluation.md"). For no-code paths built with
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/ "https://aws.amazon.com/quicksuite/"), the same stages apply through the identity and
instructions configuration. A four-stage lifecycle works for most
teams:

1. Draft (under development, not deployed)
2. Review (under peer review and evaluation)
3. Active (deployed to production)
4. Archived (retired but retained for audit)

Gate stage transitions by approval workflows implemented in
[AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") or
[AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/"), not by convention.

Every prompt entry needs required metadata: purpose, target agent,
expected behavior, evaluation criteria, and owner.
Parameterization should be used to reduce duplication across
related agents. Steering files in Kiro or equivalent conventions
codify these standards so they are applied automatically during
development rather than enforced after the fact.

[Amazon
Bedrock Evaluations](../../../bedrock/latest/userguide/model-evaluation.md "../../../bedrock/latest/userguide/model-evaluation.md") runs each prompt version against a
standardized dataset and produces scores for task success,
response relevance, and adherence to behavioral guidelines. A
prompt that can't meet its minimum thresholds doesn't advance from
review to active. Once in production, quality metrics published to
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") as custom metrics give the team an early warning
when a prompt that passed evaluation starts degrading in the real
world, triggering a review workflow.

### Implementation steps

1. **Stand up the central prompt
   repository:** Configure
   [Amazon
   Bedrock Prompt Management](../../../bedrock/latest/userguide/prompt-management.md "../../../bedrock/latest/userguide/prompt-management.md") with four lifecycle stages
   (draft, review, active, archived) and required metadata
   fields (purpose, target agent, expected behavior, evaluation
   criteria, owner).
2. **Define prompt authoring
   standards:** Specify required metadata, formatting
   conventions, and documentation requirements. Apply them
   through shared templates or steering files so they are
   enforced during development.
3. **Build versioned evaluation
   datasets:** Create datasets for each agent's
   primary use cases and store them with versioning enabled so
   evaluation results are reproducible.
4. **Gate transitions on automated
   evaluation:** Configure an
   [Amazon
   Bedrock Evaluations](../../../bedrock/latest/userguide/model-evaluation.md "../../../bedrock/latest/userguide/model-evaluation.md") pipeline that runs on every
   transition from draft to review, with minimum quality
   thresholds.
5. **Enforce lifecycle stages in
   CI/CD:** Use
   [AWS CodePipeline](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md") to block promotion to active without
   approval and evaluation threshold checks.
6. **Reference prompts by ID, not by
   value:** Deploy agents with parameterized
   references to the prompt repository rather than hardcoded
   strings, so prompts evolve independently of application
   code.
7. **Monitor active prompts in
   production:** Publish quality metrics to
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"), build dashboards per agent, and configure
   alarms that trigger review workflows when thresholds are
   exceeded.

## Resources

**Related best practices:**

- [AGENTOPS01-BP03 Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes](agentops01-bp03.md "agentops01-bp03.md")
- [AGENTOPS02-BP03
  Implement agent behavior versioning and rollback capabilities](agentops02-bp03.md "agentops02-bp03.md")
- [AGENTOPS06-BP01
  Design multi-layered testing frameworks](agentops06-bp01.md "agentops06-bp01.md")
- [AGENTREL02-BP04
  Develop clear instruction protocols for agents](agentrel02-bp04.md "agentrel02-bp04.md")

**Related documents:**

- [Operationalizing agentic AI on AWS](../../../prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.md "../../../prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.md")
- [Evolving software delivery for agentic AI](../../../prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.md "../../../prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.md")
- [AI agents in enterprises: Best practices with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/ "https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/")
- [Kiro](https://kiro.dev/ "https://kiro.dev/")
- [Kiro
  Steering](https://kiro.dev/docs/steering/ "https://kiro.dev/docs/steering/")

**Related videos:**

- [AWS 2025 - Amazon Bedrock Prompt Management Demo](https://www.youtube.com/watch?v=CE_-zrMvcuk "https://www.youtube.com/watch?v=CE_-zrMvcuk")
- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y "https://www.youtube.com/watch?v=wuVpCc5a81Y")

**Related examples:**

- [GitHub:
  Sample Bedrock Evaluation Adapter](https://github.com/aws-samples/sample-bedrock-evaluation-adapter "https://github.com/aws-samples/sample-bedrock-evaluation-adapter")
- [GitHub:
  Sample Bedrock Model Evaluation](https://github.com/aws-samples/sample-bedrock-model-evaluation "https://github.com/aws-samples/sample-bedrock-model-evaluation")
- [GitHub:
  Amazon Bedrock Samples, GenAI Quick-Start PoCs](https://github.com/aws-samples/genai-quickstart-pocs "https://github.com/aws-samples/genai-quickstart-pocs")

**Related services:**

- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
