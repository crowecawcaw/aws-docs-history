# Offboard from AMS Accelerate

AMS Accelerate provides an easy way to operate an enterprise-class operating environment. And, AMS Accelerate provides the supporting
infrastructure operations model for AWS migration and usage. However, after using AMS Accelerate, you might decide to in-source, or
re-assign AWS infrastructure operations responsibilities to other teams. To do this, you must offboard your accounts from the AMS service.

When you offboard an account from AMS Accelerate, AMS transfers all the responsibilities defined in our service description back to you.
For example, you won't have the ability to cut incidents or service requests to AMS. Similarly, our operations
engineers and automation will no longer have access to your Accelerate accounts, preventing us from remediating health, availability, and
security and compliance findings. Your AWS workloads can continue to run in the same accounts that AMS was operating.

The team that will be performing your infrastructure operations services going forward must be included to define what people, tools, and
processes you will use after your Accelerate offboarding. AMS leaves some of the AMS tooling such as guardrails and logs to allow the development
of a "to be" operating environment and model. Review the following documentation carefully to understand the tools that you can continue
using and how to request to offboard an account.

## AMS Accelerate offboarding effects

While preparing to offboard from Accelerate, keep the following considerations in mind.

- **Access**: The `ams-access-management` AWS CloudFormation stack that defines the `ams-access-management` AWS Identity and Access Management role isn't deleted.
  After offboarding, these resources remain, but are unused by other components that are left behind. You can delete the stack and role at your convenience.
- **AMS resource retention**: After offboarding, some AMS resources remain in your account. To see which resources are retained and what you can
  do with them, see the

[`resource_inventory.zip`](samples/resource_inventory3.md "samples/resource_inventory3.md") spreadsheet (compressed).

- **Automation**: After offboarding, the AMS-curated AWS SSM automation runbooks, and AWS Lambda functions, are
  no longer available.
- **Backup management**: AMS uses backup management to take snapshots of your resources. After offboarding, you can continue using the
  backup schedules, frequency, and retention periods defined on AWS Backup except for the AMS backup plans; see [Select an AMS backup plan](acc-backup-select-plan.md "acc-backup-select-plan.md"). The AWS Identity and Access Management resources created by AMS Backup Orchestrator are removed, but not the AMS-authored backup vaults
  and corresponding AWS KMS key. Accelerate no longer monitors the backup jobs or performs restoration actions during incidents.
- **Cost optimization**: After offboarding, AMS Resource Scheduler is deleted. AMS Resource Scheduler helps
  you reduce operational costs by stopping the resources that are not in use and starting them back when their capacity is needed. AMS does not
  continue providing cost optimization recommendations. For details on Resource Scheduler, see
  [Cost optimization with AMS Resource Scheduler](acc-resource-scheduler.md "acc-resource-scheduler.md").
- **Designated experts**: After offboarding, your designated Cloud Service Delivery Manager (CSDM) and a Cloud Architect (CA)
  no longer provide guidance, report about, or drive operational and security excellence for your off-boarded Accelerate accounts.
- **Incident management**: Incident management is the process the AMS service uses to respond to your reported incidents.
  After offboarding, Accelerate no longer detects and responds to incidents, or assists your team in resolving issues.
  You will not be able to exchange incident and service request communications with Accelerate and Accelerate console access
  for your Accelerate accounts is deactivated.
- **Logging and Reporting**: After offboarding, you retain the logs stored as a result of CloudWatch, CloudTrail, and VPC Flow Logs.
  You can leave the configuration of those services as-is to continue generating logs; however, AMS no longer monitors such configurations.
  Accelerate no longer provides the monthly service report that summarizes key performance metrics of AMS. You retain the data generated from
  Self-Service Reporting (SSR) (see [Self-service reports](self-service-reporting.md "self-service-reporting.md")), but Accelerate does not
  generate new ones.
