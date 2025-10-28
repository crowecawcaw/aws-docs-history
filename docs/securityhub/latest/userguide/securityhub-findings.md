# Creating and updating findings in Security Hub CSPM

In AWS Security Hub CSPM, a _finding_ is an observable record of a
security check or security-related detection. A finding can originate from one of the
following sources:

- A security check for a control in Security Hub CSPM.
- An integration with another AWS service.
- An integration with a third-party product.
- A custom integration.
  Security Hub CSPM normalizes findings from all sources into a standard syntax and format called the
  _AWS Security Finding Format (ASFF)_. For detailed information about this
  format, including descriptions of individual ASFF fields, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md"). If
  you enable cross-Region aggregation, Security Hub CSPM also aggregates new and updated findings
  automatically from all linked Regions to an aggregation Region that you specify. For more
  information, see [Understanding cross-Region aggregation in Security Hub CSPM](finding-aggregation.md "finding-aggregation.md").

After a finding is created, it can be updated as follows:

- A finding provider can use the [BatchImportFindings](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") operation of the Security Hub CSPM API to
  update general information about the finding. Finding providers can only update
  findings that they created.
- A customer can use the Security Hub CSPM console or the [BatchUpdateFindings](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md") operation of the Security Hub CSPM API to
  update the status of the investigation into the finding. The
  `BatchUpdateFindings` operation can also be used by a SIEM,
  ticketing, incident management, SOAR, or other type of tool on behalf of a
  customer.
  To reduce finding noise and streamline tracking and analysis of individual findings, Security Hub CSPM
  automatically deletes findings that haven't been updated recently. The timing with which
  Security Hub CSPM does this depends on whether a finding is active or archived:

- An _active finding_ is a finding whose record
  state (`RecordState`) is `ACTIVE`. Security Hub CSPM stores active
  findings for 90 days. If an active finding hasn't been updated for 90 days, it
  expires and Security Hub CSPM permanently deletes it.
- An _archived finding_ is a finding whose record
  state (`RecordState`) is `ARCHIVED`. Security Hub CSPM stores archived
  findings for 30 days. If an archived finding hasn't been updated for 30 days, it
  expires and Security Hub CSPM permanently deletes it.
  For control findings, which are findings that Security Hub CSPM generates from security checks for
  controls, Security Hub CSPM determines whether a finding has expired based on the value for the
  `UpdatedAt` field of the finding. If this value was more than 90 days ago for
  an active finding, Security Hub CSPM permanently deletes the finding. If this value was more than 30
  days ago for an archived finding, Security Hub CSPM permanently deletes the finding.

For all other types of findings, Security Hub CSPM determines whether a finding has expired based on
the values for the `ProcessedAt` and `UpdatedAt` fields of the
finding. Security Hub CSPM compares the values for these fields and determines which is more recent. If
the more recent value was more than 90 days ago for an active finding, Security Hub CSPM permanently
deletes the finding. If the more recent value was more than 30 days ago for an archived
finding, Security Hub CSPM permanently deletes the finding. Finding providers can change the value for
the `UpdatedAt` field of one or more findings by using the [BatchImportFindings](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") operation of the Security Hub CSPM API.

For longer-term retention of findings, you can export findings to an S3 bucket. You can do
this by using a custom action with an Amazon EventBridge rule. For more information, see [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md").

###### Topics

- [BatchImportFindings for finding
  providers](finding-update-batchimportfindings.md "finding-update-batchimportfindings.md")
- [BatchUpdateFindings for
  customers](finding-update-batchupdatefindings.md "finding-update-batchupdatefindings.md")
- [Reviewing finding details and history in
  Security Hub CSPM](securityhub-findings-viewing.md "securityhub-findings-viewing.md")
- [Filtering findings in Security Hub CSPM](securityhub-findings-manage.md "securityhub-findings-manage.md")
- [Grouping findings in Security Hub CSPM](finding-list-grouping.md "finding-list-grouping.md")
- [Setting the workflow status of findings in
  Security Hub CSPM](findings-workflow-status.md "findings-workflow-status.md")
- [Sending findings to a custom Security Hub CSPM action](findings-custom-action.md "findings-custom-action.md")
- [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md")
