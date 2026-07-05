# What is AWS Security Incident Response?

AWS Security Incident Response is a managed security service that monitors your AWS environment for threats,
triages security findings on your behalf, and engages you only when action is required. When
a genuine security incident occurs, the Security Incident Response Engineering team investigates,
helps contain the threat, and provides guidance toward recovery.

AWS Security Incident Response covers the full incident lifecycle: detection, triage, investigation, containment,
and recovery guidance. The service aligns with the NIST 800-61 Computer Security Incident
Handling Guide, providing a consistent approach to security event management grounded in
industry best practices. It works alongside other AWS Detection and Response services and
integrates with your existing tools through Amazon EventBridge.

###### Topics

- [How it works](#how-it-works "#how-it-works")
- [Triage and deduplication](#triage-and-deduplication "#triage-and-deduplication")
- [Log access](#log-access "#log-access")
- [Suppression rules](#suppression-rules "#suppression-rules")
- [Automated and human investigation](#automated-and-human-investigation "#automated-and-human-investigation")
- [Continuous improvement](#continuous-improvement "#continuous-improvement")
- [Proactive and reactive cases](#proactive-and-reactive-cases "#proactive-and-reactive-cases")
- [Containment](#containment-overview "#containment-overview")
- [Watchers and case sharing](#watchers-and-case-sharing "#watchers-and-case-sharing")
- [Communication and case management](#communication-and-case-management "#communication-and-case-management")
- [Monitored accounts](#monitored-accounts "#monitored-accounts")
- [Integrations](#integrations "#integrations")
- [APIs and self-service](#apis-and-self-service "#apis-and-self-service")
- [Monthly reports](#monthly-reports "#monthly-reports")
- [Preparedness](#preparedness "#preparedness")
- [Service boundaries](#service-boundaries "#service-boundaries")
- [Your responsibilities](#your-responsibilities "#your-responsibilities")
- [Getting assistance](#getting-assistance "#getting-assistance")
- [Supported Regions](#supported-regions-summary "#supported-regions-summary")

## How it works

AWS Security Incident Response doesn't generate security findings. It ingests findings from detection
sources you already have (Amazon GuardDuty, third-party tools integrated through AWS Security Hub CSPM)
and triages them on your behalf.

The service ingests all findings from configured sources but doesn't triage them all
equally. An automated system evaluates whether each finding represents a genuine security
threat and contains sufficient context for investigation. Findings that pass this evaluation
proceed through a multi-stage triage process that combines automation, threat intelligence,
and human expertise.

AWS Security Incident Response only triages threat detection findings. Security posture or compliance
findings (such as misconfiguration alerts or benchmark violations) aren't triaged because
they describe a state about your environment rather than an active threat requiring
investigation.

## Triage and deduplication

Triage and deduplication are at the core of the service. AWS Security Incident Response analyzes findings,
correlates related signals, and eliminates duplicates so your team doesn't have to.

The service escalates to you only when your involvement is required. Across all
customers, less than 1% of ingested findings result in a customer-facing escalation. When
the service escalates, it means the finding requires your attention. There's no option to
mute or suppress these notifications because each one represents a validated concern that
requires action.

The triage process is dynamic. A finding evaluated as expected behavior today can be
re-evaluated differently tomorrow if context changes. This is fundamentally different from
a static suppression rule. AWS Security Incident Response prefers triage over suppression because it preserves
the ability to detect evolving threats.

## Log access

Security Incident Response accesses control plane logging only during an active investigation for the
purpose of that investigation. Log data isn't provided to customers. Only summaries and
conclusions are shared through case notes.

## Suppression rules

In rare cases, when both you and the Security Incident Response Engineering team agree
that a specific type of alert no longer needs monitoring, a suppression rule is deployed.
Suppressed alerts aren't ingested or monitored in the future. You can see suppression
rules in the GuardDuty or Security Hub CSPM console, and Security Incident Response notifies your Incident Response team when
rules are created or modified. Changes are rolled back upon request.

Suppression rules are used sparingly because suppressed findings are permanently
excluded from monitoring, whereas triaged findings remain under dynamic evaluation.
Security Incident Response engineers always discuss this with you before implementing a rule.

## Automated and human investigation

When automated triage can't determine that activity is expected, the AWS Security Incident Response Engineering team is engaged. This is a global, always-available team of security
professionals with expertise in AWS and security incident response.

During an investigation, engineers analyze service metadata and threat intelligence,
review insights from past findings in your environment, and apply incident response
expertise. As part of a security investigation, Security Incident Response can also collect investigative data
from within Amazon Elastic Compute Cloud instances using EC2 Triage (when enabled), without requiring direct
access to the instance.

## Continuous improvement

AWS Security Incident Response incorporates feedback and lessons learned from prior engagements to enhance
detection capabilities, investigative processes, and triage accuracy. As the team
investigates incidents across all customers, it develops responder-generated intelligence:
indicators of compromise (IoCs), tactics, techniques, and procedures (TTPs), and associated
patterns observed during investigations. This intelligence feeds back into the triage
process, improving the ability to detect and respond to evolving threats over time.

The effectiveness of the service improves with your collaboration. By actively engaging
and providing timely responses during investigations, you help the team understand your
environment and expected behaviors, reduce false positive detections, and ensure rapid
response to genuine incidents.

## Proactive and reactive cases

AWS Security Incident Response provides two types of cases:

**Proactive cases:** Created automatically when the triage
process identifies a genuine threat that requires your involvement. These cases carry a
"[Proactive case]" prefix in their title. No manual configuration is required beyond
enabling detection sources. When a proactive case is created, all configured stakeholders
are notified automatically.

**Reactive cases:** Cases you create when you need
assistance. There are two subtypes:

- **AWS-supported:** Escalated directly to
  Security Incident Response Engineering for investigation and guidance. These cases carry
  a 15-minute SLO for initial engagement. There's no limit on the number of reactive
  cases you can open.
- **Self-managed:** Kept internal to your
  organization for tracking and documentation. You can escalate a self-managed case to
  Security Incident Response Engineering at any time.

**24/7 availability:** Engineers respond to both proactive
and reactive cases. AWS-supported reactive cases carry a 15-minute initial response
SLO.

Both case types use the same data fields and case management portal.

## Containment

When pre-authorized, Security Incident Response engineers execute containment actions
on your behalf during active incidents. Supported containment actions include runbooks for
compromised Amazon S3 buckets, Amazon EC2 instances, and IAM principals.

If you haven't pre-authorized containment, engineers provide manual guidance during
investigations. For more information, see
[Containment
actions](contain.md "contain.md").

## Watchers and case sharing

You can grant case visibility to external parties using watchers or IAM policies.
This lets you include partners, risk and compliance teams, legal counsel, or subject matter
experts in your investigations.

Watchers receive notifications for all updates to a specific case. Each case includes
a pre-populated IAM policy scoped to that case, maintaining least-privilege access for
third-party participants.

## Communication and case management

All cases are managed through your Membership account, which centralizes communication
for all organizational accounts in one place. Communication during an investigation may
include acknowledgment of a security event, establishing a call bridge, analysis of
artifacts, requests for confirmation of expected activity, and sharing of investigation
results. Video calls are available during active security events.

Only you can close a case. AWS Security Incident Response can set a case to "Ready to Close" status, but
final closure is always your action.

## Monitored accounts

Only accounts enrolled in your membership are monitored and investigated. You choose
coverage at the AWS organization or OU level during enablement. Accounts outside your
configured scope aren't monitored. For more information, see
[Step 1:
Enable AWS Security Incident Response](deploy-configure.md "deploy-configure.md").

## Integrations

AWS Security Incident Response integrates with your existing workflows through Amazon EventBridge. Every case
lifecycle event is published to EventBridge, allowing you to build automations that connect to
any tool or process you use.

Documented integration patterns are available for:

- Jira
- Slack
- ServiceNow

You can also build custom integrations for any other tool using the EventBridge events. For
more information, see
[EventBridge
integration](EventBridge.md "EventBridge.md").

## APIs and self-service

AWS Security Incident Response provides APIs that allow you to integrate the service into your own
workflows, retrieve case information programmatically, and build customized security
solutions on top of the service. For more information, see the
[AWS Security Incident Response API
Reference](../APIReference.md "../APIReference.md").

## Monthly reports

AWS Security Incident Response delivers monthly reports summarizing activity across your accounts. These
reports provide visibility into findings ingested, triage outcomes, and cases created. For
more information, see
[Monthly
reports](monthly-report.md "monthly-report.md").

## Preparedness

During onboarding, you configure your Incident Response team with designated
individuals or groups who receive notifications when cases are created. Permission policies
define what access team members have within a case. Setting this up in advance ensures
rapid response when an incident occurs.

## Service boundaries

AWS Security Incident Response isn't a detection service — it doesn't generate findings or replace GuardDuty,
Security Hub CSPM, or third-party detection tools. It ingests and triages what those services produce.
It isn't an alert aggregator — unlike services that pass all alerts through to you, it
absorbs the vast majority of findings and only escalates the ones that require your action.
It doesn't triage security posture findings — compliance and configuration findings are
informational by nature and don't require threat investigation.

The following activities are also not covered:

| Activity                               | Description                                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **General security guidance**          | Proactive security assessments, architecture reviews, penetration testing,<br>and vulnerability scanning.     |
| **Threat hunting**                     | Proactive searching for threats that haven't generated a detection<br>finding.                                |
| **Forensic disk or endpoint analysis** | Full disk imaging, memory analysis, or endpoint forensics. Engineers<br>perform log-based investigation only. |
| **Custom reporting**                   | Reports outside the standard case notes format.                                                               |
| **Legal and regulatory guidance**      | Guidance on breach notification, regulatory filings, or other legal<br>obligations.                           |
| **Recovery and remediation execution** | Running recovery or remediation actions on your resources. Engineers<br>provide recommendations only.         |
| **Attribution**                        | Identifying the specific threat actor or group behind an<br>incident.                                         |

## Your responsibilities

- **Respond to validation requests promptly:**
  When engineers contact you to validate information, respond in a timely manner. If you
  don't respond, the investigation might be placed on hold.
- **Designate a security contact:** Provide
  and maintain an up-to-date security contact who receives notifications during active
  investigations.
- **Enable logging:** Enable AWS CloudTrail,
  Amazon VPC Flow Logs, and other relevant logging. Comprehensive logging reduces investigation
  timelines.
- **Review and implement recommendations:**
  After receiving containment and remediation recommendations, implement them to resolve
  the event and prevent recurrence.

## Getting assistance

If you have a request outside the scope of AWS Security Incident Response, see the following
resources.

| Need                                | Resource                                                                                                                                                                                                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Security posture assessments        | [AWS<br>Professional Services](https://aws.amazon.com/professional-services/ "https://aws.amazon.com/professional-services/")                                                                                                                                         |
| Compliance and audit                | [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/"),<br>[AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/")                                                                            |
| General security guidance           | [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/"),<br>[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/") |
| DDoS protection                     | [AWS Shield](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/")                                                                                                                                                                                         |
| AWS service-side event explanations | [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")                                                                                                                                                                        |

## Supported Regions

AWS Security Incident Response supports the following language and region configurations:

- Language: AWS Security Incident Response provides dedicated English support. Japanese language support is limited
  to Japan Standard Time business hours and comes with specific restrictions:

###### Note

Japanese language support is provided on a best-effort basis during business hours
(09:00-17:00, Monday-Friday, excluding holidays)

- Supported AWS Regions:

AWS Security Incident Response is available in a subset of AWS Regions. In these supported Regions,
you create a membership, create and view cases, and access the dashboard.

    + US East (Ohio)
    + US West (Oregon)
    + US East (Virginia)
    + Europe (Frankfurt)
    + Europe (Ireland)
    + Europe (London)
    + Europe (Milan)
    + Europe (Paris)
    + Europe (Spain)
    + Europe (Stockholm)
    + Europe (Zurich)
    + Asia Pacific (Hong Kong)
    + Asia Pacific (Hyderabad)
    + Asia Pacific (Jakarta)
    + Asia Pacific (Melbourne)
    + Asia Pacific (Mumbai)
    + Asia Pacific (Seoul)
    + Asia Pacific (Singapore)
    + Asia Pacific (Sydney)
    + Asia Pacific (Tokyo)
    + Canada (Central)
    + Middle East (Bahrain)
    + Middle East (UAE)
    + South America (São Paulo)
    + Africa (Cape Town)

When you enable the monitoring and investigation feature, AWS Security Incident Response monitors Amazon GuardDuty findings from all
active commercial AWS Regions. As a security best practice, AWS recommends enabling GuardDuty in all
supported AWS Regions. This configuration allows GuardDuty to generate findings about unauthorized or unusual
activity, even in AWS Regions where you don't actively deploy resources. By doing so, you enhance your overall
security posture and maintain comprehensive threat detection coverage across your AWS environment.

###### Note

Amazon GuardDuty reports findings for configured regions. If you don't enable the service in
a specific AWS Region, then alerts aren't available.
