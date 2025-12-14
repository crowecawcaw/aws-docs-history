# Detect and resolve drift in AWS Control Tower

Identifying and resolving drift is a regular operations task for AWS Control Tower
management account administrators. Resolving drift helps to ensure your compliance with
governance requirements.

When you create your landing zone, the landing zone and all the organizational units (OUs),
accounts, and resources are compliant with the governance rules enforced by your chosen
controls. As you and your organization members use the landing zone, changes in this compliance
status may occur. Some changes may be accidental, and some may be made intentionally to
respond to time-sensitive operational events.

Drift detection assists you in identifying resources that need changes or configuration
updates to resolve the drift.

## Detecting drift

AWS Control Tower detects drift automatically. To detect drift, the
`AWSControlTowerAdmin` role requires persistent access to your management
account so AWS Control Tower can make read-only API calls to AWS Organizations. These API calls show up as
AWS CloudTrail events.

Drift for a member account is surfaced in the Amazon Simple Notification Service (Amazon SNS) notifications that are aggregated in the
audit account. Notifications in each member account send alerts to a local Amazon SNS topic,
and to a Lambda function.

###### Note

When the auto-enroll capability for accounts is enabled in **Settings**, these SNS notifications are not available.

For controls that are part of the AWS Security Hub CSPM **Service-Managed Standard:
AWS Control Tower**, drift is shown on the **Account** and
**Account details** pages in the AWS Control Tower console, as well as by
means of an Amazon SNS notification.

Member account administrators can (and as a best practice, they should) subscribe to
the SNS drift notifications for specific accounts. For example, the
`aws-controltower-AggregateSecurityNotifications` SNS topic provides
drift notifications. The AWS Control Tower console indicates to management account administrators
when drift has occurred. For more information about SNS topics for drift detection and
notification, see [Drift
prevention and notification](prevention-and-notification.md "prevention-and-notification.md").

**Drift notification de-duplication**

If the same type of drift occurs on the same set of resources multiple times, AWS Control Tower
sends an SNS notification only for the initial instance of drift. If AWS Control Tower detects
that this instance of drift has been remediated, it sends another notification only if
drift re-occurs for those identical resources.

###### Example: SCP drift is handled in the following manner

- If you modify the same managed SCP multiple times, you receive a notification
  for the first time you modify it.
- If you modify a managed SCP, then remediate drift, then modify it again,
  you'll receive two notifications.

###### Types of account drift

