# Setting the workflow status of findings in

Security Hub CSPM

Workflow status tracks the progress of your investigation into a finding. Workflow
status is specific to an individual finding and doesn't affect generation of new findings.
For example, if you change the workflow status of a finding to `SUPPRESSED` or
`RESOLVED`, your change doesn't prevent Security Hub CSPM from generating a new finding
for the same issue.

The workflow status of a finding can be one of the following values.

**NEW**

The initial state of a finding before you review it.

Findings that are ingested from integrated AWS services, such as AWS Config, have `NEW` as their initial status.

Security Hub CSPM also resets the workflow status from either `NOTIFIED` or
`RESOLVED` to `NEW` in the following cases:

- `RecordState` changes from `ARCHIVED` to
  `ACTIVE`.
- `Compliance.Status` changes from `PASSED` to `FAILED`,
  `WARNING`, or `NOT_AVAILABLE`.

These changes imply that additional investigation is required.

**NOTIFIED**

Indicates that you notified the resource owner about the security issue. You can use this
status when you are not the resource owner, and you need intervention from the resource owner
in order to resolve a security issue.

If one of the following occurs, the workflow status is changed automatically from
`NOTIFIED` to `NEW`:

- `RecordState` changes from `ARCHIVED` to
  `ACTIVE`.
- `Compliance.Status` changes from `PASSED` to `FAILED`,
  `WARNING`, or `NOT_AVAILABLE`.

**SUPPRESSED**

Indicates that you reviewed the finding and do not believe that any action is
needed.

The workflow status of a `SUPPRESSED` finding does not change if
`RecordState` changes from `ARCHIVED` to
`ACTIVE`.

**RESOLVED**

The finding was reviewed and remediated and is now considered resolved.

The finding remains `RESOLVED` unless one of the following occurs:

- `RecordState` changes from `ARCHIVED` to
  `ACTIVE`.
- `Compliance.Status` changes from `PASSED` to `FAILED`,
  `WARNING`, or `NOT_AVAILABLE`.

In those cases, the workflow status is automatically reset to `NEW`.

For findings from controls, if `Compliance.Status` is
`PASSED`, Security Hub CSPM automatically sets the workflow status to
`RESOLVED`.

## Setting the workflow status of findings

To change the workflow status of one or more findings, you can use the Security Hub CSPM console
or the Security Hub CSPM API. If you change the workflow status of a finding, note that it can take
several minutes for Security Hub CSPM to process your request and update the finding.

###### Tip

You can also change the workflow status of findings automatically by using
automation rules. With automation rules, you configure Security Hub CSPM to automatically update
the workflow status of findings based on criteria that you specify. For more
information, see [Understanding automation rules in Security Hub CSPM](automation-rules.md "automation-rules.md").

To change the workflow status of one or more findings, choose your preferred
method and follow the steps.

Security Hub CSPM console

###### To change the workflow status of findings

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, do one of the following to display a
   table of findings:
   - Choose **Findings**.
   - Choose **Insights**. Then choose an
     insight. In the insight results, choose a result.
   - Choose **Integrations**. Then, in the
     section for the integration, choose **See
     findings**.
   - Choose **Security standards**. Then,
     in the section for the standard, choose **View
     results**. In the table of controls, choose a
     control to display findings for the control.

3. In the findings table, select the check box for each finding
   whose workflow status you want to change.
4. At the top of the page, choose **Workflow
   status**, and then choose the new workflow status for
   the selected findings.
5. In the **Set workflow status** dialog box,
   optionally enter a note that details the reason for changing the
   workflow status. Then choose **Set status**.

Security Hub CSPM API
Use the [BatchUpdateFindings](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md") operation. Provide both the finding ID and
the ARN of the product that generated the finding. You can get these details
by using the [GetFindings](../../1.0/APIReference/API_GetFindings.md "../../1.0/APIReference/API_GetFindings.md") operation.

AWS CLI
Run the [batch-update-findings](../../../cli/latest/reference/securityhub/batch-update-findings.md "../../../cli/latest/reference/securityhub/batch-update-findings.md") command. Provide both the finding ID and
the ARN of the product that generated the finding. You can get these details
by running the [get-findings](../../../cli/latest/reference/securityhub/get-findings.md "../../../cli/latest/reference/securityhub/get-findings.md") command.

```
batch-update-findings --finding-identifiers Id="`<findingID>`",ProductArn="`<productARN>`" --workflow Status="`<workflowStatus>`"
```

**Example**

```
aws securityhub batch-update-findings --finding-identifiers Id="arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",ProductArn="arn:aws:securityhub:us-west-1::product/aws/securityhub" --workflow Status="RESOLVED"
```
