

# AGENTSEC09-BP05 Implement runtime threat detection, security event correlation, and automated remediation for agents
<a name="agentsec09-bp05"></a>

 Scanning finds latent weaknesses. Runtime detection catches the attacks happening now. Correlating events across agent interaction surfaces and triggering automated remediation compresses the gap between an active exploit and the response that contains it. 

 **Desired outcome:** 
+  You continually monitor security events from agent activity, correlate them across interaction surfaces, and analyze them for multi-step attack sequences. 
+  You detect active threats targeting agentic systems within minutes, with critical attack sequences surfaced at the highest severity. 
+  Automated remediation workflows trigger containment actions and generate ready-to-implement fixes, reducing mean time to detection and mean time to remediation. 
+  Security teams have a unified view of agent-related threats alongside findings from vulnerability scanning and penetration testing. 

 **Common anti-patterns:** 
+  Treating agent security events in isolation rather than correlating them across interaction surfaces, missing multi-step attack sequences where individual events look benign but together constitute a coordinated attack. 
+  Relying on pre-deployment vulnerability scanning alone without runtime threat detection, leaving a gap where vulnerabilities introduced through configuration drift, new tool integrations, or novel attack techniques go undetected until the next scheduled assessment. 
+  Generating security alerts without automated remediation workflows, creating alert fatigue where security teams are overwhelmed by findings but lack the tooling to act quickly. 
+  Not correlating penetration testing findings with runtime threat detection signals, missing the connection between known vulnerabilities and active exploitation attempts that together provide a high-confidence remediation prioritization signal. 

 **Benefits of establishing this best practice:** 
+  AI/ML-powered event correlation identifies coordinated attacks spanning multiple agent interaction surfaces, time periods, and resources. 
+  Automated workflows trigger containment actions and generate fix recommendations when threats are detected, closing the loop between detection and response. 
+  Centralized findings from vulnerability scanning, penetration testing, and runtime threat detection enable risk-based prioritization across the full threat lifecycle. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Scanning and penetration testing find weaknesses before exploit. Runtime detection catches the exploit as it happens. Both are necessary because neither alone is sufficient. An agentic system adds surface area (tools, APIs, memory stores, other agents) that is exploited through prompt injection chains, credential misuse, data exfiltration sequences, and privilege escalation paths. Detection has to correlate across that surface, not treat each channel in isolation. 

 Deploy Amazon GuardDuty across all accounts where agents operate to provide continuous threat detection for agent IAM roles, API activity, and data access patterns. [GuardDuty Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/) correlates security signals to identify active attack sequences (privilege discovery followed by API manipulation, persistence activities, and data exfiltration) and surfaces them as critical-severity attack sequence findings with natural language summaries, MITRE ATT&CK mapping, and prescriptive remediation recommendations. 

 For agent-specific threat detection, configure GuardDuty monitoring across the data sources most relevant to agentic workloads: 
+  AWS CloudTrail management events for API call patterns 
+  Amazon VPC Flow Logs for network behavior 
+  DNS logs for command-and-control detection 
+  Amazon S3 data events for data access monitoring 

 Enable GuardDuty Runtime Monitoring for compute resources running agent workloads to detect threats at the operating system level, including suspicious process execution and network connections. 

 AWS Security Hub CSPM is the aggregation layer. Findings from Amazon GuardDuty (runtime threats), [AWS Security Agent](https://aws.amazon.com/security-agent/) (vulnerability scanning and penetration testing), Amazon Macie (sensitive data exposure), and Amazon Inspector (software vulnerability scanning) normalize into the AWS Security Finding Format (ASFF) for consistent prioritization and automated response regardless of source. Security Hub CSPM insights correlate penetration testing findings with runtime detection signals, identifying cases where known vulnerabilities are being actively exploited (a high-confidence prioritization signal). 

 Amazon EventBridge rules trigger AWS Lambda functions or AWS Step Functions workflows when high-severity findings are generated. For agent-specific threats, the remediation workflow captures forensic state (agent memory, active sessions, recent tool invocations) to Amazon S3, applies containment actions (credential revocation, network isolation) as described in AGENTSEC07-BP04, generates remediation recommendations based on the finding type, and creates tracked remediation tasks. Findings from AWS Security Agent penetration testing that include suggested code fixes route directly to development teams through the existing remediation tracking workflow. 

 [Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds a complementary detection layer. Continuous evaluation scoring detects behavioral drift that precedes or accompanies security incidents. A sudden drop in safety or correctness scores combined with a GuardDuty finding for the same agent is a high-confidence signal that warrants immediate investigation. Amazon CloudWatch composite alarms triggered when both evaluation score degradation and a GuardDuty finding occur within the same time window surface those cases automatically. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable GuardDuty across agent accounts:** Turn on Amazon GuardDuty with monitoring configured for AWS CloudTrail events, Amazon VPC Flow Logs, DNS logs, Amazon S3 data events, and GuardDuty Runtime Monitoring for agent compute resources. 

1.  **Centralize findings in Security Hub CSPM:** Aggregate findings from Amazon GuardDuty, [AWS Security Agent](https://aws.amazon.com/security-agent/), Amazon Macie, and Amazon Inspector in AWS Security Hub CSPM, and configure Security Hub CSPM insights to correlate penetration testing findings with runtime threat detection signals. 

1.  **Automate containment on high-severity findings:** Use Amazon EventBridge rules and AWS Lambda functions to trigger containment actions and generate fix recommendations when high-severity findings are generated. 

1.  **Combine evaluation drift with GuardDuty findings:** Configure Amazon CloudWatch composite alarms that combine [Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) score degradation with GuardDuty findings to surface high-confidence threat signals. 

1.  **Route fixes to developers and measure MTTR:** Route remediation recommendations, including code fixes from AWS Security Agent, to development teams through a tracked workflow, and monitor mean time to detection and mean time to remediation as key security metrics. 

1.  **Tune detection quarterly:** Review detection rules, remediation workflows, and finding correlation logic quarterly based on observed threat patterns and false positive rates. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html) 
+  [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](agentsec07-bp04.html) 
+  [AGENTSEC09-BP01 Integrate AI-powered vulnerability scanning across the development lifecycle](agentsec09-bp01.html) 
+  [AGENTSEC09-BP02 Conduct context-aware penetration testing with multi-agent attack simulation](agentsec09-bp02.html) 

 **Related documents:** 
+  [Amazon GuardDuty Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/) 
+  [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) 
+  [AWS Security Hub CSPM documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 
+  [Automate cloud security vulnerability assessment and alerting using Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/automate-cloud-security-vulnerability-assessment-and-alerting-using-amazon-bedrock/) 
+  [How government agencies can transform cybersecurity operations with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/publicsector/how-government-agencies-can-transform-cybersecurity-operations-with-amazon-bedrock-agentcore/) 
+  [AWS Security Agent](https://aws.amazon.com/security-agent/) 

 **Related services:** 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Macie](https://aws.amazon.com/macie/) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 