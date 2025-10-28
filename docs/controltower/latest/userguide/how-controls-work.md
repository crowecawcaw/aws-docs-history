# How controls work

A control is a high-level rule that provides ongoing governance for your overall AWS
environment. Each control enforces a single rule, and it's expressed in plain
language. You can change the elective or strongly recommended controls that are in
force, at any time, from the AWS Control Tower console or the AWS Control Tower APIs. Mandatory controls are always applied,
and they can't be changed.

Preventive controls prevent actions from occurring. For example, the elective
control called **Disallow Changes to Bucket Policy for Amazon S3
Buckets** (Previously called **Disallow Policy Changes to Log
Archive**) prevents any IAM policy changes within the log archive shared
account. Any attempt to perform a prevented action is denied and logged in CloudTrail. The
resource is also logged in AWS Config.

Detective controls detect specific events when they occur and log the action in
CloudTrail. For example, the strongly recommended control called **Detect Whether
Encryption is Enabled for Amazon EBS Volumes Attached to Amazon EC2
Instances** detects whether an unencrypted Amazon EBS volume is attached to an
EC2 instance in your landing zone.

Proactive controls check whether resources are compliant with your company policies
and objectives, before the resources are provisioned in your accounts. If the resources
are out of compliance, they are not provisioned. Proactive controls monitor resources
that would be deployed in your accounts by means of AWS CloudFormation templates.

_For those who are familiar with AWS:_ In AWS Control Tower
preventive controls are implemented with service control policies (SCPs) and resource control policies (RCPs). Detective
controls are implemented with AWS Config rules. Proactive controls are implemented with AWS CloudFormation hooks.

## Related Topics

- [Detect and resolve drift in AWS Control Tower](drift.md "drift.md")
