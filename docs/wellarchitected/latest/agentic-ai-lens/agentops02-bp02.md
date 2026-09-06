

# AGENTOPS02-BP02 Implement configuration drift detection and remediation
<a name="agentops02-bp02"></a>

 Configurations can drift, creating outdated or unstable versions over time. For example, a manual tweak in one environment, a guardrail flag changed during an incident, or an experimental override never reverted can produce agents that behave differently in production than in testing. Automated drift detection catches these events before they turn into incidents. 

 **Desired outcome:** 
+  Agent configurations stay consistent with approved baselines across every environment. 
+  Unauthorized or unintended changes are detected and remediated automatically. 
+  Every configuration change follows a documented approval workflow with a full audit trail. 
+  Cross-environment consistency is validated continually so development, staging, and production don't drift apart. 

 **Common anti-patterns:** 
+  Managing agent configurations through manual console changes without version control, making it impossible to track what changed, when, and by whom. 
+  Allowing different environments to drift apart without automated consistency checks, so agents behave differently in production than in testing. 
+  Detecting configuration drift only after it causes a production incident rather than through proactive monitoring. 
+  Treating behavioral configurations (system prompts, guardrail settings) as low-risk and skipping approval workflows for changes that fundamentally alter agent behavior. 

 **Benefits of establishing this best practice:** 
+  Automated drift detection helps keep agent configurations inside approved boundaries continually, supporting audit requirements and reducing the risk of unauthorized behavioral change. 
+  Configuration monitoring provides visibility beyond runtime metrics, exposing issues at the configuration layer before they manifest as behavioral problems. 
+  Cross-environment consistency validation helps detect failures that passed in testing or staging environments by detecting divergence between environments early. 
+  Change events are captured with full attribution, making root-cause analysis faster when incidents do occur. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 First, determine your source of truth for configuration. If approved baselines live in a wiki, a shell history, or in the AWS console, then drift detection has nothing to compare against. Storing baselines as infrastructure as code (IaC) in [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) gives every deployment a reproducible reference point and makes the IaC definition the single artifact that authoritatively determines what resources should look like. 

 [AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) reveals when deployed resources have diverged from their stack definitions. [AWS Config](https://aws.amazon.com/config/) rules add the runtime layer, monitoring agent infrastructure continuously and triggering automated remediation when deviations appear. [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) captures every configuration change event with full attribution, so when drift is detected, the team can determine exactly how a change was made without reconstructing events. 

 Behavioral configurations, system prompts, guardrail settings, tool permissions, and decision boundaries need a parallel track because they don't consistently sit in CloudFormation-manageable resources. A versioned configuration store with strict access controls and change notifications handles this layer. Production changes should require documented justification and sign-off. 

 The goal isn't to slow teams down but to send a prompt adjustment that alters downstream behavior through the same review as a code change. Teams using steering files in Kiro or equivalent can codify configuration standards so drift is less likely to be introduced at the source. 

 Scheduled cross-environment validation catches the slow category of drift that single-event detection misses. Snapshot the configuration of each environment on a cadence, compare the snapshots, and alert on any discrepancy that isn't explained by an approved change. This check reveals drift that accumulated gradually over months rather than arriving in a single event. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define configuration baselines as IaC:** Store agent infrastructure definitions in [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) under version control, with the IaC definition as the single source of truth. 

1.  **Configure drift detection:** Use [AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) for infrastructure and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rules for agent-specific configurations (guardrail settings, model parameters) against approved baselines. 

1.  **Enable change event capture with full attribution:** Turn on [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and route change events to alerting and automated remediation workflows. 

1.  **Version behavioral configurations:** Store prompts, guardrail settings, and decision boundaries in a versioned configuration store with access controls and mandatory approval workflows for production changes. 

1.  **Validate cross-environment consistency on a schedule:** Compare configuration snapshots across development, staging, and production, and alert on unexplained discrepancies. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs](agentops02-bp01.html) 
+  [AGENTOPS02-BP03 Implement agent behavior versioning and rollback capabilities](agentops02-bp03.html) 
+  [AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance](agentops03-bp01.html) 
+  [AGENTREL08-BP01 Establish consistent configuration management practices](agentrel08-bp01.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Guidance for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/) 
+  [Kiro Steering](https://kiro.dev/docs/steering/) 
+  [Evolving software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Architecting scalable and secure agentic AI with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc) 

 **Related examples:** 
+  [GitHub: Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform) 

 **Related services:** 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 