# Understanding security checks and

scores in Security Hub CSPM

For each control that you enable, AWS Security Hub CSPM runs security checks. A security check produces a finding that tells you whether
a specific AWS resource is in compliance with the rules that the control includes.

Some checks run on a periodic schedule. Other checks only run when there is a change to the
resource state. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md").

Many security checks use AWS Config managed or custom rules to establish the compliance requirements. To run
these checks, you must set up AWS Config and turn on resource recording for required resources. For more information on setting up AWS Config, see [Enabling and configuring AWS Config for Security Hub CSPM](securityhub-setup-prereqs.md "securityhub-setup-prereqs.md").
For a list of AWS Config resources that you must record for each standard, see [Required AWS Config resources for control
findings](controls-config-resources.md "controls-config-resources.md"). Other controls use custom Lambda functions, which are managed by Security Hub CSPM and don't require any prerequisites.

As Security Hub CSPM runs security checks, it generates findings and assigns them a compliance status. For more information about
compliance status, see [Evaluating the compliance
status of Security Hub CSPM findings](controls-overall-status.md#controls-overall-status-compliance-status "controls-overall-status.md#controls-overall-status-compliance-status").

Security Hub CSPM uses the compliance status of control findings to determine an overall control status. Based on the control status, Security Hub CSPM also calculates a security score
across all enabled controls and for specific standards. For more information, see [Evaluating compliance status and control
status](controls-overall-status.md "controls-overall-status.md") and [Calculating security scores](standards-security-score.md "standards-security-score.md").

If you've turned on
consolidated control findings, Security Hub CSPM generates a single finding even when a control is associated with more than one standard.
For more information, see [Consolidated control findings](controls-findings-create-update.md#consolidated-control-findings "controls-findings-create-update.md#consolidated-control-findings").

###### Topics

- [Required AWS Config resources for control
  findings](controls-config-resources.md "controls-config-resources.md")
- [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md")
- [Generating and updating control findings](controls-findings-create-update.md "controls-findings-create-update.md")
- [Evaluating compliance status and control
  status](controls-overall-status.md "controls-overall-status.md")
- [Calculating security scores](standards-security-score.md "standards-security-score.md")
