

# COST10-BP01 Perform automation for operations

 Repetitive tasks such as provisioning, configuration, patching, monitoring, and cleanup consume engineering time and introduce errors that raise cost. Automate them to lower operational overhead, make cost control repeatable, and free your teams for higher-value work. 

 **Desired outcome:** 
+  Your routine operational tasks run automatically without manual intervention, including provisioning, configuration, patching, monitoring, and resource cleanup. 
+  Your automation code is version-controlled, tested, and documented, so operations stay reliable as the environment changes. 
+  Your cost visibility improves because automated tracking and reporting run on a defined schedule rather than on demand. 
+  You prioritize automation by value and risk, so the tasks with the highest manual cost or error rate are automated first. 

 **Common anti-patterns:** 
+  Teams run routine operations through manual steps and one-off scripts that live on individual machines. 
+  Automation ships without documentation, tests, or version control, which makes it fragile and hard to maintain. 
+  Organizations automate low-value tasks first because they are easy, leaving the costly, error-prone work manual. 
+  Unused resources accumulate in development and sandbox accounts because no automated process removes them. 

 **Benefits of establishing this best practice:** 
+  Manual effort drops, so engineers spend time on higher-value work instead of repetitive operations. 
+  Cost visibility improves through scheduled, automated tracking and reporting. 
+  Resource use improves because automated scaling and cleanup remove over-provisioned and idle capacity. 
+  Operations become more consistent and repeatable, which lowers the risk of costly human error. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automation is itself a cost. Building, testing, and maintaining it takes engineering time, and poorly built automation can cost more to maintain than the manual work it replaced. Weigh the recurring cost of doing the task manually against the cost to build the automation and the cost to keep it running. 

 Not every task is worth automating. Prioritize by two factors: how much manual effort the task consumes, and how much risk manual work carries. Tasks that repeat often, take a long time, or fail expensively when done wrong give the best return. A rare task that takes five minutes and causes no harm when done wrong rarely justifies automating. Measure the current cost of operations first, including human hours and management overhead, so you can rank candidates by expected benefit. 

 Scripts that live on one engineer's machine disappear when that person leaves. Automation without tests breaks silently when the environment changes, and you cannot review, roll back, or audit automation without version control. Treat automation code the same way you treat application code: store it in source control, test it, and document what it does and why. 

 You don't have to build every automation yourself. Managed operations offerings, professional services, and partner tools can run infrastructure on your behalf or supply pre-built automation for common tasks. This trades a higher direct cost for lower engineering investment and faster adoption. Smaller teams often buy capability they can't staff to build and maintain. Larger teams with infrastructure engineering functions might prefer to build automation that fits their exact requirements. Match the choice to your team's maturity and the value of the task. 

 On AWS, several services support these tasks. [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) define infrastructure as code, so you deploy consistent environments repeatedly. [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) automates configuration, patching, and routine management across fleets. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) run event-driven or scheduled actions. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) evaluates resource configurations against rules, so compliance checks and remediation run continuously. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Measure the current cost of operations:** Inventory the recurring operational tasks your teams perform, and record the time and management overhead each consumes. Rank candidates by the value-and-risk criteria from the guidance, so you automate the costly, error-prone work first. This baseline lets you show the return on each automation investment. 

1.  **Build once and deploy many with infrastructure as code:** Define environments with [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), so you deploy consistent stacks for new environments and disaster recovery scenarios. Publish approved templates through [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html), so teams provision self-service resources within guardrails. Tag resources at deployment so consumption stays traceable. Use [AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/) to size and deploy common enterprise workloads. 

1.  **Automate continuous compliance:** Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to record configurations and evaluate them against your standards, and pair it with [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to manage rules across member accounts. Trigger automated remediation when a resource drifts from the standard: associate an [AWS Systems Manager Automation runbook with each rule](https://docs.aws.amazon.com/config/latest/developerguide/setup-autoremediation.html) so the fix runs when a resource becomes non-compliant, and use the [stack drift rule](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html) to catch environments that have drifted from the template that defines them. This replaces periodic manual audits with continuous checks. 

1.  **Automate monitoring:** Build a monitoring plan that collects data from every part of the workload, so a multi-point failure is faster to diagnose. Configure [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms and automated status checks to report problems without manual polling. Route alerts to the teams that own the affected resources. 

1.  **Automate maintenance and scaling:** Run routine operations on a schedule or in response to events using [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html), [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). Use [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) to match capacity to demand, and [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) to build and patch images. For actions no managed service covers, script them with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) or an AWS SDK. 

1.  **Automate the resource lifecycle:** Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) to centrally manage and automate data protection across data stores. Use [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) to automate creation, retention, and deletion of EBS snapshots and EBS-backed AMIs. Enforce retention policies so backups do not accumulate cost beyond their useful life. 

1.  **Automate cleanup of idle resources:** Identify unused resources with [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html), [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html), and [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html). Reclaim them automatically: Compute Optimizer can apply its [recommended actions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rec.html) for you, and automation rules run them on a recurring schedule when they match criteria you set, snapshotting and deleting EBS volumes that have been unattached for 32 or more days and upgrading previous-generation volume types. Use CloudFormation stack deletion to clean up resources defined in a template. Confirm data is backed up or no longer needed before deletion. 

1.  **Use managed and third-party options where they fit:** For capability you lack the staff to build, evaluate [AWS Professional Services](https://aws.amazon.com/professional-services/), and partner solutions in [AWS Marketplace](https://aws.amazon.com/marketplace). These provide pre-built automation for cost monitoring, compliance, and provisioning, which speeds adoption. Weigh their direct cost against the engineering cost of building and maintaining equivalent automation yourself. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST10-BP02 Use generative AI services and solutions for efficiency](cost10-bp02.md) 
+  [COST06-BP03 Select resource type, size, and number automatically based on metrics](cost06-bp03.md) 
+  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md) 
+  [COST03-BP02 Implement efficient resource lifecycle management](cost03-bp02.md) 

 **Related documents:** 
+  [Modernizing operations in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration) 
+  [AWS services for automation](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/aws-services-for-automation.html) 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [AWS automations for SAP administration and operations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/automations.html) 
+  [AWS Infrastructure & Automation blog](https://aws.amazon.com/blogs/infrastructure-and-automation/) 

 **Related examples:** 
+  [Delete unused Amazon EBS volumes by using AWS Config and AWS Systems Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/) 
+  [Automating Cost Optimization Governance with AWS Config](https://aws.amazon.com/blogs/mt/automating-cost-optimization-governance-with-aws-config/) 
+  [Introducing Automated Amazon EBS Volume Optimization in AWS Compute Optimizer](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-automated-amazon-ebs-volume-optimization-in-aws-compute-optimizer/) 
+  [IT automation with AWS Lambda](https://aws.amazon.com/lambda/) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) 