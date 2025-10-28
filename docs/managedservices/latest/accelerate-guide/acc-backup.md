# Continuity management in AMS Accelerate

AMS leverages AWS Backup to centralize and automate the backing up of your data across AWS services.
AMS backup plans provide best practices for various use cases; however, you
are welcome to continue to use your existing backup plans. After you onboard to AMS backup management, AMS provides
backup reports, and AMS experts continuously monitor your backup tasks to ensure you have a reliable backup solution.

To learn more, see
[AWS Backup: How It Works](../../../aws-backup/latest/devguide/how-it-works.md "../../../aws-backup/latest/devguide/how-it-works.md") and
[Supported AWS resources and third-party applications](../../../aws-backup/latest/devguide/whatisbackup.md#supported-resources "../../../aws-backup/latest/devguide/whatisbackup.md#supported-resources").

AMS Accelerate provides a range of operational services to help you achieve operational excellence on AWS.
To gain a quick understanding of how AMS helps your teams achieve overall operational excellence in AWS Cloud with some of our key operational
capabilities including 24x7 helpdesk, proactive monitoring, security, patching, logging and backup, see
[AMS Reference Architecture Diagrams](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf").

###### Topics

- [How continuity management works in AMS](ug-automated-or-manual.md "ug-automated-or-manual.md")
- [Select an AMS backup plan](acc-backup-select-plan.md "acc-backup-select-plan.md")
- [Tag your resources to apply AMS backup plans](acc-backup-assign-plan-resources.md "acc-backup-assign-plan-resources.md")
- [View backups in AMS vaults](acc-backup-ams-vaults.md "acc-backup-ams-vaults.md")
- [AMS backup monitoring and reporting](#acc-backup-report "#acc-backup-report")

## AMS backup monitoring and reporting

###### Important

AMS backup monitoring and reporting are only available in AMS-supported regions. Those are US East (Virginia), US West (N. California), US West (Oregon), US East (Ohio), Canada (Central), South America (São Paulo), EU (Ireland), EU (Frankfurt), EU (London), EU (Paris), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo).

AMS generates daily self-service reports as well as monthly reports on resource coverage and backup job status. The monthly reports are shared in Monthly Business Reviews (MBRs). To learn more about daily backup reports, see [Daily backup report](daily-backup-report.md "daily-backup-report.md").

AMS experts monitor all your backup tasks that are configured using AWS Backup. In case of backup failures, AMS investigates the failure and notifies you with the root cause and remediation options, if available. To avoid alert noise, during events that cause a high number of backup failures in your accounts, AMS makes a collective recommendation, through your CSDM, instead of notifying you for each individual failure.

Note that AMS does not monitor any backups configured using an AWS service’s standalone backup feature.