- Account moved between OUs (see _[Inheritance drift on enabled baselines](governance-drift.md#drift-enabled-baseline "governance-drift.md#drift-enabled-baseline")_ and [Inheritance drift on enabled controls](governance-drift.md#drift-enabled-controls "governance-drift.md#drift-enabled-controls"))
- Account removed from organization

###### Note

When you move an account from one OU to another, the controls from the previous OU
are not removed. If you enable any new hook-based control on the destination OU, the
old  hook-based control is removed from the account, and the new control replaces
it. Controls implemented with SCPs and AWS Config rules always must be removed manually
when an account changes OUs.

###### Examples of policy drift

- SCP updated
- SCP detached from OU

For more information, see [Types of Governance
Drift](governance-drift.md "governance-drift.md").

## Considerations about drift and policy scans

AWS Control Tower scans your managed SCPs, RCPs, and Declarative policies daily to verify that the corresponding controls are
applied correctly and that they have not drifted. To retrieve these resources and run checks on
them, AWS Control Tower calls AWS Organizations on your behalf, using a role in your management
account.

If an AWS Control Tower scan discovers drift, you'll receive a notification. AWS Control Tower sends
only one notification per drift issue, so if your landing zone already is in a state of
drift, you won't receive additional notifications unless a new drift item is
found.

AWS Organizations limits how often each of its APIs can be called. This limit is expressed in
transactions per second (TPS), and known as the _TPS
limit_, _throttling rate_, or _API request rate_. When AWS Control Tower audits your SCPs, RCPs, and Declarative policies by calling
AWS Organizations, the API calls that AWS Control Tower makes are counted towards your TPS limit, because
AWS Control Tower uses the management account to make the calls.

In rare situations, this limit can be reached when you call the same APIs repeatedly,
whether through a third-party solution or a custom script you wrote. For example, if you
and AWS Control Tower call the same AWS Organizations APIs at the same moment in time (within 1 second),
and the TPS limits are reached, subsequent calls are throttled. That is, these calls
return an error such as `Rate exceeded`.

###### If an API request rate is exceeded

- If AWS Control Tower hits the limit and is throttled, we pause the execution of the
  audit and resume it at a later time.
- If your workload hits the limit and is throttled, the result can range from
  slight latency all the way to a fatal error in the workload, depending on how
  the workload is configured. This edge case is something to be aware of.

###### A daily SCP scan consists of

1. Retrieving your recently active OUs.
2. For each registered OU, retrieving all SCPs managed by AWS Control Tower that are
   attached to the OU. Managed SCPs have identifiers that begin with
   `aws-guardrails`.
3. For each preventive control enabled on the OU, verifying that the control's
   policy statement is present in the OU's managed SCPs.

An OU may have one or more managed SCPs.

## Types of drift to resolve right away

Most types of drift can be resolved by administrators. A few types of drift must be
resolved immediately, including deletion of an organizational unit that the AWS Control Tower
landing zone requires. Here are some examples of major drift that you may wish to
avoid:

- _Don't delete the Security OU:_ The
  organizational unit originally named **Security** during
  landing zone setup by AWS Control Tower should not be deleted. If you delete it, you'll
  see an error message instructing you to reset the landing zone immediately. You
  won't be able to take any other actions in AWS Control Tower until the reset is
  complete.
- _Don't delete required roles:_ AWS Control Tower
  checks certain AWS Identity and Access Management (IAM) roles when you log into the console for
  _IAM role drift_. If these roles are
  missing or inaccessible, you'll see an error page instructing you to reset your
  landing zone. These roles are `AWSControlTowerAdmin`
  `AWSControlTowerCloudTrailRole`
  `AWSControlTowerStackSetRole`.

For more information about these roles, see [Permissions Required to use
the AWS Control Tower console](additional-console-required-permissions.md "additional-console-required-permissions.md").

- _Don't delete all Additional OUs:_ At least one Additional OU is required
  for AWS Control Tower to operate, but it doesn’t have to be the
  **Sandbox** OU.
- _Don't remove shared accounts:_ If you remove
  shared accounts from Foundational OUs with the AWS Organizations console or APIs, such as removing the logging account from
  the Security OU. Moving these accounts creates a type of **Move Account** drift that must be remediated. To remediate this type of drift, you must update the landing zone.

###### Note

As a best practice, do not move these shared accounts out of the Foundational OU.

## Repairable changes to

resources

Here's a list of changes to AWS Control Tower resources that are permitted, although they
create _resolvable drift_. Results of these permitted operations are
viewable in the AWS Control Tower console, although a refresh may be required.

For more information about how to resolve the resulting drift, see [Managing Resources Outside of AWS Control Tower](external-resources.md "external-resources.md").

###### Changes permitted outside the AWS Control Tower console

- Change the name of a registered OU.
- Change the name of the Security OU.
- Change the name of member accounts in non-Foundational OUs.
- Change the name of AWS Control Tower shared accounts in the Security OU.
- Delete a non-Foundational OU.
- Delete an enrolled account from a non-Foundational OU.
- Change the email address of a shared account in the Security OU.
- Change the email address of a member account in a registered OU.

###### Note

Moving accounts between OUs is considered drift, and it must be resolved.

## Drift and new account provisioning

If your landing zone is in a state of drift, the **Enroll account**
feature in AWS Control Tower will not work. In that case, you must provision new accounts through
AWS Service Catalog. For instructions, see [Provision accounts in the Service Catalog console, with Account Factory](provision-as-end-user.md "provision-as-end-user.md") .

In particular, if you've made certain changes to your accounts by means of Service Catalog, such
as changing the name of your portfolio, the **Enroll account** feature
will not work.
