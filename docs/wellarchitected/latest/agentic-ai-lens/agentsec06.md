

# Secure multi-agent orchestration
<a name="agentsec06"></a>

 Multi-agent systems introduce coordination challenges that don't exist in single-agent architectures. Agents need to discover peers, share capabilities, delegate tasks, and exchange context across trust boundaries. Without proper identity verification and communication security, agent impersonation and message tampering can affect entire multi-agent workflows. Standardized protocols like Agent-to-Agent (A2A) and Model Context Protocol (MCP) provide interoperability across frameworks, but organizations must layer security controls on top of these protocols to maintain trust boundaries. 


|  AGENTSEC06: How do you secure multi-agent orchestration and coordination?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-5"></a>
+  Agents are segmented into trust zones based on role, capability, and risk profile, and inter-zone communication flows only along documented paths enforced at both the network and the application layer. 
+  Inter-agent messages that cross trust boundaries or traverse intermediary services are signed and encrypted at the message level, so payload integrity persists beyond the transport. 
+  Orchestration layers enforce schema validation, scoped IAM permissions, and circuit breakers, so a failure in one agent can't cascade through the workflow or divert it onto unexpected execution paths. 
+  Coordination patterns are monitored continually against established baselines, so deviations are detected proactively rather than discovered after the fact. 
+  Every coordination step is attributable to a verified agent identity and recorded for investigation. This includes agent card discovery (the [A2A protocol](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) mechanism by which one agent locates a peer and reads a JSON agent card describing its name, capabilities, supported skills, and authentication requirements), task delegation, and result collection. 

## Maturity levels
<a name="maturity-levels-5"></a>

 These levels summarize what each stage of maturity looks like for secure multi-agent orchestration as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Agents run in a flat network with no segmentation. Inter-agent messages rely on transport-level encryption alone, with no message signing or identity verification on the receiving side. Orchestration is unstructured, with broad IAM permissions on workflow APIs and no circuit breakers, and coordination patterns are not monitored.  | 
|  2  |  Emerging  |  Basic network segmentation groups agents by trust tier, typically through separate [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) or [Amazon VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). [Amazon SQS server-side encryption](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html) helps protect queued messages with [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) keys. [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) orchestrates workflows with execution logging turned on, although IAM permissions remain broad and circuit breakers are not currently in place.  | 
|  3  |  Defined  |  Message-level signing through [AWS KMS asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html#asymmetric-cmks) covers messages that cross trust boundaries or traverse queues and event buses, with separate keys per trust zone. Step Functions state machines are managed as code through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html) or the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions-readme.html), [input validation](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-input-output-processing.html) and [circuit breakers](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html#error-handling-retrying-after-an-error) are in place, and [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) keeps cross-zone traffic on private paths.  | 
|  4  |  Proactive  |  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) with [A2A protocol](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) support structures inter-agent discovery and task delegation, and [Cedar policies](https://docs.cedarpolicy.com/) in [AgentCore Policy](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) enforce trust boundaries at the tool layer. Coordination metrics are captured as [Amazon CloudWatch custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) with baselines, and [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) flags deviations. [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) findings are correlated with coordination logs in [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-what-is.html).  | 
|  5  |  Optimized  |  Trust boundary configurations are continuously validated through [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) managed and [custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html), with alerts on any configuration that creates unauthorized cross-zone connectivity. [AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) feed tool selection accuracy and correctness scores into coordination monitoring as an early-warning layer. Incident response runbooks for coordination anomalies are exercised regularly, and validated patterns are folded back into the organization's reference architecture.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-5"></a>
+  Multi-agent systems are deployed as a single trust zone, so an issue with any one agent can spread laterally across the entire network before the scope is understood. 
+  Teams rely on transport-level encryption for inter-agent traffic and treat message-level signing as unnecessary, which means messages sitting in queues or event buses can't be verified at consumption time. 
+  Orchestrator IAM permissions authorize any principal to start, stop, or modify any workflow in the account, rather than scoping access to the specific state machines each principal needs. 
+  Monitoring covers infrastructure metrics and individual agent health but ignores coordination metrics, so inter-agent message rate spikes, unexpected communication paths, and topology changes go undetected. 
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) findings and coordination logs are treated as separate data streams, leaving investigators without the context to tie an API anomaly to the specific multi-agent workflow it affected. 

**Topics**
+ [Capability intent](#capability-intent-5)
+ [Maturity levels](#maturity-levels-5)
+ [Common issues to watch for](#common-issues-to-watch-for-5)
+ [AGENTSEC06-BP01 Encrypt and sign inter-agent messages](agentsec06-bp01.md)
+ [AGENTSEC06-BP02 Implement workflow orchestration security controls](agentsec06-bp02.md)
+ [AGENTSEC06-BP03 Establish trust boundaries between agents](agentsec06-bp03.md)
+ [AGENTSEC06-BP04 Monitor and detect coordination anomalies](agentsec06-bp04.md)