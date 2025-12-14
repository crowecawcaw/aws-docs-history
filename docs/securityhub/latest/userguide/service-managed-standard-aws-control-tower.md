# Service-Managed Standard: AWS Control Tower

This section provides information about Service-Managed Standard: AWS Control Tower.

## What is Service-Managed Standard: AWS Control Tower?

Service-Managed Standard: AWS Control Tower is a service-managed standard which AWS Control Tower manages that supports a subset of Security Hub controls.
This standard is designed for users of AWS Security Hub CSPM and AWS Control Tower. It lets you configure the detective controls of Security Hub CSPM from the AWS Control Tower service.

Detective controls detect noncompliance of resources (for example, misconfigurations) within your
AWS accounts.

###### Tip

Service-managed standards differ from standards that AWS Security Hub CSPM manages. For
example, you must create and delete a service-managed standard in the managing service. For more
information, see [Service-managed standards in Security Hub CSPM](service-managed-standards.md "service-managed-standards.md").

When you enable a Security Hub CSPM control through AWS Control Tower, Control Tower also enables Security Hub CSPM for you in those specific accounts and Regions, if not already enabled.
In the Security Hub CSPM console and API, you can view Service-Managed Standard: AWS Control Tower alongside other Security Hub CSPM
standards, once the standard is enabled from AWS Control Tower.

For more information about this standard, see [Security Hub CSPM
controls](../../../controltower/latest/userguide/security-hub-controls.md "../../../controltower/latest/userguide/security-hub-controls.md") in the _AWS Control Tower User Guide_.

## Creating the standard

This standard is available in Security Hub CSPM only if you enable Security Hub CSPM controls from AWS Control Tower. AWS Control Tower
creates the standard when you first enable an applicable control by using one of the
following methods:

- AWS Control Tower console
- AWS Control Tower API (call the [`EnableControl`](../../../controltower/latest/APIReference/API_EnableControl.md "../../../controltower/latest/APIReference/API_EnableControl.md") API)
- AWS CLI (run the [`enable-control`](../../../cli/latest/reference/controltower/enable-control.md "../../../cli/latest/reference/controltower/enable-control.md") command)

When you enable a Security Hub CSPM control through AWS Control Tower, if you haven’t already enabled Security Hub CSPM, AWS Control Tower also
enables Security Hub CSPM for you in those specific accounts and Regions.

