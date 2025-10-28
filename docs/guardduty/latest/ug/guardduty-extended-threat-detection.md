# GuardDuty Extended Threat Detection

GuardDuty Extended Threat Detection automatically detects multi-stage attacks that span
data sources, multiple types of AWS resources, and time, within an AWS account. With this capability, GuardDuty
focuses on the sequence of multiple events that it observes by monitoring different types of data sources. Extended Threat Detection correlates
these events to identify scenarios that present themselves as a potential threat
to your AWS environment, and then generates an attack sequence finding.

###### Topics

- [Attack sequence threat scenario examples](#extended-threat-detection-scenario-examples "#extended-threat-detection-scenario-examples")
- [How it works](#extended-threat-detection-how-it-works "#extended-threat-detection-how-it-works")
- [Enabling protection plans to maximize threat detection](#extended-threat-detection-related-gdu-protection-plans "#extended-threat-detection-related-gdu-protection-plans")
- [Extended Threat Detection in GuardDuty console](#extended-threat-detection-in-guardduty-console "#extended-threat-detection-in-guardduty-console")
- [Understanding and managing attack
  sequence findings](#extended-threat-detection-understanding-attack-sequence-findings "#extended-threat-detection-understanding-attack-sequence-findings")
- [Additional resources](#guardduty-extended-threat-detection-additional-resources "#guardduty-extended-threat-detection-additional-resources")

## Attack sequence threat scenario examples

Extended Threat Detection covers threat scenarios that involve compromise related to AWS credentials misuse, data
compromise attempts in Amazon S3 buckets, and container and Kubernetes resource compromise in
Amazon EKS clusters. A single finding can encompass an entire attack sequence. For example, the
following list describes the scenarios
that GuardDuty might detect:

**Example 1 - AWS credentials and Amazon S3 bucket data compromise**

- A threat actor gaining unauthorized access to a compute workload.
- The actor then performing a series of actions such as privilege escalation and establishing persistence.
- Finally, the actor exfiltrating data from an Amazon S3 resource.

**Example 2 - Amazon EKS cluster compromise**

- A threat actor attempts to exploit a container application within an Amazon EKS cluster.
- The actor uses that compromised container to obtain privileged service account tokens.
- The actor then leverages these elevated privileges to access sensitive Kubernetes secrets or AWS
  resources through pod identities.

Because of the nature of
the associated threat scenarios, GuardDuty considers all [Attack sequence finding
types](guardduty-attack-sequence-finding-types.md "guardduty-attack-sequence-finding-types.md")
as **Critical**.

The following video provides a demonstration of how you can use Extended Threat Detection.

## How it works

When you enable Amazon GuardDuty in your account in a specific AWS Region, Extended Threat Detection is also enabled by default.
There is no additional cost associated with the usage of Extended Threat Detection. By default, it correlates events across all [Foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md"). However,
when you enable more GuardDuty protection plans, such as S3 Protection, EKS Protection, and Runtime Monitoring, this will open additional types of
attack sequence detections by widening the range of event sources. This will potentially
help with a more comprehensive threat analysis and better detection of attack sequences.
For more information, see [Enabling protection plans to maximize threat detection](#extended-threat-detection-related-gdu-protection-plans "#extended-threat-detection-related-gdu-protection-plans").

GuardDuty correlates multiple events, including API activities and GuardDuty findings. These events are called
**Signals**.
Sometimes, there might be events in your environment that, on their own, don't present themselves
as a clear potential threat. GuardDuty terms them as _weak_ signals. With Extended Threat Detection, GuardDuty identifies when
a sequence of multiple actions align to a potentially suspicious activity, and generates an attack sequence finding in your
account. These multiple actions can include weak signals and already identified GuardDuty findings in your account.

###### Note

When correlating events for attack sequences, Extended Threat Detection doesn't consider archived findings,
including those findings that are automatically archived because of
[Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md"). This behavior ensures
that only active, relevant signals contribute to attack sequence detection. To ensure that you're
not impacted by this, review existing suppression rules in your account. For more information,
see [Using suppression rules with
Extended Threat Detection](findings_suppression-rule.md#using-suppression-rules-with-extended-threat-detection "findings_suppression-rule.md#using-suppression-rules-with-extended-threat-detection").

GuardDuty is also designed to identify potential in-progress or recent attack behaviors (within a 24-hour rolling time window)
in your account. For example, an attack could start by an actor gaining unintended access to a compute workload. The
actor would then perform a series of steps, including enumeration, escalation of privileges, and exfiltration
of AWS credentials. These credentials could potentially be used for further compromise or malicious access
to data.

## Enabling protection plans to maximize threat detection

For any GuardDuty account in a Region, the Extended Threat Detection capability gets enabled automatically. By default, this capability
takes into consideration the
multiple events across all [Foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md"). To benefit from this capability,
you don't need to enable all the [use-case
focused GuardDuty protection plans](what-is-guardduty.md#features-of-guardduty "what-is-guardduty.md#features-of-guardduty"). For example,
with foundational threat detection, GuardDuty can identify a potential attack sequence starting from IAM privilege
discovery activity on Amazon S3 APIs, and detect subsequent S3 control plane alterations, such as changes that make
bucket resource policy more permissive.

Extended Threat Detection is designed in a way that if you enable more protection plans, it helps GuardDuty correlate
more diverse signals across multiple data sources. This will potentially enhance the breadth of
security signals for comprehensive threat analysis and coverage of attack sequences. To identify
findings that could potentially be one of the multiple stages in an attack sequence, GuardDuty
**recommends** enabling specific protection plans – S3 Protection, EKS Protection,
and Runtime Monitoring (with EKS add-on).

###### Topics

- [Detecting attack sequences in Amazon EKS clusters](#extended-threat-detection-eks-clusters "#extended-threat-detection-eks-clusters")
- [Detecting attack sequences in Amazon S3 buckets](#extended-threat-detection-s3-buckets "#extended-threat-detection-s3-buckets")

### Detecting attack sequences in Amazon EKS clusters

GuardDuty correlated multiple security signals across EKS audit logs, runtime behavior of processes, and
AWS API activity to detect sophisticated attack patterns. To benefit from Extended Threat Detection for EKS, you must
enable at least one of these features – EKS Protection or Runtime Monitoring (with EKS add-on). EKS Protection monitors
control plane activities through audit logs, while Runtime Monitoring observes behaviors within containers.

For maximum coverage and comprehensive threat detection, GuardDuty recommends enabling both protection plans. Together,
they create a complete view of your EKS clusters, enabling GuardDuty to detect complex attack patterns. For example,
it can identify an anomalous deployment of a privileged
container (detected with EKS Protection), followed by persistence attempts, crypto-mining, and reverse shell
creation within that container (detected with Runtime Monitoring). GuardDuty represents these related events as a single, critical-severity
finding, called [AttackSequence:EKS/CompromisedCluster](guardduty-attack-sequence-finding-types.md#attack-sequence-eks-compromised-cluster "guardduty-attack-sequence-finding-types.md#attack-sequence-eks-compromised-cluster"). When you enable both the protection plans,
the attack sequence finding covers the following threat scenarios:

- Compromise of containers running vulnerable web applications
- Unauthorized access through misconfigured credentials
- Attempts to escalate privileges
- Suspicious API requests
- Attempts to access data maliciously

The following list provides details when these dedicated protection plans are enabled individually:

**EKS Protection**

Enabling EKS Protection gives GuardDuty an ability to detect attack sequences involving Amazon EKS cluster control
plane activities. This allows GuardDuty to correlate EKS audit logs and AWS API activity. For example,
GuardDuty can detect an attack sequence where an actor attempts unauthorized access to cluster secrets,
modifies Kubernetes role-based access control (RBAC) permissions, and creates privileged pods. For
more information about enabling this protection plan, see [EKS Protection](kubernetes-protection.md "kubernetes-protection.md").

**Runtime Monitoring for Amazon EKS**

Enabling Runtime Monitoring for Amazon EKS clusters gives GuardDuty an ability to enhance EKS attack sequence detection
with container-level visibility. This helps GuardDuty detect potential malicious processes, suspicious runtime behaviors,
and potential malware execution. For example, GuardDuty can detect an attack sequence where a container starts exhibiting
suspicious behavior, such as cryptomining processes or establishing connections
to known malicious endpoints. For more information about enabling this protection plan,
see [Runtime Monitoring](runtime-monitoring.md "runtime-monitoring.md").

If you don't enable EKS Protection or Runtime Monitoring, GuardDuty will not be able to generate individual
[EKS Protection finding
types](guardduty-finding-types-eks-audit-logs.md "guardduty-finding-types-eks-audit-logs.md")
or [Runtime Monitoring finding types](findings-runtime-monitoring.md "findings-runtime-monitoring.md"). Therefore,
GuardDuty will not be able to detect multi-stage attack sequences that involve associated findings.

### Detecting attack sequences in Amazon S3 buckets

Enabling S3 Protection gives GuardDuty an ability to detect attack sequences involving attempts to data compromise in your Amazon S3
buckets. Without S3 Protection, GuardDuty can detect when your S3 bucket resource policy becomes overly permissive. When you enable
S3 Protection, GuardDuty gains the ability to detect potential data exfiltration activities that may occur after your
S3 bucket becomes overly permissive.

If S3 Protection is not enabled, GuardDuty will not be able to generate individual
[S3 Protection finding types](guardduty_finding-types-s3.md "guardduty_finding-types-s3.md"). Therefore, GuardDuty will not be able to detect multi-stage attack sequences
that involve associated findings. For more information about enabling this protection plan, see [S3 Protection](s3-protection.md "s3-protection.md").

## Extended Threat Detection in GuardDuty console

By default, the Extended Threat Detection page in GuardDuty
console displays the **Status** as **Enabled**. With foundational threat detection,
the status represents that GuardDuty can detect a potential attack sequence involving IAM privilege discovery activity on Amazon S3
APIs and detecting subsequent S3 control plane alterations.

Use the following steps to access the Extended Threat Detection page in GuardDuty console:

1. You can open GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the left navigation pane, choose **Extended Threat Detection**.

This page provides details about the threat scenarios that Extended Threat Detection covers. 3. On the **Extended Threat Detection** page, view the **Related protection plans** section.
If you **want to** enable dedicated protection plans to enhance threat detection coverage in your
account, select **Configure** option for that protection plan.

## Understanding and managing attack

sequence findings

Attack sequence findings are just like other GuardDuty findings in your account.
You can view them on the **Findings** page in the GuardDuty console. For information about
viewing findings, see [Findings page in GuardDuty
console](guardduty_working-with-findings.md "guardduty_working-with-findings.md").

Similar to other GuardDuty findings, attack sequence findings are also automatically sent to Amazon EventBridge.
Based on your settings, attack sequence findings are also exported
to a publishing destination (Amazon S3 bucket). To set a new publishing destination or update an existing one, see
[Exporting generated findings to
Amazon S3](guardduty_exportfindings.md "guardduty_exportfindings.md").

## Additional resources

View the following sections to gain more understanding about attack sequences:

- After learning about Extended Threat Detection and attack sequences, you can generate sample attack sequence
  finding types by following the steps in [Sample findings](sample_findings.md "sample_findings.md").
- Learn about [Attack sequence finding
  types](guardduty-attack-sequence-finding-types.md "guardduty-attack-sequence-finding-types.md").
- Review findings and explore finding details associated with
  [Attack sequence
  finding details](guardduty_findings-summary.md#guardduty-extended-threat-detection-attack-sequence-finding-details "guardduty_findings-summary.md#guardduty-extended-threat-detection-attack-sequence-finding-details").
- Prioritize and address attack sequence finding types by following the steps for the associated impacted resources in
  [Remediating findings](guardduty_remediate.md "guardduty_remediate.md").
