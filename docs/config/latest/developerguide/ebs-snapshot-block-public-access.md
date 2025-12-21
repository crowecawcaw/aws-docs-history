# ebs-snapshot-block-public-access

Checks if block public access is enabled for Amazon EBS snapshots in an AWS Region. The rule is NON_COMPLIANT if block public access is not enabled for all public sharing of EBS snapshots in an AWS Region.

**Identifier:** EBS_SNAPSHOT_BLOCK_PUBLIC_ACCESS

**Resource Types:** AWS::EC2::SnapshotBlockPublicAccess

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
