

# REL12-BP01 Use playbooks to investigate failures

 A playbook guides responders through detecting, analyzing, containing, and resolving a failure scenario. Playbooks shorten the time to diagnose an incident and make investigations repeatable. 

 **Desired outcome:** 
+  You maintain a living collection of playbooks that give step-by-step guidance for investigating known failure scenarios. 
+  Your playbooks include clear escalation paths and decision points, so responders know when to act and when to hand off. 
+  Your investigation data, logs, and metrics are retained long enough to support analysis of both current and historical incidents. 
+  You update playbooks after each incident, and high-value procedures run as automation rather than manual steps. 

 **Common anti-patterns:** 
+  Teams wait until an incident occurs to document how to investigate it. 
+  Investigation depends on tribal knowledge held by a few experienced engineers. 
+  Playbooks exist but sit as static documents that no one revises as new scenarios appear. 
+  Teams keep every playbook as a manual procedure, even where automation would be faster and more reliable. 
+  Logs and metrics are collected only after an incident starts, with no predefined monitoring strategy. 
+  Data is retained for too short a period, which prevents historical analysis. 

 **Benefits of establishing this best practice:** 
+  Mean time to resolution drops because responders follow a known path instead of improvising. 
+  Investigation quality stays consistent regardless of who responds. 
+  Knowledge is captured and reused, so the same failure is diagnosed faster the second time. 
+  Automated playbooks reduce human error during high-pressure incidents. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A runbook automates a routine task with a predictable result, such as a deployment. A playbook guides investigation of a non-routine event with unknown cause. 

 When investigation depends on the memory of a few engineers, response quality varies with who is on call. Documented investigation processes remove that variance. They also capture experienced responders' reasoning in a form the whole team can apply. This matters most for rare, high-severity events that no one investigates often enough to remember well. 

 A playbook can be a written document, executable code, or an agentic investigation. A written document is fast to create and easy to change, but depends on responders interpreting each step correctly under pressure. Automation reduces manual error and speeds diagnosis, but costs more to build and maintain. An agentic approach uses [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) to autonomously correlate signals, form hypotheses, and recommend actions for non-routine events without a predefined playbook. Start with written playbooks, then convert high-frequency or high-risk procedures to code over time. Use agentic investigation to augment responders for novel or complex incidents. [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runs predefined steps through Automation and Run Command. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) automates individual investigation actions. [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) identifies resilience gaps and recommends improvements to your runbooks. 

 If you retain logs and metrics for too short a period, historical analysis becomes impossible and recurring failures look like isolated events. Decide retention periods before an incident. Use event-driven triggers to start investigations automatically when conditions match a known scenario. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) alarms detect the condition, and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) routes the event to automation that runs the initial response steps. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify the scenarios that need a playbook:** List the failures that warrant a documented investigation process. Include anticipated events such as an unavailable service dependency, performance degradation, capacity limits, and component failures. Include known reliability findings and alerts, so that when an alert fires, responders have clear steps and do not ignore or mishandle it. 

1.  **Define a consistent playbook structure:** Give every playbook the same shape so responders can navigate it under pressure. Include an overview of the scenario and goal, prerequisites such as required monitoring and expected notifications, and communication and escalation contacts with their responsibilities. Add response steps that walk through detection, analysis, containment, resolution, and recovery, each with its expected outcome. 

1.  **Implement high-value playbooks as code:** Convert the procedures you run most often or that carry the most risk into automation. Use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) and [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) to run predefined steps, and use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) for custom investigation actions. Compose complex playbooks from several scripts, each representing one investigation step. 

1.  **Connect playbooks to monitoring and event-driven triggers:** Wire playbooks to your detection and alerting so investigations start quickly. Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) alarms to detect conditions and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to initiate the response automatically. Confirm that data retention supports investigation of past incidents, not just live ones. 

1.  **Keep playbooks living:** Treat playbooks as version-controlled artifacts that evolve with your workload. After each unplanned incident, document what responders did and fold those steps into an existing or new playbook. Over time this builds a tested library of investigation procedures. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL12-BP02 Perform post-incident analysis](rel12-bp02.md) 
+  [REL12-BP05 Conduct game days regularly](rel12-bp05.md) 
+  [REL08-BP01 Use runbooks for standard activities such as deployment](rel08-bp01.md) 
+  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 

 **Related documents:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) 
+  [What is AWS Resilience Hub?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
+  [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) 

 **Related examples:** 
+  [GitHub - aws-samples/aws-customer-playbook-framework: This repository provides sample templates for security playbooks against various scenarios when using Amazon Web Services.](https://github.com/aws-samples/aws-customer-playbook-framework) 
+  [GitHub - aws-samples/aws-incident-response-playbooks](https://github.com/aws-samples/aws-incident-response-playbooks) 