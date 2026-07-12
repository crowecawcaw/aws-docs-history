# Validating your AWS Security Incident Response configuration

After you complete onboarding, you can validate that enrollment, detection sources, AWS Identity and Access Management (IAM) permissions,
containment, and notifications are configured correctly before a real security event occurs.
This section provides step-by-step verification procedures using both the AWS Management Console and
the AWS CLI.

###### Topics

- [Before you validate](#config-validation-before "#config-validation-before")
- [Step 1: Verify enrollment and membership](#config-validation-step1 "#config-validation-step1")
- [Step 2: Verify detection sources and triage](#config-validation-step2 "#config-validation-step2")
- [Step 3: Verify the automated finding pipeline](#config-validation-step3 "#config-validation-step3")
- [Step 4: Verify notifications and incident response team](#config-validation-step4 "#config-validation-step4")
- [Step 5: Verify containment readiness (optional)](#config-validation-step5 "#config-validation-step5")
- [Step 6: Confirm ongoing operation](#config-validation-step6 "#config-validation-step6")
- [Validation checklist](#config-validation-checklist "#config-validation-checklist")
- [Billing verification](#config-validation-billing "#config-validation-billing")
- [Troubleshooting](#config-validation-troubleshooting "#config-validation-troubleshooting")
- [Related resources](#config-validation-related-resources "#config-validation-related-resources")

## Before you validate

### Prerequisites for validating your Security Incident Response configuration

To complete these validation steps, make sure that you have the following:

- Console or AWS Command Line Interface (AWS CLI) access to your **delegated administrator account** (the account you designated during onboarding)
- The AWS Region where you activated your subscription
- Your membership ID (if validating using the AWS CLI)

### Confirm log readiness

AWS Security Incident Response doesn't enable log sources on your behalf. During an investigation, engineers
rely on logs that are already present in your environment. Before validating your setup,
confirm the following logs are enabled in all covered accounts and AWS Regions. Without these logs, Security Incident Response engineers have limited visibility during investigations. Enable
them before proceeding.

- **AWS CloudTrail**: management events trail (required)
- **Amazon VPC Flow Logs** (recommended)
- **Amazon S3 server access logging** for sensitive buckets (recommended)
- **Amazon Route 53 Resolver DNS query logging** (recommended)

### Verify GuardDuty is enabled

Use the following command to verify that Amazon GuardDuty is active in your accounts:

```
aws guardduty list-detectors
```

A non-empty response confirms GuardDuty is enabled in the current AWS Region. Repeat this step for each
active Region, or verify across your organization through the GuardDuty delegated
administrator account.

###### Note

AWS Security Incident Response costs don't include GuardDuty usage costs. See the
[GuardDuty pricing page](https://aws.amazon.com/guardduty/pricing/ "https://aws.amazon.com/guardduty/pricing/") for details.

## Step 1: Verify enrollment and membership

### Using the AWS Security Incident Response console

1. Sign in to the delegated administrator account.
2. Open the [AWS Security Incident Response console](https://console.aws.amazon.com/security-ir/ "https://console.aws.amazon.com/security-ir/").
3. Confirm that your membership status shows **Active**. A status of _Pending_ indicates onboarding is incomplete.
4. Under **Account scope**, verify that the OUs you intended to cover are listed. Coverage is selected at the organizational unit (OU) level, not at the individual account level. All accounts within a selected OU (including child OUs) are covered.
5. Confirm that the **Region** listed matches where your workloads run. Region selection is locked at registration and can't be changed after setup.

### Using the AWS CLI

Run the following command from your delegated administrator account:

```
aws security-ir list-memberships
```

The preceding command returns your membership ID and status.

To get full membership details including your incident response team configuration, run the following command:

```
aws security-ir get-membership --membership-id `membership-id`
```

Use the command output to verify the following information.

- Membership status is `Active`
- The incident response team members listed match your intended stakeholders
- At least two incident response team members are configured (required)

### Verify the delegated administrator

To confirm that the correct account is registered as the delegated administrator for
Security Incident Response, run the following command:

```
aws organizations list-delegated-administrators \
  --service-principal security-ir.amazonaws.com
```

###### Note

**Best practice:** Use the same delegated administrator
account that you set for other AWS security services (such as AWS Security Hub CSPM and GuardDuty).
The [AWS
Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md") recommends using the Security Tooling account.

## Step 2: Verify detection sources and triage

AWS Security Incident Response monitors security findings from GuardDuty and third-party tools through Security Hub CSPM. The
service uses a service-linked role to ingest findings through Amazon EventBridge rules deployed to your
accounts during onboarding.

### Verify the Triage service-linked role

The `AWSServiceRoleForSecurityIncidentResponse_Triage` service-linked role
must exist in your management account and all in-scope member accounts.

To verify, run the following command in the management and in-scope member accounts:

```
aws iam get-role --role-name AWSServiceRoleForSecurityIncidentResponse_Triage
```

A successful response confirms the role exists. If you receive a `NoSuchEntity`
error, do one of the following:

- **If you onboarded using the console:** The role should have been created automatically. Contact AWS Support.
- **If you onboarded using the API or AWS CLI:** See [Enable Security Incident Response using the API/CLI](enable-sir-using-cli.md "enable-sir-using-cli.md") for instructions on manually creating the role.

### Verify the primary service-linked role

The `AWSServiceRoleForSecurityIncidentResponse` role should also exist in
your delegated administrator account. To verify that the role exists, run the following command:

```
aws iam get-role --role-name AWSServiceRoleForSecurityIncidentResponse
```

### Verify proactive response and EventBridge rules

In the AWS Security Incident Response console, confirm that **Proactive response** shows as
enabled. When enabled, the service does the following:

- Ingests findings from GuardDuty and Security Hub CSPM through EventBridge rules
- Automatically triages findings using customer-specific context (known IPs, expected IAM entities)
- Creates proactive investigation cases when confirmed security issues are identified
- Archives GuardDuty findings determined to be benign (viewable in the GuardDuty console under **Archived** findings)

**Verify EventBridge rules are deployed in member accounts**

To verify that EventBridge rules are deployed in member accounts, complete the following steps.

1. Open the Amazon EventBridge console in a covered member account.
2. Choose **Rules**.
3. Confirm that rules with `SecurityIncidentResponse` in their name are present and **Enabled**.

If the rules are missing, re-run the proactive response setup from the Security Incident Response console or
contact AWS Support.

### Verify third-party integrations (if applicable)

If you use third-party detection tools (such as CrowdStrike Falcon, Trend Micro Cloud
One, or Fortinet Lacework FortiCNAPP), verify that their findings are flowing through
Security Hub CSPM:

1. Open the [AWS Security Hub CSPM console](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. Go to **Integrations**.
3. Confirm your third-party vendor integration shows as **Accepting findings**.

###### Note

You don't need to enable Security Hub CSPM standards or controls. Only the vendor integrations are
required for Security Incident Response to ingest third-party findings.

## Step 3: Verify the automated finding pipeline

This step confirms that the EventBridge pipeline is active and findings are reaching automated
triage.

### About GuardDuty sample findings

GuardDuty's built-in **Generate sample findings** feature produces findings
marked as samples. Automated triage filters sample findings to prevent noise; they don't
flow through the full triage pipeline and can't be used to validate your Security Incident Response
configuration. **Don't use them for this step.**

### Validate with the GuardDuty test domain

The GuardDuty documentation provides a test domain (`guarddutyc2activityb.com`)
that generates a real finding without requiring real-world security events. Querying this
domain from an Amazon EC2 instance in a covered account produces a finding that Security Incident Response ingests
and processes.

**To generate a test finding:**

1. Connect to an Amazon EC2 instance in a covered account using Systems Manager Session Manager or SSH.
2. Run the following command:

```
dig guarddutyc2activityb.com
```

3. Open the GuardDuty console, then choose **Findings**. The finding appears within approximately 5 minutes.

**What to expect:**

- Automated triage processes the finding and determines it isn't indicative of a genuine security event.
- The finding is **archived** in GuardDuty. To view it, select **Archived** from the **Status** filter.
- If you use Security Hub CSPM, the finding's workflow status changes to `SUPPRESSED`.
- **No proactive case is created**: this is correct behavior. A case is only opened when automated triage identifies activity that warrants human investigation.

###### Note

If the test finding doesn't appear in the GuardDuty archived list within 15 minutes, see
[Troubleshooting](#config-validation-troubleshooting "#config-validation-troubleshooting").
If no Amazon EC2 instance is available, proceed to Step 4 and return to this test when your
environment is ready.

## Step 4: Verify notifications and incident response team

### Verify your incident response team

In the Security Incident Response console, review your configured incident response team members. Each member
receives immediate email notifications when a case is created.

Or, run the following command to verify using the AWS CLI:

```
aws security-ir get-membership --membership-id `membership-id`
```

Confirm that:

- All intended stakeholders are listed
- Email addresses are correct
- Each member's communication preferences are set appropriately (all communication options are enabled by default — if a member isn't receiving notifications, verify their preferences haven't been cleared)

### Understanding case watchers

Case watchers are stakeholders who are granted access to view a specific case. Key
details:

- **Watchers are per case, not per account.** Adding a watcher to one case doesn't grant them access to any other case. You must explicitly add watchers to each case where you want them to have visibility.
- **Watchers have view-only access.** They can view case details and receive notifications for case updates, but can't perform containment or remediation actions on resources.
- **Up to 30 stakeholders** can be added per individual case.
- Each case includes a pre-scoped IAM policy that grants access only to that specific case, maintaining least-privilege access.

This per-case scoping is particularly important when granting access to external parties
such as managed detection and response (MDR) partners or third-party investigation teams
who should only see the specific case they're involved in.

### Verify notification delivery with a test case

The most effective way to validate end-to-end notification flow is to create a reactive
(self-managed) test case:

1. In the Security Incident Response console, create a new **self-managed case**.
2. In the case title and description, clearly state: **"This is a configuration validation test, there is no real security event."**
3. Verify that all configured incident response team members receive the email notification.
4. Close the case after confirming notifications were received.

###### Important

Creating a test case may trigger a response from Security Incident Response engineers if you request
AWS-supported engagement. Clearly mark your case as a test to avoid unnecessary
escalation. Use this step once to confirm the channel is working, then close the case
promptly.

### What to expect from case notifications

When a case is created (either proactively by the service or reactively by your team),
all configured incident response team members receive an email notification containing
the case details.

### Verify EventBridge integration (if configured)

If you configured EventBridge to route case events to third-party platforms (such as
ServiceNow, Jira, Slack, or PagerDuty), verify that your test case triggers the expected
notification in those systems.

## Step 5: Verify containment readiness (optional)

###### Note

**Containment is optional and isn't enabled by default.**
The containment infrastructure described in this section is only required if you choose
to enable containment; it isn't needed for Security Incident Response to monitor your environment,
investigate findings, or open cases.

### If you haven't enabled containment

Nothing to validate here. Security Incident Response provides guidance and investigation during security
events but doesn't take automated containment actions unless you explicitly authorize it.

### If you have enabled containment

**Check containment status in the console.** Verify whether
containment actions are shown as **Authorized**. Supported containment
actions include runbooks for:

- Affected Amazon S3 buckets
- Affected Amazon EC2 instances
- Affected IAM principals

**Verify the CloudFormation StackSet is deployed.**
Containment requires IAM roles (`AWSSecurityIncidentResponseContainment`
and `AWSSecurityIncidentResponseContainmentExecution`) in your covered
accounts:

1. Open AWS CloudFormation in your management account.
2. Choose **StackSets**.
3. Confirm the Security Incident Response containment StackSet shows `SUCCEEDED` in all target accounts.

If the StackSet isn't deployed, containment authorization in the console doesn't result
in actual containment actions being taken.

**Confirm your containment preference.** Security Incident Response supports
three containment levels:

- **Approval Required** (default): no containment action without your explicit case-by-case authorization.
- **Contain Confirmed**: proactive containment of resources confirmed as affected.
- **Contain Suspected**: proactive containment of resources with high likelihood of being affected.

To submit or update your preference, create an AWS Support case with case type
**Technical: Security Incident Response Service / Other**.

**If you want EC2 Triage:** Deploy the
**Containment with EC2 Triage** CloudFormation template.
This allows Security Incident Response engineers to collect investigative data from Amazon EC2 instances using
AWS Systems Manager.

## Step 6: Confirm ongoing operation

After completing initial validation, use these indicators to confirm that Security Incident Response is
continuously operating as expected.

### The absence of cases is normal

Security Incident Response creates a proactive case only when automated triage identifies activity that
warrants human investigation. When triage determines a finding is benign, it archives
the finding without creating a case or contacting your team. A deployment with no open
cases and a consistent flow of archived GuardDuty findings is operating as intended.

If you see no cases _and_ no archived findings after your environment
has been active for several days, the pipeline may not be connected; verify Steps 2 and 3.

###### Note

Proactive cases with no customer response for 5 days are automatically closed.

### Archived findings and suppression rules as health signals

As Security Incident Response processes findings over time, it creates two observable artifacts:

- **Archived findings:** findings that automated triage determined to be benign. These accumulate over time and are visible in the GuardDuty console under **Findings**, then select **Archived**.
- **GuardDuty suppression rules:** for finding types confirmed as expected activity in your environment, Security Incident Response deploys named suppression rules (prefixed with `SIRTriage-`). These are the clearest ongoing signal that automated triage is actively working. View them in the GuardDuty console under **Suppression rules**.

Your incident response team is notified when a suppression rule is created. If a rule
was created in error, contact AWS Support to request a rollback. Archived findings are
retained in GuardDuty for 90 days.

### Monthly activity report

Security Incident Response sends a monthly activity report to your incident response team summarizing findings
processed, triage outcomes, and any cases that were opened. If your team hasn't received
a report after your first full calendar month of operation, verify that incident response
team members have communications enabled. For any other issues related to the monthly
report, contact your Account Team or open a Support Case with case type:
**Technical: Security Incident Response Service / Other**
and include the following information:

- Your organization name
- The reporting month/year you expected (for example, "May 2026")
- Your Security Incident Response Membership ID if known
- The account IDs covered by your Security Incident Response membership

### What to expect from Security Incident Response engineers

When you create an AWS-supported case or the service proactively creates one, Security Incident Response
engineers acknowledge new cases within **15 minutes**. This
15-minute acknowledgment SLO applies to all AWS-supported case types; both active
security events and investigations. The initial acknowledgment confirms your case is
being reviewed; the full assessment timeline may vary based on case severity and
complexity.

For proactive cases (auto-created when the triage service identifies a confirmed security
issue), the service creates the case after automated triage confirms the issue, and your
incident response team is notified when the case is opened.

## Validation checklist

Use this checklist to confirm your configuration is complete:

- Log sources enabled: CloudTrail management events (required), Amazon VPC Flow Logs, Amazon S3 access logging, DNS query logging (recommended)
- GuardDuty is enabled in all accounts and active Regions
- Membership status is **Active** in the Security Incident Response console
- Region is correct (locked at registration)
- Delegated administrator account is correct (Security Tooling account recommended)
- Account scope covers intended OUs
- `AWSServiceRoleForSecurityIncidentResponse_Triage` exists in management account
- `AWSServiceRoleForSecurityIncidentResponse_Triage` exists in in-scope member accounts
- `AWSServiceRoleForSecurityIncidentResponse` exists in delegated administrator account
- Third-party integrations (if applicable) show as accepting findings in Security Hub CSPM
- EventBridge rules with `SecurityIncidentResponse` in the name are present and enabled in member accounts
- Incident response team members are configured with correct contact information and communications enabled
- Test case created and email notifications received by all team members
- Test domain finding (`guarddutyc2activityb.com`) archived within 15 minutes
- Containment StackSet deployed successfully (if containment enabled)
- Containment preference submitted (if containment enabled)
- EventBridge integrations (if configured) are delivering events to third-party platforms
- Archived findings visible in GuardDuty after first week of operation

## Billing verification

**Enterprise Support and Unified Operations customers:**
Security Incident Response is included at no additional cost as part of your support plan. You don't see Security Incident Response
charges in AWS Cost Explorer or the AWS Cost and Usage Report.

**All other customers:** Pricing is based on the number of
security findings ingested. The first 10,000 findings per month are free. For details, see
[AWS Security Incident Response pricing](https://aws.amazon.com/security-incident-response/pricing/ "https://aws.amazon.com/security-incident-response/pricing/").

## Troubleshooting

| Symptom                                       | Likely cause                                                          | Resolution                                                                                                  |
| --------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Membership status is Pending                  | Onboarding not completed                                              | Complete all setup steps. See [Getting started](getting-started.md "getting-started.md").                   |
| `list-memberships` returns empty              | CLI Region doesn't match subscription Region                          | Specify the Region where you activated: `--region `region``                                                 |
| Triage SLR not found in management account    | Onboarded via API/CLI without creating it                             | Create manually: `aws iam create-service-linked-role --aws-service-name "triage.security-ir.amazonaws.com"` |
| Member accounts missing from coverage         | SLR not deployed to member account                                    | Re-run proactive response setup from the Security Incident Response console                                 |
| EventBridge rules not present in an account   | Proactive response setup incomplete                                   | Re-run setup or check for StackSet failures in CloudFormation                                               |
| GuardDuty sample findings not processed       | Sample findings are filtered by automated triage (expected)           | Check archived findings in GuardDuty                                                                        |
| Test domain finding not archived after 15 min | EventBridge rules missing or disabled; GuardDuty not enabled          | Verify Steps 2 and 3                                                                                        |
| No cases after extended period                | All findings archived by triage (expected), or pipeline not connected | Check archived findings in GuardDuty. If none exist, verify EventBridge rules and proactive response.       |
| No GuardDuty findings being triaged           | GuardDuty not enabled or not generating findings                      | Verify GuardDuty is enabled: `aws guardduty list-detectors`                                                 |
| Service not processing findings               | Automated triage determined that the detected activity is expected    | Review GuardDuty *_Archived_<br>• findings and Security Hub CSPM `SUPPRESSED` findings                      |
| Team members not receiving notifications      | Incorrect email, communications disabled, or email in spam            | Verify email addresses and communication preferences; check spam folders                                    |
| Containment actions not executing             | StackSet not deployed or preference not submitted                     | Verify StackSet status in CloudFormation and confirm preference submitted via AWS Support                   |

## Related resources

- [Onboarding prerequisites](onboarding-prerequisites.md "onboarding-prerequisites.md")
- [Step 1: Enable AWS Security Incident Response](deploy-configure.md "deploy-configure.md")
- [Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md")
- [Contain](contain.md "contain.md")
- [Considerations and recommendations for using AWS Security Incident Response with AWS Organizations](considerations_important.md "considerations_important.md")
- [Enable Security Incident Response and configure your incident response team using the API/CLI](enable-sir-using-cli.md "enable-sir-using-cli.md")
- [AWS Security Incident Response pricing](https://aws.amazon.com/security-incident-response/pricing/ "https://aws.amazon.com/security-incident-response/pricing/")
- [Amazon GuardDuty pricing](https://aws.amazon.com/guardduty/pricing/ "https://aws.amazon.com/guardduty/pricing/")
