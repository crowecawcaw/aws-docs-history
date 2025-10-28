# Evaluating compliance status and control

status

The `Compliance.Status` field of the AWS Security Finding Format describes the result of a control
finding. AWS Security Hub CSPM uses the compliance status of control findings to determine an overall
control status. The control status is displayed on the details page of a control on the
Security Hub CSPM console.

## Evaluating the compliance

status of Security Hub CSPM findings

The compliance status for each finding is assigned one of the following values:

- `PASSED` – Indicates that the control passed the security
  check for the finding. This automatically sets the Security Hub CSPM
  `Workflow.Status` to `RESOLVED`.
- `FAILED` – Indicates that the control didn't pass the
  security check for the finding.
- `WARNING` – Indicates that Security Hub CSPM can't determine whether the
  resource is in a `PASSED` or `FAILED` state. For example,
  [AWS Config resource recording](securityhub-setup-prereqs.md#config-resource-recording "securityhub-setup-prereqs.md#config-resource-recording")
  isn't turned on for the corresponding resource type.
- `NOT_AVAILABLE` – Indicates that the check can't be
  completed because a server failed, the resource was deleted, or the result of
  the AWS Config evaluation was `NOT_APPLICABLE`. If the AWS Config evaluation
  result was `NOT_APPLICABLE`, Security Hub CSPM automatically archives the
  finding.

If the compliance status for a finding changes from
`PASSED` to `FAILED`, `WARNING`, or
`NOT_AVAILABLE`, and `Workflow.Status` was either
`NOTIFIED` or `RESOLVED`, Security Hub CSPM automatically changes
`Workflow.Status` to `NEW`.

If you don't have resources corresponding to a control, Security Hub CSPM produces a
`PASSED` finding at the account level. If you have a resource
corresponding to a control but then delete the resource, Security Hub CSPM creates a
`NOT_AVAILABLE` finding and archives it immediately. After 18 hours, you
receive a `PASSED` finding because you no longer have resources corresponding
to the control.

## Deriving control status from compliance status

Security Hub CSPM derives an overall control status from the compliance status of the control findings.
When determining control status, Security Hub CSPM ignores findings that have a
`RecordState` of `ARCHIVED` and findings that have a
`Workflow.Status` of `SUPPRESSED`.

Control status is assigned one of the following values:

- **Passed** – Indicates that all findings have a
  compliance status of `PASSED`.
- **Failed** – Indicates that at least one finding has a
  compliance status of `FAILED`.
- **Unknown** – Indicates that at least one finding has
  a compliance status of `WARNING` or
  `NOT_AVAILABLE`. No findings have a compliance status of `FAILED`.
- **No data** – Indicates that there are no findings for
  the control. For example, a newly enabled control has this status until Security Hub CSPM
  starts to generate findings for it. A control also has this status if all of its
  findings are `SUPPRESSED` or it's unavailable in the current
  AWS Region.
- **Disabled** – Indicates that the control is disabled
  in the current account and Region. No security checks are currently being
  performed for this control in the current account and Region. However, the
  findings of a disabled control may have a value for compliance status for up to
  24 hours after disablement.

For an administrator account, control status reflects the control status for the
administrator account and the member accounts. Specifically, the overall status of a
control appears as **Failed** if the control has one or more failed
findings in the administrator account or any of the member accounts. If you have set an
aggregation Region, the control status in the aggregation Region reflects the control
status in the aggregation Region and the linked Regions. Specifically, the overall
status of a control appears as **Failed** if the control has one or
more failed findings in the aggregation Region or any of the linked Regions.

Security Hub CSPM typically generates the initial control status within 30 minutes after your
first visit to the **Summary** page or the **Security
standards** page on the Security Hub CSPM console. You must have [AWS Config resource recording](controls-config-resources.md "controls-config-resources.md") configured for
the control status to appear. After control statuses are generated for the first time,
Security Hub CSPM updates control statuses every 24 hours based on the findings from the previous 24
hours. A timestamp on the control details page indicates when control status was last
updated.

###### Note

After enabling a control for first time, it can take up to 24 hours for control
statuses to be generated in the China Regions and the AWS GovCloud (US) Region.
