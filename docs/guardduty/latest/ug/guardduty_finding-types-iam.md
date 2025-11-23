# GuardDuty IAM finding types

The following findings are specific to IAM entities and access keys and always have a
**Resource Type** of `AccessKey`. The severity and details
of the findings differ based on the finding type.

The findings listed here include the data sources and models used to generate that finding
type. For more information, see [GuardDuty foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md").

For all IAM-related findings, we recommend that you examine the entity in question and
ensure that their permissions follow the best practice of least privilege. If the activity
is unexpected, the credentials may be compromised. For information about remediating
findings, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

###### Topics

- [CredentialAccess:IAMUser/AnomalousBehavior](#credentialaccess-iam-anomalousbehavior "#credentialaccess-iam-anomalousbehavior")
- [DefenseEvasion:IAMUser/AnomalousBehavior](#defenseevasion-iam-anomalousbehavior "#defenseevasion-iam-anomalousbehavior")
- [DefenseEvasion:IAMUser/BedrockLoggingDisabled](#defenseevasion-iam-bedrockloggingdisabled "#defenseevasion-iam-bedrockloggingdisabled")
- [Discovery:IAMUser/AnomalousBehavior](#discovery-iam-anomalousbehavior "#discovery-iam-anomalousbehavior")
- [Exfiltration:IAMUser/AnomalousBehavior](#exfiltration-iam-anomalousbehavior "#exfiltration-iam-anomalousbehavior")
- [Impact:IAMUser/AnomalousBehavior](#impact-iam-anomalousbehavior "#impact-iam-anomalousbehavior")
- [InitialAccess:IAMUser/AnomalousBehavior](#initialaccess-iam-anomalousbehavior "#initialaccess-iam-anomalousbehavior")
- [PenTest:IAMUser/KaliLinux](#pentest-iam-kalilinux "#pentest-iam-kalilinux")
- [PenTest:IAMUser/ParrotLinux](#pentest-iam-parrotlinux "#pentest-iam-parrotlinux")
- [PenTest:IAMUser/PentooLinux](#pentest-iam-pentoolinux "#pentest-iam-pentoolinux")
- [Persistence:IAMUser/AnomalousBehavior](#persistence-iam-anomalousbehavior "#persistence-iam-anomalousbehavior")
- [Policy:IAMUser/RootCredentialUsage](#policy-iam-rootcredentialusage "#policy-iam-rootcredentialusage")
- [Policy:IAMUser/ShortTermRootCredentialUsage](#policy-iam-user-short-term-root-credential-usage "#policy-iam-user-short-term-root-credential-usage")
- [PrivilegeEscalation:IAMUser/AnomalousBehavior](#privilegeescalation-iam-anomalousbehavior "#privilegeescalation-iam-anomalousbehavior")
- [Recon:IAMUser/MaliciousIPCaller](#recon-iam-maliciousipcaller "#recon-iam-maliciousipcaller")
- [Recon:IAMUser/MaliciousIPCaller.Custom](#recon-iam-maliciousipcallercustom "#recon-iam-maliciousipcallercustom")
- [Recon:IAMUser/TorIPCaller](#recon-iam-toripcaller "#recon-iam-toripcaller")
- [Stealth:IAMUser/CloudTrailLoggingDisabled](#stealth-iam-cloudtrailloggingdisabled "#stealth-iam-cloudtrailloggingdisabled")
- [Stealth:IAMUser/PasswordPolicyChange](#stealth-iam-passwordpolicychange "#stealth-iam-passwordpolicychange")
- [UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B](#unauthorizedaccess-iam-consoleloginsuccessb "#unauthorizedaccess-iam-consoleloginsuccessb")
- [UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.InsideAWS](#unauthorizedaccess-iam-instancecredentialexfiltrationinsideaws "#unauthorizedaccess-iam-instancecredentialexfiltrationinsideaws")
- [UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS](#unauthorizedaccess-iam-instancecredentialexfiltrationoutsideaws "#unauthorizedaccess-iam-instancecredentialexfiltrationoutsideaws")
- [UnauthorizedAccess:IAMUser/MaliciousIPCaller](#unauthorizedaccess-iam-maliciousipcaller "#unauthorizedaccess-iam-maliciousipcaller")
- [UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom](#unauthorizedaccess-iam-maliciousipcallercustom "#unauthorizedaccess-iam-maliciousipcallercustom")
- [UnauthorizedAccess:IAMUser/TorIPCaller](#unauthorizedaccess-iam-toripcaller "#unauthorizedaccess-iam-toripcaller")

## CredentialAccess:IAMUser/AnomalousBehavior

### An API used to

gain access to an AWS environment was invoked in an anomalous way.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with the
credential access stage of an attack when an adversary is attempting to collect
passwords, usernames, and access keys for your environment. The APIs in this
category are `GetPasswordData`, `GetSecretValue`,
`BatchGetSecretValue`, and `GenerateDbAuthToken`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## DefenseEvasion:IAMUser/AnomalousBehavior

### An API used to

evade defensive measures was invoked in an anomalous way.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with defense
evasion tactics where an adversary is trying to cover their tracks and avoid
detection. APIs in this category are typically delete, disable, or stop
operations, such as, `DeleteFlowLogs`,
`DisableAlarmActions`, or `StopLogging`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## DefenseEvasion:IAMUser/BedrockLoggingDisabled

### Logging for Amazon Bedrock was disabled.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that logging was disabled for Bedrock model invocations in your account. This can be an attacker's attempt to hide malicious activity like data exfiltration or abuse of AI models. Disabling logging removes visibility into the data sent to models and how the models are used.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Discovery:IAMUser/AnomalousBehavior

### An API commonly used

to discover resources was invoked in an anomalous way.

**Default severity: Low**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with the
discovery stage of an attack when an adversary is gathering information to
determine if your AWS environment is susceptible to a broader attack. APIs in
this category are typically get, describe, or list operations, such as,
`DescribeInstances`, `GetRolePolicy`, or
`ListAccessKeys`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Exfiltration:IAMUser/AnomalousBehavior

### An API commonly

used to collect data from an AWS environment was invoked in an anomalous
way.

**Default severity: High**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with
exfiltration tactics where an adversary is trying to collect data from your
network using packaging and encryption to avoid detection. APIs for this finding
type are management (control-plane) operations only and are typically related to
S3, snapshots, and databases, such as, `PutBucketReplication`,
`CreateSnapshot`, or
`RestoreDBInstanceFromDBSnapshot`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Impact:IAMUser/AnomalousBehavior

### An API commonly used to

tamper with data or processes in an AWS environment was invoked in an
anomalous way.

**Default severity: High**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with impact
tactics where an adversary is trying to disrupt operations and manipulate,
interrupt, or destroy data in your account. APIs for this finding type are
typically delete, update, or put operations, such as,
`DeleteSecurityGroup`, `UpdateUser`, or
`PutBucketPolicy`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## InitialAccess:IAMUser/AnomalousBehavior

### An API commonly

used to gain unauthorized access to an AWS environment was invoked in an
anomalous way.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with the
initial access stage of an attack when an adversary is attempting to establish
access to your environment. APIs in this category are typically get token, or
session operations, such as,
`StartSession`, or `GetAuthorizationToken`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## PenTest:IAMUser/KaliLinux

### An API was invoked from a Kali

Linux machine.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that a machine running Kali Linux is making API calls
using credentials that belong to the listed AWS account in your environment.
Kali Linux is a popular penetration testing tool that security professionals use
to identify weaknesses in EC2 instances that require patching. Attackers also
use this tool to find EC2 configuration weaknesses and gain unauthorized access
to your AWS environment.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## PenTest:IAMUser/ParrotLinux

### An API was invoked from a

Parrot Security Linux machine.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that a machine running Parrot Security Linux is
making API calls using credentials that belong to the listed AWS account in
your environment. Parrot Security Linux is a popular penetration testing tool
that security professionals use to identify weaknesses in EC2 instances that
require patching. Attackers also use this tool to find EC2 configuration
weaknesses and gain unauthorized access to your AWS environment.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## PenTest:IAMUser/PentooLinux

### An API was invoked from a

Pentoo Linux machine.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that a machine running Pentoo Linux is making API
calls using credentials that belong to the listed AWS account in your
environment. Pentoo Linux is a popular penetration testing tool that security
professionals use to identify weaknesses in EC2 instances that require patching.
Attackers also use this tool to find EC2 configuration weaknesses and gain
unauthorized access to your AWS environment.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Persistence:IAMUser/AnomalousBehavior

### An API commonly used

to maintain unauthorized access to an AWS environment was invoked in an
anomalous way.

**Default severity: Medium**

- **Data source:** CloudTrail management
  event

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with
persistence tactics where an adversary has gained access to your environment and
is attempting to maintain that access. APIs in this category are typically
create, import, or modify operations, such as, `CreateAccessKey`,
`ImportKeyPair`, or `ModifyInstanceAttribute`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Policy:IAMUser/RootCredentialUsage

### An API was invoked

using root user sign-in credentials.

**Default severity: Low**

- **Data source:** CloudTrail management events
  or CloudTrail data events for S3

This finding informs you that the root user sign-in credentials of the listed
AWS account in your environment are being used to make requests to AWS
services. It is recommended that users never use root user sign-in credentials to
access AWS services. Instead, AWS services should be accessed using least
privilege temporary credentials from AWS Security Token Service (STS). For situations where AWS STS
is not supported, IAM user credentials are recommended. For more information,
see [IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

###### Note

If S3 Protection is enabled for the account, then this finding may be
generated in response to the attempts to run S3 data plane operations on Amazon S3
resources by using the root user sign-in credentials of the AWS account. The API
call used will be listed in the finding details. If S3 Protection is
not enabled, then this finding can only be triggered by Event log APIs. For more
information about S3 Protection, see [S3 Protection](s3-protection.md "s3-protection.md").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Policy:IAMUser/ShortTermRootCredentialUsage

### An API was invoked

by using restricted root user credentials.

**Default severity: Low**

- **Data source:** AWS CloudTrail management
  events or AWS CloudTrail data events for S3

This finding informs you that restricted user credentials created for
the listed AWS account in your environment, are being used
to make requests to AWS services. It is recommended to use root user
credentials only for those [tasks that require root user
credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

When possible, access the AWS services by using least privilege IAM roles with
temporary credentials from AWS Security Token Service (AWS STS). For scenarios where AWS STS is not supported,
the best practice is to use IAM user credentials. For more information,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
and [Root user best practices for your AWS account](../../../IAM/latest/UserGuide/root-user-best-practices.md "../../../IAM/latest/UserGuide/root-user-best-practices.md") in
the _IAM User Guide_.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## PrivilegeEscalation:IAMUser/AnomalousBehavior

### An API

commonly used to obtain high-level permissions to an AWS environment was
invoked in an anomalous way.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an anomalous API request was observed in your
account. This finding may include a single API or a series of related API
requests made in proximity by a single [user identity](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). The API observed is commonly associated with
privilege escalation tactics where an adversary is attempting to gain
higher-level permissions to an environment. APIs in this category typically
involve operations that change IAM policies, roles, and users, such as,
`AssociateIamInstanceProfile`, `AddUserToGroup`, or
`PutUserPolicy`.

This API request was identified as anomalous by GuardDuty's anomaly detection
machine learning (ML) model. The ML model evaluates all API requests in your
account and identifies anomalous events that are associated with techniques used
by adversaries. The ML model tracks various factors of the API request, such as,
the user that made the request, the location the request was made from, and the
specific API that was requested. Details on which factors of the API request are
unusual for the user identity that invoked the request can be found in the
[finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Recon:IAMUser/MaliciousIPCaller

### An API was invoked from a

known malicious IP address.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an API operation that can list or describe AWS
resources in an account within your environment was invoked from an IP address
that is included on a threat list. An attacker may use stolen credentials to
perform this type of reconnaissance of your AWS resources in order to find
more valuable credentials or determine the capabilities of the credentials they
already have.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Recon:IAMUser/MaliciousIPCaller.Custom

### An API was invoked

from a known malicious IP address.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an API operation that can list or describe AWS
resources in an account within your environment was invoked from an IP address
that is included on a custom threat list. The threat list used will be listed in
the finding's details. An attacker might use stolen credentials to perform this
type of reconnaissance of your AWS resources in order to find more valuable
credentials or determine the capabilities of the credentials they already
have.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Recon:IAMUser/TorIPCaller

### An API was invoked from a Tor

exit node IP address.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an API operation that can list or describe AWS
resources in an account within your environment was invoked from a Tor exit node
IP address. Tor is software for enabling anonymous communication. It encrypts
and randomly bounces communications through relays between a series of network
nodes. The last Tor node is called the exit node. An attacker would use Tor to
mask their true identity.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Stealth:IAMUser/CloudTrailLoggingDisabled

### AWS CloudTrail logging

was disabled.

**Default severity: Low**

- **Data source:** CloudTrail management
  events

This finding informs you that a CloudTrail trail within your AWS environment was
disabled. This can be an attacker's attempt to disable logging to cover their
tracks by eliminating any trace of their activity while gaining access to your
AWS resources for malicious purposes. This finding can be triggered by a
successful deletion or update of a trail. This finding can also be triggered by
a successful deletion of an S3 bucket that stores the logs from a trail that is
associated with GuardDuty.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Stealth:IAMUser/PasswordPolicyChange

### Account password

policy was weakened.

**Default severity: Low\***

###### Note

This finding's severity can be Low, Medium, or High depending on the
severity of the changes made to password policy.

- **Data source:** CloudTrail management
  events

The AWS account password policy was weakened on the listed account within
your AWS environment. For example, it was deleted or updated to require fewer
characters, not require symbols and numbers, or required to extend the password
expiration period. This finding can also be triggered by an attempt to update or
delete your AWS account password policy. The AWS account password policy
defines the rules that govern what kinds of passwords can be set for your
IAM users. A weaker password policy permits the creation of passwords that are
easy to remember and potentially easier to guess, thereby creating a security
risk.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B

### Multiple

worldwide successful console logins were observed.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that multiple successful console logins for the same
IAM user were observed around the same time in various geographical locations.
Such anomalous and risky access location patterns indicate potential
unauthorized access to your AWS resources.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.InsideAWS

### Credentials that were created exclusively for an EC2 instance through an

Instance launch role are being used from another account within AWS.

**Default severity: High\***

###### Note

This finding's default severity is High. However, if the API was invoked
by an account affiliated with your AWS environment, the severity is
Medium.

- **Data source:** CloudTrail management events
  or CloudTrail data events for S3

This finding informs you when your Amazon EC2 instance credentials are used to
invoke APIs from an IP address or an Amazon VPC endpoint, that is owned by a different
AWS account than the one that the associated Amazon EC2 instance is running in.
VPC endpoint detection is only available for services
that support network activity events for VPC endpoints. For information about
services that support network activity events for VPC endpoints, see
[Logging
network activity events](../../../awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.md") in the _AWS CloudTrail User Guide_.

AWS does not recommend redistributing temporary credentials outside of the
entity that created them (for example, AWS applications, Amazon EC2, or AWS Lambda).
However, authorized users can export credentials from their Amazon EC2 instances to
make legitimate API calls. If the `remoteAccountDetails.Affiliated`
field is `True` the API was invoked from an account associated with the
same administrator account. To rule out a potential attack and verify the legitimacy
of the activity, contact the AWS account owner or IAM principal to whom these credentials are
assigned.

###### Note

If GuardDuty observes continued activity from a remote account, its machine
learning (ML) model will identify this as an expected behavior. Therefore,
GuardDuty will stop generating this finding for activity from that remote
account. GuardDuty will continue to generate findings for new behavior from
other remote accounts and will re-evaluate learned remote accounts as the
behavior changes over time.

**Remediation recommendations:**

This finding gets generated when AWS
API requests are made inside AWS through an Amazon EC2 instance outside of your
AWS account, by using your Amazon EC2 instance's session credentials. It may
be customary, such as for Transit Gateway architecture in a [hub and spoke](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-vpc-solution.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-vpc-solution.md") configuration, to route
traffic through a single hub egress VPC with AWS service endpoints. If this behavior is expected,
then GuardDuty recommends you to use [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md") and create a rule with a two-filter criteria. The
first criteria is the finding type, which, in this case, is
UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.InsideAWS. The
second filter criteria is the remote account ID of the remote account details.

In response to this finding you can use the following workflow to determine a
course of action:

1. Identify the remote account involved from the
   `service.action.awsApiCallAction.remoteAccountDetails.accountId`
   field.
2. Determine if that account is affiliated with your GuardDuty
   environment from the
   `service.action.awsApiCallAction.remoteAccountDetails.affiliated`
   field.
3. If the account **is** affiliated, contact the remote account owner and
   the owner of the Amazon EC2 instance credentials to investigate.

If the account **is not** affiliated, then
the first step is to evaluate if that account is
associated with your organization but is not a part of your GuardDuty
multiple-account environment set up, or if GuardDuty has not yet been enabled in this
account. Next, contact the owner of the Amazon EC2 instance
credentials to determine if there is a use case for a remote account to use these
credentials. 4. If the owner of the credentials does not recognize the remote account
the credentials may have been compromised by a threat actor operating
within AWS. You should take the steps recommended in [Remediating a potentially compromised Amazon EC2
instance](compromised-ec2.md "compromised-ec2.md"), to
secure your environment.

Additionally, you can [submit
an abuse report](https://support.aws.amazon.com/#/contacts/report-abuse "https://support.aws.amazon.com/#/contacts/report-abuse") to the AWS Trust and Safety team to begin
an investigation into the remote account. When submitting your report to
AWS Trust and Safety, include the full JSON details of the
finding.

## UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS

### Credentials that were created exclusively for an EC2 instance through an

Instance launch role are being used from an external IP address.

**Default severity: High**

- **Data source:** CloudTrail management events
  or CloudTrail data events for S3

This finding informs you that a host outside of AWS has attempted to run
AWS API operations using temporary AWS credentials that were created on an
EC2 instance in your AWS environment. The listed EC2 instance might be
compromised, and the temporary credentials from this instance might have been
exfiltrated to a remote host outside of AWS. AWS does not recommend
redistributing temporary credentials outside of the entity that created them
(for example, AWS applications, EC2, or Lambda). However, authorized users can
export credentials from their EC2 instances to make legitimate API calls. To
rule out a potential attack and verify the legitimacy of the activity, validate
if the use of instance credentials from the remote IP in the finding is
expected.

###### Note

If GuardDuty observes continued activity from a remote account, its machine
learning (ML) model will identify this as an expected behavior. Therefore,
GuardDuty will stop generating this finding for activity from that remote
account. GuardDuty will continue to generate findings for new behavior from
other remote accounts and will re-evaluate learned remote accounts as the
behavior changes over time.

**Remediation recommendations:**

This finding is generated when networking is configured to route internet
traffic such that it egresses from an on-premises gateway rather than from a VPC
Internet Gateway (IGW). Common configurations, such as using [AWS Outposts](../../../outposts/latest/userguide.md "../../../outposts/latest/userguide.md"), or VPC
VPN connections, can result in traffic routed this way. If this is expected
behavior, we recommend that you use suppression rules and create a rule that
consists of two filter criteria. The first criteria is **finding
type**, which should be
`UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS`.
The second filter criteria is **API caller IPv4 Address** with
the IP address or CIDR range of your on-premises internet gateway. To learn more
about creating suppression rules see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").

###### Note

If GuardDuty observes continued activity from an external source its machine
learning model will identify this as expected behavior and stop generating
this finding for activity from that source. GuardDuty will continue to generate
findings for new behavior from other sources, and will reevaluate learned
sources as behavior changes over time.

If this activity is unexpected your credentials may be compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## UnauthorizedAccess:IAMUser/MaliciousIPCaller

### An API was

invoked from a known malicious IP address.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an API operation (for example, an attempt to
launch an EC2 instance, create a new IAM user, or modify your AWS
privileges) was invoked from a known malicious IP address. This can indicate
unauthorized access to AWS resources within your environment.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom

### An API

was invoked from an IP address on a custom threat list.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an API operation (for example, an attempt to
launch an EC2 instance, create a new IAM user, or modify AWS privileges) was
invoked from an IP address that is included on a threat list that you uploaded.
In GuardDuty, a threat list consists of known malicious IP addresses. This can indicate
unauthorized access to AWS resources within your environment.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## UnauthorizedAccess:IAMUser/TorIPCaller

### An API was invoked

from a Tor exit node IP address.

**Default severity: Medium**

- **Data source:** CloudTrail management
  events

This finding informs you that an API operation (for example, an attempt to
launch an EC2 instance, create a new IAM user, or modify your AWS
privileges) was invoked from a Tor exit node IP address. Tor is software for
enabling anonymous communication. It encrypts and randomly bounces
communications through relays between a series of network nodes. The last Tor
node is called the exit node. This can indicate unauthorized access to your
AWS resources with the intent of hiding the attacker's true identity.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").
