# Concepts and key terms in Amazon GuardDuty

As you get started with Amazon GuardDuty, you can benefit from learning about its concepts and associated key terms.

**Account**

A standard Amazon Web Services (AWS) account that contains your AWS resources. You can sign
in to AWS with your account and enable GuardDuty.

You can also invite other accounts to enable GuardDuty and become associated with your
AWS account in GuardDuty. If your invitations are accepted, your account is designated as
the **administrator account** GuardDuty account, and the added accounts become
your **member** accounts. You can then view and manage those
accounts' GuardDuty findings on their behalf.

Users of the administrator account can configure GuardDuty as well as view and manage GuardDuty findings for
their own account and all of their member accounts. For information about the number of
member accounts that your administrator account can manage, see [GuardDuty quotas](guardduty_limits.md "guardduty_limits.md").

Users of member accounts can configure GuardDuty as well as view and manage GuardDuty findings
in their account (either through the GuardDuty management console or GuardDuty API). Users of
member accounts can't view or manage findings in other members' accounts.

An AWS account can't be a GuardDuty administrator account and member account at the same time. An
AWS account can accept only one membership invitation. Accepting a membership invitation
is optional.

For more information, see [Multiple accounts in Amazon GuardDuty](guardduty_accounts.md "guardduty_accounts.md").

**Attack sequence**

An attack sequence is a correlation of multiple events that, as observed by GuardDuty, happened in a specific sequence
that matches the pattern of a suspicious activity. GuardDuty uses its
[Extended Threat Detection](guardduty-extended-threat-detection.md "guardduty-extended-threat-detection.md")
capability to detect these multi-stage
attacks that span foundational data sources, AWS resources, and timeline, in your account.

The following list briefly explains the key terms associated with attack sequences:

- **Indicators** – Provides information as to why a sequence of events
  aligns with a potential suspicious activity.
- **Signals** – A signal is an API activity that GuardDuty observed,
  or an already detected GuardDuty finding in your account. By correlating the events that were observed in a specific
  sequence in your account, GuardDuty identifies an attack sequence.

There are events in your account that are not indicative of a potential threat. GuardDuty considers them as
**weak** signals. However, when weak signals and GuardDuty findings are observed in a specific
sequence that, when correlated, align to a potentially suspicious activity, GuardDuty generates an attack sequence finding.

- **Endpoints** – Information about network endpoints that a threat
  actor potentially used in an attack sequence.

**Detector**

Amazon GuardDuty is a regional service. When you enable GuardDuty in a specific AWS Region,
your AWS account gets associated with a detector ID. This 32-character alphanumeric ID
is unique to your account in that Region. For example, when you enable GuardDuty for the same
account in a different Region, your account will get associated with a different detector
ID. The format of a detectorId is `12abc34d567e8fa901bc2d34e56789f0`.

All GuardDuty findings, accounts, and actions about managing findings and the GuardDuty
service use detector ID to run an API operation.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

###### Note

In multiple-account environments, all findings for member accounts roll up to the
administrator account's detector.

Some GuardDuty functionality is configured through the detector, such as configuring CloudWatch Events
notification frequency, and the enabling or disabling of optional protection plans for
GuardDuty to process.

**Using Malware Protection for S3 within GuardDuty**

When you enable Malware Protection for S3 in an account where GuardDuty is enabled, the Malware Protection for S3
actions such as enabling, editing, and disabling a protected resource are not
associated with the detector ID.

When you don't enable GuardDuty and choose the threat detection option Malware Protection for S3,
there is no detector ID that gets created for your account.

**Foundational data sources**

