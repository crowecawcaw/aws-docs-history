

# REL06-BP04 Automate responses to alarms

 Manual response to alarms introduces delay and the chance of human error. When you automate the response to a detected event, systems take corrective action in seconds and apply the same procedure every time. Automated responses range from healing a single failed component to redirecting traffic across Availability Zones or Regions. 

 **Desired outcome:** 
+  You maintain an inventory of the critical real-time alarms in your workload. 
+  Your critical alarms invoke automated corrective actions that maintain service level objectives and agreements. 
+  Your response procedures are documented, whether they run automatically or through operator action. 
+  You detect and can reverse unintended configuration changes. 

 **Common anti-patterns:** 
+  Teams keep no clear inventory or catalog of key real-time alarms. 
+  Teams configure no automated responses for critical alarms, such as scaling when compute nears exhaustion. 
+  Teams define alarm responses that contradict one another. 
+  Teams give operators no standard operating procedures to follow when alerts arrive. 
+  Teams do not monitor configuration changes, so undetected changes cause downtime. 

 **Benefits of establishing this best practice:** 
+  You improve resilience because the system corrects problems without waiting for a person. 
+  You reduce error-prone manual intervention during incidents. 
+  You meet availability goals and reduce service disruption. 
+  You respond consistently, because automation applies the same procedure every time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Without an inventory of critical alarms, you cannot reason about which ones deserve an automated response, and you risk building responses that conflict. Two alarms that each try to act on the same resource can work against each other. For example, one scales a fleet out while another scales it in, or one restarts a component that another has deliberately taken offline. Catalog your alarms first, classify them by criticality and impact, and map each to a single, deliberate response. 

 A *runbook* captures the steps for a routine, well-understood activity. A *standard operating procedure (SOP)* records what an operator does when a specific alert arrives. Examine your runbooks and playbooks to decide which tasks can be automated. If you can define the action precisely, you can usually automate it. Where you cannot, document the manual steps in an SOP and train operators on them. Revisit remaining manual steps as your tooling matures. 

 Treat automation as an ongoing plan. Each incident that requires manual intervention is a candidate for automation, and each new component adds alarms that need a response path. The team that operates the workload owns this plan. Feed it back into your incident review process so that repeated manual toil becomes a backlog item. 

 Several AWS services support automated response. [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) provides predefined and custom runbooks that codify procedures as automation documents. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) reacts to system events by matching them to rules and invoking targets such as AWS Lambda functions. [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) continuously monitors your application's resilience posture. When it detects drift, it generates automated remediation recommendations and runs corrective steps through Systems Manager. [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) applies machine learning to operational metrics to detect anomalous behavior, which shows response gaps you have not yet automated. [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) autonomously correlates alarms, logs, and metrics to diagnose incidents and suggest remediation. It complements rule-based automation for non-routine events that predefined playbooks do not cover. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build an inventory of alarms:** Retrieve every alarm so you can classify and manage them. Use the [describe-alarms](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/describe-alarms.html) command in the AWS CLI, paginating for large sets, or the equivalent SDK call. Record each alarm's criticality and intended response. 

1.  **Document all alarm actions in a runbook:** Update a runbook with every alarm and its action, whether manual or automated, so responses are consistent and free of contradiction. Use the predefined runbooks in [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) as a starting point. 

1.  **Configure automated alarm actions:** For alarms that warrant automation, define the action with the CloudWatch API or SDK, such as changing the state of Amazon EC2 instances. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules to react to system events by invoking targets such as AWS Lambda, EC2 Run Command, or Amazon Kinesis Data Streams. 

1.  **Build SOPs for operator-driven responses:** For alarms that need human judgment, document the procedure as an SOP. Use [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) to codify recovery procedures as automation documents, and use [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) resilience assessments to identify which components need documented response procedures. 

1.  **Detect anomalies with CloudWatch and Resilience Hub:** Enable [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) on key operational metrics to surface anomalous behavior without hand-tuning static thresholds. Use [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) to continuously assess your application's resilience posture and generate automated remediation recommendations. Route anomaly alarms to [EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to drive further automation. 

1.  **Use agentic investigation for non-routine events:** For incidents that fall outside predefined runbooks, use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) to autonomously investigate alarms by correlating signals across CloudWatch metrics, logs, and traces. The agent follows reasoning chains rather than rigid steps, identifies contributing factors, and suggests corrective actions for human approval, reducing mean time to resolution for novel failure modes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 
+  [REL06-BP03 Send notifications with real-time processing and alarming](rel06-bp03.md) 
+  [REL08-BP01 Use runbooks for standard activities such as deployment](rel08-bp01.md) 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 

 **Related documents:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) 
+  [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [Creating your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [What is AWS Resilience Hub?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) 
+  [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Behind the scenes: How AWS drives operational excellence & reliability (COP415)](https://www.youtube.com/watch?v=Z-eo1FMhksg) 
+  [Create Automation Runbooks with AWS Systems Manager \| Amazon Web Services](https://www.youtube.com/watch?v=fQ_KahCPBeU) 
+  [Manage Application Resilience with AWS Resilience Hub, Part 1 \| Amazon Web Services](https://www.youtube.com/watch?v=Hp9waMg2258) 

 **Related examples:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/) 
+  [Amazon CloudWatch and Systems Manager Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US) 