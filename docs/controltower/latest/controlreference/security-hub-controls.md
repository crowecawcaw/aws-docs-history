# The Security Hub CSPM standard

AWS Control Tower is integrated with AWS Security Hub CSPM to provide detective controls that help you
monitor your AWS environment. The integration is accomplished with a Security Hub CSPM standard,
called the **Service-Managed Standard: AWS Control Tower**.

The **Service-Managed Standard: AWS Control Tower** supports a subset of controls
in the **AWS Foundational Security Best Practices (FSBP)** standard. To
learn more about this standard and to view the available controls, see [Service-Managed Standard: AWS Control Tower](../../../securityhub/latest/userguide/service-managed-standard-aws-control-tower.md#aws-control-tower-standard-controls "../../../securityhub/latest/userguide/service-managed-standard-aws-control-tower.md#aws-control-tower-standard-controls"). For more general information about Security Hub CSPM
standards, see [Security standards and
controls in Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-standards.md "../../../securityhub/latest/userguide/securityhub-standards.md"), in the _AWS Security Hub User
Guide_.

This standard is available only for AWS Control Tower customers who have created the standard in
the AWS Control Tower console. AWS Control Tower creates the standard for you when you enable the first Security Hub CSPM
control in the AWS Control Tower console. When you enable the first control, if you haven’t already
enabled Security Hub CSPM, AWS Control Tower also enables Security Hub CSPM for you.

After you create this standard, you can view the Security Hub CSPM detective controls alongside other
AWS Control Tower controls, in the AWS Control Tower console and in Security Hub CSPM.

###### Control behavior

- No controls are enabled automatically when you create this standard in
  AWS Control Tower.
- The Security Hub CSPM controls are active at the OU level only, not for all AWS Control Tower OUs (if
  not enabled for all), and not for individual accounts.

## Find Security Hub CSPM Controls in AWS Control Tower

To see what Security Hub CSPM controls are supported by AWS Control Tower, you can use one of the following methods:

- AWS Control Tower console where you can filter for `"Control owner = AWS Security Hub"`
- AWS Control Catalog API (call the [ListControls](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") API) with a filter for `Implementations.Types` set to `AWS::SecurityHub::SecurityControl`
- AWS CLI (run the [list-controls](../../../cli/latest/reference/controlcatalog/list-controls.md "../../../cli/latest/reference/controlcatalog/list-controls.md") command) with a filter for `Implementations.Types` set to `AWS::SecurityHub::SecurityControl`. Example CLI command:

```
aws controlcatalog list-controls --filter '{"Implementations":{"Types":["AWS::SecurityHub::SecurityControl"]}}'
```

To identify a Security Hub CSPM control by control ID in AWS Control Tower, you can use the field `Implementation.Identifier`. This field maps to Security Hub CSPM control ID and can be used to filter for a specific control ID. To retrieve control metadata for a specific Security Hub CSPM control (say, "CodeBuild.1") in AWS Control Tower, you can use the [ListControls](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") API:

```
aws controlcatalog list-controls --filter '{"Implementations":{"Identifiers":["CodeBuild.1"],"Types":["AWS::SecurityHub::SecurityControl"]}}'
```

## Enable or remove controls for the

Service-Managed Standard

To avoid drift, always enable and remove controls for the Service-Managed Standard by
means of the AWS Control Tower service, either in the console or by calling the AWS Control Tower APIs,
`EnableControl` and `DisableControl`. When you change the
enablement status of a control in AWS Control Tower, the change also is reflected in
Security Hub CSPM.

If you deactivate a Service-Managed Standard control by means of the Security Hub CSPM
console, the AWS Control Tower member account enters a state of control drift. In this
situation, AWS Control Tower is not receiving the Security Hub CSPM findings for the control that you
deactivated. You must resolve this drift before AWS Control Tower can apply the control
successfully to your registered organizational units and member accounts.

You can delete this standard in the AWS Control Tower console by deactivating all controls in
the standard. This deletes the standard for all managed accounts and governed Regions in
AWS Control Tower. Deleting the standard does not deactivate Security Hub CSPM for your account.

The control named **[SH.S3.4] S3 buckets should have server-side encryption
enabled** is deprecated, effective July 18, 2023. It was removed from
the controls library on August 18, 2023. For more information, see [AWS Control Tower deprecates two controls](../userguide/2023-all.md#deprecate-2controls "../userguide/2023-all.md#deprecate-2controls").

The control named **[SH.RDS.18] RDS instances should be deployed in a
VPC** is deprecated, effective April 28, 2025, and is to be removed from the Control Catalog.

## Security Hub CSPM score and findings

Based on control status, Security Hub CSPM calculates a security score for the
**Service-Managed Standard: AWS Control Tower**. This security score and the
control findings are available only in Security Hub CSPM. These items aren't available in
AWS Control Tower.

###### Note

When you create **Service-Managed Standard: AWS Control Tower** and enable
controls for it, Security Hub CSPM may take up to 18 hours to generate findings for controls
that use the same underlying AWS Config service-linked rule as controls from other enabled
Security Hub CSPM standards. For more information, see [Schedule
for running security checks](../../../securityhub/latest/userguide/securityhub-standards-schedule.md "../../../securityhub/latest/userguide/securityhub-standards-schedule.md") in the AWS Security Hub CSPM User Guide.

## Security Hub CSPM control drift reporting

When reporting drift for controls that are part of the AWS Security Hub CSPM Service-Managed Standard,
AWS Control Tower receives a daily status update from Security Hub CSPM. If no update is received, AWS Control Tower
verifies whether drift has occurred. If so, AWS Control Tower reports drift. If a control shows
drift, AWS Control Tower sends an Amazon SNS notification to the
AWS Control Tower `security-aggregate-notification` channel. You must subscribe to
this SNS notification to receive information about which specific account is affected by
Security Hub CSPM control drift. For more information about Security Hub CSPM control drift in AWS Control Tower, see
[Security Hub control drift](../userguide/governance-drift.md#sh-control-drift "../userguide/governance-drift.md#sh-control-drift").

Although controls are active in every governed Region, AWS Control Tower sends the AWS Security Hub CSPM
**Finding** events to the AWS Control Tower home Region only.

**Remediate drift**

When drift is reported, you can remediate the situation by choosing
**Re-register OU** on the **Organizations** page
in the AWS Control Tower console, or by deactivating and re-activating the control that's in a
drifted state, either by means of the console, or through the AWS Control Tower API.

You can enable and manage some Security Hub CSPM controls from AWS Control Tower, with the [Security Hub CSPM Service-managed Standard: AWS Control Tower](../userguide/security-hub-controls.md "../userguide/security-hub-controls.md").

## Unsupported Regions

It is important to know that some Security Hub CSPM controls do not operate in certain
AWS Regions where AWS Control Tower is available, because those Regions do not support the
required underlying functionality. As a result, when you deploy an Security Hub CSPM control through
AWS Control Tower, the control may not be operating in all Regions that you govern with AWS Control Tower.
For more information about the Security Hub CSPM controls that cannot be deployed in certain
Regions, see the [Security Hub CSPM
controls reference documentation](../../../securityhub/latest/userguide/securityhub-controls-reference.md "../../../securityhub/latest/userguide/securityhub-controls-reference.md").

You can view the most updated list of the Regions for each control in the AWS Control Tower
console, or by calling the [`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") API.
