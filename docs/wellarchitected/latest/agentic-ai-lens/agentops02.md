# Prompt and configuration lifecycle management

Agent prompts, configurations, and tool permissions define agent behavior and evolve
continually as business needs change. Managing these artifacts requires balancing rapid
iteration with stability so that changes are tracked, tested, and reversible.

| AGENTOPS02: How do you manage prompt and configuration<br>lifecycle? |
| -------------------------------------------------------------------- |
|                                                                      |

## Capability intent

- Agent prompts, behavioral configurations, and tool permissions are managed
  as first-class operational artifacts with full version history, documented
  ownership, and a defined lifecycle from authoring through retirement.
- Behavioral changes reach production only after passing automated
  evaluation against documented quality thresholds, and they move through
  staged rollout rather than full-traffic deployment.
- Configurations remain consistent across development, staging, and
  production environments, and drift from approved baselines is detected and
  remediated automatically.
- Rollback to a known-good behavioral baseline is automated, tested
  regularly, and completes within minutes of the decision to revert.
- Operational signals, user feedback, and business outcome metrics flow into
  a structured improvement backlog that closes the loop from observation to
  validated change.

## Maturity levels

These levels summarize what each stage of maturity looks like for prompt and
configuration lifecycle management as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Initial   | Prompts and behavioral configurations are embedded in application<br>code or maintained by hand in each environment. Changes are deployed<br>directly to production without evaluation, and there is no version<br>history to roll back to when a change regresses. Configuration<br>differences between development, staging, and production are common<br>and only noticed after incidents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2     | Emerging  | Prompts and behavioral configurations are stored outside<br>application code in a versioned repository such as [Amazon Bedrock Prompt Management](../../../bedrock/latest/userguide/prompt-management.md "../../../bedrock/latest/userguide/prompt-management.md"). Infrastructure<br>baselines are defined in [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") or the [AWS<br>CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md"), and changes follow a documented lifecycle with peer<br>review. Rollback is possible but manual.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3     | Defined   | A full prompt lifecycle (Draft, Review, Active, Archived) is<br>enforced through [AWS CodePipeline](../../../codepipeline/latest/userguide/approvals-action-add.md "../../../codepipeline/latest/userguide/approvals-action-add.md") approval gates, with automated<br>evaluation using [Amazon Bedrock Evaluations](../../../bedrock/latest/userguide/evaluation.md "../../../bedrock/latest/userguide/evaluation.md") as a promotion gate. [AWS CloudFormation drift detection](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md") and [AWS Config rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") monitor for configuration drift, and<br>[AWS CloudTrail](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md") captures change attribution. Rollback<br>runbooks are defined and tested. |
| 4     | Proactive | Behavioral changes roll out in stages using [Amazon Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md") weighted routing, with<br>automated promotion gates driven by [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") quality metrics. A/B testing compares<br>behavioral variants under traffic, and [automated remediation](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md") restores approved configurations<br>when drift is detected. A multi-channel feedback pipeline built on<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") feeds an improvement<br>backlog.                                                                                                                                                                         |
| 5     | Optimized | The full lifecycle is self-service for teams, with automated<br>rollback that restores behavioral baselines within minutes of a<br>quality threshold being exceeded. Cross-environment consistency is<br>validated continuously, and [Amazon Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") correlates<br>deployment timestamps with quality trends so every metric change is<br>attributable to a specific behavioral version.<br>Feedback-to-improvement workflows close the loop from signal to<br>validated change, and the organization contributes its patterns back<br>to the broader agentic AI community.                                                                                                                                                                                                                                                                                                                                                            |

## Common issues to watch for

- Prompts are embedded directly in application code, so any behavioral
  change forces a full code deployment and makes it impossible to iterate on
  agent behavior independently.
- Configuration changes are applied through manual console edits in
  individual environments, which causes development, staging, and production
  to drift apart and produces "it worked in test" failures in
  production.
- Behavioral changes roll straight to 100 percent of traffic without staged
  rollout or pre-deployment evaluation, maximizing the scope of impact of any
  regression and leaving no safe path to catch issues early.
- Rollback is treated as a manual, exploratory activity rather than a
  tested, automated procedure, so recovery takes hours instead of minutes when
  a behavioral change goes wrong.
- User feedback, quality metrics, and business outcome signals are collected
  but never connected to specific prompt or configuration versions, leaving
  teams unable to attribute quality changes to the behavioral changes that
  caused them.

###### Best practices

- [AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs](agentops02-bp01.md "agentops02-bp01.md")
- [AGENTOPS02-BP02 Implement configuration drift detection and remediation](agentops02-bp02.md "agentops02-bp02.md")
- [AGENTOPS02-BP03 Implement agent behavior versioning and rollback capabilities](agentops02-bp03.md "agentops02-bp03.md")
- [AGENTOPS02-BP04 Maintain feedback control loops for continuous improvement](agentops02-bp04.md "agentops02-bp04.md")
