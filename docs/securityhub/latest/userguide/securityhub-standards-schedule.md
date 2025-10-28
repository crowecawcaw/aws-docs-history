# Schedule for running security checks

After you enable a security standard, AWS Security Hub CSPM begins to run all checks within two hours.
Most checks begin to run within 25 minutes. Security Hub CSPM runs checks by evaluating the rule underlying a control.
Until a control completes its first run of checks, its
status is **No data**.

When you enable a new standard, it might take up to 24 hours for Security Hub CSPM to generate findings
for controls that use the same underlying AWS Config service-linked rule as enabled controls from other
enabled standards. For example, if you enable the [Lambda.1](lambda-controls.md#lambda-1 "lambda-controls.md#lambda-1") control
in the AWS Foundational Security Best Practices (FSBP) standard, Security Hub CSPM creates the
service-linked rule and typically generates findings within minutes. After this, if you enable the
Lambda.1 control in the Payment Card Industry Data Security Standard (PCI DSS), it might take up to
24 hours for Security Hub CSPM to generate findings for the control because it uses the same service-linked
rule.

After the initial check, the schedule for each control can be either periodic or change
triggered. For a control that is based on a managed AWS Config rule, the control description includes a
link to the rule description in the _AWS Config Developer Guide_. That
description specifies whether the rule is change triggered or periodic.

## Periodic security checks

Periodic security checks run automatically within 12 or 24 hours after the most recent run. Security Hub CSPM determines the periodicity, and you can't change it.
Periodic controls reflect an evaluation at the moment the check runs.

If you update the workflow status of a periodic control finding, and then in the next check
the compliance status of the finding stays the same, the workflow status remains in its modified
state. For example, if you have a failed finding for the [KMS.4](kms-controls.md#kms-4 "kms-controls.md#kms-4")
control (_AWS KMS key rotation should be enabled_), and then
remediate the finding, Security Hub CSPM changes the workflow status from `NEW` to
`RESOLVED`. If you disable KMS key rotation before the next periodic check, the
workflow status of the finding remains `RESOLVED`.

Checks that use Security Hub CSPM custom Lambda functions are periodic.

## Change-triggered security checks

Change-triggered security checks run when the associated resource changes state. AWS Config lets you
choose between _continuous recording_ of changes in resource state and _daily recording_. If you choose daily recording, AWS Config delivers
resource configuration data at the end of each 24 hour period if there are changes in resource state. If there are no changes, no data
is delivered. This may delay the generation of Security Hub CSPM findings until a 24-hour period is complete. Regardless of your chosen recording
period, Security Hub CSPM checks every 18 hours to ensure no resource updates from AWS Config were missed.

In general, Security Hub CSPM uses change-triggered rules whenever possible. For a resource to use a
change-triggered rule, it must support AWS Config configuration items.
