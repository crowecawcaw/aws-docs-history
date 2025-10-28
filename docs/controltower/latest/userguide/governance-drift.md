# Types of governance drift

Governance drift, also called _organizational drift_
occurs when OUs, SCPs, and member accounts are changed or updated. The types of
governance drift that can be detected in AWS Control Tower are as follows:

- Account and OU governance drift
- Landing zone drift
- Control drift for non-SCP controls
- Inheritance drift for baselines and controls
  The next sections provide detail about these types of drift that AWS Control Tower reports, and how to resolve them.

###### Account and OU governance drift

- [Moved member account](#drift-account-moved "#drift-account-moved")
- [Removed member account](#drift-account-removed "#drift-account-removed")
- [Unplanned update to managed SCP](#drift-scp-update "#drift-scp-update")
- [SCP detached from managed OU](#drift-scp-detached-ou "#drift-scp-detached-ou")
  **Landing zone drift**

Another type of drift is _landing zone drift_, which
may be found through the management account. Landing zone drift consists of IAM role
drift, or any type of organizational drift that specifically affects Foundational OUs
and shared accounts.

- [Deleted Foundational OU](#drift-ou-deleted "#drift-ou-deleted")
- [Trusted access disabled](#drift-disable-trust "#drift-disable-trust")
  A special case of landing zone drift is _role drift_,
  which is detected when a required role is not available. If this type of drift occurs,
  the console displays a warning page and some instructions on how to restore the role.
  Your landing zone is unavailable until the role drift is resolved. For more information
  about role drift, see _Don't delete required roles_ in the
  section called [Types of drift to resolve right away](drift.md#types-of-drift "drift.md#types-of-drift").

**Control drift for non-SCP controls**

AWS Control Tower reports _control drift_ regarding controls implemented
with resource control policies (RCPs), declarative policies and controls that are part of the
**AWS Security Hub Service-managed Standard: AWS Control Tower**.

- [Security Hub control drift](#sh-control-drift "#sh-control-drift")
- [Control policy drift](#control-policy-drift "#control-policy-drift")
  **Inheritance drift for baselines and controls**

- **Enabled baseline drift**

When baseline configurations on a member account are different than those applied to the parent OU, AWS Control Tower reports inheritance drift for enabled baselines (resource configurations) on those OUs and accounts. For more information about baselines, see [Types of baselines](types-of-baselines.md "types-of-baselines.md").

    + [Inheritance drift on enabled baselines](#drift-enabled-baseline "#drift-enabled-baseline")

- **Enabled control drift**

When enabled control configurations on a member account are different than those applied to the parent OU, AWS Control Tower reports inheritance drift for enabled controls on those OUs and accounts.

    + [Inheritance drift on enabled controls](#drift-enabled-controls "#drift-enabled-controls")

###### Drift that is not reported

- AWS Control Tower does not look for drift regarding other services that work with
  the management account, including AWS CloudTrail, Amazon CloudWatch, IAM Identity Center, AWS CloudFormation, AWS Config,
  and so forth.
- AWS Control Tower does not detect resource drift or other kinds of drift that may
  happen if you modify the resources contained in a baseline.

## Moved member account

This type of drift occurs on the account rather than the OU. This type of drift
can occur when an AWS Control Tower member account, the audit account, or the log archive
account is moved from a registered AWS Control Tower OU to any other OU. In many cases, you can avoid this type of drift if you activate the auto-enrollment feature for accounts, on the **Settings** page. For more details, see [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md").

The following is an
example of the Amazon SNS notification when this type of drift is detected.

```

{
  "Message" : "AWS Control Tower has detected that your member account '`account-email`@amazon.com (`012345678909`)' has been moved from organizational unit 'Sandbox (`ou-0123-eEXAMPLE`)' to 'Security (`ou-3210-1EXAMPLE`)'. For more information, including steps to resolve this issue, see 'https://docs.aws.amazon.com/console/controltower/move-account'",
  "ManagementAccountId" : "`012345678912`",
  "OrganizationId" : "`o-123EXAMPLE`",
  "DriftType" : "ACCOUNT_MOVED_BETWEEN_OUS",
  "RemediationStep" : "Re-register this organizational unit (OU), or if the OU has more than 1000 accounts, you must update the provisioned product in Account Factory.",
  "AccountId" : "`012345678909`",
  "SourceId" : "`012345678909`",
  "DestinationId" : "`ou-3210-1EXAMPLE`"
}

```

### Resolutions

When this type of drift occurs for an Account Factory provisioned account in an OU
with up to 1000 accounts, you can resolve it by:

- Navigating to the **Organization** page in the
  AWS Control Tower console, selecting the account, and choosing **Update
  account** at the upper right (fastest option for individual
  accounts).
- Navigating to the **Organization** page in the
  AWS Control Tower console, then choosing **Re-register** for the
  OU that contains the account (fastest option for multiple accounts). For
  more information, see [Register an existing organizational unit with
  AWS Control Tower](importing-existing.md "importing-existing.md").
- Updating the provisioned product in Account Factory. For more information,
  see [Update and move accounts with AWS Control Tower](updating-account-factory-accounts.md "updating-account-factory-accounts.md").

###### Note

If you have several individual accounts to update, also see this
method for making updates with a script: [Provision and update accounts using
automation](update-accounts-by-script.md "update-accounts-by-script.md").

- When this type of drift occurs in an OU with more than 1000 accounts,
  the drift resolution may depend on which type of account has been moved,
  as explained in the next paragraphs. For more information, see [Update your landing zone](update-controltower.md "update-controltower.md").
  - **If an Account Factory provisioned account is
    moved** – In an OU with fewer than 1000
    accounts, you can resolve the account drift by updating the
    provisioned product in Account Factory, by re-registering the OU, or
    by updating your landing zone.

  In an OU with more than 1000 accounts, you _must_ resolve the drift by making an
  update to each moved account, either through the AWS Control Tower
  console or the provisioned product, because
  **Re-register OU** will not perform the
  update. For more information, see [Update and move accounts with AWS Control Tower](updating-account-factory-accounts.md "updating-account-factory-accounts.md").
  - **If a shared account is moved**
    – You can resolve the drift from moving the audit or log
    archive account by updating your landing zone. For more information,
    see [Update your landing zone](update-controltower.md "update-controltower.md").

###### Deprecated field name

The field name `MasterAccountID` has been changed to
`ManagementAccountID` to comply with AWS guidelines. The
old name is **deprecated**. Since 2022, scripts
that contain the deprecated field name no longer work.

## Removed member account

This type of drift can occur when a member account is removed from a registered
AWS Control Tower organizational unit. The following example shows the Amazon SNS notification
when this type of drift is detected.

```

{
  "Message" : "AWS Control Tower has detected that the member account `012345678909` has been removed from organization `o-123EXAMPLE`. For more information, including steps to resolve this issue, see 'https://docs.aws.amazon.com/console/controltower/remove-account'",
  "ManagementAccountId" : "`012345678912`",
  "OrganizationId" : "`o-123EXAMPLE`",
  "DriftType" : "ACCOUNT_REMOVED_FROM_ORGANIZATION",
  "RemediationStep" : "Add account to Organization and update Account Factory provisioned product",
  "AccountId" : "`012345678909`"
}

```

### Resolution

- When this type of drift occurs in a member account, you can resolve
  the drift by updating the account in the AWS Control Tower console, or in
  Account Factory. For example, you can add the account to another registered
  OU from the Account Factory update wizard. For more information, see [Update and move accounts with AWS Control Tower](updating-account-factory-accounts.md "updating-account-factory-accounts.md").
- If a shared account is removed from a Foundational OU, you must
  resolve the drift by resetting your landing zone. Until this drift is
  resolved, you will not be able to use the AWS Control Tower console.
- For more information about resolving drift for accounts and OUs, see
  [If you manage resources outside of AWS Control Tower](external-resources.md "external-resources.md").

###### Note

In Service Catalog, the Account Factory provisioned product that represents the
account is not updated to remove the account. Instead, the provisioned
product is displayed as `TAINTED` and in an error state. To clean
up, go to the Service Catalog, choose the provisioned product, and then choose
**Terminate**.

## Unplanned update to managed SCP

This type of drift can occur when an SCP for a control is updated in the AWS Organizations
console or programmatically using the AWS CLI or one of the AWS SDKs. The following is
an example of the Amazon SNS notification when this type of drift is detected.

```

{
  "Message" : "AWS Control Tower has detected that the managed service control policy '`aws-guardrails-012345` (`p-tEXAMPLE`)', attached to the registered organizational unit 'Security (`ou-0123-1EXAMPLE`)', has been modified. For more information, including steps to resolve this issue, see 'https://docs.aws.amazon.com/console/controltower/update-scp'",
  "ManagementAccountId" : "`012345678912`",
  "OrganizationId" : "`o-123EXAMPLE`",
  "DriftType" : "SCP_UPDATED",
  "RemediationStep" : "Update Control Tower Setup",
  "OrganizationalUnitId" : "`ou-0123-1EXAMPLE`",
  "PolicyId" : "`p-tEXAMPLE`"
}

```

### Resolution

When this type of drift occurs in an OU with up to 1000 accounts, you can
resolve it by:

- Navigating to the **Organization** page in the
  AWS Control Tower console to re-register the OU (fastest option). For more
  information, see [Register an existing organizational unit with
  AWS Control Tower](importing-existing.md "importing-existing.md").
- Updating your landing zone (slower option). For more information, see [Update your landing zone](update-controltower.md "update-controltower.md").

When this type of drift occurs in an OU with more than 1000 accounts, resolve
it by updating your landing zone. For more information, see [Update your landing zone](update-controltower.md "update-controltower.md").

## SCP detached from managed OU

This type of drift can occur when an SCP for a control has been detached from an
OU that's managed by AWS Control Tower. This occurrence is especially common when you're
working from outside of the AWS Control Tower console. The following is an example of the
Amazon SNS notification when this type of drift is detected.

```

{
  "Message" : "AWS Control Tower has detected that the managed service control policy '`aws-guardrails-012345` (`p-tEXAMPLE`)' has been detached from the registered organizational unit 'Sandbox (`ou-0123-1EXAMPLE`)'. For more information, including steps to resolve this issue, see 'https://docs.aws.amazon.com/console/controltower/scp-detached'",
  "ManagementAccountId" : "`012345678912`",
  "OrganizationId" : "`o-123EXAMPLE`",
  "DriftType" : "SCP_DETACHED_FROM_OU",
  "RemediationStep" : "Update Control Tower Setup",
  "OrganizationalUnitId" : "`ou-0123-1EXAMPLE`",
  "PolicyId" : "`p-tEXAMPLE`"
}

```

### Resolution

When this type of drift occurs in an OU with up to 1000 accounts, you can
resolve it by:

- Navigating to the OU in the AWS Control Tower console to re-register the OU
  (fastest option). For more information, see [Register an existing organizational unit with
  AWS Control Tower](importing-existing.md "importing-existing.md").
- Updating your landing zone (slower option). If the drift is affecting a
  mandatory control, the update process creates a new service control
  policy (SCP) and attaches it to the OU to resolve the drift. For more
  information about how to update your landing zone, see [Update your landing zone](update-controltower.md "update-controltower.md").

When this type of drift occurs in an OU with more than 1000 accounts, resolve
it by updating your landing zone. If the drift is affecting a mandatory control, the
update process creates a new service control policy (SCP) and attaches it to the
OU to resolve the drift. For more information about how to update your landing zone,
see [Update your landing zone](update-controltower.md "update-controltower.md").

## Deleted Foundational OU

This type of drift applies only to AWS Control Tower Foundational OUs, such as the Security
OU. It can occur if a Foundational OU is deleted outside of the AWS Control Tower console.
Foundational OUs cannot be moved without creating this type of drift, because moving
an OU is the same as deleting it and then adding it someplace else. When you resolve
the drift by updating your landing zone, AWS Control Tower replaces the Foundational OU in the
original location. The following example shows an Amazon SNS notification you may receive
when this type of drift is detected.

```

{
  "Message" : "AWS Control Tower has detected that the registered organizational unit 'Security (`ou-0123-1EXAMPLE`)' has been deleted. For more information, including steps to resolve this issue, see 'https://docs.aws.amazon.com/console/controltower/delete-ou'",
  "ManagementAccountId" : "`012345678912`",
  "OrganizationId" : "`o-123EXAMPLE`",
  "DriftType" : "ORGANIZATIONAL_UNIT_DELETED",
  "RemediationStep" : "Delete organizational unit in Control Tower",
  "OrganizationalUnitId" : "`ou-0123-1EXAMPLE`"
}

```

### Resolution

Because this drift occurs for Foundational OUs only, the resolution is to
update the landing zone. When other types of OUs are deleted, AWS Control Tower is
updated automatically.

For more information about resolving drift for accounts and OUs, see [If you manage resources outside of AWS Control Tower](external-resources.md "external-resources.md").

## Security Hub control drift

This type of drift occurs when a control that's part of the **AWS Security Hub
Service-Managed Standard: AWS Control Tower** reports a state of drift. The
AWS Security Hub service itself does not report a state of drift for these controls.
Instead, the service sends its findings to AWS Control Tower.

Security Hub control drift also can be detected if AWS Control Tower has not received a status
update from Security Hub in more than 24 hours. If those findings are not received as
expected, AWS Control Tower verifies that the control is in drift. The following example
shows an Amazon SNS notification you may receive when this type of drift is
detected.

```
{
"Message" : "AWS Control Tower has detected that an AWS Security Hub control was removed in your account example-account@amazon.com <mailto:example-account@amazon.com>. The artifact deployed on the target OU and accounts does not match the expected template and configuration for the control. This mismatch indicates that configuration changes were made outside of AWS Control Tower. For more information, view Security Hub standard",
"MasterAccountId" : "123456789XXX",
"ManagementAccountId" : "123456789XXX",
"OrganizationId" : "o-123EXAMPLE",
"DriftType" : "SECURITY_HUB_CONTROL_DISABLED",
"RemediationStep" : "To remediate the issue, Re-register the OU, or remove the control and enable it again. If the problem persists, contact AWS support.",
"AccountId" : "7876543219XXX",
"ControlId" : "SH.XXXXXXX.1",
"ControlName" : "EBS snapshots should not be publicly restorable",
"ApiControlIdentifier" : "arn:aws:controltower:us-east-1::control/PYBETSAGNUZB",
"EnabledControlIdentifier": "arn:aws:controltower:us-east-1::enabledcontrol/`<UNIQUE_ID>`".
"Region" : "us-east-1"
}
```

### Resolution

For OUs with fewer than 1000 accounts, the recommended resolution is to call
the **ResetEnabledControl** API for the drifted control. In the
console, you can select **Re-register** for the OU, which
resets the control to the original state. Alternatively, for any OU, you can
remove and re-enable the control through the console or the AWS Control Tower APIs, which
also resets the control.

For more information about resolving drift for accounts and OUs, see [If you manage resources outside of AWS Control Tower](external-resources.md "external-resources.md").

## Control policy drift

This type of drift occurs when a control that's implemented with _resource control policies_ (RCPs) or _declarative policies_ reports a state of drift. It returns a state of `CONTROL_INEFFECTIVE`, which you can view in the AWS Control Tower console and in the drift message. The drift message for this type of drift also includes the `EnabledControlIdentifier` for the affected control.

This type of drift is not reported for SCP-based controls.

The following example shows an Amazon SNS notification you may receive when this type
of drift is detected.

```
{
    "Message": "AWS Control Tower detects that a policy it owns was updated unexpectedly. This mismatch indicates that configuration changes were made outside of AWS Control Tower.",
    "MasterAccountId": "123456789XXX",
    "ManagementAccountId": "123456789XXX",
    "OrganizationId": "o-123EXAMPLE",
    "DriftType": "CONTROL_INEFFECTIVE",
    "RemediationStep": "To remediate the issue, Reset the DRIFTED enabled control if permitted or Re-register the OU. If the problem persists, contact AWS support.",
    "TargetIdentifier": "arn:aws:::organizations/o-123456/ou-1234-4567",
    "ControlId": "CT.XXXXXXX.PV.1",
    "ControlName": "EBS snapshots should not be publicly restorable",
    "ApiControlIdentifier": "arn:aws:controlcatalog:::control/`<UNIQUE_ID>"`,
    "EnabledControlIdentifier": "arn:aws:controltower:us-east-1::enabledcontrol/`<UNIQUE_ID>`"
}
```

### Resolution

The easiest resolution for control policy drift on RCP controls, declarative policy controls, and Security Hub
controls enabled in AWS Control Tower is to call the `ResetEnabledControl`
API.

For OUs with fewer than 1000 accounts, another resolution from the console or
API is to **Re-register** the OU, which resets the control to
the original state.

For any individual OU, you can remove and re-enable the control through the
console or the AWS Control Tower APIs, which also resets the control.

For more information about resolving drift for accounts and OUs, see [If you manage resources outside of AWS Control Tower](external-resources.md "external-resources.md").

## Trusted access disabled

This type of drift applies to AWS Control Tower landing zones. It occurs when you disable
trusted access to AWS Control Tower in AWS Organizations after you set up your AWS Control Tower landing zone.

When trusted access is disabled, AWS Control Tower no longer receives change events from
AWS Organizations. AWS Control Tower relies on these change events to stay synchronized with AWS Organizations.
As a result, AWS Control Tower may miss organizational changes in accounts and OUs. That is
why it is important to re-register each OU, each time you update your landing zone.

###### Example: Amazon SNS notification

The following is an example of the Amazon SNS notification that you receive when
this type of drift occurs.

```
{
  "Message" : "AWS Control Tower has detected that trusted access has been disabled in AWS Organizations. For more information, including steps to resolve this issue, see https://docs.aws.amazon.com/controltower/latest/userguide/drift.html#drift-trusted-access-disabled",
  "ManagementAccountId" : "`012345678912`",
  "OrganizationId" : "`o-123EXAMPLE`",
  "DriftType" : "TRUSTED_ACCESS_DISABLED",
  "RemediationStep" : "Reset Control Tower landing zone."
}
```

### Resolution

AWS Control Tower notifies you when this type of drift occurs in the AWS Control Tower console.
The resolution is to reset your AWS Control Tower landing zone. For more information, see
[Resolving
drift](drift.md#resolving-drift "drift.md#resolving-drift").

## Inheritance drift on enabled baselines

This type of drift can occur to AWS Control Tower OUs and accounts.

### Resolution

AWS Control Tower notifies you when this type of drift occurs. For almost all cases of inheritance drift, you will receive an SNS notification for _Moved member account_ drift. That's because this type of drift typically occurs when an account has been moved, or an account fails enrollment.

**View and resolve drift in the console**

In the AWS Control Tower console, you can view this inherited drift status in the
**Baseline state** column on the
**Organizations** page. The resolution from the console is
to **Re-register** your OU or **Update** your
account.

**View and resolve drift programmatically**

To view drift status programmatically, you can call the
[`ListEnabledBaselines`](../APIReference/API_ListEnabledBaselines.md "../APIReference/API_ListEnabledBaselines.md") API to view statuses for the
enabled baselines on your OUs. To view statuses for individual accounts programmatically with the
`ListEnabledBaselines` API, use the `includeChildren` flag.

You can resolve this type of
drift programmatically, by calling the [`ResetEnabledBaseline`](../APIReference/API_ResetEnabledBaseline.md "../APIReference/API_ResetEnabledBaseline.md") API.

## Inheritance drift on enabled controls

This type of drift can occur to AWS Control Tower OUs and accounts.

### Resolution

AWS Control Tower notifies you when this type of drift occurs. For almost all cases of inheritance drift, you will receive an SNS notification for _Moved member account_ drift. That's because this type of drift typically occurs when an account has been moved, or an account fails enrollment.

**View and resolve drift in the console**

In the AWS Control Tower console, you can view this inherited drift status in the
**Organizations** page, the **Enabled controls** page, and the **Account details** page. The resolution from the console is
to **Re-register** your OU or **Update** your
account.

**View and resolve drift programmatically**

To view inherited drift status for enabled controls programmatically, you can call the
[`ListEnabledControls`](../APIReference/API_ListEnabledControls.md "../APIReference/API_ListEnabledControls.md") API to view statuses for the
enabled controls on your OUs. To view statuses for individual accounts programmatically with the
`ListEnabledControls` API, use the `includeChildren` flag.

You can resolve this type of inheritance
drift programmatically, by calling the [`ResetEnabledControl`](../APIReference/API_ResetEnabledControl.md "../APIReference/API_ResetEnabledControl.md") API.