To identify an Security Hub CSPM control by control ID in Control Catalog, you can use the field `Implementation.Identifier` in AWS Control Tower.
This field maps to Security Hub CSPM control ID and can be used to filter for a specific control ID. To retrieve control metadata for
a specific Security Hub CSPM control (say, "CodeBuild.1") in AWS Control Tower, you can use the [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") API:

`aws controlcatalog list-controls --filter '{"Implementations":{"Identifiers":["CodeBuild.1"],"Types":["AWS::SecurityHub::SecurityControl"]}}'`

You can't view or access this standard in the Security Hub CSPM console, Security Hub CSPM API, or AWS CLI without first setting up AWS Control Tower
and enabling Security Hub CSPM controls from AWS Control Tower using one of the preceding methods.

This standard is only available in the [AWS Regions where AWS Control Tower is
available](../../../controltower/latest/userguide/region-how.md "../../../controltower/latest/userguide/region-how.md").

## Enabling and disabling

controls in the standard

After you've enabled Security Hub CSPM controls through AWS Control Tower and the Service-Managed Standard: AWS Control Tower standard has been created, you can view the standard
and its available controls in Security Hub CSPM.

When Security Hub CSPM adds new controls to the Service-Managed Standard: AWS Control Tower standard, they aren't
automatically enabled for customers who have the standard enabled. You should enable and disable controls for
the standard from AWS Control Tower by using one of the following methods:

- AWS Control Tower console
- AWS Control Tower API (call the [`EnableControl`](../../../controltower/latest/APIReference/API_EnableControl.md "../../../controltower/latest/APIReference/API_EnableControl.md") and [`DisableControl`](../../../controltower/latest/APIReference/API_DisableControl.md "../../../controltower/latest/APIReference/API_DisableControl.md") APIs)
- AWS CLI (run the [`enable-control`](../../../cli/latest/reference/controltower/enable-control.md "../../../cli/latest/reference/controltower/enable-control.md") and [`disable-control`](../../../cli/latest/reference/controltower/disable-control.md "../../../cli/latest/reference/controltower/disable-control.md") commands)

When you change the enablement status of a control in AWS Control Tower, the change is also
reflected in Security Hub CSPM.

However, disabling a control in Security Hub CSPM that's enabled in AWS Control Tower results in control
drift. The control status in AWS Control Tower shows as `Drifted`. You can resolve
this drift by using the [ResetEnabledControl](../../../controltower/latest/APIReference/API_ResetEnabledControl.md "../../../controltower/latest/APIReference/API_ResetEnabledControl.md")
API to reset the control which is in drift, or by selecting
[Re-register OU](../../../controltower/latest/userguide/drift.md#resolving-drift "../../../controltower/latest/userguide/drift.md#resolving-drift") in the AWS Control Tower console,
or by disabling and re-enabling the control in AWS Control Tower using one of the preceding methods.

Completing enablement and disablement actions in AWS Control Tower helps you avoid control
drift.

When you enable or disable controls in AWS Control Tower, the action applies across accounts
and Regions governed by AWS Control Tower. If you enable and disable controls in Security Hub CSPM (not recommended for this
standard), the action applies only to the current account and region.

###### Note

[Central
configuration](central-configuration-intro.md "central-configuration-intro.md") can't be used to manage Service-Managed Standard: AWS Control Tower. You can use _only_
the AWS Control Tower service to enable and disable controls in this standard.

## Viewing enablement status

and control status

You can view the enablement status of a control by using one of the following
methods:

- Security Hub CSPM console, Security Hub CSPM API, or AWS CLI
- AWS Control Tower console
- AWS Control Tower API to see a list of enabled controls (call the [`ListEnabledControls`](../../../controltower/latest/APIReference/API_ListEnabledControls.md "../../../controltower/latest/APIReference/API_ListEnabledControls.md") API)
- AWS CLI to see a list of enabled controls (run the [`list-enabled-controls`](../../../cli/latest/reference/controltower/list-enabled-controls.md "../../../cli/latest/reference/controltower/list-enabled-controls.md") command)

A control that you disable in AWS Control Tower has an enablement status of
`Disabled` in Security Hub CSPM unless you explicitly enable that control in
Security Hub CSPM.

Security Hub CSPM calculates control status based on the workflow status and compliance status of
the control findings. For more information about enablement status and control status,
see [Reviewing the details of controls in
Security Hub CSPM](securityhub-standards-control-details.md "securityhub-standards-control-details.md").

Based on control statuses, Security Hub CSPM calculates a [security score](standards-security-score.md "standards-security-score.md") for Service-Managed Standard: AWS Control Tower. This score is only available in Security Hub CSPM.
In addition, you can only view [control
findings](controls-findings-create-update.md "controls-findings-create-update.md") in Security Hub CSPM. The standard security score and control findings aren't
available in AWS Control Tower.

###### Note

When you enable controls for Service-Managed Standard: AWS Control Tower, Security Hub CSPM may take up to 18 hours to
generate findings for controls that use an existing AWS Config service-linked rule. You
may have existing service-linked rules if you've enabled other standards and
controls in Security Hub CSPM. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md").

## Deleting the standard

You can delete this service managed standard in AWS Control Tower by disabling all applicable controls using
one of the following methods:

- AWS Control Tower console
- AWS Control Tower API (call the [`DisableControl`](../../../controltower/latest/APIReference/API_DisableControl.md "../../../controltower/latest/APIReference/API_DisableControl.md") API)
- AWS CLI (run the [`disable-control`](../../../cli/latest/reference/controltower/disable-control.md "../../../cli/latest/reference/controltower/disable-control.md") command)

Disabling all controls deletes the standard in all managed accounts and governed
Regions in AWS Control Tower. Deleting the standard in AWS Control Tower removes it from the
**Standards** page of the Security Hub CSPM console, and you can no longer
access it by using the Security Hub CSPM API or AWS CLI.

###### Note

Disabling all controls from the standard in Security Hub CSPM doesn't disable or delete the
standard.

Disabling the Security Hub CSPM service removes Service-Managed Standard: AWS Control Tower and any other standards that
you’ve enabled.

## Finding field format for

Service-Managed Standard: AWS Control Tower

When you create Service-Managed Standard: AWS Control Tower and enable controls for it, you'll start to receive
control findings in Security Hub CSPM. Security Hub CSPM reports control findings in the [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").
These are the ASFF values for this standard's Amazon Resource Name (ARN) and
`GeneratorId`:

- **Standard ARN** –
  ``arn:aws:us-east-1`:securityhub:::standards/service-managed-aws-control-tower/v/1.0.0`
- **GeneratorId** –
  `service-managed-aws-control-tower/v/1.0.0/`CodeBuild.1``

For a sample finding for Service-Managed Standard: AWS Control Tower, see [Samples of control findings](sample-control-findings.md "sample-control-findings.md").

## Controls that apply to

Service-Managed Standard: AWS Control Tower

Service-Managed Standard: AWS Control Tower supports a subset of controls that are part of the AWS Foundational Security Best Practices (FSBP) standard.
Choose a control to view information about it, including remediation steps for failed findings.

To see what Security Hub CSPM controls are supported by AWS Control Tower, you can use one of the following
methods:

- AWS Control Catalog console where you can filter for `“Control owner = AWS Security Hub”`
- AWS Control Catalog API (call the [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") API) with filter for `Implementations`
  to check for `Types` is `AWS::SecurityHub::SecurityControl`
- AWS CLI (run the [`list-controls`](../../../cli/latest/reference/controlcatalog/list-controls.md "../../../cli/latest/reference/controlcatalog/list-controls.md") command) with filter for `Implementations`.
  Example CLI command:

`aws controlcatalog list-controls --filter '{"Implementations":{"Types":["AWS::SecurityHub::SecurityControl"]}}'`

Regional limits on Security Hub CSPM controls when enabled through Control Tower standard may not match Regional limits on the underlying controls.

In Security Hub CSPM, if [consolidated control findings](controls-findings-create-update.md#consolidated-control-findings "controls-findings-create-update.md#consolidated-control-findings") is
turned off in your account, the `ProductFields.ControlId` field in the generated findings uses the
standard-based control ID. The standard-based control ID is formatted as
**CT.`ControlId`** (for example,
**CT.CodeBuild.1**).

For more information about this standard, see [Security Hub CSPM
controls](../../../controltower/latest/userguide/security-hub-controls.md "../../../controltower/latest/userguide/security-hub-controls.md") in the _AWS Control Tower User Guide_.
