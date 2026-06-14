# Secure multi-agent orchestration

Multi-agent systems introduce coordination challenges that don't
exist in single-agent architectures. Agents need to discover
peers, share capabilities, delegate tasks, and exchange context
across trust boundaries. Without proper identity verification and
communication security, agent impersonation and message tampering
can affect entire multi-agent workflows. Standardized protocols
like Agent-to-Agent (A2A) and Model Context Protocol (MCP) provide
interoperability across frameworks, but organizations must layer
security controls on top of these protocols to maintain trust
boundaries.

| AGENTSEC06: How do you secure multi-agent orchestration<br>and coordination? |
| ---------------------------------------------------------------------------- |
|                                                                              |

## Capability intent

- Agents are segmented into trust zones based on role,
  capability, and risk profile, and inter-zone communication
  flows only along documented paths enforced at both the
  network and the application layer.
- Inter-agent messages that cross trust boundaries or traverse
  intermediary services are signed and encrypted at the
  message level, so payload integrity persists beyond the
  transport.
- Orchestration layers enforce schema validation, scoped IAM
  permissions, and circuit breakers, so a failure in one agent
  can't cascade through the workflow or divert it onto
  unexpected execution paths.
- Coordination patterns are monitored continually against
  established baselines, so deviations are detected
  proactively rather than discovered after the fact.
- Every coordination step is attributable to a verified agent
  identity and recorded for investigation. This includes agent
  card discovery (the
  [A2A
  protocol](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/ "https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/") mechanism by which one agent locates a peer
  and reads a JSON agent card describing its name,
  capabilities, supported skills, and authentication
  requirements), task delegation, and result collection.

## Maturity levels

These levels summarize what each stage of maturity looks like
for secure multi-agent orchestration as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents run in a flat network with no segmentation.<br>Inter-agent messages rely on transport-level encryption<br>alone, with no message signing or identity verification<br>on the receiving side. Orchestration is unstructured,<br>with broad IAM permissions on workflow APIs and no<br>circuit breakers, and coordination patterns are not<br>monitored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2     | Emerging  | Basic network segmentation groups agents by trust tier,<br>typically through separate<br>[security<br>groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") or<br>[Amazon VPCs](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").<br>[Amazon SQS server-side encryption](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.md") helps protect queued<br>messages with<br>[AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") keys.<br>[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") orchestrates workflows with<br>execution logging turned on, although IAM permissions<br>remain broad and circuit breakers are not currently in<br>place.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 3     | Defined   | Message-level signing through<br>[AWS KMS asymmetric keys](../../../kms/latest/developerguide/symm-asymm-concepts.md#asymmetric-cmks "../../../kms/latest/developerguide/symm-asymm-concepts.md#asymmetric-cmks") covers messages that cross<br>trust boundaries or traverse queues and event buses,<br>with separate keys per trust zone. Step Functions state<br>machines are managed as code through<br>[AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md") or the<br>[AWS Cloud Development Kit (AWS CDK)](../../../cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions-readme.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions-readme.md"),<br>[input<br>validation](../../../step-functions/latest/dg/amazon-states-language-input-output-processing.md "../../../step-functions/latest/dg/amazon-states-language-input-output-processing.md") and<br>[circuit<br>breakers](../../../step-functions/latest/dg/concepts-error-handling.md#error-handling-retrying-after-an-error "../../../step-functions/latest/dg/concepts-error-handling.md#error-handling-retrying-after-an-error") are in place, and<br>[AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") keeps cross-zone traffic on private<br>paths.                                                                                                                                                                                                                                                  |
| 4     | Proactive | [Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md") with<br>[A2A<br>protocol](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/ "https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/") support structures inter-agent discovery<br>and task delegation, and<br>[Cedar<br>policies](https://docs.cedarpolicy.com/ "https://docs.cedarpolicy.com/") in<br>[AgentCore<br>Policy](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/ "https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/") enforce trust boundaries at the tool<br>layer. Coordination metrics are captured as<br>[Amazon CloudWatch custom metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") with baselines, and<br>[CloudWatch<br>anomaly detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") flags deviations.<br>[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") findings are correlated with<br>coordination logs in<br>[AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-what-is.md "../../../securityhub/latest/userguide/securityhub-what-is.md"). |
| 5     | Optimized | Trust boundary configurations are continuously validated<br>through<br>[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") managed and<br>[custom<br>rules](../../../config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.md "../../../config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.md"), with alerts on any configuration that<br>creates unauthorized cross-zone connectivity.<br>[AgentCore<br>Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") feed tool selection accuracy and<br>correctness scores into coordination monitoring as an<br>early-warning layer. Incident response runbooks for<br>coordination anomalies are exercised regularly, and<br>validated patterns are folded back into the<br>organization's reference architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Common issues to watch for

- Multi-agent systems are deployed as a single trust zone, so
  an issue with any one agent can spread laterally across the
  entire network before the scope is understood.
- Teams rely on transport-level encryption for inter-agent
  traffic and treat message-level signing as unnecessary,
  which means messages sitting in queues or event buses can't
  be verified at consumption time.
- Orchestrator IAM permissions authorize any principal to
  start, stop, or modify any workflow in the account, rather
  than scoping access to the specific state machines each
  principal needs.
- Monitoring covers infrastructure metrics and individual
  agent health but ignores coordination metrics, so
  inter-agent message rate spikes, unexpected communication
  paths, and topology changes go undetected.
- [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") findings and coordination logs are treated
  as separate data streams, leaving investigators without the
  context to tie an API anomaly to the specific multi-agent
  workflow it affected.

###### Best practices

- [AGENTSEC06-BP01 Encrypt and sign inter-agent messages](agentsec06-bp01.md "agentsec06-bp01.md")
- [AGENTSEC06-BP02 Implement workflow orchestration security controls](agentsec06-bp02.md "agentsec06-bp02.md")
- [AGENTSEC06-BP03 Establish trust boundaries between agents](agentsec06-bp03.md "agentsec06-bp03.md")
- [AGENTSEC06-BP04 Monitor and detect coordination anomalies](agentsec06-bp04.md "agentsec06-bp04.md")