The origin or location of a set of data. To detect an unauthorized or unexpected
activity in your AWS environment. GuardDuty analyzes and processes data from AWS CloudTrail event
logs, AWS CloudTrail management events, AWS CloudTrail data events for S3, VPC flow logs, DNS logs,
see [GuardDuty foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md").

**Feature**

A feature object configured for your GuardDuty protection plan helps to detect an
unauthorized or unexpected activity in your AWS environment. Each GuardDuty protection plan
configures the corresponding feature object to analyze and process data. Some of the
feature objects include EKS audit logs, RDS login activity monitoring, Lambda network activity logs,
and EBS volumes. For more information, see [Feature names for protection plans in GuardDuty
API](guardduty-features-activation-model.md "guardduty-features-activation-model.md").

**Finding**

A potential security issue discovered by GuardDuty. For more information, see [Understanding and generating Amazon GuardDuty findings](guardduty_findings.md "guardduty_findings.md").

Findings are displayed in the GuardDuty console and contain a detailed description of the
security issue. You can also retrieve your generated findings by calling the [GetFindings](../APIReference/API_GetFindings.md "../APIReference/API_GetFindings.md") and [ListFindings](../APIReference/API_ListFindings.md "../APIReference/API_ListFindings.md") API operations.

You can also see your GuardDuty findings through Amazon CloudWatch events. GuardDuty sends findings to
Amazon CloudWatch through HTTPS protocol. For more information, see [Processing GuardDuty findings with
Amazon EventBridge](guardduty_findings_eventbridge.md "guardduty_findings_eventbridge.md").

**IAM role**

This is the IAM role with the required permissions to scan the S3 object. When
tagging scanned objects is enabled, the IAM PassRole permissions help GuardDuty add tags to
the scanned object.

**Malware Protection plan resource**

After you enable Malware Protection for S3 for a bucket, GuardDuty creates a Malware Protection plan resource. This
resource is associated with Malware Protection plan ID, a unique identifier for your protected
bucket. Use Malware Protection plan resource to perform API operations on a protected resource.

**Protected bucket (protected resource)**

An Amazon S3 bucket is considered to be protected when you enable Malware Protection for S3 for this bucket
and its protection status changes to **Active**.

GuardDuty supports only an S3 bucket as a protected resource.

**Protection status**

The status associated with your Malware Protection plan resource. After you enable Malware Protection for S3 for your
bucket, this status represents whether or not your bucket is set up correctly.

**S3 object prefix**

In an Amazon Simple Storage Service (Amazon S3) bucket, you can use prefixes to organize your storage. A prefix
is a logical grouping of the objects in an S3 bucket. For more information, see [Organizing and listing objects](../../../AmazonS3/latest/userguide/organizing-objects.md "../../../AmazonS3/latest/userguide/organizing-objects.md") in the
_Amazon S3 User Guide_.

**Scan options**

When GuardDuty Malware Protection for EC2 is enabled, it allows you to specify which Amazon EC2 instances and
Amazon Elastic Block Store(EBS) volumes to scan or skip. This feature lets you add the existing tags that
are associated with your EC2 instances and EBS volume to either an inclusion tags list or
exclusion tags list. The resources associated to the tags that you add to an inclusion
tags list, are scanned for malware, and those added to an exclusion tags list are not
scanned. For more information, see [Scan options with user-defined tags](malware-protection-customizations.md#mp-scan-options "malware-protection-customizations.md#mp-scan-options").

**Snapshots retention**

When GuardDuty Malware Protection for EC2 is enabled, it provides an option to retain the snapshots of your EBS
volumes in your AWS account. GuardDuty generates the replica EBS volumes based on the
snapshots of your EBS volumes. You can retain the snapshots of your EBS volumes only if
the Malware Protection for EC2 scan detects malware in the replica EBS volumes. If no malware is detected in
the replica EBS volumes, GuardDuty automatically deletes the snapshots of your EBS volumes,
irrespective of the snapshots retention setting. For more information, see [Snapshots retention](malware-protection-customizations.md#mp-snapshots-retention "malware-protection-customizations.md#mp-snapshots-retention").

**Suppression rule**

Suppression rules allow you to create very specific combinations of attributes to
suppress findings. For example, you can define a rule through the GuardDuty filter to
auto-archive `Recon:EC2/Portscan` from only those instances in a specific VPC,
running a specific AMI, or with a specific EC2 tag. This rule would result in port scan
findings being automatically archived from the instances that meet the criteria. However,
it still allows alerting if GuardDuty detects those instances conducting other malicious
activity, such as crypto-currency mining.

Suppression rules defined in the GuardDuty administrator account apply to the GuardDuty member accounts.
GuardDuty member accounts can't modify suppression rules.

With suppression rules, GuardDuty still generates all findings. Suppression rules provide
suppression of findings while maintaining a complete and immutable history of all
activity.

Typically suppression rules are used to hide findings that you have determined as
false positives for your environment, and reduce the noise from low-value findings so you
can focus on larger threats. For more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").

**Trusted IP list**

A list of trusted IP addresses for highly secure communication with your AWS
environment. GuardDuty does not generate findings based on trusted IP lists. For more
information, see [Customizing threat detection with entity lists and
IP address lists](guardduty_upload-lists.md "guardduty_upload-lists.md").

**Threat IP list**

A list of known malicious IP addresses. In addition to generating findings because of
a potentially suspicious activity, GuardDuty also generates findings based on these threat
lists. For more information, see [Customizing threat detection with entity lists and
IP address lists](guardduty_upload-lists.md "guardduty_upload-lists.md").
