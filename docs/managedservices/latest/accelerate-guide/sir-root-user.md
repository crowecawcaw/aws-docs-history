# Response to root user activity

The 
[root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") is the superuser within your AWS account.
Note that AMS monitors root usage. It's a best practice to use the root user only for the few tasks that require it, such as to change your account
settings, activate AWS Identity and Access Management (IAM) access to billing and cost management, change your root password, and turn on multi-factor authentication (MFA). For more information, see 
[Tasks that require root user credentials](../../../general/latest/gr/root-vs-iam.md#aws_tasks-that-require-root "../../../general/latest/gr/root-vs-iam.md#aws_tasks-that-require-root").

For more information on how to inform AMS of planned root usage, see
[When and how to use the root account in AMS](../userguide/how-when-to-use-root.md "../userguide/how-when-to-use-root.md").

When root user activity is detected, either failed attempts to login that might indicate a brute force attack or activity in the account after a successful login, an event generates and an incident sent to your defined security contacts.

AWS Managed Services Operations investigates unplanned root user activity, perform data collection, triage and analysis, and
perform containment activities at your direction, followed by post event analysis.

If you have the AMS Advanced operating model, you receive additional communications from AMS CSDM and AMS Ops
engineers that confirm unplanned root user activity due AMS's responsibility to secure root user credentials. AMS
investigates root user activity until you confirm a path forward.

## Prepare

Advise AMS of any planned use of root user by submitting an AMS service request with data and times of planned event to prevent
unnecessary incident response activities.

Periodically conduct GameDays with AMS to validate AMS's customer incident response processes, people and systems are current, and
build muscle memory with responsible individuals to achieve faster incident response.

## Phase A: Detect

AMS monitors for root activity in the accounts through detection sources including GuardDuty and AMS monitoring.

If you have AMS Accelerate, the operating model responds to the incident requesting investigation for unexpected
root user activity. When this occurs, AMS Operations initiates the Compromised Account runbook.

If you have AMS Advanced, the operating model responds to the incident, or informs the CSDM of any planned root user
activity to terminate an active Account Compromise investigation.

## Phase B: Analyze

AMS performs a thorough investigation of the root user events when it's determined that the activity isn't
authorized. Using both automations and AMS security response team, logs and events are analyzed for anomalies and
unexpected behavior for root users. Logs are provided to you to help determine if the activity is unknown, or if it's an
authorized root user event, or if it requires further investigation.

Some examples of the information provided during the investigation to support internal checks includes:

- Account information: What account was the root account used on?
- E-mail address for root user: Each root user is associated with an e-mail address from your organization
- Authentication details: Where and when did the root user access your environment from?
- Activity records: What did the user do when logged in as root? These records are in the form of CloudWatch events.
  Understanding how to read these logs aids in investigation.

It's a best practice that you are prepared to receive the analysis information and have a plan for how to reach authorized
points of contact for accounts within your organization. Because root users aren't named as individuals, determining who has access
to the root e-mail address used for the account within your organization helps to quickly route questions internally.

## Phase C: Contain and Eradicate

AMS partners with your security teams to perform containment at the direction of your authorized Customer Security contacts. Containment options include:

- Rotating appropriate credentials and keys.
- Terminating active sessions to accounts and resources.
- Eradicating resources created.

During the containment activities AMS works closely with your security team to ensure any disruption to your
workloads are minimized and the root credentials are appropriately secured.

After the containment plan is completed, you work with AMS Operations team for any recovery actions as required.

## Post Incident Report

As required, AMS initiates the investigation review process to identify any lessons learned. As part of completing a COE,
AMS communicates any relevant findings to affected customers to help them improve their incident response process.

AMS documents all final details of the investigation, collects appropriate metrics, and then reports the incident to any AMS
internal teams that require information, including your assigned CSDM and CA.
