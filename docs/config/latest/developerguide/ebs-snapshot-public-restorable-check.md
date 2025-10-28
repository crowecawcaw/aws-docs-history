# ebs-snapshot-public-restorable-check

Checks if Amazon Elastic Block Store (Amazon EBS) snapshots are not publicly restorable. The rule is NON_COMPLIANT if one or more snapshots with RestorableByUserIds field are set to all, that is, Amazon EBS snapshots are public.

**Identifier:** EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West, Europe (Spain) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