- **Monitoring**: Monitoring is the process the AMS service uses to track your resources.
  During offboarding, AMS removes AMS-specific tools, such as Alarm Manager and Resource Tagger, and any
  EventBridge event rules and CloudWatch alarms that AMS deployed as part of the AMS monitoring baseline.
  Accelerate will no longer respond to alarms or configure new ones after offboarding. For details on Alarm Manager and Resource Tagger,
  see [Tag-based Alarm Manager](acc-mem-tag-alarms.md "acc-mem-tag-alarms.md") and
  [Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").
- **Operations tools**: AMS Accelerate can provide ongoing operations for your workload's infrastructure in AWS.
  After offboarding an Accelerate account you no longer have access to tools like Resource Tagger to help you tag your resources based on rules,
  or automated instance configuration to install required agents in your EC2 instances. CloudWatch and SSM Agents on instances are left in place with
  existing configurations. The `AMSOSConfigurationCustomerInstanceRole` IAM profile and the `AMSInstanceProfileBasePolicy`
  are detached from your instances and be removed from your Accelerate accounts.
- **Patch management**: Patch management is the process the AMS service uses to update your EC2 instances.
  After offboarding, AMS no longer creates a snapshot of the instance prior to patching, no longer installs and monitors the patch installation,
  and no longer notifies you of the outcome. You retain the Patch baselines and snapshots created in the past. Additionally, the configuration
  of your patch maintenance windows remains but the patches are no longer installed by Accelerate.
- **Problem management**: After offboarding, Accelerate no longer performs analysis to identify and investigate problems and to
  identify the root cause.
- **Security**: Security management is the process the AMS service uses to protect your resources.
  After offboarding, you keep your Amazon GuardDuty detector and findings, and any AWS Config rules that you created. AWS Config rules deployed by Accelerate are removed. Accelerate no longer
  monitors, remediates, or reports on the findings from these tools.
- **Service termination date**: The service termination date is the last day of the calendar month following the end of the 30 days requisite termination notice period. If the end of the requisite termination notice period falls after the 20th day of the calendar month, then the service termination date is the last day of the following calendar month. The following are example scenarios for termination dates.
  - If the termination notice is provided on April 12, then the 30 days notice ends on May 12. The service termination date is May 31.
  - If a termination notice is provided on April 29, then the 30 days notice ends on May 29. The service termination date is June 30.

## Offboarding from AMS Accelerate with dependencies on Alarm Manager and Resource Tagger

Customized AWS CloudFormation stacks that deploy configurations related to Alarm Manager or Resource Tagger, along with the AMS-supplied Alarm Manager and Resource Tagger configuration stacks, remain in your account when you offboard from AWS Managed Services.

To delete the AMS configuration stacks during the offboarding process, you must remove any dependencies and references on Alarm Manager or Resource Tagger from the custom CloudFormation templates before you initiate the offboarding process. Removing the references helps make sure that the stacks are properly removed from your account when you offboard from AMS.

###### Important

Carefully review your CloudFormation templates and remove any references to Alarm Manager and Resource Tagger before you start the offboarding process. Failure to do so might result in the retention of these stacks in your account, even after you offboard from AMS. Note that while these stacks contain configuration information specific to Alarm Manager and Resource Tagger, their presence doesn't incur ongoing charges or fees.

## Getting offboarding assistance for an Accelerate account

AMS offboards your account after receiving at least 30 days notice through a AMS Account Service Termination Request. The Service Termination Date is
the last day of the calendar month following the end of the 30 days requisite termination notice period; provided that, if the end of the requisite
termination notice period falls after the 20th day of the calendar month, the Service Termination Date will be the last day of the following calendar month.

To request off-boarding an account you must:

1. Submit a formal request to offboard the account using a service request. One service request (SR) documenting
   all of the accounts you want to offboard, or one SR per account.

In the request, provide the list of account IDs to offboard, the reason for offboarding, and any additional considerations. 2. Inform your CSDM about the accounts you want to offboard and request their help executing the offboarding process.
