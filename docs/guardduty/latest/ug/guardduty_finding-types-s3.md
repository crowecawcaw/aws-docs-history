# GuardDuty S3 Protection finding types

The following findings are specific to Amazon S3 resources and will have a **Resource
Type** of `S3Bucket` if the data source is **CloudTrail data events for S3**, or `AccessKey` if the data source is
**CloudTrail management events**. The severity and details of the
findings will differ based on the finding type and the permission associated with the
bucket.

The findings listed here include the data sources and models used to generate that finding
type. For more information data sources and models, see [GuardDuty foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md").

###### Important

Findings with a data source of **CloudTrail data events for
S3** are only generated if you have enabled S3 Protection. By default, after July
31, 2020, S3 Protection is enabled when an account enables GuardDuty for the first time, or when a
delegated GuardDuty administrator account enables GuardDuty in an existing member account. However, when a new member joins
the GuardDuty organization, the organization's auto-enable preferences will apply. For
information about auto-enable preferences, see [Setting organization auto-enable
preferences](set-guardduty-auto-enable-preferences.md "set-guardduty-auto-enable-preferences.md"). For information about how
to enable S3 Protection, see [GuardDuty S3 Protection](s3-protection.md "s3-protection.md")

For all `S3Bucket` type findings, it is recommended that you examine the
permissions on the bucket in question and the permissions of any users involved in the
finding, if the activity is unexpected see the remediation recommendations detailed in [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

###### Topics

- [Discovery:S3/AnomalousBehavior](#discovery-s3-anomalousbehavior "#discovery-s3-anomalousbehavior")
- [Discovery:S3/MaliciousIPCaller](#discovery-s3-maliciousipcaller "#discovery-s3-maliciousipcaller")
- [Discovery:S3/MaliciousIPCaller.Custom](#discovery-s3-maliciousipcallercustom "#discovery-s3-maliciousipcallercustom")
- [Discovery:S3/TorIPCaller](#discovery-s3-toripcaller "#discovery-s3-toripcaller")
- [Exfiltration:S3/AnomalousBehavior](#exfiltration-s3-anomalousbehavior "#exfiltration-s3-anomalousbehavior")
- [Exfiltration:S3/MaliciousIPCaller](#exfiltration-s3-maliciousipcaller "#exfiltration-s3-maliciousipcaller")
- [Impact:S3/AnomalousBehavior.Delete](#impact-s3-anomalousbehavior-delete "#impact-s3-anomalousbehavior-delete")
- [Impact:S3/AnomalousBehavior.Permission](#impact-s3-anomalousbehavior-permission "#impact-s3-anomalousbehavior-permission")
- [Impact:S3/AnomalousBehavior.Write](#impact-s3-anomalousbehavior-write "#impact-s3-anomalousbehavior-write")
- [Impact:S3/MaliciousIPCaller](#impact-s3-maliciousipcaller "#impact-s3-maliciousipcaller")
- [PenTest:S3/KaliLinux](#pentest-s3-kalilinux "#pentest-s3-kalilinux")
- [PenTest:S3/ParrotLinux](#pentest-s3-parrotlinux "#pentest-s3-parrotlinux")
- [PenTest:S3/PentooLinux](#pentest-s3-pentoolinux "#pentest-s3-pentoolinux")
- [Policy:S3/AccountBlockPublicAccessDisabled](#policy-s3-accountblockpublicaccessdisabled "#policy-s3-accountblockpublicaccessdisabled")
- [Policy:S3/BucketAnonymousAccessGranted](#policy-s3-bucketanonymousaccessgranted "#policy-s3-bucketanonymousaccessgranted")
- [Policy:S3/BucketBlockPublicAccessDisabled](#policy-s3-bucketblockpublicaccessdisabled "#policy-s3-bucketblockpublicaccessdisabled")
- [Policy:S3/BucketPublicAccessGranted](#policy-s3-bucketpublicaccessgranted "#policy-s3-bucketpublicaccessgranted")
- [Stealth:S3/ServerAccessLoggingDisabled](#stealth-s3-serveraccessloggingdisabled "#stealth-s3-serveraccessloggingdisabled")
- [UnauthorizedAccess:S3/MaliciousIPCaller.Custom](#unauthorizedaccess-s3-maliciousipcallercustom "#unauthorizedaccess-s3-maliciousipcallercustom")
- [UnauthorizedAccess:S3/TorIPCaller](#unauthorizedaccess-s3-toripcaller "#unauthorizedaccess-s3-toripcaller")

## Discovery:S3/AnomalousBehavior

### An API commonly used to

discover S3 objects was invoked in an anomalous way.

**Default severity: Low**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an IAM entity has invoked an S3 API to
discover S3 buckets in your environment, such as `ListObjects`. This
type of activity is associated with the discovery stage of an attack wherein an
attacker gathers information to determine if your AWS environment is
susceptible to a broader attack. This activity is suspicious because the IAM
entity invoked the API in an unusual way. For example, an IAM entity with no
previous history invokes an S3 API, or an IAM entity invokes an S3 API from an
unusual location.

This API was identified as anomalous by GuardDuty's anomaly detection machine
learning (ML) model. The ML model evaluates all the API requests in your account
and identifies anomalous events that are associated with techniques used by
adversaries. It tracks various factors of the API requests, such as the user who
made the request, the location from which the request was made, the specific API
that was requested, the bucket that was requested, and the number of API calls
made. For more information on which factors of the API request are unusual for
the user identity that invoked the request, see [Finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Discovery:S3/MaliciousIPCaller

### An S3 API commonly used

to discover resources in an AWS environment was invoked from a known malicious
IP address.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API operation was invoked from an IP
address that is associated with known malicious activity. The observed API is
commonly associated with the discovery stage of an attack when an adversary is
gathering information about your AWS environment. Examples include
`GetObjectAcl` and `ListObjects`.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Discovery:S3/MaliciousIPCaller.Custom

### An S3 API was

invoked from an IP address on a custom threat list.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API, such as `GetObjectAcl` or
`ListObjects`, was invoked from an IP address that is included on
a threat list that you uploaded. The threat list associated with this finding is
listed in the **Additional information** section of a finding's
details. This type of activity is associated with the discovery stage of an
attack wherein an attacker is gathering information to determine if your AWS
environment is susceptible to a broader attack.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Discovery:S3/TorIPCaller

### An S3 API was invoked from a

Tor exit node IP address.

**Default severity: Medium**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API, such as `GetObjectAcl` or
`ListObjects`, was invoked from a Tor exit node IP address. This
type of activity is associated with the discovery stage of an attack wherein an
attacker is gathering information to determine if your AWS environment is
susceptible to a broader attack. Tor is software for enabling anonymous
communication. It encrypts and randomly bounces communications through relays
between a series of network nodes. The last Tor node is called the exit node.
This can indicate unauthorized access to your AWS resources with the intent of
hiding the attacker's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Exfiltration:S3/AnomalousBehavior

### An IAM entity

invoked an S3 API in a suspicious way.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an IAM entity is making API calls that involve
an S3 bucket and this activity differs from that entity's established baseline.
The API call used in this activity is associated with the exfiltration stage of
an attack, wherein an attacker attempts to collect data. This activity is
suspicious because the IAM entity invoked the API in an unusual way. For
example, an IAM entity with no previous history invokes an S3 API, or an IAM
entity invokes an S3 API from an unusual location.

This API was identified as anomalous by GuardDuty's anomaly detection machine
learning (ML) model. The ML model evaluates all the API requests in your account
and identifies anomalous events that are associated with techniques used by
adversaries. It tracks various factors of the API requests, such as the user who
made the request, the location from which the request was made, the specific API
that was requested, the bucket that was requested, and the number of API calls
made. For more information on which factors of the API request are unusual for
the user identity that invoked the request, see [Finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Exfiltration:S3/MaliciousIPCaller

### An S3 API commonly

used to collect data from an AWS environment was invoked from a known
malicious IP address.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API operation was invoked from an IP
address that is associated with known malicious activity. The observed API is
commonly associated with exfiltration tactics where an adversary is trying to
collect data from your network. Examples include `GetObject` and
`CopyObject`.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Impact:S3/AnomalousBehavior.Delete

### An IAM entity

invoked an S3 API that attempts to delete data in a suspicious way.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an IAM entity in your AWS environment is
making API calls that involve an S3 bucket, and this behavior differs from that
entity's established baseline. The API call used in this activity is associated
with an attack that attempts to delete data. This activity is suspicious because
the IAM entity invoked the API in an unusual way. For example, an IAM entity
with no previous history invokes an S3 API, or an IAM entity invokes an S3 API
from an unusual location.

This API was identified as anomalous by GuardDuty's anomaly detection machine
learning (ML) model. The ML model evaluates all the API requests in your account
and identifies anomalous events that are associated with techniques used by
adversaries. It tracks various factors of the API requests, such as the user who
made the request, the location from which the request was made, the specific API
that was requested, the bucket that was requested, and the number of API calls
made. For more information on which factors of the API request are unusual for
the user identity that invoked the request, see [Finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

We recommend an audit of your S3 bucket's contents to determine if you the
previous object version can or should be restored.

## Impact:S3/AnomalousBehavior.Permission

### An API commonly

used to set the access control list (ACL) permissions was invoked in an
anomalous way.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an IAM entity in your AWS environment has
updated a bucket policy or ACL on the listed S3 buckets. This change may
publicly expose your S3 buckets to all the authenticated AWS users.

This API was identified as anomalous by GuardDuty's anomaly detection machine
learning (ML) model. The ML model evaluates all the API requests in your account
and identifies anomalous events that are associated with techniques used by
adversaries. It tracks various factors of the API requests, such as the user who
made the request, the location from which the request was made, the specific API
that was requested, the bucket that was requested, and the number of API calls
made. For more information on which factors of the API request are unusual for
the user identity that invoked the request, see [Finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

We recommend an audit of your S3 bucket's contents to ensure that no objects
were unexpectedly allowed to be accessed publicly.

## Impact:S3/AnomalousBehavior.Write

### An IAM entity

invoked an S3 API that attempts to write data in a suspicious way.

**Default severity: Medium**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an IAM entity in your AWS environment is
making API calls that involve an S3 bucket, and this behavior differs from that
entity's established baseline. The API call used in this activity is associated
with an attack that attempts to write data. This activity is suspicious because
the IAM entity invoked the API in an unusual way. For example, an IAM entity
with no previous history invokes an S3 API, or an IAM entity invokes an S3 API
from an unusual location.

This API was identified as anomalous by GuardDuty's anomaly detection machine
learning (ML) model. The ML model evaluates all the API requests in your account
and identifies anomalous events that are associated with techniques used by
adversaries. It tracks various factors of the API requests, such as the user who
made the request, the location from which the request was made, the specific API
that was requested, the bucket that was requested, and the number of API calls
made. For more information on which factors of the API request are unusual for
the user identity that invoked the request, see [Finding details](guardduty_findings-summary.md#finding-anomalous "guardduty_findings-summary.md#finding-anomalous").

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

We recommend an audit of your S3 bucket's contents to ensure that this API
call didn't write malicious or unauthorized data.

## Impact:S3/MaliciousIPCaller

### An S3 API commonly used to

tamper with data or processes in an AWS environment was invoked from a known
malicious IP address.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API operation was invoked from an IP
address that is associated with known malicious activity. The observed API is
commonly associated with impact tactics where an adversary is trying manipulate,
interrupt, or destroy data within your AWS environment. Examples include
`PutObject` and `PutObjectAcl`.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## PenTest:S3/KaliLinux

### An S3 API was invoked from a Kali

Linux machine.

**Default severity: Medium**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that a machine running Kali Linux is making S3 API
calls using credentials that belong to your AWS account. Your credentials
might be compromised. Kali Linux is a popular penetration testing tool that
security professionals use to identify weaknesses in EC2 instances that require
patching. Attackers also use this tool to find EC2 configuration weaknesses and
gain unauthorized access to your AWS environment.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## PenTest:S3/ParrotLinux

### An S3 API was invoked from a

Parrot Security Linux machine.

**Default severity: Medium**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that a machine running Parrot Security Linux is
making S3 API calls using credentials that belong to your AWS account. Your
credentials might be compromised. Parrot Security Linux is a popular penetration
testing tool that security professionals use to identify weaknesses in EC2
instances that require patching. Attackers also use this tool to find EC2
configuration weaknesses and gain unauthorized access to your AWS
environment.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## PenTest:S3/PentooLinux

### An S3 API was invoked from a

Pentoo Linux machine.

**Default severity: Medium**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that a machine running Pentoo Linux is making S3 API
calls using credentials that belong to your AWS account. Your credentials
might be compromised. Pentoo Linux is a popular penetration testing tool that
security professionals use to identify weaknesses in EC2 instances that require
patching. Attackers also use this tool to find EC2 configuration weaknesses and
gain unauthorized access to your AWS environment.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Policy:S3/AccountBlockPublicAccessDisabled

### An IAM

entity invoked an API used to disable S3 Block Public Access on an
account.

**Default severity: Low**

- **Data source:** CloudTrail management
  events

This finding informs you that Amazon S3 Block Public Access was disabled at
the account level. When S3 Block Public Access settings are enabled, they are
used to filter the policies or access control lists (ACLs) on buckets as a
security measure to prevent inadvertent public exposure of data.

Typically, S3 Block Public Access is turned off in an account to allow public
access to a bucket or to the objects in the bucket. When S3 Block Public Access
is disabled for an account, access to your buckets is controlled by the
policies, ACLs, or bucket-level Block Public Access settings applied to your
individual buckets. This does not necessarily mean that the buckets are shared
publicly, but that you should audit the permissions applied to the buckets to
confirm that they provide the appropriate level of access.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Policy:S3/BucketAnonymousAccessGranted

### An IAM

principal has granted access to an S3 bucket to the internet by changing bucket
policies or ACLs.

**Default severity: High**

- **Data source:** CloudTrail management
  events

This finding informs you that the listed S3 bucket has been made publicly
accessible on the internet because an IAM entity has changed a bucket policy or
ACL on that bucket.

After a policy or ACL change is detected, GuardDuty uses
automated reasoning powered by [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/"), to determine if the bucket is publicly accessible.

###### Note

If a bucket's ACLs or bucket policies are configured to explicitly deny or
to deny all, this finding may not reflect the current state of the bucket.
This finding will not reflect any [S3 Block Public Access](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") settings that may have been enabled for
your S3 bucket. In such cases, the `effectivePermission` value in
the finding will be marked as `UNKNOWN`.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Policy:S3/BucketBlockPublicAccessDisabled

### An IAM

entity invoked an API used to disable S3 Block Public Access on a
bucket.

**Default severity: Low**

- **Data source:** CloudTrail management
  events

This finding informs you that Block Public Access was disabled for the listed
S3 bucket. When enabled, S3 Block Public Access settings are used to filter the
policies or access control lists (ACLs) applied to buckets as a security measure
to prevent inadvertent public exposure of data.

Typically, S3 Block Public Access is turned off on a bucket to allow public
access to the bucket or to the objects within. When S3 Block Public Access is
disabled for a bucket, access to the bucket is controlled by the policies or
ACLs applied to it. This does not mean that the bucket is shared publicly, but
you should audit the policies and ACLs applied to the bucket to confirm that
appropriate permissions are applied.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Policy:S3/BucketPublicAccessGranted

### An IAM principal

has granted public access to an S3 bucket to all AWS users by changing bucket
policies or ACLs.

**Default severity: High**

- **Data source:** CloudTrail management
  events

This finding informs you that the listed S3 bucket has been publicly exposed
to all authenticated AWS users because an IAM entity has changed a bucket
policy or ACL on that S3 bucket.

After a policy or ACL change is detected, GuardDuty uses
automated reasoning powered by [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/"), to determine if the bucket is publicly accessible.

###### Note

If a bucket's ACLs or bucket policies are configured to explicitly deny or
to deny all, this finding may not reflect the current state of the bucket.
This finding will not reflect any [S3 Block Public Access](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") settings that may have been enabled for
your S3 bucket. In such cases, the `effectivePermission` value in
the finding will be marked as `UNKNOWN`.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## Stealth:S3/ServerAccessLoggingDisabled

### S3 server

access logging was disabled for a bucket.

**Default severity: Low**

- **Data source:** CloudTrail management
  events

This finding informs you that S3 server access logging is disabled for a
bucket within your AWS environment. If disabled, no web request logs are
created for any attempts to access the identified S3 bucket, however, S3
management API calls to the bucket, such as [DeleteBucket](../../../AmazonS3/latest/API/API_DeleteBucket.md "../../../AmazonS3/latest/API/API_DeleteBucket.md"), are
still tracked. If S3 data event logging is enabled through CloudTrail for this bucket,
web requests for objects within the bucket will still be tracked. Disabling
logging is a technique used by unauthorized users in order to evade detection.
To learn more about S3 logs, see [S3 Server Access Logging](../../../AmazonS3/latest/dev/ServerLogs.md "../../../AmazonS3/latest/dev/ServerLogs.md")
and [S3 Logging Options](../../../AmazonS3/latest/userguide/logging-with-S3.md "../../../AmazonS3/latest/userguide/logging-with-S3.md") .

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## UnauthorizedAccess:S3/MaliciousIPCaller.Custom

### An S3

API was invoked from an IP address on a custom threat list.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API operation, for example,
`PutObject` or `PutObjectAcl`, was invoked from an IP
address that is included on a threat list that you uploaded. The threat list
associated with this finding is listed in the **Additional
information** section of a finding's details.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").

## UnauthorizedAccess:S3/TorIPCaller

### An S3 API was

invoked from a Tor exit node IP address.

**Default severity: High**

- **Data source:** CloudTrail data events for
  S3

This finding informs you that an S3 API operation, such as
`PutObject` or `PutObjectAcl`, was invoked from a Tor
exit node IP address. Tor is software for enabling anonymous communication. It
encrypts and randomly bounces communications through relays between a series of
network nodes. The last Tor node is called the exit node. This finding can
indicate unauthorized access to your AWS resources with the intent of hiding
the attacker's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated principal, it may indicate that the credentials have been exposed or your S3 permissions are not restrictive enough. For more information, see [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").
