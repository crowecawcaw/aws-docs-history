# AWS Backup Audit Manager

You can use AWS Backup Audit Manager to audit the compliance of your AWS Backup policies against
controls that you define. A _control_ is a procedure designed to audit the
compliance of a backup requirement, such as the backup frequency or the backup retention period.

AWS Backup Audit Manager helps you answer questions such as:

- "Am I backing up all my resources?"
- "Are all of my backups encrypted?"
- "Are my backups taking place daily?"
  You can use AWS Backup Audit Manager to find backup activity and resources that are not yet
  compliant with the controls that you defined. Note that only active resources will be included
  when controls evaluate resources for compliance. For example, an Amazon EC2 instance in a running state
  will be evaluated. An EC2 instance in a stopped state will not be included in the compliance
  evaluation.

You can also use it to automatically generate an
audit trail of daily and on-demand reports for your backup governance purposes.

The following steps provide an overview of how to use AWS Backup Audit Manager. For detailed
walkthroughs, choose one of the topics at the end of this page.

1. Create frameworks that contain one or more governance control templates. The preceding
   questions are examples of three governance control templates. You can customize the
   parameters of some governance control templates. For example, you can customize the last
   control to ask, “Are my backups taking place weekly?” instead of daily.
2. View your framework to see how many of your resources are compliant (or non-compliant)
   with the controls you defined in that framework.
3. Create reports of your backup and compliance status. Store these reports as demonstrable
   evidence of your compliance practices, or to identify individual backup activities and
   resources that are not yet in compliance.

AWS Backup Audit Manager automatically generates a new report for you every 24 hours and
publishes it to Amazon S3. You can also generate on-demand reports.

###### Note

Before you create your first compliance-related framework, you must turn on resource
tracking. Doing so allows AWS Config to track your AWS Backup resources. For technical documentation
about how to manage resource tracking, see [Setting up AWS Config with the console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md")
in the _AWS Config Developer Guide_.

Charges apply when you turn on resource tracking. For information about resource tracking
pricing and billing for AWS Backup Audit Manager, see [Metering, costs, and
billing](metering-and-billing.md "metering-and-billing.md").

###### Topics

- [Working with audit frameworks](working-with-audit-frameworks.md "working-with-audit-frameworks.md")
- [Working with audit reports](working-with-audit-reports.md "working-with-audit-reports.md")
- [Using AWS Backup Audit Manager with CloudFormation](bam-cfn-integration.md "bam-cfn-integration.md")
- [Using AWS Backup Audit Manager with
  AWS Audit Manager](aws-audit-manager-integration.md "aws-audit-manager-integration.md")
- [Controls and
  remediation](controls-and-remediation.md "controls-and-remediation.md")
