# Finding non-compliant resources

AWS Backup Audit Manager helps you find which resources are non-compliant in two ways.

- When [Viewing framework compliance
  status](viewing-frameworks.md "viewing-frameworks.md"), choose the control name in the **Details section**.
  Doing so takes you to the AWS Config console, where you can view a list of your of your
  `Non-Compliant` resources.
- After you [Create a report plan
  with the resource compliance template](create-report-plan-console.md "create-report-plan-console.md") that includes your framework, you can
  [View
  your report](view-reports.md "view-reports.md") to identify all your `Non-Compliant` resources across
  all your controls.

Furthermore, your `Resource compliance report` shows the last time AWS Backup
Audit Manager last evaluated each of your controls.
